---
name: add-learning-path
description: Scaffold a new learning path page in the house format (frontmatter, mentor instructions, learner profile, phases with checkpoints, what-not-to-teach) and wire it into the nav and landing page. Use when adding a new topic path.
argument-hint: "[topic-slug] [one-line description]"
---

# Add a learning path: $ARGUMENTS

1. **Clarify scope with the user** if the topic, target learner or length is unclear. Ask once, grouped.
2. Create `docs/ai-engineering/<current-version>/<topic-slug>.md` (or a new top-level topic folder if it isn't AI engineering) with:
   - YAML frontmatter: `title`, `description`, `icon`, `tags`
   - `## Instructions For The Teaching Model` — numbered rules; point to the Claude Harness Kit
   - `## Learner Profile` — background, gaps, goal, time budget
   - `## What NOT To Teach` — deprecated patterns with their replacements
   - `## Phase 0: ...` through the final phase; each phase ends with `### 🔨 Phase N Checkpoint Project`
   - Resource cards in the Quick Stats format used in `v2/ai-mastery-plan.md`
3. **Verify every resource** before listing it: fetch the URL, confirm the title matches, and record the source. Don't invent courses, durations or statistics; write "Short course (~1–2 hrs)" when the platform doesn't publish a duration.
4. Keep code provider-neutral (`config.py` with `PROVIDER` + `model_id()`).
5. Add the page to `mkdocs.yml` nav and, if it's a featured path, a card in `docs/index.md`.
6. Run `python3 scripts/check_docs.py <new file>` and `mkdocs build -d /tmp/site`; fix all problems.
