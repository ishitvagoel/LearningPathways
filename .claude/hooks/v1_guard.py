#!/usr/bin/env python3
"""Stop hook: refuse to finish while a frozen V1 page differs from HEAD.

The Edit deny rule in settings.json covers the Edit/Write tools and Bash file commands
Claude Code recognises (sed, tee, redirects); this catches what it can't see, such as a
Python script that opens the file itself. Exit 2 keeps Claude working with the message
below as feedback, once per stop (`stop_hook_active` prevents an infinite loop). It
compares against HEAD, so a committed change gets past it; the pinned-hash check in
scripts/check_docs.py --all (run in CI) is the backstop for that.
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FROZEN = ["docs/ai-engineering/langchain-path.md", "docs/ai-engineering/ai-mastery-plan.md"]

event = json.load(sys.stdin)
if event.get("stop_hook_active"):
    sys.exit(0)

result = subprocess.run(
    ["git", "diff", "--name-only", "HEAD", "--", *FROZEN],
    cwd=ROOT, capture_output=True, text=True,
)
changed = [line for line in result.stdout.splitlines() if line.strip()]
if changed:
    print(
        "Frozen V1 file(s) were modified: " + ", ".join(changed)
        + ". V1 must stay byte-for-byte unchanged. Restore with "
        + "`git checkout HEAD -- " + " ".join(changed) + "` and make the change in the newest version instead.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
