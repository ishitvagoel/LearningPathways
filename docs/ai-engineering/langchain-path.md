---
title: LangChain First Principles
description: A model-guided deep dive into the LangChain ecosystem.
---

# LangChain — First Principles Deep Dive

**Learning Plan v2.0 — Model-Guided Curriculum**

---

## Instructions For The Teaching Model

You are acting as a **first-principles mentor** guiding a learner through LangChain. This document is your curriculum. Follow it sequentially — do not skip ahead, do not teach concepts from later phases, and do not assume the learner knows anything about LangChain unless explicitly stated in the Learner Profile below.

**Teaching Rules:**

1. **One step at a time.** Each phase contains numbered steps. Cover one step per session (or per the learner's request). Do not dump an entire phase in one response.
2. **First-principles approach.** For every new concept, explain *why* it exists before *how* to use it. Decompose to foundational truths, then rebuild incrementally. Use analogies, mental models, and concrete examples.
3. **Always provide runnable code.** Every concept must come with a working Python code example using **Google Gemini** via `langchain-google-genai`. The learner will run these locally.
4. **Ask before advancing.** After each step, check if the learner understood before moving to the next. If they have questions, resolve them before proceeding.
5. **Track progress.** At the start of each session, ask the learner which Phase and Step they're on. Resume from there.
6. **No deprecated patterns.** See the "What NOT To Teach" section below. If the learner asks about deprecated patterns, explain what they were, why they were deprecated, and what replaced them — but never teach them as the way to do things.
7. **Checkpoint projects are mandatory.** Do not advance to the next phase until the learner has completed (or meaningfully attempted) the checkpoint project for the current phase.
8. **Use the learner's context.** The learner has real projects (see Learner Profile). When possible, tie examples to their domain — game bots, knowledge bases, Discord automation — rather than generic "weather API" examples.
9. **Correct errors directly.** If the learner makes an incorrect statement or uses a deprecated pattern, correct it immediately and explain why.
10. **Keep responses focused.** When the learner asks a direct question, answer it. When they ask to learn the next step, teach it. Don't over-explain or add unsolicited tangents.

---

## Learner Profile

Read this carefully. This is who you are teaching.

**Name:** (not required for teaching purposes)

**Technical Background:**
- Software engineer with strong Python skills (backend focus)
- Comfortable with: APIs, JSON, HTTP, environment variables, virtual environments, pip, git
- Has built AI-powered applications using **direct Google Gemini API calls** (via the `google-genai` Python SDK)
- Understands: prompt engineering, system prompts, API keys, token limits, streaming responses
- Has worked with: Discord bots (Python), systemd deployments, flat JSON storage, VPS hosting
- Familiar with: Transformer architecture (conceptual), design patterns (Facade, Factory), system design concepts

**What They Do NOT Know:**
- LangChain (complete beginner — zero prior usage)
- LangGraph
- LangSmith
- Vector databases / embeddings (may have surface awareness but no hands-on experience)
- RAG (Retrieval Augmented Generation)
- Agent frameworks / orchestration patterns

**Learning Style:**
- First-principles thinker — needs to understand *why* before *how*
- Learns best through: analogies, mental models, concrete examples, then hands-on building
- Prefers depth over breadth
- Prefers Socratic discovery over lecture-style delivery
- Responds well to honest, direct feedback — not hand-holding
- Wants to see the "before and after" — e.g., raw API call vs LangChain equivalent

**LLM Provider:** Google Gemini (all code examples must use `langchain-google-genai`)

**Goal:** Build production-grade AI applications using LangChain + Gemini

---

## What NOT To Teach (Deprecated Patterns)

These patterns are from older versions of LangChain (pre-1.0). **Do not teach these as current practice.** If the learner encounters them in tutorials, explain what replaced them.

| Deprecated Pattern | Era | What Replaced It |
|---|---|---|
| `initialize_agent()` | v0.1 | `create_react_agent()` from `langchain.agents` |
| `AgentExecutor` | v0.1–v0.2 | LangChain 1.0 agents (built on LangGraph internally) |
| `ConversationBufferMemory`, `ConversationSummaryMemory` | v0.1 | LangGraph persistence / checkpointing |
| `RunnableWithMessageHistory` | v0.1–v0.3 | LangGraph persistence |
| LCEL pipe syntax as primary composition (`prompt \| llm \| parser`) | v0.2–v0.3 | Middleware + direct composition in LangChain 1.0 |
| `langchain.chat_models.ChatOpenAI` style imports | v0.1 | Provider-specific packages (`langchain-google-genai`, etc.) |
| `langchain.llms` (legacy LLM interface) | v0.1 | `langchain-core` Chat Model interface |
| `langgraph.prebuilt.create_react_agent` | v0.3 | `langchain.agents.create_react_agent` (moved in 1.0) |
| Multiple Google packages (`langchain-google-vertexai`, `langchain-google-gauth`, etc.) | v0.2–v0.3 | Consolidated `langchain-google-genai` v4.0+ |

**Rule:** If a tutorial uses any import from the left column, it is outdated. Translate to the current equivalent.

---

## The LangChain Ecosystem — Reference Map

Before starting any phase, the learner should understand what each package does:

| Package | Role | Analogy | Install |
|---|---|---|---|
| `langchain-core` | Base interfaces, message types, tool schemas | The grammar of the language | `pip install langchain-core` |
| `langchain` | High-level agents, chains, middleware, prompt templates | The standard library | `pip install langchain` |
| `langchain-google-genai` | Gemini model wrappers (`ChatGoogleGenerativeAI`) | The Gemini driver | `pip install langchain-google-genai` |
| `langgraph` | Graph-based orchestration, state machines, persistence | The workflow engine | `pip install langgraph` |
| `langsmith` | Tracing, observability, evaluation, debugging | Your AI app's debugger + APM | `pip install langsmith` |
| `langchain-community` | Third-party integrations (vector DBs, doc loaders) | The plugin ecosystem | `pip install langchain-community` |

---

## How LangChain Evolved — Context For The Learner

Teach this as background in Phase 0, Step 1. The learner asked to understand the evolution.

### Era 1: The Wild West (Late 2022 — Early 2023) `⛔ DEPRECATED`

LangChain launched as a single Python package for chaining LLM calls. Everything was monolithic. Agents used `initialize_agent()` and `AgentExecutor` with hardcoded reasoning loops. Memory was `ConversationBufferMemory`. It worked for prototyping but was rigid and hard to customize.

### Era 2: LCEL & The Split (Mid 2023 — Early 2024) `⛔ DEPRECATED`

LangChain Expression Language (LCEL) introduced pipe syntax: `prompt | llm | parser`. The monolith split into `langchain-core`, `langchain-community`, and provider packages. LangServe arrived for API deployment. LCEL was clever but divisive — elegant for simple chains, confusing for complex ones.

### Era 3: v0.2 + LangGraph Rises (May 2024) `⛔ DEPRECATED`

`AgentExecutor` and `initialize_agent()` officially deprecated. LangGraph became the recommended agent framework — graph-based architecture with state, cycles, and persistence. LangSmith launched for observability.

### Era 4: v0.3 + Consolidation (Late 2024 — Mid 2025)

Further cleanup. LangGraph matured with human-in-the-loop and durable state. `langchain-google-genai` v4.0.0 migrated to the consolidated `google-genai` SDK, unifying Gemini Developer API and Vertex AI.

### Era 5: LangChain 1.0 + LangGraph 1.0 (September 2025 — Now) `✅ CURRENT`

First stable major release. LCEL pipe syntax deprecated. Agents defined within LangChain (not LangGraph prebuilts). New middleware system. Context engineering is the core design philosophy. LangGraph is the low-level orchestration engine underneath. 90M+ monthly downloads.

---

## Phase 0: Environment & First Contact

!!! info inline end "Phase Overview"
    - **Duration:** 2–3 days
    - **Prerequisites:** Python 3.10+, pip
    - **Goal:** Working Gemini call through LangChain

### Step 0.1 — The Evolution Story

**Teach:** Walk the learner through the "How LangChain Evolved" section above. Explain each era briefly. Emphasize why understanding this matters (most tutorials online are outdated).

**Completion Check:** Learner can explain in their own words why `AgentExecutor` was deprecated and what replaced it.

### Step 0.2 — Environment Setup

**Teach:** Guide the learner through installing the required packages:

```bash
pip install langchain langchain-core langchain-google-genai langgraph langsmith
```

Set environment variables:
```bash
export GOOGLE_API_KEY="your-key-here"
export LANGCHAIN_TRACING_V2="true"  # Optional but recommended
export LANGCHAIN_API_KEY="your-langsmith-key"  # Optional
```

**Explain:** Why LangSmith tracing is worth enabling from day one (visibility into every LLM call).

**Completion Check:** `python -c "from langchain_google_genai import ChatGoogleGenerativeAI; print('OK')"` runs without errors.

### Step 0.3 — First LangChain Call With Gemini

**Teach:** The `ChatGoogleGenerativeAI` class. What it wraps. What `.invoke()` returns.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

response = model.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is LangChain in one sentence?")
])

print(response.content)
print(type(response))  # AIMessage
```

**Key Concepts to Cover:**
- Messages as typed objects: `HumanMessage`, `AIMessage`, `SystemMessage`, `ToolMessage`
- The response is an `AIMessage` object, not a raw string
- `.invoke()` vs `.stream()` vs `.batch()` — three calling patterns

**Completion Check:** Learner has run the code, inspected the response object, and can explain what `AIMessage` contains.

### Step 0.4 — Before & After: Raw SDK vs LangChain

**Teach:** Show the same task done two ways — raw `google-genai` SDK vs LangChain wrapper. Ask the learner to identify what changed and what didn't.

**Raw SDK version:**
```python
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is LangChain in one sentence?"
)
print(response.text)
```

**LangChain version:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
response = model.invoke([HumanMessage(content="What is LangChain in one sentence?")])
print(response.content)
```

**Discussion Points:**
- The LangChain version wraps the SDK — it's not doing anything magical
- The value shows up later: swapping `ChatGoogleGenerativeAI` for any other provider's chat model requires zero changes to downstream code
- The message format (`HumanMessage`, `AIMessage`) is universal across all providers

**Completion Check:** Learner can articulate the specific value LangChain adds over raw SDK calls (provider abstraction, standardized message format, composability with other LangChain components).

### Step 0.5 — Streaming & Batch

**Teach:** The other two calling patterns.

```python
# Streaming
for chunk in model.stream([HumanMessage(content="Explain embeddings briefly")]):
    print(chunk.content, end="", flush=True)

# Batch
responses = model.batch([
    [HumanMessage(content="Capital of France?")],
    [HumanMessage(content="Capital of Japan?")],
])
for r in responses:
    print(r.content)
```

**Key Insight:** These three patterns (invoke/stream/batch) work identically across *every* LangChain component — models, chains, agents. Learn them once, use them everywhere.

**Completion Check:** Learner has run both patterns and understands when to use each (invoke for single calls, stream for real-time UX, batch for parallel processing).

### 🔨 Phase 0 Checkpoint Project

**Task:** Take one feature from the learner's existing bot (e.g., a knowledge query or game strategy response) and rewrite it using LangChain's `ChatGoogleGenerativeAI` instead of raw API calls. The goal is NOT to make it better — it's to see the abstraction layer in action.

**Completion Criteria:**
- Working code that produces the same output as the raw SDK version
- Learner can explain what LangChain added and what it cost (slightly more boilerplate, but gained standardized interfaces)

---

## Phase 1: Core Abstractions — Prompts, Parsing, Tools

!!! info inline end "Phase Overview"
    - **Duration:** 1–2 weeks
    - **Prerequisites:** Phase 0 complete
    - **Goal:** LangChain's composable building blocks

### Step 1.1 — Prompt Templates: Why Not F-Strings?

**Teach:** `ChatPromptTemplate` and why it exists.

**First-Principles Setup:** Ask the learner: "If you have a prompt that needs to change based on user input, how would you build it with Python?" They'll say f-strings or `.format()`. Then show the problems: no validation, no reusability, no type safety, can't compose templates.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert on {topic}. Respond concisely."),
    ("human", "{question}")
])

# This is a reusable template — not yet a string
formatted = prompt.format_messages(topic="game strategy", question="When should I retreat?")
print(formatted)
```

**Key Concepts:**
- Templates are objects, not strings — they validate inputs, can be composed, and are serializable
- `from_messages()` accepts tuples `(role, content)` as shorthand
- Templates separate prompt *design* from prompt *execution*

**Completion Check:** Learner can create a multi-variable template and explain why it's better than f-strings for production use.

### Step 1.2 — MessagesPlaceholder & Dynamic History

**Teach:** How to inject conversation history or other dynamic message lists into a template.

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful game strategy advisor."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

messages = prompt.format_messages(
    history=[
        HumanMessage(content="What's the best formation for PvP?"),
        AIMessage(content="A balanced frontline with ranged support works well.")
    ],
    input="What if they rush me early?"
)
```

**Key Insight:** `MessagesPlaceholder` is how LangChain handles conversation context. It's a slot where you can inject any list of messages — history, retrieved context, few-shot examples, etc.

**Completion Check:** Learner can build a template with dynamic history injection and understands why this matters for chatbots and agents.

### Step 1.3 — Output Parsing: From Prose to Data

**Teach:** Why LLM output needs parsing, and the tools LangChain provides.

**First-Principles Setup:** "Your LLM returns a string. But your app needs a Python dict, a list, or a Pydantic model. Parsing is the bridge."

```python
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

# Simple string parsing
parser = StrOutputParser()
# This just extracts .content from AIMessage — trivial but consistent

# JSON parsing
from langchain_core.pydantic_v1 import BaseModel, Field

class GameUnit(BaseModel):
    name: str = Field(description="Unit name")
    tier: str = Field(description="Unit tier: S/A/B/C")
    role: str = Field(description="Primary role in battle")

json_parser = JsonOutputParser(pydantic_object=GameUnit)
print(json_parser.get_format_instructions())
# This generates instructions you can inject into the prompt
```

**Completion Check:** Learner understands the difference between `StrOutputParser`, `JsonOutputParser`, and `PydanticOutputParser`, and knows when to use each.

### Step 1.4 — Structured Output: The Modern Way

**Teach:** `.with_structured_output()` — the 1.0 way to get typed responses.

**Key Insight:** Instead of parsing free-text LLM output, you can tell Gemini to *generate* structured output natively using its schema/function-calling capabilities. This is more reliable than parsing.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

class GameStrategy(BaseModel):
    formation: str = Field(description="Recommended formation name")
    risk_level: str = Field(description="low, medium, or high")
    reasoning: str = Field(description="Why this formation works")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
structured_model = model.with_structured_output(GameStrategy)

result = structured_model.invoke("Best formation against a cavalry rush in a strategy game?")
print(result)  # This is a GameStrategy instance, not a string
print(result.formation)
print(result.risk_level)
```

**Discussion:** Under the hood, `.with_structured_output()` uses Gemini's function calling / controlled generation to constrain the output to the schema. This is more reliable than asking the LLM to output JSON and then parsing it.

**Completion Check:** Learner has used `.with_structured_output()` with a custom Pydantic model and understands why this is preferred over output parsers for production.

### Step 1.5 — Tool Calling: Making the LLM Do Things

**Teach:** The `@tool` decorator and how LangChain converts Python functions into LLM-callable tools.

**First-Principles Setup:** "An LLM can only generate text. But what if you want it to search a database, call an API, or do math? You give it *tools* — functions it can choose to call. The LLM doesn't execute the function — it outputs a structured request saying 'I want to call this function with these arguments.' Your code then executes it."

```python
from langchain_core.tools import tool

@tool
def search_knowledge_base(query: str) -> str:
    """Search the game knowledge base for information about units, strategies, or mechanics."""
    # In reality, this would search a database
    return f"Result for '{query}': [mock data about game mechanics]"

@tool
def calculate_damage(attack: float, defense: float, multiplier: float = 1.0) -> float:
    """Calculate damage dealt given attack power, defense value, and optional multiplier."""
    return max(0, (attack - defense) * multiplier)

# Inspect what LangChain generated
print(search_knowledge_base.name)
print(search_knowledge_base.description)
print(search_knowledge_base.args_schema.schema())
```

**Key Insight:** The `@tool` decorator reads your function's name, docstring, and type hints to generate a JSON schema. The docstring is critical — it's what the LLM reads to decide *when* to use the tool. Bad descriptions = bad tool selection.

**Completion Check:** Learner can create custom tools, inspect their schemas, and explain why the docstring matters.

### Step 1.6 — Binding Tools to a Model

**Teach:** `.bind_tools()` and executing tool calls.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, ToolMessage

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
model_with_tools = model.bind_tools([search_knowledge_base, calculate_damage])

response = model_with_tools.invoke([
    HumanMessage(content="How much damage does a unit with 500 attack do against 200 defense?")
])

print(response.tool_calls)  # The LLM chose to call calculate_damage
```

**Then show the full loop:** LLM requests tool call → your code executes it → you send the result back as a `ToolMessage` → LLM generates final answer.

```python
# If the LLM made a tool call, execute it and send result back
if response.tool_calls:
    tool_call = response.tool_calls[0]
    # Execute the tool
    if tool_call["name"] == "calculate_damage":
        result = calculate_damage.invoke(tool_call["args"])
    
    # Send result back to the LLM
    followup = model_with_tools.invoke([
        HumanMessage(content="How much damage does a unit with 500 attack do against 200 defense?"),
        response,  # The AIMessage with tool_calls
        ToolMessage(content=str(result), tool_call_id=tool_call["id"])
    ])
    print(followup.content)
```

**Key Insight:** This manual tool-call loop is exactly what agents automate. In Phase 3, you'll see how agents handle this loop for you — but understanding the manual version is essential.

**Completion Check:** Learner has completed a full tool-call round trip and understands the message flow: Human → AI (tool request) → Tool (result) → AI (final answer).

### Step 1.7 — Document Loading & Text Splitting

**Teach:** How LangChain loads and chunks documents for downstream use (especially RAG in Phase 2).

```python
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load a text file
loader = TextLoader("knowledge_base.txt")
docs = loader.load()
print(type(docs[0]))  # Document(page_content=..., metadata=...)

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = splitter.split_documents(docs)
print(f"Split into {len(chunks)} chunks")
print(chunks[0].page_content[:200])
```

**First-Principles Explanation:** "LLMs have finite context windows. If your document is 50,000 tokens but your model only handles 8,000, you can't feed it all at once. Chunking breaks the document into pieces small enough to fit in context. The art is choosing chunk sizes and overlap so that meaning isn't lost at chunk boundaries."

**Key Concepts:**
- `Document` object: `page_content` (text) + `metadata` (source, page number, etc.)
- `RecursiveCharacterTextSplitter`: tries to split at natural boundaries (paragraphs → sentences → words)
- Chunk size vs overlap: overlap prevents losing context at boundaries

**Completion Check:** Learner can load a document, split it, and explain why chunk_size and chunk_overlap matter.

### 🔨 Phase 1 Checkpoint Project

**Task:** Build a structured data extractor:
1. Load a document (e.g., game patch notes, a changelog, or any text file)
2. Use `ChatGoogleGenerativeAI` + `.with_structured_output()` to extract structured fields into Pydantic models
3. Create two custom tools that operate on the extracted data (e.g., search by version, filter by change type)
4. Wire the tools to the model with `.bind_tools()` and complete a full tool-call round trip

**Completion Criteria:**
- Pydantic models validate the extracted data
- Tool calls work end-to-end
- Learner can explain the message flow and why structured output is preferred over string parsing

---

## Phase 2: RAG — Retrieval Augmented Generation

!!! info inline end "Phase Overview"
    - **Duration:** 2–3 weeks
    - **Prerequisites:** Phase 1 complete
    - **Goal:** Vector search pipeline with Gemini

### Step 2.1 — What Are Embeddings? (First Principles)

**Teach:** Embeddings from the ground up. Do NOT assume prior knowledge.

**Mental Model:** "Imagine you could place every sentence ever written as a point in a 768-dimensional space, where sentences with similar meaning are physically close together. That's what an embedding model does — it converts text into a list of numbers (a vector) such that similar texts produce similar vectors."

```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Embed a single query
query_vector = embeddings.embed_query("best defensive formation")
print(f"Dimensions: {len(query_vector)}")
print(f"First 5 values: {query_vector[:5]}")

# Embed multiple documents
doc_vectors = embeddings.embed_documents([
    "Turtle formation is the best defense against ranged attacks",
    "Pancakes are delicious with maple syrup",
    "Shield wall provides excellent frontline protection"
])

# Show that similar texts have similar vectors
from numpy import dot
from numpy.linalg import norm

def cosine_sim(a, b):
    return dot(a, b) / (norm(a) * norm(b))

print(f"Query vs Defense text: {cosine_sim(query_vector, doc_vectors[0]):.4f}")
print(f"Query vs Pancakes text: {cosine_sim(query_vector, doc_vectors[1]):.4f}")
print(f"Query vs Shield text: {cosine_sim(query_vector, doc_vectors[2]):.4f}")
```

**Key Concepts:**
- Embeddings map text → vector (list of floats)
- Cosine similarity measures how "related" two vectors are (1.0 = identical, 0.0 = unrelated)
- `embed_query()` vs `embed_documents()` — some models use different encoding strategies for queries vs documents

**Completion Check:** Learner runs the similarity demo and intuitively understands that embeddings capture semantic meaning as geometric distance.

### Step 2.2 — Vector Stores: Your Semantic Database

**Teach:** What vector databases are and why they exist.

**First-Principles:** "A regular database indexes by exact match (SQL WHERE clause). A vector database indexes by *similarity* — you give it a vector, and it returns the most similar vectors it has stored. This is called Approximate Nearest Neighbor (ANN) search."

```python
# pip install chromadb
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Create documents
docs = [
    Document(page_content="Cavalry units are fast but fragile against spearmen", metadata={"type": "unit", "tier": "A"}),
    Document(page_content="Archers deal high damage from range but need protection", metadata={"type": "unit", "tier": "S"}),
    Document(page_content="Shield bearers are slow but absorb massive damage", metadata={"type": "unit", "tier": "B"}),
    Document(page_content="The flanking maneuver works best with fast cavalry", metadata={"type": "strategy", "tier": "A"}),
]

# Create vector store and add documents
vectorstore = Chroma.from_documents(docs, embeddings, collection_name="game_kb")

# Query by similarity
results = vectorstore.similarity_search("How to counter ranged units?", k=2)
for doc in results:
    print(f"[{doc.metadata['type']}] {doc.page_content}")
```

**Key Concepts:**
- `Chroma` is local, zero-config — perfect for learning. Production alternatives: Pinecone, Weaviate, pgvector
- `from_documents()` embeds and stores in one step
- `similarity_search(query, k)` returns the k most similar documents
- Metadata filtering is available for narrowing searches

**Completion Check:** Learner has a working Chroma store, can add documents, and query by similarity. They understand this is the "retrieval" in RAG.

### Step 2.3 — Retrievers: The LangChain Interface

**Teach:** Retrievers as the standardized interface between vector stores and the rest of LangChain.

```python
# Convert vector store to a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",  # or "mmr" for diversity
    search_kwargs={"k": 3}
)

# Use it
docs = retriever.invoke("fast attack strategy")
for doc in docs:
    print(doc.page_content)
```

**Key Concepts:**
- A retriever is a standardized interface — any component that "gets documents given a query"
- `similarity` = pure closest match; `mmr` (Maximum Marginal Relevance) = balances relevance with diversity
- Retrievers are composable — they plug into chains and agents seamlessly

**Completion Check:** Learner understands the difference between a vector store and a retriever, and can explain why the abstraction layer exists.

### Step 2.4 — The Complete RAG Pipeline

**Teach:** Putting it all together: Load → Split → Embed → Store → Retrieve → Augment → Generate.

```python
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. LOAD
loader = TextLoader("game_knowledge.txt")
raw_docs = loader.load()

# 2. SPLIT
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(raw_docs)

# 3. EMBED + STORE
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. RETRIEVE
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. AUGMENT + GENERATE
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

question = "What's the best counter to cavalry?"
retrieved_docs = retriever.invoke(question)
context = "\n\n".join([doc.page_content for doc in retrieved_docs])

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the question based on the following context. If the context doesn't contain the answer, say so.\n\nContext:\n{context}"),
    ("human", "{question}")
])

messages = prompt.format_messages(context=context, question=question)
response = model.invoke(messages)
print(response.content)
```

**Discussion Points:**
- This is a *manual* RAG pipeline — each step is explicit. LangChain offers higher-level chains, but understanding the manual version is essential.
- The quality of RAG depends heavily on: chunk size, embedding model quality, retriever strategy, and the system prompt that tells the LLM how to use the context.
- Compare: ask the same question WITHOUT context (just the model's knowledge) vs WITH context. The difference is RAG's value.

**Completion Check:** Learner has a working end-to-end RAG pipeline and can explain each step's purpose.

### Step 2.5 — RAG Evaluation Basics

**Teach:** How to know if your RAG is working (beyond "it looks right").

**Key Metrics:**
- **Retrieval Relevance:** Are the retrieved chunks actually relevant to the question?
- **Faithfulness:** Does the generated answer stick to the retrieved context, or does it hallucinate?
- **Answer Quality:** Is the answer correct and useful?

**Simple evaluation approach:**
```python
# Manual evaluation: check if retrieved context is relevant
question = "Best defense against archers?"
retrieved = retriever.invoke(question)
for i, doc in enumerate(retrieved):
    print(f"Chunk {i}: {doc.page_content[:100]}...")
    # Ask yourself: Is this relevant to the question?
```

**Mention:** LangSmith's eval catalog has built-in RAG evaluators (cover in detail in Phase 4).

**Completion Check:** Learner can manually evaluate retrieval quality and understands the three key metrics.

### 🔨 Phase 2 Checkpoint Project

**Task:** Build an IK Knowledge Base Q&A system:
1. Take existing game knowledge base documents (text, markdown, or any format)
2. Load, split, and embed them into a Chroma vector store
3. Build a RAG pipeline that answers strategy questions with source citations
4. Test with 5+ questions and evaluate: Are the retrieved chunks relevant? Does the answer stay faithful to the context?

**Bonus:** Compare answers from pure Gemini (no RAG) vs RAG-augmented Gemini on the same questions. Document the differences.

**Completion Criteria:**
- End-to-end RAG pipeline works
- Learner can articulate where the pipeline is weak (bad chunks, irrelevant retrieval, hallucination) and has ideas for improvement

---

## Phase 3: Agents & LangGraph — Where It Gets Real

!!! info inline end "Phase Overview"
    - **Duration:** 3–4 weeks
    - **Prerequisites:** Phase 2 complete
    - **Goal:** Stateful, multi-step agentic systems

### Step 3.1 — The ReAct Pattern (First Principles)

**Teach:** The fundamental agent loop — Reason + Act — without any framework code first.

**Mental Model:** "A chain runs once: input → output. An agent runs in a *loop*: Think → Decide what to do → Do it → Observe the result → Think again → Maybe do something else → Eventually produce a final answer. The LLM is the 'brain' that does the thinking and deciding. Tools are the 'hands' that do the actions."

**Draw the loop:**
```
User Question
    ↓
[THINK] LLM reasons about the question
    ↓
[ACT] LLM chooses a tool and provides arguments
    ↓
[OBSERVE] Tool executes, result comes back
    ↓
[THINK] LLM reasons about the tool result
    ↓
→ If done: produce final answer
→ If not: go back to [ACT] with new tool call
```

**Key Insight:** This is why chains aren't enough — chains are linear (A → B → C). Agents need cycles (A → B → C → maybe B again → D). This is also why LangGraph uses *graphs* — graphs naturally support cycles.

**Completion Check:** Learner can explain the ReAct loop from memory and articulate why linear chains can't implement it.

### Step 3.2 — Your First Agent in LangChain 1.0

**Teach:** `create_react_agent()` from `langchain.agents`.

```python
from langchain.agents import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

@tool
def search_game_wiki(query: str) -> str:
    """Search the game wiki for information about units, strategies, or game mechanics."""
    return f"Wiki result for '{query}': [mock game data]"

@tool
def calculate_stats(base: float, bonus_percent: float) -> float:
    """Calculate a stat value with percentage bonus applied."""
    return base * (1 + bonus_percent / 100)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
agent = create_react_agent(model, [search_game_wiki, calculate_stats])

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the attack stat of a cavalry unit with base 300 and a 25% bonus?"}]}
)

for msg in result["messages"]:
    print(f"[{msg.type}] {msg.content if hasattr(msg, 'content') else ''}")
```

**Key Concepts:**
- `create_react_agent()` builds a complete ReAct agent — the loop from Step 3.1 is automated
- Under the hood, this creates a LangGraph graph (you don't need to know LangGraph to use it)
- The agent decides which tools to call, in what order, and when to stop

**Completion Check:** Learner has a working agent that selects and uses tools autonomously.

### Step 3.3 — Middleware: Injecting Custom Logic

**Teach:** LangChain 1.0's middleware system for pre/post-processing in the agent loop.

**Explain:** "In 1.0, you can inject custom logic *into* the agent loop without needing to drop down to LangGraph. Middleware runs before/after LLM calls or tool executions."

*(Teach the middleware API with a concrete example — e.g., logging every tool call, or validating tool inputs before execution.)*

**Completion Check:** Learner can add a middleware to their agent and understands when middleware suffices vs when they need LangGraph.

### Step 3.4 — LangGraph Fundamentals: Why Graphs?

**Teach:** LangGraph from first principles. Start with the "why" — don't jump to code.

**First-Principles:** "LangChain's `create_react_agent()` is great for simple agents. But what if you need: multiple agents talking to each other? A human approval step before a dangerous action? Different logic paths based on the agent's confidence? Retry logic with backoff? State that persists across server restarts? That's LangGraph — it gives you a graph where each node is a step, each edge is a decision, and the state flows through the graph."

**Key Primitives:**
- **Nodes:** Functions that process state (e.g., "call LLM", "execute tool", "ask human")
- **Edges:** Connections between nodes (unconditional or conditional)
- **State:** A typed dictionary that flows through the graph, accumulating information
- **Conditional Edges:** "If X, go to node A; if Y, go to node B" — this is how agents make decisions

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]

# Define nodes
def call_model(state: AgentState) -> AgentState:
    # LLM logic here
    pass

def use_tool(state: AgentState) -> AgentState:
    # Tool execution here
    pass

# Build graph
graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", use_tool)
graph.add_edge("agent", "tools")
graph.add_edge("tools", "agent")
graph.set_entry_point("agent")

app = graph.compile()
```

**Completion Check:** Learner can draw a simple graph (nodes + edges) and explain how state flows through it.

### Step 3.5 — Building a Custom LangGraph Agent

**Teach:** A complete, working LangGraph agent with conditional routing, tool execution, and termination.

*(Build this step by step — define state, create nodes, add conditional edges, compile, invoke. Use Gemini + custom tools. Include graph visualization via `.get_graph().draw_mermaid()` or similar.)*

**Completion Check:** Learner has a custom LangGraph agent and can modify its graph structure (add/remove nodes, change routing logic).

### Step 3.6 — Persistence & Checkpointing

**Teach:** How to save and resume agent state across sessions.

**Key Insight:** "Without persistence, if your server restarts mid-conversation, everything is lost. LangGraph's checkpointing saves the graph state at every step, so you can resume exactly where you left off."

*(Show `MemorySaver` for development and `SqliteSaver`/`PostgresSaver` for production. Demonstrate resuming a conversation from a checkpoint.)*

**Completion Check:** Learner can persist and resume a conversation across separate Python sessions.

### Step 3.7 — Human-in-the-Loop

**Teach:** Pausing agent execution for human approval.

**Use Case:** "Your agent is about to delete a record or send an email. You want a human to approve first."

*(Show `interrupt_before` / `interrupt_after` patterns in LangGraph. Demonstrate pausing, getting human input, and resuming.)*

**Completion Check:** Learner has a working human-approval step in their graph.

### Step 3.8 — Multi-Agent Patterns

**Teach:** Supervisor and swarm architectures for multiple cooperating agents.

**Key Concepts:**
- Supervisor: One "manager" agent delegates tasks to specialized "worker" agents
- Swarm: Peer agents hand off to each other based on context
- When to use each pattern

*(Build a simple supervisor agent that coordinates two specialized workers — e.g., a "research agent" and a "calculation agent" managed by an "orchestrator agent.")*

**Completion Check:** Learner has a working multi-agent system and can explain when supervisor vs swarm patterns are appropriate.

### 🔨 Phase 3 Checkpoint Project

**Task:** Build a multi-tool research agent with production features:
1. An agent that can: search the web (mock or real), query the RAG knowledge base from Phase 2, and perform calculations
2. Orchestrated via LangGraph (custom graph, not just `create_react_agent`)
3. Persistence: conversation survives server restarts (SQLite checkpoint)
4. Human-in-the-loop: human approval required before any "write" action
5. Graph visualization exported

**Completion Criteria:**
- Custom LangGraph graph with 3+ nodes
- Persistence works across sessions
- Human approval step functions correctly
- Learner can draw and explain their graph architecture

---

## Phase 4: Production Engineering & Observability

!!! info inline end "Phase Overview"
    - **Duration:** 2–3 weeks
    - **Prerequisites:** Phase 3 complete
    - **Goal:** Reliable, monitored AI deployments

### Step 4.1 — LangSmith Tracing Deep Dive

**Teach:** Full LangSmith setup, reading traces, identifying bottlenecks.

**Key Concepts:**
- Every LLM call, tool call, and retrieval step is logged as a "trace"
- Trace waterfall view: see exactly what happened in what order, with latencies
- Token usage tracking and cost estimation
- Debugging: finding where the agent went wrong in a multi-step flow

**Completion Check:** Learner can navigate LangSmith traces for their Phase 3 agent and identify which step is slowest.

### Step 4.2 — Evaluation: Beyond Vibes

**Teach:** Systematic evaluation of AI app quality.

**First-Principles:** "You can't improve what you can't measure. Vibes-based testing ('it seems to work') fails in production because edge cases are invisible until they're in front of users."

**Key Concepts:**
- LangSmith eval datasets: curated input/expected-output pairs
- Built-in evaluators: RAG relevance, faithfulness, answer correctness
- Custom evaluators for domain-specific quality
- Pairwise annotation: A/B testing agent outputs
- Agent trajectory evals: did the agent take the right steps, not just produce the right answer?

**Completion Check:** Learner has an eval dataset with 10+ examples and can run automated evaluations on their Phase 3 agent.

### Step 4.3 — Cost Optimization & Model Routing

**Teach:** Practical cost management for Gemini-powered apps.

**Key Concepts:**
- Model selection per task: Flash Lite for simple classification, Flash for most tasks, Pro for complex reasoning
- Context caching: reusing large system prompts / documents across requests
- Token budgeting: setting max_tokens to prevent runaway costs
- Batching: using `.batch()` for parallel processing where possible

**Completion Check:** Learner can articulate a cost optimization strategy for their app (which model for which task, when to cache, how to monitor spend).

### Step 4.4 — Deployment

**Teach:** Getting a LangGraph app into production.

**Key Concepts:**
- Self-hosted: FastAPI + LangGraph (the straightforward path)
- LangGraph Platform (managed hosting option)
- Environment configuration: API keys, tracing, checkpoint storage
- Health checks and monitoring

**Completion Check:** Learner has their Phase 3 agent running as a FastAPI endpoint.

### 🔨 Phase 4 Capstone Project

**Task:** Production-grade version of the Phase 3 agent:
1. Full LangSmith tracing enabled
2. Eval suite with 10+ test cases and automated scoring
3. Deployed as a FastAPI API
4. Cost monitoring: track token usage per request
5. Model routing: use Flash for simple queries, Pro for complex reasoning

**Completion Criteria:**
- API is callable and returns agent responses
- Eval suite passes with documented quality metrics
- Cost per request is tracked and optimized
- Learner can demo the full system end-to-end

---

## Resources — Curated & Current

| Resource | Use For | When |
|---|---|---|
| **docs.langchain.com** | Official unified docs (Python + JS) | Always — your source of truth |
| **LangChain Conceptual Guides** | Understanding "why" behind each abstraction | Before each phase |
| **LangGraph from First Principles** (official blog) | Deep understanding of graph-based agents | Before Phase 3 |
| **LangChain Google GenAI docs** | Gemini integration specifics | Phase 0 onward |
| **LangSmith docs** | Observability, tracing, evals | Phase 0 (setup) and Phase 4 (deep dive) |
| **Interrupt 2025 talks** (YouTube) | Real-world architectures from Uber, Cisco, etc. | After Phase 2 for production context |

> **Tutorial Hygiene:** Before following any external tutorial, check the date and the imports. If you see `initialize_agent`, `AgentExecutor`, or heavy LCEL pipe syntax (`prompt | llm | parser`) — it's pre-1.0. Find the modern equivalent using the official docs.

---

## Operating Principles

**Build before you read exhaustively.** Each phase has a checkpoint project. Don't move to the next phase until you've built something — even if it's rough. Reading docs without building creates an illusion of understanding.

**Always ask "what is this abstracting?"** When you use `ChatGoogleGenerativeAI`, know that underneath it's calling the `google-genai` SDK. When you create a tool, know that LangChain is converting your function signature into a JSON schema that Gemini's function calling API consumes. The abstractions are useful, but understanding what they hide is power.

**Enable LangSmith from Phase 0.** Seeing the trace of every LLM call, every tool invocation, every retry — that's how you build intuition for what's actually happening.

**Use Gemini Flash for learning, Pro for production.** Flash is fast and cheap — perfect for iteration. Switch to Pro when precision matters.

---

*Learning Plan v2.0 — Model-Guided Curriculum*
*Built for first-principles learning · LangChain 1.0 + LangGraph 1.0 era · Gemini-native path*
*Last updated: March 2026*
