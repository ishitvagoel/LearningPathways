---
name: checkpoint-review
description: Independent review of a phase's checkpoint project against the curriculum's completion criteria. Runs in an isolated reviewer context and writes a verdict to reviews/.
argument-hint: "<phase number> [path to project, default projects/phase-<N>]"
disable-model-invocation: true
context: fork
agent: checkpoint-reviewer
background: false
---

Review the checkpoint project for phase `$ARGUMENTS`.

1. Find that phase's "🔨 Checkpoint" section in `curriculum/` and list its tasks and completion criteria verbatim.
2. Inspect the project (default `projects/phase-<N>/`): read the code and README, and run its tests and eval scripts if they exist. Don't modify any file except the review file below.
3. For each criterion, record **met / partly met / not met**, with evidence (file:line, command output).
4. Check for the recurring problems: hard-coded provider or model IDs instead of `config.py`, secrets in code, tools that write or spend without approval or budgets, no evals, deprecated APIs.
5. Write `reviews/phase-<N>.md` containing the criteria table, the three most important improvements, and a final line that is exactly `VERDICT: PASS` or `VERDICT: REVISE`.
6. Return a short summary with the verdict.

Be rigorous and specific; a PASS the learner didn't earn is worse than a REVISE.
