# Learning Pathways — Claude Code mentor kit

A small Claude Code harness that turns Claude Code into a first-principles mentor for the
[Learning Pathways](https://ishitvagoel.github.io/LearningPathways/) AI engineering curriculum.
It's also a worked example of the harness engineering the curriculum teaches: every file here is a
**guide**, a **sensor** or a **constraint**.

## Install

1. Create a practice repository and copy this kit's contents into it, including the hidden `.claude/` folder:
   ```bash
   mkdir ai-practice && cp -r mentor-kit/. ai-practice/ && cd ai-practice && git init
   ```
2. Put the curriculum pages in `curriculum/`. The downloadable kit zip already includes them; from a clone of the
   repository, run:
   ```bash
   cp ../docs/ai-engineering/v2/langchain-path.md ../docs/ai-engineering/v2/ai-mastery-plan.md curriculum/
   ```
3. Edit `learner-profile.md` once. Optionally set `PROVIDER` / `CHAT_MODEL` (see `config.py`).
4. Make the hook scripts executable: `chmod +x .claude/hooks/*.py`.
5. Start Claude Code in the folder (`claude`), approve the project hooks when prompted, and run `/lesson`.

## What's inside

| File | Type | Purpose |
|---|---|---|
| `CLAUDE.md` | Guide | Mentor rules; imports `learner-profile.md` and `progress.md` |
| `.claude/skills/lesson` | Guide | `/lesson [step]` — teach the next step |
| `.claude/skills/quiz` | Guide | `/quiz` — spaced repetition on weak spots |
| `.claude/skills/checkpoint-review` | Guide → sensor | `/checkpoint-review <phase>` — forks an isolated reviewer |
| `.claude/skills/log-progress` | Guide | `/log-progress` — keep `progress.md` current |
| `.claude/agents/checkpoint-reviewer.md` | Inferential sensor | Independent reviewer that writes `reviews/phase-N.md` |
| `.claude/hooks/session_context.py` | Computational guide | SessionStart: injects today's date and installed package versions |
| `.claude/hooks/checkpoint_gate.py` | Computational sensor | Blocks marking a checkpoint "passed" without a PASS review on file |
| `.claude/settings.json` | Constraint | Edits under `projects/` always ask first; `.env` is unreadable |
| `config.py` | Guide | The only place provider and model IDs live |

## Adapting it

Treat the kit like any harness: when the mentor makes the same mistake twice, fix it in the harness
rather than repeating yourself. Prefer a hook or a check (something that *runs*) over another sentence in `CLAUDE.md`.
Write down why each rule exists, and delete rules that newer models no longer need.
