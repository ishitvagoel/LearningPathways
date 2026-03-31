---
title: AI Developer Mastery Plan
description: Strategic roadmap for becoming a senior AI engineer.
---

# The AI Developer Mastery Plan for Web Developers

**You're in an ideal position to transition from web development to AI engineering.** Your Python/Flask/Django background gives you the software engineering foundation that most AI courses assume you lack — meaning you can skip the "learn Python first" stages and jump straight into applied AI. Based on analysis of 100+ courses across DeepLearning.ai, Coursera, Udemy, YouTube, and open-source platforms, plus multiple 2025–2026 AI engineer roadmaps, here is a phased plan that takes you from prompt engineering to building production agentic AI systems over 6+ months. The total cost: **$0–50**, with the bulk of this plan completely free.

A key insight from multiple roadmaps (roadmap.sh, KDnuggets, DataUnboxed): AI engineering is *not* ML research. As Andrej Karpathy noted, "One can be quite successful in this role without ever training anything." This plan prioritizes building with LLMs first, then deepens into internals — the fastest path for a working developer.

---
## Phase 1: Foundation and prompt engineering (Weeks 1–3)

You've already completed *AI for Everyone* and *Generative AI for Everyone*, and you're currently working through *ChatGPT Prompt Engineering for Developers*. This phase rounds out your foundation by extending prompt engineering to different models and building your first LLM-powered systems.

### 1. ChatGPT Prompt Engineering for Developers ✅ { #prompt-eng-dev }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Isa Fulford (OpenAI) & Andrew Ng

**Description:**
Covers two key principles of effective prompting, systematic prompt engineering, and building a custom chatbot with the OpenAI API. Finish this first — it's the gateway to everything else.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/){ .md-button .md-button--primary }

### 2. Building Systems with the ChatGPT API { #building-systems }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Isa Fulford & Andrew Ng

**Description:**
The natural next step after prompt engineering. Teaches you to chain multiple API calls into complex workflows — classifying queries, evaluating safety, multi-step reasoning. This is where your web development instincts kick in: you're building *systems*, not just writing prompts.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/){ .md-button .md-button--primary }

### 3. Prompt Engineering with Llama 2 & 3 { #prompt-eng-llama }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Amit Sangani (Meta)

**Description:**
Extends your skills beyond OpenAI to open-source models. Covers few-shot, chain-of-thought, and Llama Guard for safe AI. Understanding both proprietary and open-source models is essential for cost-effective production work.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/prompt-engineering-with-llama-2/){ .md-button .md-button--primary }

### 4. Reasoning with o1 { #reasoning-o1 }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Covers OpenAI's reasoning models and how to leverage chain-of-thought capabilities — a newer paradigm that changes how you architect certain LLM applications.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/reasoning-with-o1/){ .md-button .md-button--primary }

### 5. 3Blue1Brown: Neural networks and transformers series { #3b1b-neural }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~3 hrs total

**Instructor:** Grant Sanderson

**Description:**
Watch "But what is a Neural Network?", "Gradient descent", "Backpropagation", then the newer transformer chapters: "Transformers, the tech behind LLMs" and "Attention in transformers, step-by-step." These stunning visual explanations build intuition that will pay dividends throughout the entire plan. No code required — pure conceptual understanding with beautiful animations.

[**Watch Series :octicons-arrow-right-24:**](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi){ .md-button .md-button--primary }

### 6. Karpathy: "Deep Dive into LLMs like ChatGPT" { #karpathy-deep-dive }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~3.5 hrs

**Instructor:** Andrej Karpathy

**Description:**
A comprehensive end-to-end overview of how LLMs work: pretraining, tokenization, transformer internals, supervised fine-tuning, hallucinations, tool use, RLHF, and DeepSeek-R1's reasoning breakthroughs. Designed for a general audience — no code required.

[**Watch Video :octicons-arrow-right-24:**](https://www.youtube.com/watch?v=7xTGNNLPyMI){ .md-button .md-button--primary }

---

## Phase 2: LLM APIs and building AI-powered apps (Weeks 4–7)

This is where your web development background becomes a superpower. You already know how to build APIs, handle requests, manage state, and deploy applications. Now you're adding LLMs as a new tool in your stack.

### 1. LangChain for LLM Application Development { #langchain-app-dev }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Harrison Chase (LangChain creator) & Andrew Ng

**Description:**
LangChain is the most widely adopted framework for LLM applications. This course covers the fundamentals: models, prompts, parsers, memory, chains, and agents as reasoning engines. Harrison Chase explains *when and why* to use each component.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/){ .md-button .md-button--primary }

### 2. Open Source Models with Hugging Face { #os-models-hf }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Not every application needs GPT-4. This teaches you to find, select, and deploy open-source models from the Hugging Face ecosystem — critical for cost-sensitive or privacy-sensitive deployments.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/open-source-models-hugging-face/){ .md-button .md-button--primary }

### 3. Getting Structured LLM Output { #structured-output }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Real applications need structured, reliable outputs (JSON, typed schemas). This course solves the #1 frustration developers hit when integrating LLMs into existing systems.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/getting-structured-llm-output/){ .md-button .md-button--primary }

### 4. Improving Accuracy of LLM Applications { #accuracy-llm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Covers techniques to improve reliability — the gap between "cool demo" and "production system" that your engineering background will appreciate.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/improving-accuracy-of-llm-applications/){ .md-button .md-button--primary }

### 5. MCP: Build Rich-Context AI Apps with Anthropic { #mcp-anthropic }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Anthropic Partner

**Description:**
The **Model Context Protocol** has become an industry standard (adopted by OpenAI, Google, Microsoft, and Anthropic) for connecting LLMs to external tools and data. This is the modern way to build integrations — directly relevant to your web development background.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/){ .md-button .md-button--primary }

### 6. Hugging Face LLM Course { #hf-llm-course }

!!! info inline end "Quick Stats"
    - **Platform:** huggingface.co/learn
    - **Cost:** Free
    - **Duration:** Self-paced

**Description:**
Comprehensive text-based course covering the Transformers library, tokenizers, datasets, and fine-tuning. Includes Gradio for building quick demos. Work through Chapters 1–4 alongside the DeepLearning.ai courses for deeper framework mastery.

[**Visit Course :octicons-arrow-right-24:**](https://huggingface.co/learn/llm-course){ .md-button .md-button--primary }

### 7. Udemy: LLM Engineering — Master AI and Large Language Models { #udemy-llm-eng }

!!! info inline end "Quick Stats"
    - **Platform:** Udemy
    - **Cost:** ~$10–15 on sale
    - **Duration:** ~15 hrs

**Instructor:** Ed Donner

**Description:**
Consistently ranked the **#1 LLM engineering course on Udemy**. Includes 8 real-world projects: AI brochure generator, multimodal customer support agent, meeting minutes tool, Python-to-C++ code optimizer. Covers 20+ models, LangChain, HuggingFace, Gradio, RAG, QLoRA fine-tuning, and agents.

[**Visit Course :octicons-arrow-right-24:**](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/){ .md-button .md-button--primary }

---

## Phase 3: RAG, vector databases, and advanced app patterns (Weeks 8–13)

RAG is the **single most practical AI pattern for production applications** — it lets you ground LLMs in your own data without fine-tuning. This phase is where you build the applications that make up most real-world AI deployments today.

### 1. LangChain: Chat with Your Data { #langchain-rag }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Harrison Chase

**Description:**
The definitive introduction to RAG. Covers the full pipeline: document loading (80+ loaders), document splitting, vector stores, embeddings, and advanced retrieval. You'll build a chatbot that answers questions from your own documents.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/){ .md-button .md-button--primary }

### 2. Vector Databases: from Embeddings to Applications { #vector-db-apps }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Zain Hassan (Weaviate)

**Description:**
Goes deeper into *how* vector databases work: embeddings, distance metrics, ANN algorithms (HNSW), sparse/dense/hybrid search. Understanding the internals helps you choose the right vector DB and tune performance.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/){ .md-button .md-button--primary }

### 3. Building Applications with Vector Databases { #build-apps-vector-db }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Pinecone Partner

**Description:**
Six practical applications beyond basic RAG: semantic search, recommendation systems, hybrid search (text+images), facial similarity, anomaly detection. Broadens your mental model of what vector databases can do.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/){ .md-button .md-button--primary }

### 4. Advanced Retrieval for AI with Chroma { #adv-retrieval-chroma }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Chroma Partner

**Description:**
Focuses on *improving* retrieval quality: using LLMs to improve queries, query expansion, cross-encoder re-ranking, and training embedding adapters with user feedback. This is where you learn to make RAG actually *good*.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/){ .md-button .md-button--primary }

### 5. Building and Evaluating Advanced RAG Applications { #eval-rag }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** LlamaIndex & TruEra Partners

**Description:**
Introduces evaluation — the most underappreciated skill in AI engineering. You can't improve what you can't measure. Covers RAG evaluation techniques using TruEra tools.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/){ .md-button .md-button--primary }

### 6. Preprocessing Unstructured Data for LLM Applications { #preprocess-data }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Unstructured.io Partner

**Description:**
Real-world data is messy: PDFs, Word docs, tables, images. This course teaches data extraction and preparation for RAG pipelines — the unglamorous but critical work that separates demos from production systems.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/preprocessing-unstructured-data-for-llm-applications/){ .md-button .md-button--primary }

### 7. Knowledge Graphs for RAG { #knowledge-graphs-rag }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Neo4j Partner

**Description:**
Graph-based retrieval is increasingly important for complex domains where relationships between entities matter. Combines Neo4j with RAG for more sophisticated knowledge retrieval.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/){ .md-button .md-button--primary }

### 8. Generative AI with Large Language Models { #coursera-genai-llm }

!!! info inline end "Quick Stats"
    - **Platform:** Coursera
    - **Cost:** Free to audit
    - **Duration:** ~20 hrs

**Instructors:** Chris Fregly, Antje Barth (AWS & DeepLearning.AI)

**Description:**
This is the single most important longer course in the plan. Covers the **complete LLM lifecycle**: transformer architecture, training, fine-tuning, RLHF, scaling laws, and deployment. It bridges Phases 3 and 4, providing the theoretical backbone that makes everything else click.

[**Visit Course :octicons-arrow-right-24:**](https://www.coursera.org/learn/generative-ai-with-llms){ .md-button .md-button--primary }

### 9. LangChain — Develop AI Agents with LangChain & LangGraph { #udemy-langchain }

!!! info inline end "Quick Stats"
    - **Platform:** Udemy
    - **Cost:** ~$10–15 on sale
    - **Duration:** ~21 hrs

**Instructor:** Eden Marco

**Description:**
The **most popular LangChain course on Udemy**, re-recorded for LangChain V1.0+. Builds three full projects: Ice Breaker agent, Documentation Helper (RAG chatbot), and a ChatGPT Code Interpreter clone. Designed for experienced software engineers — explains *when and why*, not just *how*.

[**Visit Course :octicons-arrow-right-24:**](https://www.udemy.com/course/langchain/){ .md-button .md-button--primary }

---

## Phase 4: LLM internals — transformers, embeddings, and fine-tuning (Weeks 14–21)

Now that you've built practical applications, this phase gives you the *understanding* of what's happening under the hood. This isn't academic — it directly improves your ability to debug, optimize, and architect AI systems.

### 1. Andrej Karpathy's "Neural Networks: Zero to Hero" { #karpathy-zero-to-hero }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~14.5 hrs

**Instructor:** Andrej Karpathy

**Description:**
Widely considered **the single best deep learning tutorial series ever created**. Karpathy builds everything from absolute scratch in Python/PyTorch: micrograd, bigram language models, MLP character-level models, and a GPT from scratch following the "Attention is All You Need" paper.

[**Watch Series :octicons-arrow-right-24:**](https://karpathy.ai/zero-to-hero.html){ .md-button .md-button--primary }

### 2. 3Blue1Brown: "How might LLMs store facts" + "Attention in transformers" { #3b1b-transformer-mech }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~40 min total

**Instructor:** Grant Sanderson

**Description:**
These videos visualize the mechanics of how transformers actually store and retrieve knowledge — concepts that are extremely hard to grasp from text alone.

[**Watch Video :octicons-arrow-right-24:**](https://www.youtube.com/watch?v=9-Jl0dxWQs8){ .md-button .md-button--primary }

### 3. Understanding and Applying Text Embeddings { #apply-embeddings }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Andrew Ng (with Google Cloud)

**Description:**
Solidifies your understanding of what embeddings are, how they're created, and how to use them effectively. Essential theoretical grounding for all the RAG work in Phase 3.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/google-cloud-vertex-ai/){ .md-button .md-button--primary }

### 4. Embedding Models { #embedding-models-arch }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Deeper dive into how embedding models work, including training approaches and architectural choices.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/embedding-models-from-architecture-to-implementation/){ .md-button .md-button--primary }

### 5. Finetuning Large Language Models { #finetune-llm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Sharon Zhou (Lamini)

**Description:**
The essential starting point for fine-tuning: when to fine-tune vs. prompt, preparing training data, the complete fine-tuning pipeline. Clarifies *decision-making* around fine-tuning, not just mechanics.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/){ .md-button .md-button--primary }

### 6. Efficiently Serving LLMs { #serve-llm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Predibase Partner

**Description:**
Covers **LoRA** (Low-Rank Adaptation) for parameter-efficient fine-tuning and quantization for reducing model memory. These are the techniques that make fine-tuning affordable on consumer hardware.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/efficiently-serving-llms/){ .md-button .md-button--primary }

### 7. Pretraining LLMs { #pretrain-llm }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Sung Kim & Lucy Park (Upstage)

**Description:**
The complete pretraining pipeline from data preparation through training execution. Covers the Depth Upscaling technique that reduces costs by **70%**. Even if you never pretrain a model, understanding this process deepens your intuition about how LLMs behave.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/pretraining-llms/){ .md-button .md-button--primary }

### 8. Quantization Fundamentals with Hugging Face { #quantization-hf }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~2 hrs total

**Description:**
Quantization is how you run large models on smaller hardware. This course goes from fundamentals to advanced techniques — directly practical for deploying open-source models.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/quantization-fundamentals-with-hugging-face/){ .md-button .md-button--primary }

### 9. Reinforcement Learning from Human Feedback { #rlhf-course }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
RLHF is how models like ChatGPT get aligned with human preferences. Understanding this process helps you understand model behavior and the alignment landscape.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/reinforcement-learning-from-human-feedback/){ .md-button .md-button--primary }

### Optional Deeper Dives

#### Deep Learning Specialization { #dl-specialization }

!!! info inline end "Quick Stats"
    - **Platform:** Coursera
    - **Cost:** Free to audit
    - **Duration:** ~3 months

**Instructor:** Andrew Ng

**Description:**
Five courses covering neural networks from scratch through CNNs, RNNs, and transformers. Take this if you want the full theoretical foundation.

[**Visit Specialization :octicons-arrow-right-24:**](https://www.coursera.org/specializations/deep-learning){ .md-button .md-button--primary }

#### NLP Specialization { #nlp-specialization }

!!! info inline end "Quick Stats"
    - **Platform:** Coursera
    - **Cost:** Free to audit
    - **Duration:** 4 courses

**Instructors:** Łukasz Kaiser et al.

**Description:**
Co-taught by **Łukasz Kaiser, co-author of the original Transformer paper**. Covers sentiment analysis through attention mechanisms and BERT.

[**Visit Specialization :octicons-arrow-right-24:**](https://www.coursera.org/specializations/natural-language-processing){ .md-button .md-button--primary }

#### freeCodeCamp: "Code an LLM From Scratch" { #fcc-llm-scratch }

!!! info inline end "Quick Stats"
    - **Platform:** YouTube
    - **Cost:** Free
    - **Duration:** ~6 hrs

**Description:**
Builds from transformer architecture through RLHF alignment. An excellent free alternative to the Coursera courses.

[**Watch Video :octicons-arrow-right-24:**](https://www.youtube.com/watch?v=quh7z1q7-uc){ .md-button .md-button--primary }

#### Udemy: Data Science — Transformers for NLP { #udemy-transformers-nlp }

!!! info inline end "Quick Stats"
    - **Platform:** Udemy
    - **Cost:** ~$10–15 on sale
    - **Duration:** ~12.5 hrs

**Instructor:** Lazy Programmer

**Description:**
Implements transformers from scratch in both PyTorch and TensorFlow. Covers both practical usage and deep theory.

[**Visit Course :octicons-arrow-right-24:**](https://www.udemy.com/course/data-science-transformers-nlp/){ .md-button .md-button--primary }

---

## Phase 5: Agentic AI — agents, tool use, and multi-agent systems (Weeks 22–30)

Agentic AI is the **fastest-moving frontier in AI development**. This phase covers four key agentic design patterns (Reflection, Tool Use, Planning, Multi-Agent), three major frameworks (LangGraph, CrewAI, AutoGen), and the emerging protocols (MCP, A2A) that are becoming industry standards.

### 1. Agentic AI (by Andrew Ng) { #agentic-ai-ng }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free to audit
    - **Duration:** 3–10 hrs

**Instructor:** Andrew Ng

**Description:**
**Start here before any framework-specific course.** Andrew Ng teaches all four agentic design patterns — Reflection, Tool Use, Planning, and Multi-Agent — from first principles in raw Python, with no framework hiding the details. You build a complete deep research agent that searches, synthesizes, and reports.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/courses/agentic-ai/){ .md-button .md-button--primary }

### 2. AI Agentic Design Patterns with AutoGen { #autogen-patterns }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Chi Wang & Qingyun Wu

**Description:**
Reinforces the four patterns from a different angle using AutoGen's ConversableAgent. Seeing patterns implemented in multiple ways deepens understanding.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/){ .md-button .md-button--primary }

### 3. Functions, Tools and Agents with LangChain { #langchain-functions-tools }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Harrison Chase

**Description:**
Covers OpenAI function calling, LangChain Expression Language (LCEL), and building conversational agents. This bridges the gap between the LangChain work in Phase 2 and full agentic systems.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/){ .md-button .md-button--primary }

### 4. AI Agents in LangGraph { #langgraph-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1.5 hrs

**Instructors:** Harrison Chase & Rotem Weiss

**Description:**
Builds agents from scratch with Python + LLM, then rebuilds with LangGraph. Covers agentic search, ReAct agents, persistence, streaming, and human-in-the-loop. **LangGraph is the top choice for fine-grained control.**

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/){ .md-button .md-button--primary }

### 5. Long-Term Agentic Memory with LangGraph { #langgraph-long-term-memory }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Harrison Chase

**Description:**
Covers the three memory types (semantic, episodic, procedural) that make agents genuinely useful over time. Builds an email agent with routing, writing, and scheduling tools.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/){ .md-button .md-button--primary }

### 6. LangChain Academy: Introduction to LangGraph { #langchain-academy-langgraph }

!!! info inline end "Quick Stats"
    - **Platform:** LangChain Academy
    - **Cost:** Free
    - **Duration:** Self-paced

**Description:**
The official LangGraph course with progressive modules covering state, nodes, edges, and memory. Work through the notebooks alongside the DeepLearning.ai courses for hands-on practice.

[**Visit Course :octicons-arrow-right-24:**](https://academy.langchain.com/courses/intro-to-langgraph){ .md-button .md-button--primary }

### 7. Multi AI Agent Systems with crewAI { #crewai-systems }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** João Moura (CrewAI founder/CEO)

**Description:**
CrewAI excels at **role-based multi-agent teams**. This course builds 6 business automations: resume tailoring, tech articles, customer support, outreach campaigns, event planning, financial analysis.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/){ .md-button .md-button--primary }

### 8. Practical Multi AI Agents with CrewAI { #crewai-practical-advanced }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** João Moura

**Description:**
The successor course covering production concerns: execution hooks, Flows orchestration, observability, LLM-as-a-Judge evaluation, and deployment.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/){ .md-button .md-button--primary }

### 9. Building Agentic RAG with LlamaIndex { #agentic-rag-llamaindex }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Jerry Liu (LlamaIndex co-founder)

**Description:**
Bridges your RAG knowledge from Phase 3 with agentic patterns. Builds a multi-document research agent with router query engines and tool retrieval.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/){ .md-button .md-button--primary }

### 10. Building AI Browser Agents { #browser-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Description:**
Browser agents represent a practical frontier — AI that can navigate the web. Directly relevant for web developers.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/building-ai-browser-agents/){ .md-button .md-button--primary }

### 11. Agent Memory: Building Memory-Aware Agents { #memory-aware-agents }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructor:** Oracle Partner

**Description:**
Covers **Memory Engineering** — building persistent memory stores, Memory Managers, and semantic tool retrieval that scales without bloating context.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents/){ .md-button .md-button--primary }

### 12. Agent Skills with Anthropic { #anthropic-agent-skills }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Elie Schoppik & Andrew Ng

**Description:**
Covers creating reusable agent skills, composing workflows, and building research agents with the Claude Agent SDK.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/){ .md-button .md-button--primary }

### 13. A2A: The Agent2Agent Protocol { #a2a-protocol }

!!! info inline end "Quick Stats"
    - **Platform:** DeepLearning.ai
    - **Cost:** Free
    - **Duration:** ~1 hr

**Instructors:** Google Cloud & IBM Partners

**Description:**
The **A2A protocol** is becoming the standard for agent-to-agent communication. Builds a healthcare multi-agent system with sequential and hierarchical workflows.

[**Visit Course :octicons-arrow-right-24:**](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/){ .md-button .md-button--primary }

### 14. Udemy: The Complete Agentic AI Engineering Course { #udemy-agentic-ai }

!!! info inline end "Quick Stats"
    - **Platform:** Udemy
    - **Cost:** ~$15 on sale
    - **Duration:** 6-week program

**Instructor:** Ed Donner

**Description:**
Eight real-world projects across all major frameworks. The most comprehensive hands-on agentic AI course available, including a Trading Floor Capstone.

[**Visit Course :octicons-arrow-right-24:**](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/){ .md-button .md-button--primary }

### 15. IBM RAG and Agentic AI Professional Certificate { #ibm-cert-agentic }

!!! info inline end "Quick Stats"
    - **Platform:** Coursera
    - **Cost:** ~$49/month
    - **Duration:** 4–6 months

**Description:**
Covers RAG pipelines, agentic architectures, LangChain/LangGraph, MCP, CrewAI, AG2, and BeeAI. Good for a job-ready credential.

[**Visit Certificate :octicons-arrow-right-24:**](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai){ .md-button .md-button--primary }

### Framework decision guide

When building agents, choosing the right framework matters. Here's the industry consensus as of early 2026:

- **LangGraph** — Best for controllability and stateful workflows. The most production-ready option
- **CrewAI** — Best for role-based multi-agent teams. Easiest to get started with
- **OpenAI Agents SDK** — Best if you're all-in on OpenAI. Released March 2025
- **AutoGen / Microsoft Agent Framework** — Best for Azure/Microsoft environments
- **LlamaIndex** — Best for knowledge-heavy, document-centric agents
- **PydanticAI** — Newest (Dec 2024). Type-safe, MCP-native, built by the Pydantic team

Learn the **patterns** first (Reflection, Tool Use, Planning, Multi-Agent), then pick 1–2 frameworks to go deep on. LangGraph + CrewAI is the most versatile combination.

---

## Phase 6: Capstone projects and portfolio (Weeks 31+)

Everything converges here. These projects demonstrate the full range of skills from Phases 1–5 and give you a portfolio that proves you can build production AI systems.

### Project 1: AI-powered documentation chatbot (RAG + web app)
Build a production RAG application using your Flask/Django skills. Ingest your own documentation (PDFs, Markdown, code), use a vector database (Chroma or Pinecone), implement advanced retrieval with re-ranking, and deploy it as a web application with authentication and rate limiting. **This project alone demonstrates Phases 2 and 3.**

### Project 2: Multi-agent research assistant
Build a CrewAI or LangGraph system with specialized agents: a Researcher (web search), an Analyst (data processing), a Writer (content generation), and a Reviewer (quality control). Add memory persistence and human-in-the-loop approval. Deploy with a web UI. **Demonstrates Phase 5 mastery.**

### Project 3: Fine-tuned domain-specific model
Take an open-source model (Llama or Mistral), fine-tune it with LoRA/QLoRA on domain-specific data, evaluate it against the base model, and serve it through an API. Compare cost/performance against GPT-4. **Demonstrates Phase 4 depth.**

### Project 4: Full-stack AI application with MCP
Build a complete application that uses MCP to connect an LLM to external tools (calendar, email, databases, APIs). Implement the A2A protocol for agent-to-agent communication. Add evaluation pipelines. This is your capstone — **it demonstrates everything**.

### Portfolio presentation tips

Open-source all projects on GitHub with clear READMEs. Write blog posts explaining your design decisions and trade-offs. Include evaluation metrics, not just demos. Show cost analysis (comparing different models and approaches). Highlight the engineering work — error handling, monitoring, testing — that distinguishes a developer from someone who followed a tutorial.

---

## Additional resources that support the entire journey

### Essential YouTube channels to follow throughout

**Andrej Karpathy** (~1M subscribers) — The gold standard for understanding AI from first principles. Follow his channel for new content beyond Zero to Hero.

**3Blue1Brown** (~6M subscribers) — Visual math explanations. Return to his videos whenever a concept feels abstract.

**Yannic Kilcher** (~300K subscribers) — AI research paper breakdowns. Start watching in Phase 4 to stay current with new developments.

**Two Minute Papers** (~1.5M subscribers) — Quick updates on cutting-edge AI research. Good for staying informed without time investment.

### Free platforms for ongoing learning

**Hugging Face Learn** (huggingface.co/learn) — Free courses on LLMs, AI agents (with smolagents, LangGraph, LlamaIndex), and MCP. Community-driven with leaderboards.

**LangChain Academy** (academy.langchain.com) — Free notebooks for LangGraph and ambient agents. The official learning platform.

**CrewAI Learn** (learn.crewai.com) — Free official platform with **100,000+ certified developers**. Covers multi-agent systems through production deployment.

**Microsoft "AI Agents for Beginners"** — Free 10-lesson course on Microsoft Learn covering agent fundamentals.

**Anthropic Courses** (anthropic.skilljar.com) — Free MCP course covering tools, resources, prompts, and building servers/clients.

### Reference books (for when you want to go deeper)

"**Build a Large Language Model (From Scratch)**" by Sebastian Raschka — The hands-on companion to Karpathy's videos. Builds an LLM step by step.

"**AI Engineering**" by Chip Huyen — Covers real-world engineering, MLOps, and inference optimization. The practical production guide.

"**The LLM Engineering Handbook**" by Paul Iusztin & Maxime Labonne — Covers RAG, evals, LangChain, and fine-tuning from an engineering perspective.

### Key roadmaps to bookmark

**roadmap.sh/ai-engineer** — Interactive visual roadmap maintained by one of GitHub's most-starred projects. Continuously updated.

**DataUnboxed AI Engineering Roadmap** — Emphasizes that AI engineering focuses on building with existing LLMs, not training from scratch. Highlights **evals** as a core competence that most courses underemphasize.

---

## Summary: the complete plan at a glance

| Phase | Focus | Duration | Free courses | Paid options | Key outcome |
|-------|-------|----------|-------------|-------------|-------------|
| 1 | Prompt Engineering | Weeks 1–3 | 4 DeepLearning.ai + 3Blue1Brown + Karpathy Deep Dive | — | Systematic prompting + LLM mental model |
| 2 | LLM APIs & AI Apps | Weeks 4–7 | 5 DeepLearning.ai + HuggingFace | Ed Donner Udemy (~$12) | Build LLM-powered web applications |
| 3 | RAG & Vector DBs | Weeks 8–13 | 7 DeepLearning.ai + Coursera audit | Eden Marco Udemy (~$12) | Production RAG systems |
| 4 | LLM Internals | Weeks 14–21 | Karpathy (14.5h) + 7 DeepLearning.ai | Lazy Programmer Udemy (~$12) | Understand transformers and fine-tuning |
| 5 | Agentic AI | Weeks 22–30 | Andrew Ng Agentic AI + 11 DeepLearning.ai + LangChain Academy + CrewAI Learn | Ed Donner Agentic (~$15) | Multi-agent systems in production |
| 6 | Portfolio Projects | Weeks 31+ | — | — | 4 portfolio-ready applications |

**Totals: 37+ free courses and resources, ~$0–50 in optional paid courses, 6+ months to mastery.**

The free path alone includes **30+ DeepLearning.ai short courses**, Andrew Ng's full Agentic AI course, Karpathy's 14.5-hour Zero to Hero series plus his 3.5-hour Deep Dive, 3Blue1Brown's visual explanations, the Coursera *Generative AI with LLMs* course (audited free), HuggingFace courses, LangChain Academy, and CrewAI Learn. The optional Udemy courses add ~**$50 total** during sales for the most comprehensive hands-on projects available. This is arguably the most cost-effective AI education path possible in 2026 — leveraging resources that rival or exceed what any bootcamp or degree program offers.
