# AGENTS.md — Learning Pathways

Instructions for any coding agent (Claude Code, Codex, Gemini CLI, Cursor, ...) working in this repository.
Claude-specific harness details live in `CLAUDE.md`, which imports this file.

## What this repo is

A static MkDocs Material site (hosted on Vercel) hosting versioned learning paths for AI engineering.
Content is Markdown in `docs/`; there is no application code to run in production.

```text
docs/
  index.md                          # landing page (grid cards)
  ai-engineering/
    langchain-path.md               # V1 (March 2026) — FROZEN
    ai-mastery-plan.md              # V1 (March 2026) — FROZEN
    v2/                             # current edition
      langchain-path.md
      ai-mastery-plan.md
      claude-harness.md             # explains the harness kit
      review-notes.md               # audit + research + sources
  assets/custom.css
mentor-kit/                         # Claude Code harness learners copy into their practice repo
scripts/check_docs.py               # structure + stale-API checks (run on every page you edit)
scripts/check_links.py              # external link checker
scripts/build_site.py               # the production build: checks, MkDocs, sources, mentor-kit.zip
mkdocs.yml                          # nav, theme, plugins
vercel.json                         # Vercel build settings (runs scripts/build_site.py)
.github/workflows/ci.yml            # runs the same build on pushes to main and on pull requests; deploys nothing
```

## Commands

```bash
pip install -r requirements.txt          # site dependencies
python3 scripts/build_site.py            # the full production build into ./site (what Vercel and CI run)
mkdocs build -d /tmp/site                # quick build only; must succeed with no new warnings
python3 scripts/check_docs.py --all      # must print "OK"
python3 scripts/check_links.py docs/ai-engineering/v2/*.md   # before publishing new resources
```

## Hosting

Vercel builds and deploys from Git: pushes to `main` go to production, and other branches and pull requests get previews. The build settings live in `vercel.json` (Framework Preset "Other"), so the Vercel dashboard needs no overrides. The one setting the build needs is the site URL, which comes from `SITE_URL` or, by default, Vercel's `VERCEL_PROJECT_PRODUCTION_URL` (on if "Automatically expose System Environment Variables" is ticked). `scripts/build_site.py` fails with instructions if neither is available. Vercel's Python is managed by `uv` and refuses system-wide `pip install` (PEP 668), so `vercel.json` installs into a `.venv` and builds with that interpreter. Vercel clones with `--depth=10`, so the script fetches the full history for the "last updated" dates, and turns them off if that isn't possible. Keep links to the site's own files relative (no domain in content), so the site can move again.

## Rules

1. **Never edit frozen versions.** V1 files above are kept byte-for-byte for learners mid-way through them. Fix problems in the newest version and record them in its `review-notes.md`.
2. **Version, don't rewrite.** A substantial refresh goes in a new sibling folder (`v3/`) with the same filenames, its own `review-notes.md`, and nav/landing-page updates listing it first.
3. **Every page starts with YAML frontmatter** containing `title` and `description` (optional `icon`, `tags`).
4. **Learning-path structure:** mentor instructions, learner profile, phases starting at Phase 0, a 🔨 checkpoint project per phase, and a "what NOT to teach" section.
5. **Resource cards** use the Quick Stats admonition format already used in `v2/ai-mastery-plan.md` (heading with `{ #anchor }`, `!!! info inline end "Quick Stats"`, instructors, description, `.md-button` link).
6. **Provider-neutral content.** Teach concepts first. Code uses `"provider:model"` strings from one `config.py`; Claude is the reference provider. Don't hard-wire a vendor into every example.
7. **Verify, don't recall.** Model IDs, SDK signatures, course URLs and statistics change monthly. Check primary sources before writing them, cite them in `review-notes.md`, and never invent a course, link or number.
8. **Runnable code must parse** and must not use deprecated APIs; `scripts/check_docs.py` enforces the list. If a rule there is outdated, update the script, not the content.
9. **No secrets** (API keys, tokens) anywhere in the repo. The site is static: no server-side code.
10. Keep `superpowers/` as historical design notes; don't update it.
