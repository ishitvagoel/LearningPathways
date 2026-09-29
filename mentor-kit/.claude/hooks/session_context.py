#!/usr/bin/env python3
"""SessionStart hook: give the mentor facts it would otherwise guess.

Plain-text stdout from a SessionStart hook is added to Claude's context. We report today's
date and the installed versions of the libraries the curriculum teaches, so lessons target
what is actually installed instead of what the model remembers.
"""
import datetime
import importlib.metadata as md
import os

PACKAGES = [
    # LangChain Path
    "langchain", "langchain-core", "langgraph", "langsmith", "langchain-anthropic",
    "anthropic", "langchain-huggingface", "langchain-chroma", "deepagents", "fastmcp",
    "openevals", "agentevals",
    # Mastery Plan: apps (Phase 2), retrieval (Phase 3), model internals and post-training (Phase 8)
    "fastapi", "pydantic", "sentence-transformers", "claude-agent-sdk",
    "torch", "transformers", "peft", "trl", "vllm",
]

lines = [f"Today is {datetime.date.today().isoformat()}."]
installed = []
for name in PACKAGES:
    try:
        installed.append(f"{name}=={md.version(name)}")
    except md.PackageNotFoundError:
        pass
if installed:
    lines.append("Installed packages: " + ", ".join(installed) + ".")
else:
    lines.append("No curriculum packages are installed in this Python environment yet "
                 "(activate the project's virtualenv, or teach Step 0.2 setup first).")
lines.append(f"Provider from environment: PROVIDER={os.getenv('PROVIDER', 'anthropic (default in config.py)')}.")
lines.append("Read progress.md before teaching; resume from the current position for the path being studied.")
print("\n".join(lines))
