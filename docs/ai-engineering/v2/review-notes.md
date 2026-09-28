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

---

## 1. Review of V1 — LangChain Path

### Code that no longer runs or was never correct

| # | V1 content | Problem | V2 fix |
|---|---|---|---|
| 1 | `ChatGoogleGenerativeAI(model="gemini-2.0-flash")` in every example | Gemini 2.0 Flash is **shut down** on the Gemini API | Model IDs centralised in `config.py`; default `gemini-3.8-flash` |
| 2 | `from langchain.agents import create_react_agent` presented as the LangChain 1.0 agent API (and in the "What replaced it" column) | LangChain 1.0's agent API is `create_agent`; `langgraph.prebuilt.create_react_agent` is the *deprecated* one | All agents use `create_agent`; deprecation table corrected |
| 3 | "LCEL pipe syntax deprecated" | Inaccurate: Runnables/LCEL remain in `langchain-core`; what moved to `langchain-classic` are legacy *chains* and some retrievers | Explicit correction note in V2 |
| 4 | `from langchain_core.pydantic_v1 import BaseModel` | Pydantic v1 shim removed; LangChain 1.x is Pydantic v2 | Plain `pydantic` imports |
| 5 | `args_schema.schema()` | Pydantic v1 method | `tool.args` / `model_json_schema()` |
| 6 | `models/text-embedding-004` | Superseded | `gemini-embedding-001` (and optional multimodal `gemini-embedding-2-preview`) |
| 7 | `from langchain_community.vectorstores import Chroma` | Replaced by the dedicated package | `from langchain_chroma import Chroma` |
| 8 | `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY` | Legacy variable names | `LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT` |
| 9 | `graph.set_entry_point(...)` | Legacy | `add_edge(START, ...)` |
| 10 | `interrupt_before` / `interrupt_after` for human approval | Superseded | `interrupt()` + `Command(resume=...)`; `HumanInTheLoopMiddleware` for agents; `version="v2"` → `result.interrupts` |
| 11 | "LangGraph Platform" | Renamed **LangSmith Deployment** (Oct 2025) | Updated |
| 12 | "Era 5 … September 2025" | LangChain/LangGraph 1.0 went GA on **20 Oct 2025** | Corrected; Era 6 (1.1 → 1.4) added |

### Gaps

- **Placeholders instead of lessons:** Steps 3.3 (middleware), 3.5 (custom graph), 3.6 (persistence), 3.7 (HITL) and 3.8 (multi-agent) contained "(Teach this…)" notes with no code. V2 provides runnable code for each.
- **Missing 2026 essentials:** context engineering, built-in middleware (retries, fallbacks, limits, PII, summarisation), MCP (now built into LangChain 1.4 as `langchain.mcp`), agent security/prompt injection, trajectory evals and evals-in-CI, Deep Agents, streaming v2, runtime context vs state, long-term memory stores, Gemini 3 thinking levels and the temperature caveat, the Interactions API (Google's default since mid-2026), multimodal content blocks.
- **Ordering:** V1 taught RAG before agents; V2 teaches agents first so retrieval can be taught both as a fixed pipeline *and* as an agent tool (agentic RAG), which is how it is used in 2026.

## 2. Review of V1 — AI Mastery Plan

| Area | Finding | V2 response |
|---|---|---|
| Evals | One course, buried in the RAG phase, although practitioners and hiring guides now call evals the key differentiator | New **Phase 4: Evaluation & observability**, placed *before* agents |
| Context engineering | Absent | Anchors Phase 3 |
| Coding agents | Absent, despite being the biggest change in day-to-day engineering work | New **Phase 0** |
| Security & governance | Absent (no prompt injection, OWASP, permissions) | New **Phase 6** |
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

- **Keep V1 intact**; V2 lives in `docs/ai-engineering/v2/` and is the default in the navigation.
- **Order by dependency and by what's hired for:** build → retrieve/context → **evaluate** → agents → **secure/operate** → internals/post-training.
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
