---
title: AI Developer Mastery Plan (V2)
description: A 2026-current roadmap from web developer to production AI engineer — context engineering, evals, agents, security and post-training.
icon: material/rocket-launch
tags:
  - AI
  - Career
  - Agents
  - Evals
---

# The AI Developer Mastery Plan for Web Developers (V2)

**Curriculum V2 · researched September 2026**

!!! abstract "What changed from V1"
    V1 (March 2026) is preserved unchanged at [AI Mastery Plan (V1)](../ai-mastery-plan.md). V2 re-orders the plan around what the industry now hires for — **building and evaluating agentic systems** — and adds five things V1 was missing or under-weighted: **working with coding agents, context engineering, a dedicated evals phase, agent security & governance, and modern post-training (RL fine-tuning)**. It also retires resources that aged out (o1-specific prompting, Llama 2 prompt formats, AutoGen for new projects) and updates the framework guide. Progress you made on V1 carries over — see the [carry-over table](#v1-progress-carry-over). The full audit and sources are in [V2 Review & Research Notes](review-notes.md).

You're still in an ideal position to move from web development into AI engineering. Your Python/Flask/Django background is the part most AI courses assume you lack: APIs, state, auth, deployment, testing. The core of AI engineering in 2026 is *systems work around models* — deciding what goes into the model's context, wiring tools, measuring quality, and keeping costs, latency and risk under control. As Andrej Karpathy put it, you can be very successful in this role "without ever training anything"; V2 still teaches internals and fine-tuning, but *after* you can ship and evaluate systems, because that's where they pay off.

---

## Why the plan changed: what the evidence says (2025 → 2026)

**1. Demand moved from "prompting" to "agentic systems".** The Stanford *AI Index 2026* reports AI skills in 2.5% of all US job postings, with the "Agentic AI" skill cluster up more than 280% in a year, and LangGraph among the fastest-growing named skills; postings mentioning ChatGPT/chatbots as a skill *declined*. Employers want people who build and manage systems, not people who write clever prompts.

**2. Evals became the differentiator.** Practitioners (e.g., Hamel Husain and Shreya Shankar, who have trained thousands of engineers on evals) and hiring guides converge on the same point: teams that can't measure quality can't ship safely. V1 had one evaluation course buried in the RAG phase; V2 gives evals their own phase *before* agents.

**3. Context engineering replaced prompt engineering as the core craft.** Anthropic's *Effective context engineering for AI agents* (Sept 2025) framed the job as curating "the smallest possible set of high-signal tokens". Datadog's *State of AI Engineering* (July 2026) shows why it matters in practice: system prompts are ~69% of input tokens, only ~28% of LLM calls use prompt caching, >70% of organisations use three or more models, and rate limits cause about a third of LLM call failures.

**4. Standards consolidated.** MCP (tools/context) and Agent Skills (packaged instructions) are now stewarded by the Linux Foundation's Agentic AI Foundation; MCP's July 2026 spec revision made the protocol stateless. A2A (agent-to-agent) reached v1.0 in early 2026 under the Linux Foundation. OpenAI's Assistants API shut down on 26 Aug 2026 (replaced by the Responses API); Microsoft put AutoGen into maintenance mode and shipped Microsoft Agent Framework 1.0 (April 2026).

**5. Coding agents changed how engineers work.** Anthropic's *2026 Agentic Coding Trends Report* describes engineers shifting from implementer to orchestrator of agents, while noting developers can "fully delegate" only a small fraction of tasks — supervision, validation and good context are the skill. Learning to use coding agents well is now part of the job, and it accelerates everything else in this plan.

**6. Post-training went mainstream.** Reinforcement fine-tuning (e.g., GRPO) and open tooling (TRL, Unsloth) made "teach a small model a narrow skill" accessible; strong open-weight families (Qwen, DeepSeek, GLM, Kimi, gpt-oss, Gemma) make self-hosting realistic. This justifies a modern internals/post-training phase — still after evals, because you can't fine-tune toward a target you can't measure.

---

## Learner Profile

- **Background:** Web developer with strong Python (Flask/Django), REST APIs, databases, auth, deployment.
- **Already completed:** *AI for Everyone*, *Generative AI for Everyone*, and (in progress in V1) *ChatGPT Prompt Engineering for Developers*.
- **Gaps:** LLM internals, retrieval, evaluation methodology, agent architectures, AI security, model adaptation.
- **Goal:** Become a production-grade AI engineer who can design, build, evaluate, secure and operate LLM-powered and agentic systems.
- **Time budget assumed:** ~8–10 hours/week. At that pace the plan takes ~8 months; double the hours and it takes ~4.
- **Budget:** $0 core path; optional paid items are marked.

## How to use this plan with an AI mentor

Paste this page into your AI assistant of choice and ask it to act as a mentor with these rules: (1) one resource or concept per session; (2) explain *why* before *how*; (3) quiz with reasoning questions, not recall; (4) don't advance until the phase's checkpoint project is attempted; (5) verify fast-changing facts (model IDs, SDK APIs) against official docs rather than memory; (6) track which phase you're in. For LangChain-specific depth, switch to the [LangChain Path (V2)](langchain-path.md) at Phase 5.

---

## V1 progress carry-over

| If you finished this in V1… | …it counts toward V2 | Notes |
|---|---|---|
| Phase 1 prompt engineering courses | Phase 1 | Principles still hold; ignore model-specific API syntax |
| *Reasoning with o1*, *Prompt Engineering with Llama 2 & 3* | Phase 1 (optional) | Now optional/historical; see Phase 1 for the current view of reasoning models |
| Phase 2 LLM API courses, MCP course | Phase 2 | Re-read the MCP section: the protocol changed in July 2026 |
| Phase 3 RAG courses | Phase 3 | Add the context-engineering reading |
| *Building and Evaluating Advanced RAG* | Phase 4 | Then do the new evals resources |
| Phase 4 internals courses | Phase 7 | Internals moved later; nothing lost |
| Phase 5 agent courses | Phase 5 | AutoGen course is now optional; see the framework guide |

---

## Phase 0: Your AI-augmented workflow (Week 1)

Before learning *about* AI systems, learn to work *with* one. Coding agents will write a lot of the boilerplate in this plan; your job is to specify, supervise and verify. Doing this first compounds over every later phase.

### 1. Claude Code: A Highly Agentic Coding Assistant { #claude-code-course }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Elie Schoppik (Anthropic)

**Description:**
How an agentic coding tool explores a codebase, plans, edits and runs code — and how to steer it with context files, subagents and MCP servers.

- Treat the agent as a fast junior engineer: give it a spec, review its diffs, run the tests
- Learn the vocabulary (context files, subagents, hooks, MCP) you'll meet again when *building* agents in Phase 5

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant){ .md-button .md-button--primary }

### 2. Spec-Driven Development with Coding Agents { #spec-driven-dev }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** JetBrains

**Description:**
Writing specifications that agents can execute reliably — the antidote to "vibe coding" that doesn't survive contact with production.

- Specs, acceptance criteria and tests as the contract between you and the agent
- Directly transferable to writing tool descriptions and system prompts later

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents){ .md-button .md-button--primary }

### 3. Claude Code in Action (optional) { #claude-code-in-action }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Academy
    - **Cost:** Free
    - **Duration:** Self-paced

**Description:**
Anthropic's own course on integrating a coding agent into day-to-day development: workflows, context management and extending it with tools. Take it if you want more depth than the DeepLearning.ai course.

[**Visit Course :octicons-arrow-right-24:**](https://anthropic.skilljar.com/claude-code-in-action){ .md-button .md-button--primary }

### 🔨 Phase 0 checkpoint

Use a coding agent to add one small feature to an existing Flask/Django project *from a written spec*, with tests written first. Keep a short log: where did the agent go wrong, and what context would have prevented it? (You'll reuse this log when you design agent context in Phase 3.)

---

## Phase 1: LLM foundations and mental models (Weeks 1–3)

Goal: an accurate mental model of what an LLM is, how it's trained, why it hallucinates, and how "reasoning" models differ — enough to predict behaviour and debug it.

### 1. ChatGPT Prompt Engineering for Developers ✅ { #prompt-eng-dev }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Isa Fulford (OpenAI) & Andrew Ng

**Description:**
Finish this if you haven't. The *principles* (clear instructions, give the model time to think, iterate systematically) are timeless; the API syntax is dated — don't copy it.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/){ .md-button .md-button--primary }

### 2. Karpathy: "Deep Dive into LLMs like ChatGPT" { #karpathy-deep-dive }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~3.5 hrs

**Instructor(s):** Andrej Karpathy

**Description:**
The best single overview of the LLM lifecycle: pretraining, tokenization, post-training (SFT, RLHF), hallucinations, tool use, and reinforcement-learned reasoning. No code required.

- Explains *why* models are bad at spelling and counting (tokens) and why tools fix it
- Gives you the vocabulary for Phase 7

[**Watch Video :octicons-arrow-right-24:**](https://www.youtube.com/watch?v=7xTGNNLPyMI){ .md-button .md-button--primary }

### 3. 3Blue1Brown: Neural networks and transformers { #3b1b-neural }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~3 hrs total

**Instructor(s):** Grant Sanderson

**Description:**
Visual intuition for neural networks, gradient descent, backpropagation, and the transformer chapters ("Transformers, the tech behind LLMs", "Attention in transformers", "How might LLMs store facts"). Rewatch whenever a concept feels abstract.

[**Watch Series :octicons-arrow-right-24:**](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi){ .md-button .md-button--primary }

### 4. How Transformer LLMs Work { #how-transformer-llms-work }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Jay Alammar & Maarten Grootendorst

**Description:**
A code-light walkthrough of tokenizers, embeddings, attention and the modern transformer block (including mixture-of-experts), by the authors of *Hands-On Large Language Models*. Bridges the 3Blue1Brown intuition and the Phase 7 code.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/how-transformer-llms-work){ .md-button .md-button--primary }

### 5. Reasoning models in practice: thinking levels and budgets { #reasoning-models }

!!! info inline end "Quick Stats"
    - **Platform:** Gemini API docs (read the equivalent page for Claude/OpenAI too)
    - **Cost:** Free
    - **Duration:** ~1 hr reading + experiments

**Description:**
*Replaces V1's "Reasoning with o1".* In 2026 essentially every frontier model reasons before answering, controlled by a thinking level/effort/budget parameter. What matters now is not model-specific prompt tricks but trade-offs:

- More thinking = more latency and tokens; measure whether it improves *your* task
- Don't micro-manage the chain of thought; give clear goals and constraints
- Provider-specific gotchas (e.g., Gemini 3.x should stay at default temperature)

[**Read the Docs :octicons-arrow-right-24:**](https://ai.google.dev/gemini-api/docs/thinking){ .md-button .md-button--primary }

### 🔨 Phase 1 checkpoint

Pick three tasks (a factual lookup, a multi-step calculation, a classification). Run each on a small/fast model and a frontier model at two thinking levels. Record accuracy on 10 examples each, latency and cost in a table, and write a paragraph explaining the results using Karpathy's mental model (tokens, training, reasoning).

---

## Phase 2: Building LLM-powered applications (Weeks 4–7)

Your web background becomes a superpower: an LLM is a new, probabilistic dependency in a system you already know how to build.

### 1. Building Systems with the ChatGPT API { #building-systems }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Isa Fulford & Andrew Ng

**Description:**
Chaining calls into a pipeline: classify → moderate → reason → check output. The patterns are provider-independent and still the right foundation; the SDK syntax is dated.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/){ .md-button .md-button--primary }

### 2. Pydantic for LLM Workflows { #pydantic-llm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Description:**
Typed, validated data at every boundary: structured outputs, tool arguments, and API responses. Pydantic models are the lingua franca of LangChain, PydanticAI, OpenAI Agents SDK and FastAPI alike.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/pydantic-for-llm-workflows){ .md-button .md-button--primary }

### 3. Getting Structured LLM Output { #structured-output }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** DotTxt

**Description:**
How constrained decoding actually guarantees schema-valid output — the #1 fix for "the model returned almost-JSON".

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/getting-structured-llm-output/){ .md-button .md-button--primary }

### 4. Building with the Claude API { #claude-api-course }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Academy
    - **Cost:** Free
    - **Duration:** Self-paced (multi-hour)

**Description:**
A thorough, provider-official course on the full surface of a modern LLM API: messages, system prompts, tool use, prompt caching, extended thinking, RAG, and evaluation workflows. Even if you'll use Gemini or OpenAI in production, this is one of the most complete free treatments of *how an LLM API is meant to be used*.

[**Visit Course :octicons-arrow-right-24:**](https://anthropic.skilljar.com/claude-with-the-anthropic-api){ .md-button .md-button--primary }

### 5. MCP: Build Rich-Context AI Apps with Anthropic { #mcp-anthropic }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Elie Schoppik (Anthropic)

**Description:**
Build MCP servers and clients. MCP is the standard way to expose tools and data to any AI host (Claude, ChatGPT, Gemini CLI, IDEs, your own agents), now governed by the Linux Foundation's Agentic AI Foundation.

!!! warning "Protocol update"
    The 2026-07-28 MCP spec made the protocol **stateless** (no initialize handshake or sessions), deprecated *Sampling*, *Roots* and *Logging*, and moved long-running *Tasks* into an extension. Courses recorded earlier still teach the right mental model; check the [current spec](https://modelcontextprotocol.io/specification/latest) for wire-level details.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic){ .md-button .md-button--primary }

### 6. Hugging Face MCP Course (optional deeper dive) { #hf-mcp-course }

!!! info inline end "Quick Stats"
    - **Platform:** huggingface.co/learn
    - **Cost:** Free
    - **Duration:** ~10–15 hrs

**Description:**
A longer, hands-on MCP course: servers, clients, tools, resources and integrating with open models. Useful if MCP will be central to your work.

[**Visit Course :octicons-arrow-right-24:**](https://huggingface.co/learn/mcp-course){ .md-button .md-button--primary }

### 7. Open Source Models with Hugging Face { #os-models-hf }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Finding, running and serving open-weight models. In 2026 open-weight families (Qwen, DeepSeek, GLM, Kimi, gpt-oss, Gemma) are competitive for many tasks; choose by license, size and *your own* evals rather than leaderboards.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/open-source-models-hugging-face/){ .md-button .md-button--primary }

### 8. Udemy: LLM Engineering — Master AI and Large Language Models (optional, paid) { #udemy-llm-eng }

!!! info inline end "Quick Stats"
    - **Platform:** Udemy
    - **Cost:** ~$10–20 on sale
    - **Duration:** Long-form, project-based

**Instructor(s):** Ed Donner

**Description:**
Project-heavy survey (multi-model apps, Gradio UIs, RAG, QLoRA fine-tuning, agents). Good if you like building alongside an instructor; check the "last updated" date and skip lectures on retired models/APIs.

[**Visit Course :octicons-arrow-right-24:**](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/){ .md-button .md-button--primary }

### 🔨 Phase 2 checkpoint

Build a Flask/Django or FastAPI service with: (a) one endpoint that returns **schema-validated** structured output, (b) one tool-calling endpoint (manual tool loop, no framework), and (c) one MCP server exposing a capability from your own app, tested from an off-the-shelf MCP client. Log tokens and latency per request.

---

## Phase 3: Retrieval and context engineering (Weeks 8–11)

Retrieval is still the most common production pattern — but in 2026 it is taught as one tool within **context engineering**: choosing what enters the model's window, when, and in what form.

### 1. Effective context engineering for AI agents (essay) { #context-engineering }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Engineering blog
    - **Cost:** Free
    - **Duration:** ~30 min (read twice)

**Description:**
The clearest statement of the discipline: context rot, the attention budget, just-in-time retrieval, compaction, structured note-taking and sub-agents. Everything else in this phase is an implementation of these ideas.

[**Read Article :octicons-arrow-right-24:**](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents){ .md-button .md-button--primary }

### 2. Retrieval Augmented Generation (RAG) { #rag-course }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free to audit (check platform)
    - **Duration:** Multi-week course

**Description:**
DeepLearning.ai's full-length RAG course: retrieval fundamentals, hybrid search, chunking, re-ranking, evaluation and production concerns. *Replaces the V1 stack of three overlapping vector-DB short courses* with one coherent treatment.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag){ .md-button .md-button--primary }

### 3. Advanced Retrieval for AI with Chroma { #adv-retrieval-chroma }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Anton Troynikov (Chroma)

**Description:**
Query expansion, cross-encoder re-ranking and embedding adapters — the techniques that move retrieval from "works on the demo" to "works on real questions".

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/){ .md-button .md-button--primary }

### 4. Document AI: From OCR to Agentic Doc Extraction { #document-ai }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** LandingAI

**Description:**
Real-world data is PDFs, tables, scans and forms. This is the modern successor to V1's *Preprocessing Unstructured Data*: layout-aware parsing and agentic extraction that preserves structure for retrieval.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/document-ai-from-ocr-to-agentic-doc-extraction){ .md-button .md-button--primary }

### 5. Semantic Caching for AI Agents { #semantic-caching }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Redis

**Description:**
Reusing answers for *semantically* repeated questions — often the single biggest cost and latency win in a production assistant, and a good lesson in the precision/recall trade-offs of similarity thresholds.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/semantic-caching-for-ai-agents){ .md-button .md-button--primary }

### 6. Knowledge Graphs for RAG (optional) { #knowledge-graphs-rag }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Neo4j

**Description:**
Graph retrieval for domains where relationships matter (org charts, supply chains, codebases). Take it only if your domain is relationship-heavy; for most apps, hybrid search + re-ranking wins on effort.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/){ .md-button .md-button--primary }

### 🔨 Phase 3 checkpoint

Build a documentation assistant over your own docs (PDFs + Markdown). Implement **two** retrieval strategies (e.g., pure vector vs hybrid + re-ranking), a semantic cache, and citations. Create a 25-question test set and report retrieval hit rate@5 and answer faithfulness for each strategy. Then write down, for one long conversation, exactly what was in the context window at turn 10 and what you'd remove.

---

## Phase 4: Evaluation and observability (Weeks 12–14) — *new in V2*

You can't improve what you can't measure, and you can't safely ship agents you can't evaluate. This phase comes **before** agents on purpose: every agent you build afterwards gets an eval suite from day one.

### 1. AI Evals FAQ + free email course { #evals-faq }

!!! info inline end "Quick Stats"
    - **Platform:** hamel.dev
    - **Cost:** Free
    - **Duration:** ~3–4 hrs reading

**Instructor(s):** Hamel Husain & Shreya Shankar

**Description:**
The practitioner consensus on evals, distilled: start with **error analysis** (read traces, write notes, cluster failures, count them) before building metrics; prefer binary pass/fail judgements; validate every LLM judge against human labels; wire evals into CI.

[**Read the FAQ :octicons-arrow-right-24:**](https://hamel.dev/blog/posts/evals-faq/){ .md-button .md-button--primary }

### 2. Evaluating AI Agents { #evaluating-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Arize AI

**Description:**
Tracing an agent, evaluating router decisions, tool calls and trajectories (not just final answers), and running structured experiments when you change prompts or models.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/evaluating-ai-agents){ .md-button .md-button--primary }

### 3. NVIDIA NeMo Agent Toolkit: Making Agents Reliable { #nemo-reliable }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** NVIDIA

**Description:**
Turning a proof-of-concept agent into a production candidate with observability, evaluation and deployment tooling. A good complement to the Arize course's vendor perspective.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/nvidia-nat-making-agents-reliable){ .md-button .md-button--primary }

### 4. AI Evals for Engineers & PMs (optional, paid) { #maven-evals }

!!! info inline end "Quick Stats"
    - **Platform:** Maven (live cohort)
    - **Cost:** Paid — check site
    - **Duration:** Multi-week cohort

**Instructor(s):** Hamel Husain & Shreya Shankar

**Description:**
The most in-depth evals training available: data collection, error analysis, code-based and LLM-as-judge evaluators, RAG and agent evaluation, CI/CD and review interfaces. Their O'Reilly book *Evals for AI Engineers* is scheduled for late 2026 as a cheaper alternative.

[**Visit Course :octicons-arrow-right-24:**](https://maven.com/parlance-labs/evals){ .md-button .md-button--primary }

### 🔨 Phase 4 checkpoint

Instrument your Phase 3 assistant with tracing (LangSmith, Arize Phoenix, Langfuse or Braintrust — any is fine). Collect or synthesise 100 traces, do error analysis, produce a failure taxonomy with counts, then build: 3 deterministic checks, 1 LLM-as-judge validated against 50 of your own labels (report agreement), and a CI job that fails when scores regress.

---

## Phase 5: Agentic AI — patterns, frameworks, memory and protocols (Weeks 15–22)

Now build agents — with evals from Phase 4 attached from the first commit. Learn the **patterns** in raw Python first, then one or two frameworks deeply.

### 1. Agentic AI (by Andrew Ng) { #agentic-ai-ng }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free to audit
    - **Duration:** 3–10 hrs

**Instructor(s):** Andrew Ng

**Description:**
**Start here.** Reflection, tool use, planning and multi-agent patterns built from first principles in plain Python — plus a strong emphasis on evaluation and error analysis for agents. You build a research agent end to end.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/agentic-ai){ .md-button .md-button--primary }

### 2. Building effective agents (essay) { #building-effective-agents }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Engineering blog
    - **Cost:** Free
    - **Duration:** ~30 min

**Description:**
The canonical distinction between **workflows** (predefined code paths) and **agents** (model-directed loops), with the advice most teams need: use the simplest thing that works, and add autonomy only when it measurably helps.

[**Read Article :octicons-arrow-right-24:**](https://www.anthropic.com/engineering/building-effective-agents){ .md-button .md-button--primary }

### 3. LangChain Path (V2) — in this repo { #langchain-path-v2 }

!!! info inline end "Quick Stats"
    - **Platform:** Learning Pathways
    - **Cost:** Free
    - **Duration:** ~10–14 weeks part-time

**Description:**
The deep, mentor-guided track for LangChain 1.x, LangGraph and Deep Agents with Gemini: agents, context engineering, middleware, MCP, security, evals and deployment. If LangGraph is your chosen framework, do its Phases 2–5 alongside this phase.

[**Open the Path :octicons-arrow-right-24:**](langchain-path.md){ .md-button .md-button--primary }

### 4. AI Agents in LangGraph + LangChain Academy { #langgraph-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai + LangChain Academy
    - **Cost:** Free
    - **Duration:** ~1.5 hrs + self-paced

**Instructor(s):** Harrison Chase & Rotem Weiss

**Description:**
Build an agent from scratch, then rebuild it in LangGraph (state, persistence, streaming, human-in-the-loop). Follow with LangChain Academy's official, regularly updated courses. Note: some older lessons use pre-1.0 imports — translate them using the LangChain V2 path's "What NOT to teach" table.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/){ .md-button .md-button--primary }

### 5. Hugging Face AI Agents Course { #hf-agents-course }

!!! info inline end "Quick Stats"
    - **Platform:** huggingface.co/learn
    - **Cost:** Free (with certificate)
    - **Duration:** ~20–30 hrs

**Description:**
A broad, framework-comparative course (smolagents, LlamaIndex, LangGraph) with observability/evals units and a benchmarked final project. Good for seeing the same patterns in several frameworks.

[**Visit Course :octicons-arrow-right-24:**](https://huggingface.co/learn/agents-course){ .md-button .md-button--primary }

### 6. Agent Memory: Building Memory-Aware Agents { #memory-aware-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Oracle

**Description:**
Memory engineering: persistent stores, memory managers and semantic tool retrieval that scales without bloating context. Pair with *Long-Term Agentic Memory with LangGraph* if you're on LangGraph.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents/){ .md-button .md-button--primary }

### 7. Agent Skills with Anthropic { #anthropic-agent-skills }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Elie Schoppik (Anthropic)

**Description:**
Skills are folders of instructions/scripts (a `SKILL.md` plus resources) that an agent loads *on demand* — progressive disclosure for context. Published as an open standard in December 2025 and adopted by dozens of agent products. Learn to write, compose and combine them with MCP and subagents.

- Security note: third-party skills are code you run. Audit them like dependencies.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/agent-skills-with-anthropic){ .md-button .md-button--primary }

### 8. Building Coding Agents with Tool Execution { #coding-agents-exec }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** E2B

**Description:**
Agents that write and *run* code need sandboxes. Covers sandboxed execution, file I/O and iterating on results — the core of data-analysis and coding agents.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution){ .md-button .md-button--primary }

### 9. A2A: The Agent2Agent Protocol { #a2a-protocol }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Google Cloud & IBM Research

**Description:**
How independently built agents discover each other (Agent Cards) and delegate tasks. A2A reached v1.0 in early 2026 under the Linux Foundation. Mental model: **MCP connects an agent to tools; A2A connects agents to agents.** Most apps need MCP; A2A matters when agents cross team or vendor boundaries.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/){ .md-button .md-button--primary }

### 10. Optional electives (pick by interest)

- **Voice agents:** [Building AI Voice Agents for Production](https://www.deeplearning.ai/courses/building-ai-voice-agents-for-production) (LiveKit) — real-time pipelines, latency budgets
- **Browser agents:** [Building AI Browser Agents](https://www.deeplearning.ai/short-courses/building-ai-browser-agents/) — highly relevant for web developers
- **Generative UI:** [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/courses/build-interactive-agents-with-generative-ui) (CopilotKit) — agents that render UI, a natural fit for your front-end skills
- **Role-based multi-agent:** [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- **Programmatic prompt optimisation:** [DSPy: Build and Optimize Agentic Apps](https://www.deeplearning.ai/courses/dspy-build-optimize-agentic-apps) — optimise prompts against your eval set instead of hand-tuning
- **Paid, project-heavy:** Ed Donner's [Complete Agentic AI Engineering Course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/) (Udemy)

### Framework decision guide (September 2026)

Learn the **patterns** first; frameworks are interchangeable wrappers around the same loop. Then pick one primary framework and learn it deeply.

| Framework | Best for | Notes |
|---|---|---|
| **LangGraph / LangChain 1.x** | Controllable, stateful, durable workflows; provider-agnostic | Most-demanded named agent framework in 2025–26 postings; `create_agent` + middleware for simple agents, LangGraph for custom flows, Deep Agents for long-running work |
| **OpenAI Agents SDK** | Teams standardised on OpenAI's Responses API | Handoffs, guardrails, tracing built in |
| **Google ADK** | Gemini / Google Cloud shops, multi-agent and live voice | Deploys naturally to Google's agent platform; strong A2A support |
| **Claude Agent SDK** | Agents that need a coding-agent-style harness (files, shell, subagents, skills) | The harness behind Claude Code, as a library |
| **Microsoft Agent Framework** | Azure / .NET / enterprise Microsoft environments | Successor to AutoGen + Semantic Kernel; 1.0 GA April 2026. **AutoGen is in maintenance mode — don't start new projects on it** |
| **PydanticAI** | Type-safe Python agents, FastAPI-style ergonomics | Great fit for Django/FastAPI developers |
| **CrewAI** | Fast prototyping of role-based teams | Easiest start; check the control you need before committing |
| **LlamaIndex** | Document-heavy agents and ingestion pipelines | Strong parsing/indexing ecosystem |

**Recommendation for you:** LangGraph as primary (portable, most in demand, and this repo has a deep path for it) plus one vendor SDK matching your employer's model provider.

### 🔨 Phase 5 checkpoint

Build a research-and-action agent for a domain you know: ≥ 4 tools (one via MCP), long-term memory, one subagent, human approval before any write action, and a Skill that packages a repeatable procedure. Ship it with the Phase 4 eval harness extended with **trajectory** evaluation (did it call the right tools in a sensible order?).

---

## Phase 6: Production — security, governance, cost and serving (Weeks 23–26) — *new in V2*

Agents take actions with real credentials. This phase is about making them safe, affordable and operable.

### 1. OWASP Top 10 for LLM and Agentic Applications { #owasp }

!!! info inline end "Quick Stats"
    - **Platform:** OWASP Gen AI Security Project
    - **Cost:** Free
    - **Duration:** ~2–3 hrs reading

**Description:**
The shared vocabulary for AI risks: prompt injection, sensitive data disclosure and excessive agency (LLM Top 10), plus agent-specific risks such as goal hijacking, tool misuse, memory poisoning and privilege abuse (Agentic Top 10, 2026). Read alongside Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): untrusted content + private data + external communication = exfiltration risk.

[**Visit OWASP GenAI :octicons-arrow-right-24:**](https://genai.owasp.org/){ .md-button .md-button--primary }

### 2. Red Teaming LLM Applications { #red-teaming }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Giskard

**Description:**
Attack your own application: prompt injection, data leakage, jailbreaks and harmful outputs, manually and with automated scanning. Turn every successful attack into a regression test.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/){ .md-button .md-button--primary }

### 3. Governing AI Agents { #governing-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Databricks

**Description:**
Permissions, data access controls, auditability and policy for agents in an organisation — the questions security and compliance teams will ask before your agent reaches production.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/governing-ai-agents){ .md-button .md-button--primary }

### 4. Fast & Efficient LLM Inference with vLLM { #vllm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Red Hat

**Description:**
How serving engines achieve throughput (continuous batching, paged KV cache, prefix caching) and how to self-host open-weight models. Even if you only call APIs, this explains *why* prompt caching and stable prompt prefixes save money.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/fast-and-efficient-llm-inference-with-vllm){ .md-button .md-button--primary }

### 5. 12-Factor Agents (reading) { #twelve-factor-agents }

!!! info inline end "Quick Stats"
    - **Platform:** GitHub (HumanLayer)
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Engineering principles for production agents from a web-developer's perspective: own your prompts, own your context window, own your control flow, make agents stateless reducers, pause/resume via APIs. Reads like the Twelve-Factor App you already know.

[**Read on GitHub :octicons-arrow-right-24:**](https://github.com/humanlayer/12-factor-agents){ .md-button .md-button--primary }

### Production checklist to apply

- **Least privilege:** tools authorise against the *user's* identity, never the model's claims
- **Human approval** for irreversible or external actions; **budgets** (max model/tool calls, tokens, spend per user)
- **Reliability:** retries with backoff, provider fallback, timeouts (rate limits are ~⅓ of LLM call failures)
- **Cost:** model routing, stable prompt prefixes for caching, semantic caching, right-sized thinking levels
- **Observability:** traces with user/feature metadata; OpenTelemetry-compatible where possible
- **Change management:** every prompt/model/tool change runs the eval suite; model upgrades are regressions until proven otherwise

### 🔨 Phase 6 checkpoint

Take your Phase 5 agent through a security and cost review: a written threat model (which trifecta legs does it have?), five red-team attacks turned into automated tests, a permissions model enforced in code, and a cost report showing per-request spend before and after two optimisations with eval scores unchanged.

---

## Phase 7: LLM internals and post-training (Weeks 27–34)

With systems and evals in hand, going under the hood now pays off: you'll know *when* fine-tuning beats prompting + retrieval, and you'll have the evals to prove it.

### 1. Andrej Karpathy's "Neural Networks: Zero to Hero" { #karpathy-zero-to-hero }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~14.5 hrs

**Instructor(s):** Andrej Karpathy

**Description:**
Build micrograd, language models and a GPT from scratch in PyTorch. Still the best path to genuinely understanding backpropagation, attention and training dynamics.

[**Watch Series :octicons-arrow-right-24:**](https://karpathy.ai/zero-to-hero.html){ .md-button .md-button--primary }

### 2. nanochat (hands-on capstone for internals) { #nanochat }

!!! info inline end "Quick Stats"
    - **Platform:** GitHub
    - **Cost:** Free code; ~$100 of rented GPU time for the full run (optional)
    - **Duration:** Self-paced

**Instructor(s):** Andrej Karpathy

**Description:**
A minimal, readable, end-to-end ChatGPT-style pipeline (Oct 2025): tokenizer training, pretraining, supervised fine-tuning, optional RL, inference and a web UI in one small codebase. Read it even if you don't run the full training.

[**View Repository :octicons-arrow-right-24:**](https://github.com/karpathy/nanochat){ .md-button .md-button--primary }

### 3. Finetuning Large Language Models { #finetune-llm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Sharon Zhou

**Description:**
The decision framework: when to fine-tune vs prompt vs retrieve, and how to prepare data. The mechanics have moved on; the decision logic hasn't.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/){ .md-button .md-button--primary }

### 4. Post-training of LLMs { #post-training }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Banghua Zhu (University of Washington / Nexusflow)

**Description:**
SFT, Direct Preference Optimization (DPO) and online reinforcement learning — the three post-training methods that turn a base model into an assistant — and when to use each. *Replaces V1's standalone RLHF course.*

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/post-training-of-llms){ .md-button .md-button--primary }

### 5. Reinforcement Fine-Tuning LLMs With GRPO { #rft-grpo }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Predibase

**Description:**
Reinforcement fine-tuning with programmatic reward functions — the technique behind modern reasoning models, and the most practical way to teach a small model a narrow, verifiable skill without large labelled datasets. Your eval checks from Phase 4 often *become* the reward functions.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/reinforcement-fine-tuning-llms-grpo){ .md-button .md-button--primary }

### 6. Hugging Face smol course + TRL / Unsloth docs { #smol-course }

!!! info inline end "Quick Stats"
    - **Platform:** huggingface.co/learn
    - **Cost:** Free
    - **Duration:** Self-paced

**Description:**
Practical post-training of small models (instruction tuning, preference alignment, LoRA) with Hugging Face TRL. Pair with the [Unsloth docs](https://docs.unsloth.ai/) for memory-efficient LoRA/QLoRA and GRPO on a single consumer or rented GPU.

[**Visit Course :octicons-arrow-right-24:**](https://huggingface.co/learn/smol-course){ .md-button .md-button--primary }

### 7. Quantization Fundamentals with Hugging Face { #quantization-hf }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
How quantization lets large models run on smaller hardware, and what quality you trade for it. Essential before self-hosting open-weight models.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/quantization-fundamentals-with-hugging-face/){ .md-button .md-button--primary }

### Optional deeper dives

- **[Stanford CS336: Language Modeling from Scratch (Spring 2026)](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)** — the rigorous, research-grade version: tokenization, architectures, GPUs/kernels, parallelism, scaling laws, inference, alignment. Heavy but outstanding.
- **[Generative AI with Large Language Models](https://www.coursera.org/learn/generative-ai-with-llms)** (Coursera, AWS & DeepLearning.AI) — a structured tour of the LLM lifecycle; free to audit.
- **[Attention in Transformers: Concepts and Code in PyTorch](https://www.deeplearning.ai/courses/attention-in-transformers-concepts-and-code-in-pytorch)** (StatQuest) — short, code-level attention.
- **[Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)** (Andrew Ng) — only if you want the full classical foundation.

### 🔨 Phase 7 checkpoint

Pick a narrow, verifiable task from your own work (e.g., SQL generation for your schema, extracting fields from your documents). Establish a baseline with a frontier API model and a small open-weight model using your Phase 4 harness. Then fine-tune the small model (LoRA SFT, and optionally GRPO with your eval checks as rewards). Report quality, latency and cost per 1,000 requests for all three. Conclude honestly — "don't fine-tune" is a valid, valuable result.

---

## Phase 8: Capstone projects and portfolio (Weeks 35+)

Each project should ship with: a README explaining design decisions and trade-offs, an **eval report**, a **threat model**, and a **cost analysis**. That trio is what separates an AI engineer's portfolio from tutorial output.

### Project 1: Production RAG assistant as a web app

Your docs (PDF + Markdown + code) → hybrid retrieval with re-ranking → cited answers, semantic cache, auth and rate limiting in Django/Flask/FastAPI. Eval suite in CI; dashboard of cost/latency/quality. *Demonstrates Phases 2–4.*

### Project 2: Agent with tools, memory, MCP and human approval

A LangGraph (or chosen framework) agent that takes real actions in a sandboxed environment: MCP-served tools, long-term memory, approval gates, trajectory evals, red-team tests. *Demonstrates Phases 4–6.*

### Project 3: Fine-tuned small model vs frontier API

The Phase 7 experiment, polished: reproducible training, eval comparison, serving via vLLM or a managed endpoint, and a clear recommendation. *Demonstrates Phase 7.*

### Project 4: Multi-agent system across protocol boundaries

Two or more agents (ideally in different frameworks) collaborating over A2A, each using MCP tools and Skills, with end-to-end tracing across agents and a governance write-up (who can do what, how it's audited). *Demonstrates everything.*

### Portfolio presentation tips

Open-source the code, write a short blog post per project focusing on *decisions* and *measured results*, include failure analyses (what the evals caught), and show cost per request. Hiring managers in 2026 look for evidence of evaluation, reliability engineering and judgement about when *not* to use an agent.

---

## What NOT to spend time on in 2026

| Skip or de-prioritise | Why | Do this instead |
|---|---|---|
| OpenAI **Assistants API** tutorials | Shut down 26 Aug 2026 | Responses API / Agents SDK, or a framework |
| **AutoGen** for new projects | Maintenance mode since Oct 2025 | Microsoft Agent Framework (if on Microsoft stack) or LangGraph |
| Model-specific prompt tricks (o1-era "don't use CoT", Llama 2 `[INST]` formats) | Superseded by built-in reasoning and chat templates | Clear goals, good context, evals |
| Pre-1.0 LangChain tutorials (`AgentExecutor`, `initialize_agent`, `ConversationBufferMemory`) | Replaced in LangChain 1.0 (Oct 2025) | The [LangChain Path (V2)](langchain-path.md) |
| Hand-parsing JSON from model output | Native structured output is standard | Schema-constrained output with Pydantic |
| Legacy MCP HTTP+SSE transport, Sampling, Roots | Deprecated in the 2026-07-28 spec | Streamable HTTP; call model APIs directly |
| Fine-tuning before you have evals and a RAG baseline | You can't tell if it helped | Phases 3–4 first, then Phase 7 |
| Chasing leaderboards to choose models | Benchmarks rarely match your task | Your own eval set, per task |
| "Prompt engineer" as a destination role | Market shifted to systems roles | Context engineering + evals + agent engineering |
| Pasting stale model IDs (`gpt-4`, `gemini-1.5`, `gemini-2.0`) from old tutorials | Many are retired | Keep model IDs in config and check provider docs |

---

## Additional resources for the whole journey

### Free platforms

- **[DeepLearning.ai short courses](https://www.deeplearning.ai/courses/)** — new courses almost weekly; filter for agents, evals and inference.
- **[Hugging Face Learn](https://huggingface.co/learn)** — Agents, MCP, LLM and smol (post-training) courses.
- **[LangChain Academy](https://academy.langchain.com/)** — official LangGraph/LangSmith courses.
- **[Anthropic Academy](https://anthropic.skilljar.com/)** — Claude API, MCP (intro and advanced), Claude Code and Agent Skills.
- **[Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** — free lesson series on agent fundamentals.

### Books

- **_AI Engineering_** — Chip Huyen (O'Reilly, 2025). The best single book on building applications on foundation models: evaluation, RAG, agents, fine-tuning, inference optimisation.
- **_Build a Large Language Model (From Scratch)_** and **_Build a Reasoning Model (From Scratch)_** — Sebastian Raschka (Manning). Code-first companions to Phase 7; the second covers inference-time scaling, RL and distillation.
- **_Evals for AI Engineers_** — Shreya Shankar & Hamel Husain (O'Reilly, scheduled late 2026).
- **_The LLM Engineer's Handbook_** — Paul Iusztin & Maxime Labonne (Packt). An end-to-end LLMOps project.

### Reports worth reading once a year

- **[Stanford AI Index](https://hai.stanford.edu/ai-index/2026-ai-index-report)** — capability, adoption and labour-market data.
- **[Datadog State of AI Engineering](https://www.datadoghq.com/state-of-ai-engineering/)** — what production AI actually looks like (tokens, caching, failures, frameworks).
- **[Anthropic Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report)** — how engineering work is changing with coding agents.

### People and channels

**Andrej Karpathy** (first principles), **3Blue1Brown** (visual maths), **Simon Willison's blog** (pragmatic, security-aware coverage of new models and tools), **Hamel Husain** (evals), **Latent Space** podcast (AI engineering industry), **Yannic Kilcher** (paper breakdowns).

### Roadmaps

**[roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer)** — interactive, continuously updated. Use it as a checklist, not a syllabus.

---

## Summary: the complete plan at a glance

| Phase | Focus | Weeks | Core free resources | Optional paid | Key outcome |
|---|---|---|---|---|---|
| 0 | AI-augmented workflow | 1 | Claude Code course, Spec-Driven Development | — | Productive, supervised use of coding agents |
| 1 | LLM foundations | 1–3 | Karpathy Deep Dive, 3Blue1Brown, How Transformer LLMs Work, reasoning docs | — | Accurate mental model; reasoning trade-offs |
| 2 | Building LLM apps | 4–7 | Building Systems, Pydantic, Structured Output, Claude API course, MCP | Ed Donner LLM Engineering | Typed, tool-using services + an MCP server |
| 3 | Retrieval & context engineering | 8–11 | Context-engineering essay, RAG course, Advanced Retrieval, Document AI, Semantic Caching | — | Measured, cited retrieval over real documents |
| 4 | **Evals & observability** | 12–14 | Evals FAQ, Evaluating AI Agents, NeMo reliability | Maven AI Evals | Error analysis, validated judges, CI gate |
| 5 | Agentic AI | 15–22 | Agentic AI (Ng), Building Effective Agents, LangChain Path V2, HF Agents, Memory, Skills, A2A | Ed Donner Agentic | Evaluated agents with memory, MCP, HITL |
| 6 | **Security, governance, serving** | 23–26 | OWASP, Red Teaming, Governing Agents, vLLM, 12-Factor Agents | — | Threat-modelled, cost-controlled production agent |
| 7 | Internals & post-training | 27–34 | Zero to Hero, nanochat, Post-training, GRPO, smol course | — | Evidence-based fine-tuning decisions |
| 8 | Portfolio | 35+ | — | — | Four projects with evals, threat models, cost analyses |

**Totals:** ~35 core free resources (plus electives), **$0 core cost**, ~$50–100 optional paid items at sale prices (the Maven cohort is priced separately), ~8 months at 8–10 hrs/week.

The biggest change from V1 is not any single course; it's the order and the emphasis. V2 teaches you to **measure before you optimise, contain before you automate, and understand the system before the model internals** — which is how the strongest AI engineering teams worked in 2026.

---

*Curriculum V2 · researched September 2026 · V1 (March 2026) remains available at [AI Mastery Plan (V1)](../ai-mastery-plan.md).*
