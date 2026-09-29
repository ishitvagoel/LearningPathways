---
name: checkpoint-review
description: Independent review of a phase's checkpoint project against the curriculum's completion criteria. Runs in an isolated reviewer context and writes a verdict to reviews/.
argument-hint: "<mastery|langchain> <phase number> [project dir, default projects/<path>-phase-<N>]"
disable-model-invocation: true
context: fork
agent: checkpoint-reviewer
background: false
---

Review the checkpoint project for `$ARGUMENTS` (a path — `mastery` = `curriculum/ai-mastery-plan.md`, `langchain` = `curriculum/langchain-path.md` — and a phase number). If the path is missing, stop and ask for it: both curricula number phases from 0.

1. Find that phase's "🔨 Checkpoint" section in the matching curriculum page and list its tasks and its pass criteria verbatim (the "Done when" list in the Mastery Plan, "Completion Criteria" in the LangChain Path). Judge against those criteria; the tasks define the scope. If a section has no criteria, say so in the review and treat each task as a criterion, rather than inventing new ones.
2. Inspect the project (default `projects/<path>-phase-<N>/`): read the code and README, and run its tests and eval scripts if they exist. Don't modify any file except the review file below.
3. For each criterion, record **met / partly met / not met**, with evidence (file:line, command output).
4. Check for the recurring problems: hard-coded provider or model IDs instead of `config.py`, secrets in code, tools that write or spend without approval or budgets, no evals, deprecated APIs.
5. Write `reviews/<path>-phase-<N>.md` containing the criteria table, the three most important improvements, and a final line that is exactly `VERDICT: PASS` or `VERDICT: REVISE`.
6. Return a short summary with the verdict.

Be rigorous and specific; a PASS the learner didn't earn is worse than a REVISE.
