---
name: refresh-curriculum
description: Research-first workflow for producing a new version of the learning paths (e.g. v3) without touching earlier versions. Use when asked to update, refresh or revamp the curriculum for current industry trends.
argument-hint: "[new-version-folder, e.g. v3]"
disable-model-invocation: true
---

# Refresh the curriculum into `docs/ai-engineering/$ARGUMENTS/`

A curriculum refresh is research work first and writing second. Follow these steps in order.

## 1. Audit the current version
- Read every page in the newest `docs/ai-engineering/v*/` folder and its `review-notes.md`.
- Run `python3 scripts/check_docs.py --all` and `python3 scripts/check_links.py docs/ai-engineering/<current>/*.md`.
- List: code that no longer runs, retired model IDs, renamed or deprecated APIs, dead or moved courses, and claims that are now false.

## 2. Research what changed (primary sources first)
- **APIs and models:** provider docs and changelogs (LangChain release notes, Claude platform docs, other providers' model pages). Verify every function, parameter and model ID you will write.
- **Industry direction:** annual reports (Stanford AI Index, Datadog State of AI Engineering), practitioner writing (harness, context and eval engineering), conference recaps (AI Engineer World's Fair), and protocol specs (MCP, A2A, Agent Skills).
- **Courses:** the DeepLearning.ai catalogue, Anthropic Academy, Hugging Face Learn, LangChain Academy. Confirm each URL resolves to the course you name.
- Treat secondary "top 10" articles as leads, not evidence. When sources disagree, prefer the spec or the vendor's own docs, and note the disagreement.

## 3. Write the new version
- Copy the current folder to `$ARGUMENTS/` and edit there. **Never modify earlier versions.**
- Keep the house structure (see `AGENTS.md`): mentor instructions, learner profile, Phase 0…N, a 🔨 checkpoint per phase, a "what NOT to teach" list, resource cards in the Quick Stats format.
- Keep code provider-neutral via `config.py` + `model_id()`; Claude is the reference provider.
- Put volatile facts (model IDs, versions) in one clearly marked place per page.

## 4. Record the evidence
Write `$ARGUMENTS/review-notes.md` covering: the audit findings (with the old text and why it was wrong), the research findings (with dates), the design decisions, claims you deliberately did not repeat, and a full source list.

## 5. Wire up and validate
- Update `mkdocs.yml` (newest version first) and the cards in `docs/index.md`.
- Run `mkdocs build -d /tmp/site`, `python3 scripts/check_docs.py --all` and the link checker; fix every failure.
- Ask the `curriculum-reviewer` subagent for an accuracy review of the new pages and address its findings.
- Summarise for the user what changed, what you verified, and what you could not verify.
