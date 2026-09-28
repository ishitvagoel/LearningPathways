#!/usr/bin/env python3
"""PostToolUse hook (Edit|Write): run scripts/check_docs.py on the Markdown page just edited.

Exit 2 sends the problems back to Claude as feedback; exit 0 lets the session continue.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from check_docs import check_file  # noqa: E402

event = json.load(sys.stdin)
file_path = (event.get("tool_input") or {}).get("file_path", "")
path = pathlib.Path(file_path)
if not path.is_absolute():
    path = pathlib.Path(event.get("cwd", ROOT)) / path

try:
    inside_docs = path.resolve().is_relative_to(ROOT / "docs")
except OSError:
    inside_docs = False

if path.suffix == ".md" and inside_docs and path.exists():
    problems = check_file(path)
    if problems:
        print("check_docs found problems in the page you just edited:", file=sys.stderr)
        print("\n".join(problems), file=sys.stderr)
        sys.exit(2)
sys.exit(0)
