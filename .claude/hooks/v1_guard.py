#!/usr/bin/env python3
"""Stop hook: refuse to finish while a frozen V1 page differs from HEAD.

The Edit deny rule in settings.json stops the Edit tool; this catches every other
route (sed, a script, a Bash redirect). Exit 2 keeps Claude working with the message
below as feedback. `stop_hook_active` prevents an infinite loop if it can't be fixed.
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
