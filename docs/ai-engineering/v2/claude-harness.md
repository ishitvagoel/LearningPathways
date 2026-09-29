---
title: Claude Harness Kit
description: The Claude Code harness files that run this curriculum — a mentor kit for learners and the maintenance harness for this repository — and how each one works as a guide, sensor or constraint.
icon: material/cog-transfer
tags:
  - Claude Code
  - Harness Engineering
  - Tooling
---

# Claude Harness Kit

**Curriculum V2 (revised) · September 2026**

The earlier editions said "paste this page into your AI assistant". This edition ships **harness files** instead: configuration that makes Claude Code behave as a disciplined mentor, and that keeps this repository's content honest. They are also the curriculum's first worked example of **harness engineering**: *agent = model + harness*, and the harness is everything around the model (instructions, tools, checks, permissions, memory).

!!! abstract "Two harnesses"
    - **Mentor kit** (`mentor-kit/` in the repository) — copy it into your practice repo; Claude Code becomes your tutor for the [AI Engineer Mastery Plan](ai-mastery-plan.md) and the [LangChain Path](langchain-path.md).
    - **Repository harness** (`CLAUDE.md`, `AGENTS.md`, `.claude/` at the repo root) — used when maintaining this site; it replaced the old Gemini-specific `GEMINI.md`.

---

## The vocabulary: guides, sensors, constraints

Birgitta Böckeler's [harness engineering](https://martinfowler.com/articles/harness-engineering.html) article splits a harness into **guides** and **sensors**. This kit adds a third row, **constraints**, for the deterministic permission rules Claude Code provides:

| Kind | Acts | Examples in these harnesses |
|---|---|---|
| **Guide** (feed-forward) | *Before* the agent acts, steering it | `CLAUDE.md`, `AGENTS.md`, skills, `config.py`, the SessionStart context hook |
| **Sensor** (feedback) | *After* the agent acts, checking and feeding problems back | PostToolUse checkers, the Stop-time V1 guard, the checkpoint reviewer subagent |
| **Constraint** | Deterministically allows, asks or denies | `permissions` in `.claude/settings.json` |

Sensors and guides can each be **computational** (a script, deterministic and cheap) or **inferential** (another model's judgement). The kit leans on computational checks wherever possible because the 2026 evidence is consistent: written rules are often ignored, while checks that *run* are not. One study of 481 public `CLAUDE.md` files found that only 4–16% of written security rules had a measurable effect (an arXiv paper cited in [Marmelab's 2026 review](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html)).

---

## Mentor kit (for learners)

### Install

1. Get the kit: download **`mentor-kit.zip`** from the site root (`https://ishitvagoel.github.io/LearningPathways/mentor-kit.zip`, built by the deploy workflow and including the curriculum pages) or copy the `mentor-kit/` folder from the [repository](https://github.com/ishitvagoel/LearningPathways).
2. Unzip or copy it into a new practice repository (keep the hidden `.claude/` folder) and run `git init`.
3. If you copied the folder rather than the zip, put `langchain-path.md` and `ai-mastery-plan.md` into `curriculum/`.
4. Edit `learner-profile.md` once. To use a provider other than Claude, set `PROVIDER` and the model variables (see `config.py`).
5. `chmod +x .claude/hooks/*.py`, start `claude` **at the folder's root** (permission rules such as `Edit(/projects/**)` are anchored to the directory you start in), approve the project hooks when asked, and run `/lesson`.

Use a recent Claude Code: the forked, blocking `/checkpoint-review` needs v2.1.218 or later, and reading `AGENTS.md` directly needs v2.1.277 or later.

### What each file does

```text
practice-repo/
├── CLAUDE.md                 # guide: mentor rules; imports learner-profile.md + progress.md
├── learner-profile.md        # guide: who you are (edit once)
├── progress.md               # memory: position, checkpoints, weak spots, session log
├── config.py                 # guide: the only place provider + model IDs live
├── curriculum/               # the two curriculum pages
├── projects/                 # YOUR checkpoint code (mentor must ask before editing)
├── reviews/                  # checkpoint verdicts written by the reviewer
└── .claude/
    ├── settings.json         # constraints + hook registration
    ├── hooks/
    │   ├── session_context.py   # SessionStart: date + installed package versions → context
    │   └── checkpoint_gate.py   # PostToolUse: no "passed" without a PASS review on file
    ├── skills/
    │   ├── lesson/SKILL.md            # /lesson [step]
    │   ├── quiz/SKILL.md              # /quiz
    │   ├── checkpoint-review/SKILL.md # /checkpoint-review <mastery|langchain> <phase>  (forks the reviewer)
    │   └── log-progress/SKILL.md      # /log-progress
    └── agents/
        └── checkpoint-reviewer.md     # independent reviewer subagent
```

**Why these particular pieces**

- **`CLAUDE.md` stays short** and imports state with `@progress.md`, so each session starts from where you left off without a long rulebook. Claude Code's docs recommend keeping it under about 200 lines.
- **`session_context.py`** tackles a failure the V1 review found repeatedly: models teach the APIs they *remember*, not the ones you *installed*. Plain-text output from a `SessionStart` hook is added to Claude's context, so every session begins with the real package versions and today's date.
- **`/checkpoint-review` runs in a forked context** with the `checkpoint-reviewer` subagent. The reviewer never saw the lesson, so it judges the repository against the curriculum's criteria rather than the mentor's impression of what you understood.
- **`checkpoint_gate.py`** is a computational sensor. If `progress.md` marks a checkpoint "passed" without `reviews/<path>-phase-N.md` ending in `VERDICT: PASS`, the edit is flagged back to Claude (exit code 2). "Checkpoints gate phases" stops being a promise and becomes a check. Checkpoints are keyed by path (`mastery` or `langchain`) because both curricula number their phases from 0; otherwise a LangChain Phase 3 pass would satisfy the Mastery Plan's Phase 3.
- **`"ask": ["Edit(/projects/**)"]`** keeps your checkpoint code yours. The mentor explains and hints, and any edit under `projects/` (including by a subagent) needs your approval.
- **`.env` is unreadable** to Claude's file tools (`deny: Read(./.env)`). Keep API keys there or in your shell.

### Tested behaviour

Each hook was run against synthetic events before release, including **negative tests** (cases that must block):

| Hook | Case | Expected | Result |
|---|---|---|---|
| `checkpoint_gate.py` | progress untouched | allow (exit 0) | ✅ |
| `checkpoint_gate.py` | phase marked passed, no review | block (exit 2) | ✅ |
| `checkpoint_gate.py` | review ends `VERDICT: REVISE` | block (exit 2) | ✅ |
| `checkpoint_gate.py` | review ends `VERDICT: PASS` | allow | ✅ |
| `checkpoint_gate.py` | only the *other* curriculum's phase has a PASS | block (exit 2) | ✅ |
| `session_context.py` | startup | prints date, versions, provider | ✅ |

---

## Repository harness (for maintainers)

| File | Kind | Role |
|---|---|---|
| `AGENTS.md` | Guide | Tool-neutral project instructions: structure, commands, rules (V1 frozen, version-don't-rewrite, provider-neutral, verify-don't-recall) |
| `CLAUDE.md` | Guide | `@AGENTS.md` import plus Claude-specific notes; this replaces the old `GEMINI.md` |
| `.claude/skills/refresh-curriculum` | Guide | `/refresh-curriculum v3`: audit → primary-source research → new version folder → review notes → validation |
| `.claude/skills/add-learning-path` | Guide | Scaffold a new path in the house format |
| `.claude/skills/check-links` | Guide + sensor | Runs `scripts/check_links.py`, triages broken vs bot-blocked links |
| `.claude/agents/curriculum-reviewer.md` | Inferential sensor | Read-only accuracy review against primary sources |
| `scripts/check_docs.py` | Computational sensor | Frontmatter, Python blocks that parse, no deprecated APIs or retired model IDs *in code*; with `--all` (run in CI), V1 pages must match pinned SHA-256 hashes |
| `.claude/hooks/check_doc_hook.py` | Sensor wiring | PostToolUse on Edit and Write: runs `check_docs.py` on the edited page; problems go back to Claude |
| `.claude/hooks/v1_guard.py` | Sensor | Stop hook: once per stop, blocks finishing while a frozen V1 page differs from `HEAD` (catches routes the deny rule can't see, such as a Python script that opens the file itself) |
| `.claude/settings.json` | Constraint | Denies `Edit` on V1 files and reading `.env`; pre-approves the build and check commands |

**Defence in depth, on purpose.** Three layers protect V1, and each covers a gap in the one before:

1. The `Edit` deny rule covers Claude's file tools and the Bash file commands Claude Code recognises (`sed`, `tee`, redirects). It can't see a script that opens the file itself.
2. The Stop hook checks the *outcome* (`git diff` against `HEAD`) whatever route was taken, but only once per stop, and a committed change gets past it.
3. The pinned-hash check in `check_docs.py --all` runs in CI on every deploy, so even a committed change to V1 fails the build.

Guides say what should happen; sensors verify that it did.

The same testing discipline applied here. The document checker was run against a deliberately bad page (an `AgentExecutor` import and a `temperature=` argument) and blocked it. The V1 guard and the pinned-hash check were each run against a tampered V1 file (the hash check also against a deleted one) and both failed as intended. While building this, the deny rule also blocked two of the maintainer's own test commands that would have touched real V1 files. On its first run over the whole site, the checker also caught a real problem: the landing page had no `description`.

---

!!! tip "To block an action, use PreToolUse or a deny rule"
    `PostToolUse` hooks run *after* the tool, so they can only report problems back (like `check_doc_hook.py`). To stop an action before it happens, use a permission `deny` rule (e.g. `Edit(/migrations/**)`) or a `PreToolUse` hook that exits with code 2.

## Using these files with other tools

`AGENTS.md` is the cross-tool convention read by many coding agents (Codex, Cursor, Gemini CLI and others). Claude Code reads it directly only when no `CLAUDE.md` exists (v2.1.277 or later); otherwise it needs the `@AGENTS.md` import used here, which is the reliable pattern. The skills follow the open [Agent Skills](https://agentskills.io/home) format (a folder with a `SKILL.md`), which other agent products also load. Hooks and permission rules are Claude Code-specific. If you use a different agent, port the *checks* (`scripts/check_docs.py`, the guard logic) to that tool's hook or CI mechanism. The scripts themselves are plain Python.

## Keep the harness healthy

- **Fix it in the harness.** When the mentor makes the same mistake twice, add a check or a skill step instead of repeating yourself in chat.
- **Record why each rule exists** (one line), and after each model upgrade try removing rules that may no longer be needed. Harnesses rot as models improve.
- **Test your guards**, including negative cases. A guard that never fires gives false confidence.

## References

- Claude Code docs: [memory (`CLAUDE.md` / `AGENTS.md`)](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents), [hooks](https://code.claude.com/docs/en/hooks), [permissions](https://code.claude.com/docs/en/permissions)
- [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) — Birgitta Böckeler
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — Anthropic
- [The State of AI Harness Engineering 2026](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) — Marmelab
