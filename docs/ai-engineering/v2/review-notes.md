---
title: V2 Review & Research Notes
description: The audit of the V1 curricula, the September 2026 industry research behind V2, and every source used.
icon: material/clipboard-search
tags:
  - AI
  - Curriculum
---

# V2 Review & Research Notes

**Reviewed and researched: September 2026**

This page explains *why* V2 exists: what the review of V1 found, what the industry research showed, and which decisions follow from it. V1 files are untouched and remain in the site under **AI Engineering → V1 (March 2026)**.

Sections 1–5 record the original V2 research. **Section 0** records the late-September revision: a second research pass, the switch to a provider-neutral curriculum, and the Claude harness files.

---

## 0. Revision — late September 2026

### What prompted it

A stress test of V2 asked whether the curriculum covered *harness engineering*, OpenClaw and Hermes. It didn't, and a second research pass found more gaps. The owner also asked to **remove the dependency on Gemini** and to deliver the curriculum through **Claude harness files** instead of "paste this into an assistant".

### New findings from the second research pass

| Topic | Evidence | Where it landed |
|---|---|---|
| **Harness engineering** — agent = model + harness; guides vs sensors | OpenAI *Harness engineering* (Feb 2026); Böckeler on martinfowler.com (Apr 2026); Marmelab *State of AI Harness Engineering 2026*: 60% of harnesses had no tests; it also cites a Composio vendor experiment (same model, 68–88% across eight harnesses, 25 tasks) and an arXiv study (only 4–16% of written `CLAUDE.md` security rules had a measurable effect) | Mastery Plan Phase 0 and new Phase 6; LangChain Step 5.6; the harness kit itself |
| **Agentic engineering** replacing "vibe coding" | Karpathy, Sequoia AI Ascent (Apr 2026) | Mastery Plan intro and Phase 0 |
| **Loop engineering, skills everywhere, coding agents replacing IDEs, forward-deployed engineers** | AI Engineer World's Fair 2026 recap (Latent Space, July 2026) | Phase 5 (skills), Phase 6 (loops) |
| **Ambient/scheduled agents and managed agent platforms** | Claude Managed Agents public beta (Apr 2026); Claude Code routines (schedule, API and GitHub triggers; fire payloads labelled untrusted); Code with Claude (May 2026) | Phase 6; LangChain Step 5.7; harness-choice table in Phase 5 |
| **Personal agent harnesses** as a security case study | OpenClaw (≈247k stars by Mar 2026; malicious ClawHub skills; sandboxing off by default in 2.0; restrictions in China); Hermes Agent (Nous Research, Feb 2026; self-written skills) | Phase 6 teardown (sandboxed only); "what not to spend time on" |
| **Multi-agent limits** | Marmelab: a reviewer agent lowered success 8% in one ablation; more than 4 handoffs almost always failed | LangChain Step 5.4; "what not to spend time on" |
| **Computer use reality check** | OSWorld-Human (v2, May 2026): even the best agents take 2.7–4.3× more steps than necessary, with large latency; newer long-horizon benchmarks (OSWorld 2.0) report much lower success | Phase 5 electives |
| **RL environments and verifiers**, reward hacking | Industry analyses of the RL-environment market (e.g. Wing VC, 2026); RLVR practice | Phase 8 |
| **Agent identity** | OAuth 2.1 per-agent clients; MCP authorization; workload identity (SPIFFE/WIMSE) | Phase 7 |
| **Regulation** | EU Digital Omnibus in force 27 Jul 2026: high-risk obligations deferred to Dec 2027 / Aug 2028; most Art. 50 transparency duties applied from 2 Aug 2026 | Phase 7 |
| **Agentic payments** (awareness) | ACP (Stripe, OpenAI and Meta), AP2 (Google; donated to the FIDO Alliance Apr 2026), MPP (Stripe/Tempo, Mar 2026) | Phase 7 |
| **Cost patterns** | Anthropic's advisor pattern (Code with Claude, May 2026); effort as a cost lever | LangChain Step 6.5; Phase 7 checklist |

### Provider-neutral rewrite

- Every example builds models from `config.py` (`PROVIDER` + `model_id()`), so switching provider is a configuration change.
- Claude is the *reference* provider because the same vendor ships the harness the curriculum uses. Its model IDs and parameters are checked against Anthropic's models overview: `claude-opus-5-5` default (updated from `claude-opus-5` after the reviewer pass below), `claude-sonnet-5` judge, `claude-haiku-4-5` fast; adaptive thinking + `effort`; sampling parameters rejected on 4.7-and-later models. **Watch list:** Haiku 4.5 has no `effort` support and its retirement commitment is only "not sooner than 15 Oct 2026".
- Embeddings moved to a **local open-source model** (`sentence-transformers/all-mpnet-base-v2` via `langchain-huggingface`), removing any vendor dependency from retrieval.
- Gemini-specific material (the Interactions API, `thinking_level`, the Gemini temperature caveat, Gemini embedding models) was removed or generalised.
- The old `GEMINI.md` was replaced by a tool-neutral `AGENTS.md` plus a `CLAUDE.md` that imports it.

### Claude harness files

- **Mentor kit** (`mentor-kit/`): `CLAUDE.md`, four skills, a reviewer subagent, a SessionStart context hook and a checkpoint gate. It is packaged as `mentor-kit.zip` on deploy.
- **Repository harness**: `AGENTS.md`, `CLAUDE.md`, three skills, a reviewer subagent, deny rules for V1, a PostToolUse document checker and a Stop-time V1 guard.
- Every hook was tested with synthetic events, including negative cases. See [Claude Harness Kit](claude-harness.md).

### Claims deliberately not repeated

- Specific open-weight leaderboard rankings (sources disagree).
- Unverifiable percentage claims from vendor marketing about context engineering's impact.
- The exact adoption count for Agent Skills beyond "dozens of products".

### Additional sources (revision)

- OpenAI, *Harness engineering: leveraging Codex in an agent-first world* — <https://openai.com/index/harness-engineering/>
- B. Böckeler, *Harness engineering for coding agent users* — <https://martinfowler.com/articles/harness-engineering.html>
- Marmelab, *The State of AI Harness Engineering 2026* — <https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html>
- Anthropic, *Effective harnesses for long-running agents* — <https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>
- Anthropic, *Writing effective tools for agents* — <https://www.anthropic.com/engineering/writing-tools-for-agents>; *Code execution with MCP* — <https://www.anthropic.com/engineering/code-execution-with-mcp>; *Contextual Retrieval* — <https://www.anthropic.com/news/contextual-retrieval>
- Latent Space, *5 Trends That Defined AI Engineering at World's Fair 2026* — <https://www.latent.space/p/aiewf26trends>
- A. Karpathy, *Sequoia Ascent 2026* notes — <https://karpathy.bearblog.dev/sequoia-ascent-2026/>
- The Pragmatic Engineer, *The impact of AI on software engineers in 2026* — <https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026>
- Claude Managed Agents announcement — <https://claude.com/blog/claude-managed-agents>; docs — <https://platform.claude.com/docs/en/managed-agents/overview>
- InfoQ, *Code with Claude 2026* — <https://www.infoq.com/news/2026/05/code-with-claude/>
- Claude Code docs: routines <https://code.claude.com/docs/en/routines>, memory <https://code.claude.com/docs/en/memory>, skills <https://code.claude.com/docs/en/skills>, subagents <https://code.claude.com/docs/en/sub-agents>, hooks <https://code.claude.com/docs/en/hooks>, permissions <https://code.claude.com/docs/en/permissions>
- Claude Platform docs: effort <https://platform.claude.com/docs/en/build-with-claude/effort>, extended thinking <https://platform.claude.com/docs/en/build-with-claude/extended-thinking>, prompt caching <https://platform.claude.com/docs/en/build-with-claude/prompt-caching>
- LangChain Anthropic integration — <https://docs.langchain.com/oss/python/integrations/chat/anthropic>; embedding integrations — <https://docs.langchain.com/oss/python/integrations/text_embedding>
- OpenClaw — <https://en.wikipedia.org/wiki/OpenClaw>, <https://docs.openclaw.ai/>; Hermes Agent — <https://hermes-agent.nousresearch.com/>
- EU AI Act omnibus analysis (Jones Walker) — <https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon>
- Stripe, Agentic Commerce Protocol — <https://docs.stripe.com/agentic-commerce/acp>
- Wing VC, *Who will win the RL environment market* — <https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why>

### Reviewer pass (28–29 September 2026)

After publication, the repo's own `curriculum-reviewer` subagent reviewed every V2 page against primary sources. Its main findings were independently re-checked before being applied:

| Finding | Correction |
|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) is now Anthropic's current Opus; Opus 5 is legacy | Default model updated in the LangChain Path and mentor kit; Opus 5.5 behaviour notes added (default effort `medium`, thinking always on, forced tool choice rejected) |
| Haiku 4.5 has no `effort` or adaptive thinking | Phase 1 effort sweep moved to Sonnet 5 / Opus 5.5; "current Claude models reject X" claims scoped to the right generations |
| Agent Skills is *not* stewarded by the AAIF | Corrected: AAIF hosts MCP, AGENTS.md, goose, agentgateway and A2A; Agent Skills was only proposed (Sept 2026, vote pending) |
| "Agents trail humans by ~30 points" on OSWorld had no source | Removed; replaced with OSWorld-Human's measured step inefficiency |
| Three LangChain snippets couldn't do what the page claimed (interrupt graph, idempotent ambient job, persistent FastAPI threads) | Rewritten; missing imports added |
| Marmelab statistics were attributed to Marmelab's own experiments | Attributed to the underlying Composio experiment and arXiv study |
| Unsourced "36% of skills" | Cited to Snyk ToxicSkills (Feb 2026; any severity; 13.4% critical) and Koi Security |
| Both curricula number phases from 0, so mentor-kit reviews collided | Checkpoints and reviews keyed by path (`mastery` / `langchain`), with a negative test for the collision |
| The V1 Stop guard's reach was overstated, and a committed change bypassed it | Page reworded; pinned SHA-256 check for V1 added to `check_docs.py --all`, which CI runs |
| Smaller items | Claude Code in Action moved to Phase 6 (course content changed), MCP Logging/HTTP+SSE deprecation wording, paid-item costs (Maven cohort ~$4,200), course durations, LangSmith Studio rename, ACP/AP2 attribution, EU primary source |

**Applied after the owner approved them:** two hook-configuration suggestions in `settings.json`. Hook commands now quote `"${CLAUDE_PROJECT_DIR}"`, so they work when the project path contains spaces; unquoted, the shell split such a path and the hook failed to start. The mentor kit's SessionStart matcher now includes `fork`, so forked sessions also get the date and package versions. All four hooks were re-run from a directory with a space in its path, including the checkpoint gate's blocking case.

**Sources added in this pass:** Anthropic models overview <https://platform.claude.com/docs/en/about-claude/models/overview>; model deprecations <https://platform.claude.com/docs/en/about-claude/model-deprecations>; AAIF Agent Skills proposal <https://github.com/aaif/project-proposals/issues/47>; A2A joins AAIF <https://aaif.io/blog/a2a-joins-aaif>; OSWorld-Human <https://arxiv.org/abs/2506.16042>; Snyk ToxicSkills <https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/>; Koi Security ClawHavoc findings, as reported by The Hacker News (the original Koi blog now redirects to Palo Alto Networks) <https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html>; AP2 to FIDO Alliance <https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/>; EU AI Omnibus <https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force>; OWASP Agentic Top 10 <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>; LangSmith Studio <https://docs.langchain.com/langsmith/studio>; langgraph-checkpoint-postgres <https://pypi.org/project/langgraph-checkpoint-postgres/>.

---

## 1. Review of V1 — LangChain Path

### Code that no longer runs or was never correct

| # | V1 content | Problem | V2 fix |
|---|---|---|---|
| 1 | `ChatGoogleGenerativeAI(model="gemini-2.0-flash")` in every example | Gemini 2.0 Flash is **shut down** on the Gemini API | Model IDs centralised in `config.py`; default `gemini-3.8-flash` *(superseded by Section 0: provider-neutral, Claude reference)* |
| 2 | `from langchain.agents import create_react_agent` presented as the LangChain 1.0 agent API (and in the "What replaced it" column) | LangChain 1.0's agent API is `create_agent`; `langgraph.prebuilt.create_react_agent` is the *deprecated* one | All agents use `create_agent`; deprecation table corrected |
| 3 | "LCEL pipe syntax deprecated" | Inaccurate: Runnables/LCEL remain in `langchain-core`; what moved to `langchain-classic` are legacy *chains* and some retrievers | Explicit correction note in V2 |
| 4 | `from langchain_core.pydantic_v1 import BaseModel` | Pydantic v1 shim removed; LangChain 1.x is Pydantic v2 | Plain `pydantic` imports |
| 5 | `args_schema.schema()` | Pydantic v1 method | `tool.args` / `model_json_schema()` |
| 6 | `models/text-embedding-004` | Superseded | `gemini-embedding-001` *(superseded by Section 0: local open-source embeddings)* |
| 7 | `from langchain_community.vectorstores import Chroma` | Replaced by the dedicated package | `from langchain_chroma import Chroma` |
| 8 | `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY` | Legacy variable names | `LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT` |
| 9 | `graph.set_entry_point(...)` | Legacy | `add_edge(START, ...)` |
| 10 | `interrupt_before` / `interrupt_after` for human approval | Superseded | `interrupt()` + `Command(resume=...)`; `HumanInTheLoopMiddleware` for agents; `version="v2"` → `result.interrupts` |
| 11 | "LangGraph Platform" | Renamed **LangSmith Deployment** (Oct 2025) | Updated |
| 12 | "Era 5 … September 2025" | LangChain/LangGraph 1.0 went GA on **20 Oct 2025** | Corrected; Era 6 (1.1 → 1.4) added |

### Gaps

- **Placeholders instead of lessons:** Steps 3.3 (middleware), 3.5 (custom graph), 3.6 (persistence), 3.7 (HITL) and 3.8 (multi-agent) contained "(Teach this…)" notes with no code. V2 provides runnable code for each.
- **Missing 2026 essentials:** context engineering, built-in middleware (retries, fallbacks, limits, PII, summarisation), MCP (now built into LangChain 1.4 as `langchain.mcp`), agent security/prompt injection, trajectory evals and evals-in-CI, Deep Agents, streaming v2, runtime context vs state, long-term memory stores, Gemini 3 thinking levels and the temperature caveat, the Interactions API (Google's default since mid-2026), multimodal content blocks. *(The Gemini-specific items were later generalised or removed; see Section 0.)*
- **Ordering:** V1 taught RAG before agents; V2 teaches agents first so retrieval can be taught both as a fixed pipeline *and* as an agent tool (agentic RAG), which is how it is used in 2026.

## 2. Review of V1 — AI Mastery Plan

| Area | Finding | V2 response |
|---|---|---|
| Evals | One course, buried in the RAG phase, although practitioners and hiring guides now call evals the key differentiator | New **Phase 4: Evaluation & observability**, placed *before* agents |
| Context engineering | Absent | Anchors Phase 3 |
| Coding agents | Absent, despite being the biggest change in day-to-day engineering work | New **Phase 0** |
| Security & governance | Absent (no prompt injection, OWASP, permissions) | New **Phase 7** (security, identity, governance, cost) |
| Inference / cost | Only LoRA/quantization; nothing on serving, caching or cost engineering | vLLM, semantic caching, production checklist |
| Post-training | RLHF only | SFT/DPO/online RL, GRPO reinforcement fine-tuning, TRL/Unsloth, nanochat |
| Aged resources | *Reasoning with o1*, *Prompt Engineering with Llama 2 & 3*, AutoGen course, "compare against GPT-4" | Marked optional/historical or replaced |
| Framework guide | PydanticAI "newest (Dec 2024)"; no Google ADK, Claude Agent SDK or Deep Agents; AutoGen recommended | Rewritten for Sept 2026 (AutoGen maintenance mode; Microsoft Agent Framework 1.0) |
| Redundancy | Three overlapping vector-DB short courses | Consolidated into the full RAG course + one advanced-retrieval course |
| Repo standard | GEMINI.md requires a learner profile, mentor instructions, checkpoint projects and a "what not to teach" list; V1 lacked most of these | Added to V2 |
| Links | All V1 course links were checked in September 2026 and still resolve — the problem was *what* they point to, not broken URLs | Every V2 link was checked the same way |

## 3. What the industry research showed (September 2026)

1. **Demand shifted to agentic systems.** Stanford AI Index 2026: AI skills appear in 2.5% of US job postings; the "Agentic AI" skill cluster grew >280% in a year; LangGraph was among the fastest-growing skills; ChatGPT/chatbot skills declined.
2. **Production reality** (Datadog, July 2026): system prompts ≈ 69% of input tokens; only ≈ 28% of LLM calls use prompt caching; >70% of organisations use ≥ 3 models; agent-framework usage roughly doubled; rate limits ≈ ⅓ of LLM call failures.
3. **Context engineering** (Anthropic, Sept 2025) became the organising concept for agent design: context rot, attention budget, just-in-time retrieval, compaction, note-taking, sub-agents.
4. **Evals**: error analysis → validated judges → CI gates is the consensus workflow (Husain & Shankar; LangSmith pytest/Vitest integrations; openevals/agentevals).
5. **Standards**: MCP donated to the Linux Foundation's Agentic AI Foundation (Dec 2025); MCP spec **2026-07-28** made the protocol stateless and deprecated Sampling/Roots/Logging. Agent Skills published as an open standard (Dec 2025) and widely adopted. A2A reached v1.0 (early 2026) under the Linux Foundation.
6. **Platform changes**: OpenAI Assistants API shut down 26 Aug 2026; AutoGen in maintenance mode; Microsoft Agent Framework 1.0 GA (Apr 2026); LangChain 1.4 ships MCP in core (Sept 2026); Gemini's Interactions API became Google's default interface (June 2026) with `generateContent` labelled legacy; Gemini 2.0 models shut down, Gemini 3.8 Flash stable.
7. **Coding agents** (Anthropic 2026 Agentic Coding Trends Report): engineers moving from implementer to orchestrator, with only a small share of tasks fully delegable — supervision and context are the skills.
8. **Open weights & post-training**: strong open-weight families (Qwen, DeepSeek, GLM, Kimi, gpt-oss, Gemma) and accessible RL fine-tuning (GRPO) make "measure, then adapt a small model" a realistic option.

!!! warning "Claims we deliberately did not repeat"
    Several secondary sites describe an "MCP 2.0" ratified in 2026. The official specification has no such version; the current revision is dated **2026-07-28**. Open-weight leaderboard numbers vary wildly between sites, so V2 names model families without ranking them and tells learners to decide with their own evals.

## 4. Design decisions in V2

- **Keep V1 intact**; V2 lives in `docs/ai-engineering/v2/` and is the default in the navigation. (Because V2 had not yet been published when the late-September revision was made, the revision was applied to V2 in place; from now on published versions are frozen.)
- **Order by dependency and by what's hired for:** agentic engineering → build → retrieve/context → **evaluate** → agents → **harness & ambient agents** → **secure/operate** → internals/post-training.
- **Every phase ends in a checkpoint project**, and from Phase 4 on, every project ships with evals.
- **Volatile facts are isolated** (model IDs in config; "check the docs" rules for the teaching model) so the next refresh is cheaper.

## 5. Sources

- LangChain changelog — <https://docs.langchain.com/oss/python/releases/changelog>
- LangChain 1.0 migration guide — <https://docs.langchain.com/oss/python/migrate/langchain-v1>
- LangChain agents, middleware, human-in-the-loop, MCP, tools, retrieval, context-engineering docs — <https://docs.langchain.com/oss/python/langchain/overview>
- LangGraph interrupts & streaming docs — <https://docs.langchain.com/oss/python/langgraph/interrupts>, <https://docs.langchain.com/oss/python/langgraph/streaming>
- Deep Agents overview — <https://docs.langchain.com/oss/python/deepagents/overview>
- LangSmith observability quickstart & trajectory evals — <https://docs.langchain.com/langsmith/observability-quickstart>, <https://docs.langchain.com/langsmith/trajectory-evals>
- LangChain Google GenAI integration — <https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai>
- Gemini API models, Interactions API, thinking — <https://ai.google.dev/gemini-api/docs/models>, <https://ai.google.dev/gemini-api/docs/interactions>, <https://ai.google.dev/gemini-api/docs/thinking>
- MCP specification 2026-07-28 changelog — <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- MCP joins the Agentic AI Foundation — <https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/>
- Agent Skills — <https://agentskills.io/home>
- A2A one-year announcement (Linux Foundation) — <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year>
- OpenAI Assistants API deprecation — <https://developers.openai.com/api/docs/deprecations>
- Microsoft Agent Framework — <https://learn.microsoft.com/en-us/agent-framework/>; AutoGen repository status — <https://github.com/microsoft/autogen>
- Anthropic, *Effective context engineering for AI agents* — <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
- Anthropic, *2026 Agentic Coding Trends Report* — <https://resources.anthropic.com/2026-agentic-coding-trends-report>
- Stanford HAI, *AI Index 2026* — <https://hai.stanford.edu/ai-index/2026-ai-index-report>
- Datadog, *State of AI Engineering* — <https://www.datadoghq.com/state-of-ai-engineering/>
- OWASP Gen AI Security Project — <https://genai.owasp.org/>
- Simon Willison, *The lethal trifecta* — <https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/>
- Hamel Husain & Shreya Shankar, evals FAQ and course — <https://hamel.dev/blog/posts/evals-faq/>, <https://maven.com/parlance-labs/evals>
- DeepLearning.ai course catalogue — <https://www.deeplearning.ai/courses/>
- Stanford CS336 (Spring 2026) — <https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV>
- Sebastian Raschka, *Build a Reasoning Model (From Scratch)* — <https://sebastianraschka.com/reasoning-from-scratch/>
