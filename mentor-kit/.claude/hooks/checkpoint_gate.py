#!/usr/bin/env python3
"""PostToolUse hook (Edit|Write): a checkpoint may only be marked "passed" in progress.md
when reviews/<path>-phase-<N>.md exists and ends with "VERDICT: PASS".

<path> is "mastery" or "langchain": both curricula number their phases from 0, so reviews
are keyed by path to stop one curriculum's PASS satisfying the other's checkpoint.

This is a computational sensor: it checks a fact instead of trusting an instruction.
Exit 2 sends the reason back to Claude so it can correct progress.md.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
event = json.load(sys.stdin)
file_path = pathlib.Path((event.get("tool_input") or {}).get("file_path", ""))
if file_path.name != "progress.md":
    sys.exit(0)

progress = (ROOT / "progress.md").read_text(encoding="utf-8")
problems = []
# table rows look like: | mastery | 3 | Documentation assistant | passed | reviews/mastery-phase-3.md |
ROW = re.compile(r"^\|\s*(mastery|langchain)\s*\|\s*(\d+)\s*\|[^|]*\|\s*([^|]*?)\s*\|", re.M | re.I)
for path, phase, status in ROW.findall(progress):
    if status.strip().lower() != "passed":
        continue
    review = ROOT / "reviews" / f"{path.lower()}-phase-{phase}.md"
    if not review.exists():
        problems.append(f"{path} phase {phase} is marked passed but {review.relative_to(ROOT)} does not exist.")
    elif not review.read_text(encoding="utf-8").rstrip().endswith("VERDICT: PASS"):
        problems.append(f"{path} phase {phase} is marked passed but its review does not end with 'VERDICT: PASS'.")

if problems:
    print("\n".join(problems)
          + "\nRun /checkpoint-review for that phase, or record 'overridden by learner' if they chose to skip it.",
          file=sys.stderr)
    sys.exit(2)
sys.exit(0)
