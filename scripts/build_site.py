#!/usr/bin/env python3
"""Build the site the way production does: checks -> MkDocs build -> download sources -> mentor-kit.zip.

One script, so Vercel (vercel.json `buildCommand`) and CI (.github/workflows/ci.yml) run the same steps:

    python3 scripts/build_site.py                      # local build into ./site
    python3 scripts/build_site.py --require-site-url   # what Vercel runs

Output (./site) is a plain static tree. Nothing here needs a server.

The site URL comes from, in order: SITE_URL, then Vercel's VERCEL_PROJECT_PRODUCTION_URL, then the
localhost default in mkdocs.yml. It feeds canonical links and the sitemap, and always ends with
a slash. (The "Download Markdown" buttons use relative URLs, so they work on previews and localhost too.)

"Last updated" dates need full git history, but Vercel clones with `--depth=10`. In a shallow clone
the date plugin would date an unchanged page by the oldest commit it can see, which is wrong. So the
script first tries to fetch the full history and, if that fails, turns the dates off instead of
showing wrong ones.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import shutil
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
KIT = ROOT / "mentor-kit"
# The curriculum pages the mentor kit ships in curriculum/ (same files the kit's README tells you to copy).
KIT_PAGES = ["langchain-path.md", "ai-mastery-plan.md"]
KIT_PAGES_DIR = ROOT / "docs" / "ai-engineering" / "v2"


def step(title: str) -> None:
    print(f"\n==> {title}", flush=True)


def run(*cmd: str, env: dict[str, str] | None = None) -> None:
    print("+ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True, env=env)


def resolve_site_url() -> str | None:
    explicit = os.environ.get("SITE_URL", "").strip()
    if explicit:
        return explicit.rstrip("/") + "/"
    host = os.environ.get("VERCEL_PROJECT_PRODUCTION_URL", "").strip()  # host only, no scheme
    if host:
        return f"https://{host}/"
    return None


def is_shallow() -> bool | None:
    """True/False for a git checkout; None when this isn't one (or git is missing)."""
    try:
        out = subprocess.run(["git", "rev-parse", "--is-shallow-repository"], cwd=ROOT,
                             capture_output=True, text=True)
    except FileNotFoundError:
        return None
    return out.stdout.strip() == "true" if out.returncode == 0 else None


def ensure_history() -> bool:
    """Return True if 'last updated' dates can be trusted (full history available)."""
    shallow = is_shallow()
    if shallow is None:
        print("Not a git checkout: 'last updated' dates are turned off.")
        return False
    if not shallow:
        return True
    print("Shallow clone: fetching the full history so 'last updated' dates are correct...", flush=True)
    # Try the clone's own remote first. Vercel's build clone has no usable `origin`, so fall back to the
    # public repository URL Vercel describes in its system variables (the repo is public; no credentials).
    sources = [[]]
    owner, slug = os.environ.get("VERCEL_GIT_REPO_OWNER"), os.environ.get("VERCEL_GIT_REPO_SLUG")
    if os.environ.get("VERCEL_GIT_PROVIDER") == "github" and owner and slug:
        sources.append([f"https://github.com/{owner}/{slug}.git"])
    for source in sources:
        try:
            subprocess.run(["git", "fetch", "--unshallow", "--quiet", *source], cwd=ROOT, check=True,
                           timeout=180, capture_output=True, text=True)
        except subprocess.CalledProcessError as exc:
            print(f"  fetch from {source[0] if source else 'the default remote'} failed: "
                  f"{(exc.stderr or '').strip().splitlines()[-1:] or exc.returncode}")
        except (subprocess.SubprocessError, OSError) as exc:
            print(f"  fetch from {source[0] if source else 'the default remote'} failed ({exc.__class__.__name__}).")
        if is_shallow() is False:
            return True
        # With no remote configured, `git fetch` exits 0 without fetching anything.
        print(f"  {source[0] if source else 'the default remote'}: history is still shallow")
    print("NOTE: history is still shallow, so 'last updated' dates are turned off rather than shown wrong.")
    return False


def package_mentor_kit(dest: pathlib.Path) -> int:
    """Zip mentor-kit/ plus the curriculum pages, keeping file modes (the hooks stay executable)."""
    files = [p for p in sorted(KIT.rglob("*"))
             if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"]
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, path.relative_to(KIT).as_posix())
        for name in KIT_PAGES:
            zf.write(KIT_PAGES_DIR / name, f"curriculum/{name}")
    return len(files) + len(KIT_PAGES)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--require-site-url", action="store_true",
                        help="fail if no site URL can be determined (used by the Vercel build)")
    args = parser.parse_args()

    env = dict(os.environ)
    site_url = resolve_site_url()
    if site_url:
        env["SITE_URL"] = site_url
    elif args.require_site_url:
        print("ERROR: no site URL. Neither SITE_URL nor Vercel's VERCEL_PROJECT_PRODUCTION_URL is set.\n"
              "  Fix (one-time): in the Vercel project, open Settings > Environment Variables and either\n"
              "  tick 'Automatically expose System Environment Variables' or add SITE_URL=https://<your-domain>/",
              file=sys.stderr)
        return 1
    print(f"site_url = {site_url or '(mkdocs.yml default, for local use)'}")

    step("History for 'last updated' dates")
    env["GIT_DATES"] = "true" if ensure_history() else "false"

    step("Checks (front matter, code blocks, frozen V1 pages)")
    run(sys.executable, "scripts/check_docs.py", "--all")

    step("MkDocs build")
    shutil.rmtree(SITE, ignore_errors=True)
    run(sys.executable, "-m", "mkdocs", "build", "-d", str(SITE), env=env)

    step("Markdown sources (for each page's download button)")
    shutil.copytree(ROOT / "docs", SITE / "sources", dirs_exist_ok=True)

    step("Mentor kit")
    count = package_mentor_kit(SITE / "mentor-kit.zip")
    print(f"mentor-kit.zip: {count} files, {(SITE / 'mentor-kit.zip').stat().st_size // 1024} KB")

    print(f"\nDone: {SITE.relative_to(ROOT)}/ is ready to serve.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except subprocess.CalledProcessError as exc:
        print(f"\nBuild failed: '{' '.join(str(a) for a in exc.cmd[:4])}' exited with code {exc.returncode}.",
              file=sys.stderr)
        sys.exit(exc.returncode or 1)
