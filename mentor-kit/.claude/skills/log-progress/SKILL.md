---
name: log-progress
description: Update progress.md at the end of a session with the current position, checkpoint status and a one-line session log entry.
---

# Log progress

Update `progress.md`:

1. **Current position:** the next step to study, on the line for the path it belongs to (Mastery Plan or LangChain Path). Leave the other path's line as it is.
2. **Last session:** today's date.
3. **Checkpoints table:** one row per path and phase (`mastery` or `langchain`); update status from `reviews/<path>-phase-<N>.md` verdicts only (`VERDICT: PASS` means passed). If the learner chose to skip a checkpoint, record "overridden by learner" rather than "passed".
4. **Session log:** add one line at the top: date — what was covered — the learner's open questions.

Keep the file short: collapse session-log entries older than ten sessions into a single summary line.
