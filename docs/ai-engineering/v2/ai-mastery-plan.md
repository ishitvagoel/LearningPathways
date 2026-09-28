---
title: AI Engineer Mastery Plan (V2)
description: A September-2026, provider-neutral roadmap from web developer to production AI engineer — agentic and harness engineering, context engineering, evals, agents, security and post-training — with a Claude harness to run it.
icon: material/rocket-launch
tags:
  - AI
  - Career
  - Agents
  - Evals
  - Harness Engineering
---

# The AI Engineer Mastery Plan for Web Developers (V2)

**Curriculum V2 (revised) · researched September 2026 · provider-neutral, Claude as reference**

!!! abstract "What changed from V1 — and in this revision"
    V1 (March 2026) is preserved unchanged at [AI Mastery Plan (V1)](../ai-mastery-plan.md). V2 re-orders the plan around what the industry now hires for: **building, evaluating and harnessing agentic systems**. Progress you made on V1 carries over; see the [carry-over table](#v1-progress-carry-over).

    **This revision (late September 2026)** adds what a second research pass found missing:

    - **Agentic engineering and harness engineering** as core skills, with a new Phase 6
    - **Loop and skill engineering**
    - **Ambient/scheduled agents and managed agent platforms**
    - **Personal agent harnesses** (OpenClaw, Hermes) as a security case study
    - **Computer use**, with a reality check on how well it works
    - **RL environments and verifiers**
    - **Agent identity**
    - **Agentic payments**
    - **The EU AI Act's August 2026 obligations**

    The plan is now **provider-neutral**: concepts first, with Claude as the reference implementation. It ships with a **[Claude Harness Kit](claude-harness.md)** that turns Claude Code into your mentor, so you no longer paste the plan into a chatbot. The audit and every source are in [V2 Review & Research Notes](review-notes.md).

Your Python/Flask/Django background is still an advantage. It covers exactly what most AI courses assume you lack: APIs, state, auth, deployment and testing.

In 2026, AI engineering is *systems work around models*. The job is to decide what goes into the model's context, wire up its tools, surround it with checks, measure quality, and keep cost, latency and risk under control. Andrej Karpathy's framing for this is **agentic engineering**: you orchestrate "fallible, stochastic but extremely powerful" agents through specs, diff review and eval loops, rather than writing every line yourself. This plan trains that discipline. It still covers internals and fine-tuning, but *after* you can ship and evaluate systems, because that's when they pay off.

---

## What the evidence says (2025 → September 2026)

**1. Demand moved from prompting to agentic systems.** The Stanford *AI Index 2026* found:
- AI skills appear in 2.5% of all US job postings.
- The "Agentic AI" skill cluster grew more than 280% in a year.
- LangGraph was among the fastest-growing named skills.
- "ChatGPT" and "chatbot" skills *declined*.

**2. Evals became the differentiator.** Practitioners such as Hamel Husain and Shreya Shankar, and hiring guides, agree that teams that can't measure quality can't ship safely. V2 gives evals a phase of their own, *before* agents.

**3. Context engineering replaced prompt engineering.** Anthropic's *Effective context engineering for AI agents* (Sept 2025) describes the job as curating "the smallest possible set of high-signal tokens". Datadog's *State of AI Engineering* (July 2026) shows what that means in practice:
- System prompts make up about 69% of input tokens.
- Only about 28% of calls use prompt caching.
- More than 70% of organisations use three or more models.

**4. The harness now matters as much as the model.** Key points from the past eight months:
- OpenAI's *Harness engineering* post (Feb 2026) described a team shipping about a million lines of agent-written code by engineering the agent's *environment* instead of its prompts.
- Birgitta Böckeler (martinfowler.com, Apr 2026) supplied the vocabulary: **guides** steer the agent before it acts, **sensors** check its work afterwards.
- At the AI Engineer World's Fair (July 2026), the headline shift was from "agents" to "the systems around them": harness, **loop engineering** (a human outer loop around an autonomous inner loop) and **skills everywhere**.
- Marmelab's *State of AI Harness Engineering 2026* ran the same model through eight harnesses and got task success from 68% to 88%.

**5. Agents became ambient and hosted.** Agents increasingly run without a human prompt, on schedules, webhooks and events:
- Claude Managed Agents (public beta, April 2026) hosts the agent loop and its sandbox.
- Claude Code routines run prompts on schedules, API calls or GitHub events.
- Personal always-on agents went viral. OpenClaw passed about 247k GitHub stars by March 2026, and Nous Research's Hermes Agent introduced self-written skills.
- OpenClaw also became the year's clearest agent-security case study: hundreds of malicious skills on its marketplace, sandboxing off by default, and restrictions on government machines in China.

**6. Standards consolidated; some platforms retired.**
- MCP and Agent Skills are stewarded by the Linux Foundation's Agentic AI Foundation. MCP's July 2026 spec made the protocol stateless.
- A2A reached v1.0.
- OpenAI's Assistants API shut down on 26 Aug 2026.
- Microsoft put AutoGen in maintenance mode and shipped Agent Framework 1.0 (April 2026).
- Agentic payments now have competing protocols: ACP (OpenAI/Stripe), AP2 (Google), and the Machine Payments Protocol (Stripe/Tempo).

**7. Training shifted toward verifiable rewards.** The main new post-training technique is reinforcement learning with verifiable rewards (RLVR). "RL environment engineering" (tasks, sandboxes and *verifiers* that turn outcomes into rewards) became one of 2026's fastest-growing specialisms. Its central problem is **reward hacking**, which is the same skill as writing good evals, pointed at training.

**8. Regulation arrived for some systems.** The EU's Digital Omnibus (in force 27 July 2026) deferred the AI Act's high-risk obligations to December 2027 and August 2028. Most **Article 50 transparency obligations**, such as telling people they are interacting with AI, still applied from 2 August 2026.

**9. Coding agents replaced the IDE as the centre of the workflow.** Anthropic's *2026 Agentic Coding Trends Report* found developers use AI in about 60% of their work but can fully delegate only 0–20% of tasks. Supervision, verification and context are the skill. The Pragmatic Engineer's 2026 survey shows roles converging, with engineers orchestrating more and managers coding more.

---

## Provider-neutral by design

Every phase teaches the *concept* first. Code examples use **Claude** as the reference implementation, for three reasons:
- The same vendor ships the harness this plan uses: Claude Code, the Agent SDK, skills, subagents and hooks.
- Claude's API makes several 2026 ideas explicit: adaptive thinking with effort levels, prompt caching, compaction, and tool search.
- Using one reference provider keeps examples consistent.

Where an idea has a different name elsewhere, the plan says so (for example, "effort" versus "reasoning effort" versus "thinking level"). Embeddings use a **local open-source model**, so no vendor is required for retrieval. The framework guide in Phase 5 covers all the major SDKs.

## Learner Profile

- **Background:** Web developer with strong Python (Flask/Django), REST APIs, databases, auth, deployment.
- **Already completed:** *AI for Everyone*, *Generative AI for Everyone*, and (in progress in V1) *ChatGPT Prompt Engineering for Developers*.
- **Gaps:** LLM internals, retrieval, evaluation methodology, agent architectures, harness engineering, AI security, model adaptation.
- **Goal:** Become a production-grade AI engineer who can design, build, evaluate, harness, secure and operate LLM-powered and agentic systems.
- **Time budget assumed:** ~8–10 hours/week, which is about 9 months. Double the hours and it's about 5.
- **Budget:** $0 core path. You'll need an API key for your chosen model provider; set a monthly spend limit. Optional paid items are marked.

## How to use this plan: the Claude Harness Kit

Don't paste this page into a chatbot. Copy the **[Claude Harness Kit](claude-harness.md)** into a practice repository and start Claude Code there. The kit's files (`CLAUDE.md`, skills, a reviewer subagent and hooks) encode the mentor rules:
1. One concept per session; *why* before *how*.
2. Reasoning questions, not recall.
3. No advancing until you've attempted the phase's checkpoint.
4. Verify fast-changing facts against official docs.
5. Progress tracked in a file.

The kit is also your first worked example of harness engineering, and you'll modify it in Phase 0. For LangChain-specific depth, switch to the [LangChain Path (V2)](langchain-path.md) during Phase 5.

---

## V1 progress carry-over

| If you finished this in V1… | …it counts toward V2 | Notes |
|---|---|---|
| Phase 1 prompt engineering courses | Phase 1 | Principles still hold; ignore model-specific API syntax |
| *Reasoning with o1*, *Prompt Engineering with Llama 2 & 3* | Phase 1 (optional) | Historical; see Phase 1 for how reasoning models are used now |
| Phase 2 LLM API courses, MCP course | Phase 2 | Re-read the MCP note: the protocol changed in July 2026 |
| Phase 3 RAG courses | Phase 3 | Add the context-engineering reading |
| *Building and Evaluating Advanced RAG* | Phase 4 | Then do the new evals resources |
| Phase 5 agent courses | Phase 5 | AutoGen course is now optional; see the framework guide |
| Phase 4 internals courses | Phase 8 | Internals moved later; nothing lost |

---

## Phase 0: Agentic engineering — working with (and harnessing) coding agents (Weeks 1–2)

Before learning *about* AI systems, learn to work *with* one, and to harness it. Coding agents will write much of the boilerplate in this plan. Your job is to specify, supervise and verify, and to shape the agent's environment so that it fails less often. This compounds over every later phase.

### 1. Claude Code: A Highly Agentic Coding Assistant { #claude-code-course }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Elie Schoppik (Anthropic)

**Description:**
How an agentic coding tool explores a codebase, plans, edits and runs code, and how to steer it with context files, subagents and MCP servers.

- Treat the agent as a fast but fallible junior engineer: give it a spec, review its diffs, run the tests
- Learn the vocabulary (context files, skills, subagents, hooks, MCP) you'll meet again when *building* agents

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant){ .md-button .md-button--primary }

### 2. Harness engineering: the two essential essays { #harness-essays }

!!! info inline end "Quick Stats"
    - **Platform:** martinfowler.com + OpenAI blog
    - **Cost:** Free
    - **Duration:** ~1.5 hrs reading

**Instructor(s):** Birgitta Böckeler (Thoughtworks); OpenAI Codex team

**Description:**
Read OpenAI's *Harness engineering: leveraging Codex in an agent-first world* (Feb 2026), then Böckeler's *Harness engineering for coding agent users* (Apr 2026). Together they explain why the environment around the agent determines its reliability:

- **Guides** (instructions, `AGENTS.md`, skills) and **sensors** (tests, linters, review agents)
- **Computational** (deterministic) versus **inferential** (model-judged) controls
- When an agent fails, ask "what capability is missing, and how do I make it legible and enforceable for the agent?"

[**Read Böckeler's article :octicons-arrow-right-24:**](https://martinfowler.com/articles/harness-engineering.html){ .md-button .md-button--primary } [**Read OpenAI's post :octicons-arrow-right-24:**](https://openai.com/index/harness-engineering/){ .md-button }

### 3. Spec-Driven Development with Coding Agents { #spec-driven-dev }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** JetBrains

**Description:**
Writing specifications that agents can execute reliably. This is the antidote to "vibe coding" that doesn't survive production, and what Karpathy calls the shift to *agentic engineering*.

- Specs, acceptance criteria and tests as the contract between you and the agent
- Directly transferable to writing tool descriptions, skills and system prompts later

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents){ .md-button .md-button--primary }

### 4. Claude Code in Action + Claude Code docs (skills, hooks, subagents) { #claude-code-in-action }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Academy + Claude Code docs
    - **Cost:** Free
    - **Duration:** Self-paced

**Description:**
Anthropic's course on integrating a coding agent into daily work, plus the reference pages for the four harness files you'll write in this plan: [`CLAUDE.md` / `AGENTS.md` memory](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents) and [hooks](https://code.claude.com/docs/en/hooks).

- Keep `CLAUDE.md` under ~200 lines; put anything that must *always* happen in a hook, not a sentence
- `AGENTS.md` is the cross-tool instruction file; Claude Code reads it directly or via an `@AGENTS.md` import

[**Visit Course :octicons-arrow-right-24:**](https://anthropic.skilljar.com/claude-code-in-action){ .md-button .md-button--primary }

### 🔨 Phase 0 checkpoint: harness your own repo

1. Install the [Claude Harness Kit](claude-harness.md) in a practice repo and run `/lesson`.
2. In an existing Flask/Django project, write an `AGENTS.md` (under 100 lines) and a `CLAUDE.md` that imports it.
3. Add **one skill** for a task you repeat, such as "add an endpoint with tests".
4. Add **one hook** that enforces a rule you'd otherwise have to repeat, such as blocking edits to `migrations/` or running the tests after edits.
5. **Test the harness:** show the hook blocking a bad action (a negative test) and allowing a good one.
6. Use the agent to add a feature *from a written spec*, and log where it went wrong and which guide or sensor would have prevented it.

---

## Phase 1: LLM foundations and mental models (Weeks 3–4)

Goal: an accurate mental model of what an LLM is, how it's trained, why it hallucinates, and how reasoning models differ. That's enough to predict their behaviour and debug it.

### 1. ChatGPT Prompt Engineering for Developers ✅ { #prompt-eng-dev }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Isa Fulford (OpenAI) & Andrew Ng

**Description:**
Finish this if you haven't. The *principles* (clear instructions, give the model time to think, iterate systematically) are timeless and provider-independent. The API syntax is dated, so don't copy it.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/){ .md-button .md-button--primary }

### 2. Karpathy: "Deep Dive into LLMs like ChatGPT" { #karpathy-deep-dive }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~3.5 hrs

**Instructor(s):** Andrej Karpathy

**Description:**
The best single overview of the LLM lifecycle: pretraining, tokenization, post-training (SFT, RLHF), hallucinations, tool use, and reasoning learned through reinforcement learning. No code required.

- Explains why models stumble on spelling and counting (tokens) and why tools fix it
- Explains Karpathy's "jagged intelligence": superhuman at some tasks, surprisingly weak at adjacent ones, which is why harnesses and evals exist

[**Watch Video :octicons-arrow-right-24:**](https://www.youtube.com/watch?v=7xTGNNLPyMI){ .md-button .md-button--primary }

### 3. 3Blue1Brown: Neural networks and transformers { #3b1b-neural }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~3 hrs total

**Instructor(s):** Grant Sanderson

**Description:**
Visual intuition for neural networks, gradient descent, backpropagation, and the transformer chapters ("Transformers, the tech behind LLMs", "Attention in transformers", "How might LLMs store facts").

[**Watch Series :octicons-arrow-right-24:**](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi){ .md-button .md-button--primary }

### 4. How Transformer LLMs Work { #how-transformer-llms-work }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Jay Alammar & Maarten Grootendorst

**Description:**
A code-light walkthrough of tokenizers, embeddings, attention and the modern transformer block, including mixture-of-experts. It bridges the 3Blue1Brown intuition and the Phase 8 code.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/how-transformer-llms-work){ .md-button .md-button--primary }

### 5. Reasoning models in practice: adaptive thinking and effort { #reasoning-models }

!!! info inline end "Quick Stats"
    - **Platform:** Claude Platform docs (reference provider)
    - **Cost:** Free
    - **Duration:** ~1 hr reading + experiments

**Description:**
*This replaces V1's "Reasoning with o1".* In 2026, every frontier model reasons before answering. What matters now is the *trade-off* you control, not model-specific tricks. On Claude, that control is [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) plus an [effort level](https://platform.claude.com/docs/en/build-with-claude/effort) from `low` to `max`. Other providers call it "reasoning effort" or "thinking level".

- More effort means more latency and tokens. Measure whether it improves *your* task
- Current Claude models reject sampling parameters such as `temperature`; reliability comes from effort, context, structured output and evals
- Don't micro-manage the chain of thought. Give clear goals, constraints and a definition of done

[**Read the Docs :octicons-arrow-right-24:**](https://platform.claude.com/docs/en/build-with-claude/effort){ .md-button .md-button--primary }

### 6. AI Capabilities and Limitations (optional) { #capabilities-limitations }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Academy
    - **Cost:** Free
    - **Duration:** Short, self-paced

**Description:**
A short, grounded course on what current models can and can't do reliably. It's useful calibration before you design systems around them.

[**Visit Course :octicons-arrow-right-24:**](https://anthropic.skilljar.com/ai-capabilities-and-limitations){ .md-button .md-button--primary }

### 🔨 Phase 1 checkpoint

Pick three tasks: a factual lookup, a multi-step calculation and a classification. Run each at two effort levels on a small model and a frontier model; if you have access to a second provider, include it too. For 10 examples each, record accuracy, latency and cost in a table. Then write a paragraph explaining the results using Karpathy's mental model (tokens, training, reasoning, jaggedness).

---

## Phase 2: Building LLM-powered applications (Weeks 5–8)

This is where your web background becomes a superpower. An LLM is a new, probabilistic dependency inside a system you already know how to build.

### 1. Building Systems with the ChatGPT API { #building-systems }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Isa Fulford & Andrew Ng

**Description:**
Chaining calls into a pipeline: classify → moderate → reason → check the output. The patterns are provider-independent and still the right foundation; the SDK syntax is dated.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/){ .md-button .md-button--primary }

### 2. Claude Platform 101 → Building with the Claude API { #claude-api-course }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Academy
    - **Cost:** Free
    - **Duration:** Self-paced (multi-hour)

**Description:**
The reference-provider track. *Claude Platform 101* is the on-ramp. *Building with the Claude API* covers the whole surface of a modern LLM API:
- messages and system prompts
- tool use and structured outputs
- prompt caching and extended thinking
- RAG and evaluation workflows

It is one of the most complete free treatments of *how an LLM API is meant to be used*, and the concepts map directly onto any provider.

[**Visit Course :octicons-arrow-right-24:**](https://anthropic.skilljar.com/claude-with-the-anthropic-api){ .md-button .md-button--primary } [**Start with Platform 101 :octicons-arrow-right-24:**](https://anthropic.skilljar.com/claude-platform-101){ .md-button }

### 3. Pydantic for LLM Workflows + Getting Structured LLM Output { #structured-output }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** 2 short courses

**Description:**
Typed, validated data at every boundary: structured outputs, tool arguments and API responses. The second course (by DotTxt) explains *how* constrained decoding guarantees schema-valid output. That is the #1 fix for "the model returned almost-JSON".

[**Pydantic for LLM Workflows :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/pydantic-for-llm-workflows){ .md-button .md-button--primary } [**Getting Structured LLM Output :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/getting-structured-llm-output/){ .md-button }

### 4. Writing effective tools for agents (essay) { #writing-tools }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Engineering blog
    - **Cost:** Free
    - **Duration:** ~30 min

**Description:**
Tool design is interface design for a model. It covers clear names and descriptions, returning only what the model needs, token-efficient responses, and using the model itself to evaluate and improve your tools. Read it before you write your first tool.

[**Read Article :octicons-arrow-right-24:**](https://www.anthropic.com/engineering/writing-tools-for-agents){ .md-button .md-button--primary }

### 5. MCP: Build Rich-Context AI Apps + Anthropic MCP courses { #mcp-anthropic }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai + Anthropic Academy
    - **Cost:** Free
    - **Duration:** 1 short course + 2 self-paced

**Instructor(s):** Elie Schoppik (Anthropic)

**Description:**
Build MCP servers and clients. MCP is the standard way to expose tools and data to any AI host: Claude, ChatGPT, Gemini CLI, IDEs and your own agents. Follow up with Anthropic's *Introduction to MCP* and *MCP: Advanced Topics*.

!!! warning "Protocol update"
    The 2026-07-28 MCP spec made the protocol **stateless**: there's no initialize handshake and no sessions. It also deprecated *Sampling*, *Roots* and *Logging*, and moved long-running *Tasks* into an extension. Courses recorded earlier still teach the right mental model; check the [current spec](https://modelcontextprotocol.io/specification/latest) for wire-level details. Also read Anthropic's [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp): letting agents call MCP tools *from code* keeps intermediate data out of the context window.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic){ .md-button .md-button--primary } [**MCP Advanced Topics :octicons-arrow-right-24:**](https://anthropic.skilljar.com/model-context-protocol-advanced-topics){ .md-button }

### 6. Open Source Models with Hugging Face { #os-models-hf }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Finding, running and serving open-weight models. In 2026, open-weight families (Qwen, DeepSeek, GLM, Kimi, gpt-oss, Gemma) are competitive for many tasks. Choose by license, size and *your own* evals rather than leaderboards. You'll use a local open model for embeddings in Phase 3.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/open-source-models-hugging-face/){ .md-button .md-button--primary }

### 🔨 Phase 2 checkpoint

Build a FastAPI or Django service with:
- (a) an endpoint that returns **schema-validated** structured output
- (b) a tool-calling endpoint using a hand-written tool loop, with no framework
- (c) an MCP server exposing a capability from your own app, tested from an off-the-shelf MCP client

Keep the provider and model IDs in one config file, and log tokens, cache hits and latency per request.

---

## Phase 3: Retrieval and context engineering (Weeks 9–12)

Retrieval is still the most common production pattern. In 2026 it's taught as one tool within **context engineering**: choosing what enters the model's window, when, and in what form.

### 1. Effective context engineering for AI agents (essay) { #context-engineering }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Engineering blog
    - **Cost:** Free
    - **Duration:** ~30 min (read twice)

**Description:**
The clearest statement of the discipline. It covers context rot, the attention budget, just-in-time retrieval, compaction, structured note-taking and sub-agents. Everything else in this phase implements these ideas.

[**Read Article :octicons-arrow-right-24:**](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents){ .md-button .md-button--primary }

### 2. Retrieval Augmented Generation (RAG) { #rag-course }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free to audit (check platform)
    - **Duration:** Multi-week course

**Description:**
DeepLearning.ai's full-length RAG course: retrieval fundamentals, hybrid search, chunking, re-ranking, evaluation and production concerns. Pair it with Anthropic's [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) write-up, which prepends chunk-specific context before embedding and indexing. It's a cheap, well-measured improvement.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag){ .md-button .md-button--primary }

### 3. Advanced Retrieval for AI with Chroma { #adv-retrieval-chroma }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Anton Troynikov (Chroma)

**Description:**
Query expansion, cross-encoder re-ranking and embedding adapters: the techniques that move retrieval from "works on the demo" to "works on real questions".

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/){ .md-button .md-button--primary }

### 4. Document AI: From OCR to Agentic Doc Extraction { #document-ai }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** LandingAI

**Description:**
Real-world data comes as PDFs, tables, scans and forms. This covers layout-aware parsing and agentic extraction that preserves structure for retrieval.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/document-ai-from-ocr-to-agentic-doc-extraction){ .md-button .md-button--primary }

### 5. Semantic Caching for AI Agents { #semantic-caching }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Redis

**Description:**
Reusing answers for *semantically* repeated questions. It's often the biggest cost and latency win in a production assistant, and a good lesson in the precision/recall trade-off of similarity thresholds. It complements provider prompt caching, which reuses *prefixes* rather than answers.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/semantic-caching-for-ai-agents){ .md-button .md-button--primary }

### 🔨 Phase 3 checkpoint

Build a documentation assistant over your own docs (PDFs + Markdown) with **local open-source embeddings**. Implement two retrieval strategies, such as pure vector search versus hybrid search with re-ranking and contextual chunk headers. Add a semantic cache and citations. On a 25-question test set, report retrieval hit rate@5 and answer faithfulness for each strategy. Finally, for one long conversation, write down exactly what was in the context window at turn 10 and what you'd remove.

---

## Phase 4: Evaluation and observability (Weeks 13–15)

You can't improve what you can't measure, and you can't safely ship agents you can't evaluate. This phase comes **before** agents on purpose: every agent you build afterwards gets an eval suite from day one. The same skill reappears twice later, in harness tests (Phase 6) and in reward design (Phase 8).

### 1. AI Evals FAQ + free email course { #evals-faq }

!!! info inline end "Quick Stats"
    - **Platform:** hamel.dev
    - **Cost:** Free
    - **Duration:** ~3–4 hrs reading

**Instructor(s):** Hamel Husain & Shreya Shankar

**Description:**
The practitioner consensus on evals:
1. Start with **error analysis**: read traces, write notes, cluster the failures and count them.
2. Only then build metrics, preferring binary pass/fail judgements.
3. Validate every LLM judge against human labels.
4. Wire the evals into CI.

[**Read the FAQ :octicons-arrow-right-24:**](https://hamel.dev/blog/posts/evals-faq/){ .md-button .md-button--primary }

### 2. Evaluating AI Agents { #evaluating-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Arize AI

**Description:**
Tracing an agent, then evaluating its router decisions, tool calls and trajectories (not just final answers), and running structured experiments when you change prompts or models.

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
The most in-depth evals training available. Their O'Reilly book *Evals for AI Engineers* is scheduled for late 2026 as a cheaper alternative.

[**Visit Course :octicons-arrow-right-24:**](https://maven.com/parlance-labs/evals){ .md-button .md-button--primary }

### 🔨 Phase 4 checkpoint

1. Instrument your Phase 3 assistant with tracing (LangSmith, Arize Phoenix, Langfuse or Braintrust; any is fine) and collect or synthesise 100 traces.
2. Do error analysis and produce a failure taxonomy with counts.
3. Build three deterministic checks.
4. Build one LLM-as-judge on a *different, cheaper* model, validated against 50 of your own labels (report the agreement rate).
5. Add a CI job that fails when scores regress.

---

## Phase 5: Agentic AI — patterns, frameworks, memory and protocols (Weeks 16–22)

Now build agents, with the Phase 4 evals attached from the first commit. Learn the **patterns** in plain code first, then one or two frameworks deeply.

### 1. Agentic AI (by Andrew Ng) { #agentic-ai-ng }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free to audit
    - **Duration:** 3–10 hrs

**Instructor(s):** Andrew Ng

**Description:**
**Start here.** Reflection, tool use, planning and multi-agent patterns, built from first principles in plain Python, with a strong emphasis on evaluation and error analysis for agents.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/agentic-ai){ .md-button .md-button--primary }

### 2. Building effective agents (essay) { #building-effective-agents }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Engineering blog
    - **Cost:** Free
    - **Duration:** ~30 min

**Description:**
The canonical distinction between **workflows** (predefined code paths) and **agents** (loops the model directs), with the advice most teams need: use the simplest thing that works, and add autonomy only when it measurably helps.

[**Read Article :octicons-arrow-right-24:**](https://www.anthropic.com/engineering/building-effective-agents){ .md-button .md-button--primary }

### 3. LangChain Path (V2) — in this repo { #langchain-path-v2 }

!!! info inline end "Quick Stats"
    - **Platform:** Learning Pathways
    - **Cost:** Free
    - **Duration:** ~10–14 weeks part-time

**Description:**
The deep, mentor-guided, provider-neutral track for LangChain 1.x, LangGraph and Deep Agents. It covers agents, context engineering, middleware, MCP, security, harness engineering, ambient agents, evals and deployment. If LangGraph is your chosen framework, do its Phases 2–5 alongside this phase.

[**Open the Path :octicons-arrow-right-24:**](langchain-path.md){ .md-button .md-button--primary }

### 4. Agent Skills + Subagents { #anthropic-agent-skills }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai + Anthropic Academy
    - **Cost:** Free
    - **Duration:** 1 short course + 2 short self-paced

**Instructor(s):** Elie Schoppik (Anthropic)

**Description:**
**Skills** are folders of instructions and scripts (a `SKILL.md` plus resources) that an agent loads *on demand*. They're progressive disclosure for context. Published as an open standard in Dec 2025, they're now supported by dozens of agent products. At the 2026 AI Engineer World's Fair, "skill engineering" was called out as its own discipline. **Subagents** give a sub-task its own clean context and restricted tools. Take the DeepLearning.ai course, then Anthropic's *Introduction to agent skills* and *Introduction to subagents*.

- Security note: third-party skills are code you run. Audit them like dependencies. One audit found 36% of marketplace skills had a security flaw.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/agent-skills-with-anthropic){ .md-button .md-button--primary } [**Intro to agent skills :octicons-arrow-right-24:**](https://anthropic.skilljar.com/introduction-to-agent-skills){ .md-button } [**Intro to subagents :octicons-arrow-right-24:**](https://anthropic.skilljar.com/introduction-to-subagents){ .md-button }

### 5. Hugging Face AI Agents Course { #hf-agents-course }

!!! info inline end "Quick Stats"
    - **Platform:** huggingface.co/learn
    - **Cost:** Free (with certificate)
    - **Duration:** ~20–30 hrs

**Description:**
A broad course that compares frameworks (smolagents, LlamaIndex, LangGraph), with units on observability and evals and a benchmarked final project. It's good for seeing the same patterns in several frameworks and on open models.

[**Visit Course :octicons-arrow-right-24:**](https://huggingface.co/learn/agents-course){ .md-button .md-button--primary }

### 6. Agent Memory: Building Memory-Aware Agents { #memory-aware-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Oracle

**Description:**
Memory engineering: persistent stores, memory managers, and semantic tool retrieval that scales without bloating context. Know the three layers: within-session editing and compaction, cross-session memory stores, and procedural memory (skills the agent writes for itself, as Hermes Agent does). Memory is also an attack surface: memory poisoning is on the OWASP agentic Top 10.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents/){ .md-button .md-button--primary }

### 7. Building Coding Agents with Tool Execution { #coding-agents-exec }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** E2B

**Description:**
Agents that write and *run* code need sandboxes. This covers sandboxed execution, file I/O and iterating on results, which are the core of data-analysis and coding agents.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution){ .md-button .md-button--primary }

### 8. A2A: The Agent2Agent Protocol { #a2a-protocol }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Google Cloud & IBM Research

**Description:**
How independently built agents discover each other (Agent Cards) and delegate tasks. A2A reached v1.0 in early 2026 under the Linux Foundation. The mental model: **MCP connects an agent to tools; A2A connects agents to agents.** Most apps need MCP; A2A matters when agents cross team or vendor boundaries.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/){ .md-button .md-button--primary }

### 9. Optional electives (pick by interest)

- **Computer use / browser agents:** [Building AI Browser Agents](https://www.deeplearning.ai/short-courses/building-ai-browser-agents/). *Reality check:* on OSWorld-style desktop benchmarks, frontier agents still trail humans by about 30 points and take 2.7–4.3× more steps than needed (2026 papers). Use GUI automation where no API exists, and keep a human in the loop.
- **Voice agents:** [Building AI Voice Agents for Production](https://www.deeplearning.ai/courses/building-ai-voice-agents-for-production) (LiveKit): real-time pipelines and latency budgets
- **Generative UI:** [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/courses/build-interactive-agents-with-generative-ui) (CopilotKit): agents that render UI, a natural fit for your front-end skills
- **Programmatic prompt optimisation:** [DSPy: Build and Optimize Agentic Apps](https://www.deeplearning.ai/courses/dspy-build-optimize-agentic-apps): optimise prompts against your eval set instead of hand-tuning them
- **Role-based multi-agent:** [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- **Paid, project-heavy:** Ed Donner's [Complete Agentic AI Engineering Course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/) (Udemy)

### Choosing a harness: who runs the loop, who runs the infrastructure?

Before you pick a framework, answer two questions: **who supplies the agent loop** (the harness), and **who hosts it** (the deployment)? Anthropic's own documentation frames the options this way, and the same split exists on every platform.

| Option | You write | Harness | Hosting | Use when |
|---|---|---|---|---|
| **Hand-written loop** (any provider SDK) | The whole `while tool_use:` loop | You | You | Learning, or when you need full control (Phase 2 checkpoint) |
| **SDK tool runner** (e.g. Anthropic's `tool_runner`) | Just the tool functions | SDK | You | Custom-tool agents without hand-writing the loop |
| **Framework** (LangGraph, OpenAI Agents SDK, Google ADK, PydanticAI, MS Agent Framework) | Graph/agent definitions | Framework | You (or the framework's cloud) | Custom control flow, durable state, provider-neutrality |
| **Agent harness library** (Claude Agent SDK, Deep Agents) | A prompt + options | Batteries-included (files, shell, subagents, skills) | You | Coding-agent-style work on your own infra |
| **Managed agent platform** (e.g. Claude Managed Agents) | Agent config + your custom tools | Vendor | Vendor (sandbox per session, schedules, memory) | Hosted, long-running or scheduled agents without owning the infrastructure |

### Framework decision guide (September 2026)

Learn the **patterns** first. Frameworks are interchangeable wrappers around the same loop, so pick one primary framework and learn it deeply.

| Framework | Best for | Notes |
|---|---|---|
| **LangGraph / LangChain 1.x** | Controllable, stateful, durable workflows; provider-neutral | The most-demanded named agent framework in 2025–26 postings |
| **Claude Agent SDK** | Agents that need a coding-agent harness (files, shell, subagents, skills, hooks) | The harness behind Claude Code, as a library |
| **OpenAI Agents SDK** | Teams standardised on OpenAI's Responses API | Handoffs, guardrails and tracing built in |
| **Google ADK** | Google Cloud shops, multi-agent and live voice | Strong A2A support |
| **Microsoft Agent Framework** | Azure/.NET/enterprise Microsoft environments | Successor to AutoGen + Semantic Kernel (1.0 GA April 2026). **Don't start new projects on AutoGen** |
| **PydanticAI** | Type-safe Python agents with FastAPI-style ergonomics | A great fit for Django/FastAPI developers |
| **CrewAI / LlamaIndex** | Fast role-based prototypes / document-heavy agents | Check you get the control you need before committing |

**Recommendation for you:** LangGraph as your primary framework (it's portable, the most in demand, and this repo has a deep path for it), plus one harness library or managed platform that matches your employer's model provider.

### 🔨 Phase 5 checkpoint

Build a research-and-action agent for a domain you know. It needs:
- at least 4 tools, one of them via MCP
- long-term memory
- one subagent
- human approval before any write action
- a Skill that packages a repeatable procedure

Ship it with the Phase 4 eval harness, extended with **trajectory** evaluation: did the agent call the right tools in a sensible order?

---

## Phase 6: Harness engineering, long-running and ambient agents (Weeks 23–26) — *new*

The 2026 lesson: once models are capable, **reliability comes from the harness**. This phase makes harnesses a first-class engineering artefact that you design, test, measure and prune.

### 1. Effective harnesses for long-running agents { #long-running-harnesses }

!!! info inline end "Quick Stats"
    - **Platform:** Anthropic Engineering blog
    - **Cost:** Free
    - **Duration:** ~30 min

**Description:**
How to keep an agent productive across many context windows:
- an **initializer** session that sets up the environment
- a **progress file** plus git commits after each step
- a **feature list in JSON**, each feature marked failing until verified
- one feature at a time
- end-to-end verification with browser automation

The two failure modes it fixes, trying to one-shot everything and declaring victory early, show up in every long-running agent.

[**Read Article :octicons-arrow-right-24:**](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents){ .md-button .md-button--primary }

### 2. The State of AI Harness Engineering 2026 { #state-of-harness }

!!! info inline end "Quick Stats"
    - **Platform:** Marmelab blog
    - **Cost:** Free
    - **Duration:** ~45 min

**Description:**
An evidence review of 246 repositories and 57 publications, published September 2026. Its key findings:
- **Replace instructions with scripts.** Written rules often have little measurable effect.
- **Fewer tools can win.** Vercel removed 80% of its agent's tools and success went from 80% to 100%.
- **Test the harness,** including negative cases. 60% of harnesses had no tests at all.
- **Machine-generated context files can hurt.**
- **Prune harness rot** as models improve.
- **Multi-agent reviewer patterns often underperform.**

Read it critically: the authors call the field provisional.

[**Read Report :octicons-arrow-right-24:**](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html){ .md-button .md-button--primary }

### 3. Loop engineering and ambient agents { #loop-engineering }

!!! info inline end "Quick Stats"
    - **Platform:** Claude Code docs + Claude Platform docs + AI Engineer World's Fair recap
    - **Cost:** Free
    - **Duration:** ~2 hrs

**Description:**
**Loop engineering** (from the AI Engineer World's Fair 2026) is designing the nested loops around an agent: an autonomous inner loop, and a human outer loop that reviews, redirects and approves. **Ambient agents** run from schedules and events instead of chat messages. Study three real implementations:
- [Claude Code routines](https://code.claude.com/docs/en/routines): scheduled, API or GitHub triggers; untrusted fire payloads
- [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview): a hosted loop and sandbox, scheduled deployments, memory, outcomes graded against a rubric
- the LangGraph approach in [LangChain Path Step 5.7](langchain-path.md)

Design rules for when nobody is watching:
- a self-contained prompt with a definition of done
- budgets
- durable approvals for irreversible actions
- idempotent runs
- trigger payloads treated as untrusted

[**Read the recap :octicons-arrow-right-24:**](https://www.latent.space/p/aiewf26trends){ .md-button .md-button--primary }

### 4. Personal agent harnesses: OpenClaw and Hermes teardown { #personal-agents }

!!! info inline end "Quick Stats"
    - **Platform:** Project docs + reporting
    - **Cost:** Free
    - **Duration:** ~4–6 hrs (sandboxed)

**Description:**
Study these as *case studies*, not skills to master. They're products that change fast, but their architecture and failures teach durable lessons. [OpenClaw](https://docs.openclaw.ai/) and [Hermes Agent](https://hermes-agent.nousresearch.com/) are self-hosted, always-on agents with:
- messaging gateways (Discord, Telegram, WhatsApp)
- schedules
- skills and local memory
- self-written skills (Hermes)

Then read OpenClaw's [security history](https://en.wikipedia.org/wiki/OpenClaw): malicious ClawHub skills, prompt-injection exfiltration through a third-party skill, disabled-by-default sandboxing, and government restrictions. Map each incident to the lethal trifecta and the OWASP agentic risks.

- **Safety rule:** run either one only in a throwaway VM with dummy accounts. Never use real email, keys or files.

[**Read OpenClaw docs :octicons-arrow-right-24:**](https://docs.openclaw.ai/){ .md-button .md-button--primary }

### 🔨 Phase 6 checkpoint: harness-engineer your Phase 5 agent

1. Write down its **guides and sensors** in a table, split into computational and inferential. Convert at least two written rules into executable checks.
2. Add a **harness test suite** with negative cases proving each guard fires.
3. Make it **long-running**: a progress file, a JSON feature/task list and incremental commits, so a fresh session can resume.
4. Make one workflow **ambient**: a scheduled or webhook-triggered run with budgets, durable approval and idempotency.
5. Run a **harness ablation**: remove one guide or sensor at a time, re-run the evals and delete anything that doesn't earn its tokens.

---

## Phase 7: Production — security, identity, governance, cost and serving (Weeks 27–30)

Agents take actions with real credentials. This phase makes them safe, accountable, affordable and operable.

### 1. OWASP Top 10 for LLM and Agentic Applications { #owasp }

!!! info inline end "Quick Stats"
    - **Platform:** OWASP Gen AI Security Project
    - **Cost:** Free
    - **Duration:** ~2–3 hrs reading

**Description:**
The shared vocabulary for AI risks. The LLM Top 10 covers prompt injection, sensitive data disclosure and excessive agency. The Agentic Top 10 (2026) adds goal hijacking, tool misuse, memory poisoning and privilege abuse. Read it alongside Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): untrusted content + private data + external communication = exfiltration risk.

[**Visit OWASP GenAI :octicons-arrow-right-24:**](https://genai.owasp.org/){ .md-button .md-button--primary }

### 2. Red Teaming LLM Applications { #red-teaming }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor(s):** Giskard

**Description:**
Attack your own application: prompt injection, data leakage, jailbreaks and harmful outputs, both by hand and with automated scanning. Turn every successful attack into a regression test.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/){ .md-button .md-button--primary }

### 3. Governing AI Agents { #governing-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Databricks

**Description:**
Permissions, data access controls, auditability and policy for agents in an organisation. These are the questions security and compliance teams will ask before your agent reaches production.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/governing-ai-agents){ .md-button .md-button--primary }

### 4. Agent identity, regulation and payments (reading list) { #identity-regulation }

!!! info inline end "Quick Stats"
    - **Platform:** Specs and legal analysis
    - **Cost:** Free
    - **Duration:** ~3 hrs

**Description:**
Three areas that became concrete in 2026:

- **Agent identity:** treat each agent as its own OAuth client with narrow scopes and short-lived tokens, never as a shared human session. Remote MCP servers use OAuth 2.1 (see the [MCP spec](https://modelcontextprotocol.io/specification/latest)). Workload-identity standards (SPIFFE/WIMSE) are appearing in production.
- **Regulation:** the EU AI Act's **Article 50 transparency obligations** (such as disclosing that users are talking to an AI) applied from 2 Aug 2026; high-risk obligations were deferred to Dec 2027 / Aug 2028 ([analysis](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon)). Know whether your system is in scope.
- **Agentic payments (awareness):** agents that buy things use protocols such as [ACP](https://docs.stripe.com/agentic-commerce/acp) (OpenAI/Stripe), AP2 (Google) and MPP (Stripe/Tempo), built around scoped, signed spending authority. Only go deeper if your work touches commerce.

[**Read MCP authorization spec :octicons-arrow-right-24:**](https://modelcontextprotocol.io/specification/latest){ .md-button .md-button--primary }

### 5. Fast & Efficient LLM Inference with vLLM { #vllm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Red Hat

**Description:**
How serving engines get their throughput (continuous batching, paged KV cache, prefix caching) and how to self-host open-weight models. Even if you only call APIs, this explains *why* prompt caching and stable prompt prefixes save money.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/fast-and-efficient-llm-inference-with-vllm){ .md-button .md-button--primary }

### 6. 12-Factor Agents (reading) { #twelve-factor-agents }

!!! info inline end "Quick Stats"
    - **Platform:** GitHub (HumanLayer)
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Engineering principles for production agents from a web developer's perspective: own your prompts, own your context window, own your control flow, make agents stateless reducers, and pause and resume via APIs.

[**Read on GitHub :octicons-arrow-right-24:**](https://github.com/humanlayer/12-factor-agents){ .md-button .md-button--primary }

### Production checklist to apply

- **Least privilege and identity:** tools authorise against the *user's or agent's own* identity, never the model's claims. Scoped, short-lived credentials; secrets never enter the model's context.
- **Human approval** for irreversible or external actions, plus **budgets** (maximum model and tool calls, tokens, spend per user or run).
- **Reliability:** retries with backoff, provider fallback (refusals and outages), and timeouts. Rate limits cause about a third of LLM call failures, and a `refusal` stop reason must be handled, not ignored.
- **Cost:**
  - Cache first: keep prefixes stable for prompt caching, and use semantic caching.
  - Then the effort level per route.
  - Then model routing or the **advisor pattern**, where a cheap executor consults a strong model only on hard steps.
  - Judge cost per *completed task*, not per request.
- **Observability:** traces with user/feature metadata, OpenTelemetry-compatible where possible.
- **Change management:** every prompt, model, tool or harness change runs the eval suite. Model upgrades are regressions until proven otherwise.
- **Compliance:** AI disclosure where Article 50 or similar rules apply; audit logs for agent actions.

### 🔨 Phase 7 checkpoint

Take your Phase 6 agent through a security, identity and cost review:
- a written threat model: which legs of the lethal trifecta does it have?
- five red-team attacks turned into automated tests
- a per-agent identity with scoped credentials
- an AI-disclosure statement
- a cost report showing spend per completed task before and after two optimisations, with eval scores unchanged

---

## Phase 8: LLM internals, post-training and RL environments (Weeks 31–38)

With systems, evals and harnesses in hand, going under the hood pays off. You'll know *when* adapting a model beats prompting, retrieval and a better harness, and you'll have the evals to prove it.

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
A minimal, readable, end-to-end ChatGPT-style pipeline (Oct 2025): tokenizer training, pretraining, supervised fine-tuning, optional RL, inference and a web UI, all in one small codebase. Read it even if you don't run the full training.

[**View Repository :octicons-arrow-right-24:**](https://github.com/karpathy/nanochat){ .md-button .md-button--primary }

### 3. Finetuning LLMs → Post-training of LLMs { #post-training }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** 2 short courses

**Instructor(s):** Sharon Zhou; Banghua Zhu (University of Washington / Nexusflow)

**Description:**
First, the decision framework: when to fine-tune versus prompt versus retrieve versus improve the harness. Then the three post-training methods that turn a base model into an assistant: SFT, DPO, and online reinforcement learning.

[**Post-training of LLMs :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/post-training-of-llms){ .md-button .md-button--primary } [**Finetuning LLMs :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/){ .md-button }

### 4. Reinforcement Fine-Tuning LLMs With GRPO { #rft-grpo }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** Short course (~1–2 hrs)

**Instructor(s):** Predibase

**Description:**
Reinforcement fine-tuning with programmatic reward functions. It's the technique behind modern reasoning models, and the most practical way to teach a small model a narrow, verifiable skill without large labelled datasets. Your Phase 4 checks often *become* the reward functions.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/reinforcement-fine-tuning-llms-grpo){ .md-button .md-button--primary }

### 5. RL environments and verifiers: the 2026 frontier skill { #rl-environments }

!!! info inline end "Quick Stats"
    - **Platform:** Reading + your own experiment
    - **Cost:** Free
    - **Duration:** ~4 hrs

**Description:**
Frontier labs now train agents with **reinforcement learning from verifiable rewards (RLVR)** inside *environments*. An environment is a task, a sandboxed harness the model acts in, and a **verifier** that turns the outcome into a reward. Building these environments became a fast-growing specialism and startup market in 2026. The core difficulty is **reward hacking**: weak verifiers get gamed. That is eval design with higher stakes, and it reuses everything from Phases 4 and 6.

- Build: wrap one Phase 4 check as a reward function, then try to *hack it* yourself before a model does
- Read: an industry overview such as [Wing VC's analysis of the RL environment market](https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why)

[**Read the analysis :octicons-arrow-right-24:**](https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why){ .md-button .md-button--primary }

### 6. Hugging Face smol course + TRL / Unsloth docs { #smol-course }

!!! info inline end "Quick Stats"
    - **Platform:** huggingface.co/learn
    - **Cost:** Free
    - **Duration:** Self-paced

**Description:**
Practical post-training of small models (instruction tuning, preference alignment, LoRA) with Hugging Face TRL. Pair it with the [Unsloth docs](https://docs.unsloth.ai/) for memory-efficient LoRA/QLoRA and GRPO on a single consumer or rented GPU.

[**Visit Course :octicons-arrow-right-24:**](https://huggingface.co/learn/smol-course){ .md-button .md-button--primary }

### Optional deeper dives

- **[Stanford CS336: Language Modeling from Scratch (Spring 2026)](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)**: the rigorous version. Tokenization, architectures, GPUs and kernels, parallelism, scaling laws, inference and alignment.
- **[Quantization Fundamentals with Hugging Face](https://www.deeplearning.ai/short-courses/quantization-fundamentals-with-hugging-face/)**: essential before self-hosting.
- **[Attention in Transformers: Concepts and Code in PyTorch](https://www.deeplearning.ai/courses/attention-in-transformers-concepts-and-code-in-pytorch)** (StatQuest).
- **[Generative AI with Large Language Models](https://www.coursera.org/learn/generative-ai-with-llms)** (Coursera), free to audit.

### 🔨 Phase 8 checkpoint

Pick a narrow, verifiable task from your own work, such as SQL generation for your schema or extracting fields from your documents.
1. Set a baseline with a frontier API model, the same model with a better harness (tools, examples, checks), and a small open-weight model, all using your Phase 4 harness.
2. Fine-tune the small model: LoRA SFT, and optionally GRPO with your checks as rewards.
3. Report quality, latency and cost per 1,000 requests for every variant, plus any reward hacking you caught.

Conclude honestly. "A better harness beat fine-tuning" is a valid, valuable result.

---

## Phase 9: Capstone projects and portfolio (Weeks 39+)

Each project ships with a README explaining design decisions and trade-offs, plus four things that separate an AI engineer's portfolio from tutorial output: an **eval report**, a **harness description** (guides and sensors, with their tests), a **threat model** and a **cost analysis**.

### Project 1: Production RAG assistant as a web app

Your docs (PDF + Markdown + code) → hybrid retrieval with re-ranking → cited answers, a semantic cache, auth and rate limiting in Django, Flask or FastAPI. An eval suite in CI and a dashboard of cost, latency and quality. *Demonstrates Phases 2–4.*

### Project 2: Harness-engineered agent with MCP, memory and approvals

An agent that takes real actions in a sandboxed environment. It uses MCP-served tools, long-term memory, skills and approval gates, with trajectory evals and a harness test suite. Include the ablation table showing which guides and sensors earned their place. *Demonstrates Phases 4–6.*

### Project 3: Ambient agent for your community

A scheduled or event-driven agent for your Discord community or team, such as a nightly digest, triage or monitoring. It has budgets, durable approvals, idempotent runs and untrusted-input handling, and runs for two weeks unattended with a written incident log. *Demonstrates Phases 6–7.*

### Project 4: Fine-tuned small model vs frontier API vs better harness

The Phase 8 experiment, polished: reproducible training, eval comparison, serving via vLLM or a managed endpoint, and a clear recommendation. *Demonstrates Phase 8.*

### Portfolio presentation tips

Open-source the code. Write a short post per project focusing on *decisions* and *measured results*, include failure analyses (what the evals and sensors caught), and show cost per completed task. Hiring managers in 2026 look for evidence of evaluation, harness design, reliability engineering, and judgement about when *not* to use an agent.

---

## What NOT to spend time on in 2026

| Skip or de-prioritise | Why | Do this instead |
|---|---|---|
| OpenAI **Assistants API** tutorials | Shut down 26 Aug 2026 | Responses API / Agents SDK, or a framework |
| **AutoGen** for new projects | Maintenance mode since Oct 2025 | Microsoft Agent Framework (on the Microsoft stack) or LangGraph |
| Model-specific prompt tricks (o1-era "don't use CoT", Llama 2 `[INST]` formats), `temperature` tuning, fixed thinking budgets | Superseded by built-in reasoning, effort controls and chat templates | Clear goals, good context, effort levels, evals |
| Hard-wiring one vendor everywhere | Models and prices change monthly; lock-in is a cost | Provider + model in config; concepts first |
| Pre-1.0 LangChain tutorials (`AgentExecutor`, `initialize_agent`, `ConversationBufferMemory`) | Replaced in LangChain 1.0 (Oct 2025) | The [LangChain Path (V2)](langchain-path.md) |
| Hand-parsing JSON from model output | Native structured output is standard | Schema-constrained output with Pydantic |
| Legacy MCP HTTP+SSE transport, Sampling, Roots | Deprecated in the 2026-07-28 spec | Streamable HTTP; call model APIs directly |
| Ever-longer `CLAUDE.md`/`AGENTS.md` rulebooks, or machine-generated context files | Written rules are often ignored; generated context files can *reduce* success | Short guides + executable sensors (hooks, tests, linters) |
| Adding reviewer agents or long agent-to-agent chains "for quality" | Evidence shows little or negative benefit | A single agent + deterministic checks; subagents only for context isolation |
| Running personal agents (OpenClaw-style) with real credentials, or installing unvetted marketplace skills | Documented malware and exfiltration incidents | Sandboxed VM, dummy accounts, audited skills |
| Treating any single agent product as a career skill | Products rename and rework within months | Learn the patterns: harness, loop, context, evals |
| Fine-tuning before you have evals, a RAG baseline and a decent harness | You can't tell if it helped | Phases 3–6 first, then Phase 8 |
| Chasing leaderboards to choose models | Benchmarks rarely match your task | Your own eval set, per task |
| "Prompt engineer" as a destination role | The market shifted to systems roles | Agentic engineering, context engineering, evals |

---

## Additional resources for the whole journey

### Free platforms

- **[DeepLearning.ai short courses](https://www.deeplearning.ai/courses/)**: new courses almost weekly; filter for agents, evals and inference.
- **[Anthropic Academy](https://anthropic.skilljar.com/)**: Claude API, MCP (intro and advanced), Claude Code, agent skills, subagents.
- **[Hugging Face Learn](https://huggingface.co/learn)**: Agents, MCP, LLM and smol (post-training) courses.
- **[LangChain Academy](https://academy.langchain.com/)**: official LangGraph and LangSmith courses.

### Books

- **_AI Engineering_**, Chip Huyen (O'Reilly, 2025). The best single book on building applications on foundation models.
- **_Build a Large Language Model (From Scratch)_** and **_Build a Reasoning Model (From Scratch)_**, Sebastian Raschka (Manning). Code-first companions to Phase 8.
- **_Evals for AI Engineers_**, Shreya Shankar & Hamel Husain (O'Reilly, scheduled late 2026).

### Reports worth reading once a year

- **[Stanford AI Index](https://hai.stanford.edu/ai-index/2026-ai-index-report)**: capability, adoption and labour-market data.
- **[Datadog State of AI Engineering](https://www.datadoghq.com/state-of-ai-engineering/)**: what production AI actually looks like.
- **[Anthropic Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report)**: how engineering work is changing.
- **[The State of AI Harness Engineering](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html)**: evidence on harness practices.

### People and channels

**Andrej Karpathy** (first principles, agentic engineering), **3Blue1Brown** (visual maths), **Simon Willison** (pragmatic, security-aware coverage of new models and tools), **Hamel Husain** (evals), **Birgitta Böckeler** (harness engineering), the **Latent Space** podcast and the **AI Engineer World's Fair** talks (industry direction), and **The Pragmatic Engineer** (how engineering work is changing).

### Roadmaps

**[roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer)**: interactive and continuously updated. Use it as a checklist, not a syllabus.

---

## Summary: the complete plan at a glance

| Phase | Focus | Weeks | Core free resources | Key outcome |
|---|---|---|---|---|
| 0 | **Agentic engineering & harness basics** | 1–2 | Claude Code course, harness essays, Spec-Driven Dev, Claude Code docs | Supervised coding-agent workflow; a tested harness in your own repo |
| 1 | LLM foundations | 3–4 | Karpathy, 3Blue1Brown, How Transformer LLMs Work, effort docs | Accurate mental model; reasoning trade-offs |
| 2 | Building LLM apps | 5–8 | Building Systems, Claude API course, structured output, tool-writing essay, MCP | Typed, tool-using, provider-configurable services + an MCP server |
| 3 | Retrieval & context engineering | 9–12 | Context-engineering essay, RAG course, Advanced Retrieval, Document AI, Semantic Caching | Measured, cited retrieval with local embeddings |
| 4 | Evals & observability | 13–15 | Evals FAQ, Evaluating AI Agents, NeMo reliability | Error analysis, validated judges, CI gate |
| 5 | Agentic AI | 16–22 | Agentic AI (Ng), Building Effective Agents, LangChain Path V2, Skills + Subagents, Memory, A2A | Evaluated agents with memory, MCP, skills, HITL |
| 6 | **Harness engineering & ambient agents** | 23–26 | Long-running harnesses, State of Harness Engineering, routines/managed agents, OpenClaw/Hermes teardown | Tested, ablated harness; a scheduled agent |
| 7 | Security, identity, governance, cost | 27–30 | OWASP, Red Teaming, Governing Agents, identity/regulation reading, vLLM, 12-Factor Agents | Threat-modelled, identity-scoped, cost-controlled agent |
| 8 | Internals, post-training & RL environments | 31–38 | Zero to Hero, nanochat, Post-training, GRPO, RL environments, smol course | Evidence-based adapt-or-harness decisions |
| 9 | Portfolio | 39+ | — | Four projects with evals, harness docs, threat models, cost analyses |

**Totals:** about 40 core free resources (plus electives). **$0 core course cost**, plus model API usage (set a spend limit) and about $50–100 of optional paid items. About 9 months at 8–10 hrs/week.

The biggest change is the order and the emphasis, not any single course. **Measure before you optimise, harness before you automate, contain before you trust, and understand the system before the model internals.**

---

*Curriculum V2 (revised) · researched September 2026 · V1 (March 2026) remains available at [AI Mastery Plan (V1)](../ai-mastery-plan.md).*
