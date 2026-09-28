@AGENTS.md

## Claude Code harness for this repo

This repo is harnessed as described in `docs/ai-engineering/v2/claude-harness.md`. In short:

- **Guides:** this file, `AGENTS.md`, and the skills in `.claude/skills/`:
  - `/refresh-curriculum` — research-first workflow for producing a new curriculum version
  - `/add-learning-path` — scaffold a new path in the house format
  - `/check-links` — verify every external link in given pages
- **Sensors (they run whether or not you remember them):**
  - `PostToolUse` hook → `scripts/check_docs.py` on every Markdown file you edit under `docs/`; fix what it reports before moving on
  - `Stop` hook → blocks finishing while a frozen V1 file differs from `HEAD`
- **Constraints:** `.claude/settings.json` denies `Edit` on the frozen V1 files.
- **Reviewer:** delegate a pre-publish accuracy review to the `curriculum-reviewer` subagent; it is read-only and checks claims against primary sources.

When a hook blocks you, treat its message as a failing test: fix the cause, don't work around the check.
