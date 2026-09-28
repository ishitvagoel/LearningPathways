---
name: check-links
description: Verify that every external link in the given Markdown pages resolves, and report broken or moved resources. Use before publishing curriculum changes or when a course link might be stale.
argument-hint: "[files... default: docs/ai-engineering/v2/*.md]"
allowed-tools: Bash(python3 scripts/check_links.py *)
---

# Check links

Files to check: `$ARGUMENTS` (if empty, use `docs/ai-engineering/v2/*.md`). Run:

```bash
python3 scripts/check_links.py <files>
```

Then report:

- **BROKEN** (404/410/unreachable): find the resource's new URL or a verified replacement, and propose the edit. Never guess a URL.
- **UNVERIFIED** (bot-blocked, e.g. Udemy, GitHub, YouTube, some blogs): confirm with a web search that the page still exists and still matches its title; list any you could not confirm.
- **OK but title mismatch** (a URL that now redirects to a catalogue or home page): treat as broken.

Don't edit frozen V1 pages; report their broken links instead.
