#!/usr/bin/env python3
"""Deterministic checks for curriculum pages (a "computational sensor" in harness terms).

Usage:
    python3 scripts/check_docs.py docs/ai-engineering/v2/langchain-path.md [more files...]
    python3 scripts/check_docs.py --all

Checks every Markdown page for:
  1. YAML frontmatter with `title` and `description`
  2. Python code blocks that parse
  3. Deprecated API patterns and retired model IDs *inside Python code blocks*
     (prose and "what not to teach" tables may mention them; runnable code may not)

Frozen V1 pages are skipped. Exits 1 and prints problems to stderr when any check fails.
"""
import ast
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FROZEN = {
    "docs/ai-engineering/langchain-path.md",
    "docs/ai-engineering/ai-mastery-plan.md",
}

# pattern -> why it is wrong. Keep this list short and evidence-based; prune it when it rots.
DEPRECATED_IN_CODE = {
    r"\binitialize_agent\b": "removed pre-1.0 agent API; use langchain.agents.create_agent",
    r"\bAgentExecutor\b": "removed pre-1.0 agent API; use langchain.agents.create_agent",
    r"\bcreate_react_agent\b": "use langchain.agents.create_agent",
    r"ConversationBufferMemory": "use a checkpointer + thread_id",
    r"langchain_core\.pydantic_v1": "use pydantic v2 directly",
    r"langchain_community\.vectorstores": "use the dedicated package, e.g. langchain_chroma",
    r"LANGCHAIN_TRACING_V2": "use LANGSMITH_TRACING",
    r"\.set_entry_point\(": "use add_edge(START, ...)",
    r"interrupt_before=": "use interrupt() + Command(resume=...)",
    r"gemini-(1\.5|2\.0)": "retired model ID",
    r"text-embedding-004": "retired embedding model ID",
    r"budget_tokens": "fixed thinking budgets are rejected on current Claude models; use adaptive thinking + effort",
    r"\btemperature\s*=": "current reasoning models reject or discourage sampling params; use effort",
}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
PY_BLOCK = re.compile(r"```python\n(.*?)```", re.S)


def check_file(path: pathlib.Path) -> list[str]:
    rel = path.resolve().relative_to(ROOT).as_posix()
    if rel in FROZEN or path.suffix != ".md":
        return []
    text = path.read_text(encoding="utf-8")
    problems = []

    fm = FRONTMATTER.match(text)
    if not fm:
        problems.append(f"{rel}: missing YAML frontmatter")
    else:
        for key in ("title", "description"):
            if not re.search(rf"^{key}:\s*\S", fm.group(1), re.M):
                problems.append(f"{rel}: frontmatter missing '{key}'")

    for block in PY_BLOCK.finditer(text):
        line = text.count("\n", 0, block.start()) + 2
        code = block.group(1)
        try:
            ast.parse(code)
        except SyntaxError as exc:
            problems.append(f"{rel}:{line + (exc.lineno or 1) - 1}: Python code block does not parse: {exc.msg}")
        for pattern, why in DEPRECATED_IN_CODE.items():
            for m in re.finditer(pattern, code):
                problems.append(f"{rel}:{line + code.count(chr(10), 0, m.start())}: '{m.group(0)}' in code: {why}")
    return problems


def main(argv: list[str]) -> int:
    if argv == ["--all"]:
        files = sorted((ROOT / "docs").rglob("*.md"))
    else:
        files = [pathlib.Path(a) for a in argv]
    problems = [p for f in files if f.exists() for p in check_file(f)]
    for p in problems:
        print(p, file=sys.stderr)
    if problems:
        print(f"\n{len(problems)} problem(s). Fix them or, if a rule is outdated, update scripts/check_docs.py.", file=sys.stderr)
        return 1
    print(f"check_docs: {len(files)} file(s) OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
