#!/usr/bin/env python3
"""Check that every external link in the given Markdown files still resolves.

Usage:
    python3 scripts/check_links.py docs/ai-engineering/v2/*.md

Prints one line per URL: status, URL and page title. Sites that block automated
clients (Cloudflare challenges, 403/406/429 from known hosts) are reported as
UNVERIFIED rather than broken, because a human browser will usually load them.
Exits 1 only when a URL returns 404/410 or cannot be reached at all.
"""
import re
import sys
import urllib.error
import urllib.request

URL = re.compile(r"https?://[^\s)\"'<>`]+")
TITLE = re.compile(r"<title[^>]*>([^<]*)", re.I)
BOT_BLOCKED_STATUSES = {401, 403, 405, 406, 429}
UA = "Mozilla/5.0 (X11; Linux x86_64) learning-pathways-link-check"


def fetch(url: str) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            body = resp.read(200_000).decode("utf-8", "replace")
            m = TITLE.search(body)
            return str(resp.status), (m.group(1).strip()[:70] if m else "")
    except urllib.error.HTTPError as exc:
        return str(exc.code), ""
    except Exception as exc:  # DNS failure, timeout, TLS error
        return "ERR", type(exc).__name__


def main(paths: list[str]) -> int:
    urls = sorted({u.rstrip(".,;") for p in paths for u in URL.findall(open(p, encoding="utf-8").read())})
    broken = 0
    for url in urls:
        status, title = fetch(url)
        if status.isdigit() and int(status) in BOT_BLOCKED_STATUSES:
            label = "UNVERIFIED"
        elif status.isdigit() and int(status) < 400:
            label = "OK"
        else:
            label = "BROKEN"
            broken += 1
        print(f"{label:10} {status:4} {url} {title}")
    print(f"\n{len(urls)} URLs, {broken} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
