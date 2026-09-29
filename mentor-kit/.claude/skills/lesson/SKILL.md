---
name: lesson
description: Teach the learner's next curriculum step (or a named one) from first principles, with runnable provider-neutral code and a Socratic check. Use when the learner wants to continue learning or asks to be taught a step.
argument-hint: "[optional step, e.g. 2.3 or 'Phase 3 item 2']"
---

# Lesson

1. Find the step: `$ARGUMENTS` if given, otherwise the current position in `progress.md`. There is one position per path. If the learner follows both, use the Mastery Plan position, and teach a LangChain step when the Mastery Plan's "Doing both paths together" crosswalk places it in the current phase. Open the matching section in `curriculum/` and read only that section.
2. If the step depends on a concept the learner hasn't covered (check the session log), teach the missing prerequisite briefly first and say so.
3. Teach it:
   - **The problem:** what breaks without this concept (a concrete failure, ideally in the learner's own projects).
   - **The mental model:** an analogy, and where the analogy stops working.
   - **The code:** a minimal runnable example that imports from `config.py`. Check APIs against the installed versions in the session context; if you're unsure, verify in the official docs before showing code.
   - **What it abstracts:** one sentence on what's happening underneath.
4. Ask **one** question that needs reasoning (e.g. "what would break if we removed X?"). Wait for the answer; correct misconceptions directly.
5. If the step is a resource (course or article) rather than a lesson, give a 3-bullet "what to watch for" guide, then quiz on it when the learner returns.
6. Finish by proposing the next step, and remind the learner to run `/log-progress` (or run it if they agree).
