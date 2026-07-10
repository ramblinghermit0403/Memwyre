# Memwyre

### Persistent Shared Memory for Every AI.

<p align="center">
  <img src="assets/cover.png" alt="Memwyre Cover Image" width="100%">
</p>

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-blue.svg?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Vue 3](https://img.shields.io/badge/Frontend-Vue%203-green.svg?style=flat-square&logo=vue.js)](https://vuejs.org/)
[![Chrome Extension](https://img.shields.io/badge/Extension-Manifest%20V3-orange.svg?style=flat-square&logo=google-chrome)](https://developer.chrome.com/docs/extensions/mv3/intro/)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-lightgrey.svg?style=flat-square)](https://modelcontextprotocol.io/)
[![LoCoMo Accuracy](https://img.shields.io/badge/LoCoMo%20Accuracy-73.5%25-brightgreen.svg?style=flat-square)](https://github.com/ramblinghermit0403/Memwyre#-the-locomo-benchmark-evaluation)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)

Memwyre is the open-source AI Memory Platform that gives every AI tool, agent, and conversation a persistent, shared memory. 

Rather than treating AI as stateless and losing context every time you switch between ChatGPT, Claude, Cursor, VS Code, or different agent environments, Memwyre sits externally as a unified personal brain. It securely ingests, chunks, and structures your documents, web pages, conversations, and workflows—making them instantly retrievable across your entire AI toolchain (connecting directly to Cursor, VS Code, ChatGPT, Claude, and more).

---

## Table of Contents
1. [Core Features](#core-features)
2. [Ecosystem Tiers](#ecosystem-tiers)
3. [System Architecture & Core Workflows](#system-architecture--core-workflows)
4. [The LoCoMo Benchmark Evaluation](#the-locomo-benchmark-evaluation)
5. [Database Schema & Multi-Tenancy](#database-schema--multi-tenancy)
6. [Installation & Setup](#installation--setup)
7. [Environment Configuration](#environment-configuration)
8. [License](#license)

---

## Core Features

- **Decoupled Persistent Memory**: Acts as an external, LLM-agnostic memory layer. Your knowledge base follows you whether you are using OpenAI, Google Gemini, Anthropic Claude, or local model configurations.
- **Asynchronous Enrichment**: Automatically refines memories, stripping filler text, generating summaries, extracting key entities, and producing atomic factual associations.
- **Dynamic Context Pruning & Recency Decay**: Utilizes an Ebbinghaus-inspired logarithmic decay to deprecate outdated or contradictory user preferences chronologically, keeping context sizes optimized.
- **Approval-Based Inbox Flow**: Introduces a memory dashboard inbox, allowing you to review, edit, approve, or reject auto-captured memories before committing them to long-term vector indexes.
- **Project-Scoped Containerization**: Restricts vector searches and factual associations to specific workspaces or project scopes, providing robust multi-tenant containerization.

---

## Ecosystem Tiers

Memwyre provides multiple ways to ingest and retrieve information:

*   **1. Web Application & Dashboard**: Written in Vue 3 (Vite + Tailwind CSS), incorporating an onboarding tour, Monaco Editor for document management, billing integration, and a visual retrieval simulator to debug and verify vector rankings.
*   **2. Chrome Extension (Manifest V3)**: Auto-injects context into web chat clients, maps authentication tokens, and allows users to save articles, code snippets, or conversational logs directly to their vault with a single click.
*   **3. Model Context Protocol (MCP) Server**: A Python server mapping memory tools (`search_memory`, `save_memory`, `get_document`) directly into IDEs like Cursor and VS Code, or desktop assistants like Claude Desktop.
*   **4. CLI Tool**: A Node-based Command Line Interface (`cli/`) providing terminal-level interaction, query testing, and batch document uploads.
*   **5. OpenClaw Plugin**: A dedicated integration module (`openclaw-plugin/`) allowing multi-agent platforms to interface directly with the Memwyre memory vault.

---

## System Architecture & Core Workflows

### High-Level Components
Memwyre connects user clients to local or cloud vector search services and AI providers:

```mermaid
flowchart TB
    subgraph Client_Side [Client Side]
        Browser["WebApp (Vue 3 / Vite)"]
        Extension["Chrome Extension (MV3)"]
        CLI["CLI Client (Node.js)"]
    end

    subgraph Load_Balancer [Ingress]
        Nginx["Nginx Reverse Proxy"]
    end

    subgraph Backend_Core [Backend API (FastAPI)]
        Auth_Mod["Auth & Users Module"]
        Mem_Mod["Memory Management"]
        Ret_Mod["Retrieval Engine"]
        LLM_Mod["LLM Service (V1/V2)"]
    end

    subgraph Background_Workers [Celery Workers]
        Ingest_Worker["Ingestion & Chunking Worker"]
        Dedupe_Worker["Deduplication Worker"]
    end

    subgraph Data_Persistence [Data Layer]
        Postgres[("PostgreSQL / SQLite")]
        Pinecone[("Pinecone / ChromaDB")]
        Redis[("Redis Message Broker")]
    end
    
    subgraph External_Services [AI Inference]
        NVIDIA["NVIDIA NIM (Kimi K2.6)"]
        Azure["Azure OpenAI (GPT-4o-mini)"]
        Gemini["Google Gemini API"]
    end

    Browser -->|HTTPS| Nginx
    Extension -->|HTTPS| Nginx
    CLI -->|HTTPS| Nginx
    Nginx --> Backend_Core
    
    Auth_Mod --> Postgres
    Mem_Mod --> Postgres
    Mem_Mod --> Ingest_Worker
    
    Ret_Mod --> Pinecone
    Ret_Mod --> Postgres
    Ret_Mod --> External_Services
    
    Ingest_Worker --> External_Services
    Ingest_Worker --> Pinecone
    Ingest_Worker --> Postgres
```

### Ingestion Pipeline
Ingesting a memory triggers background worker tasks to process, embed, and structure raw data asynchronously:

```mermaid
sequenceDiagram
    participant User
    participant API as FastAPI API
    participant Worker as Celery Worker
    participant LLM as LLM/Embedding Provider
    participant Vector as Pinecone/ChromaDB
    participant DB as PostgreSQL/SQLite

    User->>API: POST /memory (Raw Text Content)
    API->>DB: Save Memory (Status: Pending)
    API->>Worker: Dispatch Ingest Task
    API-->>User: 202 Accepted (In progress)
    
    Note over Worker: Asynchronous Processing
    Worker->>LLM: Metadata Extraction (Titles, Tags)
    Worker->>Worker: Semantic Chunking (Overlapping Splits)
    
    loop Parallel Enrichment
        Worker->>LLM: Enrich Chunk (Q&A Pairs, Summaries)
        Worker->>LLM: Extract SPO Facts (Subject-Predicate-Object)
    end
    
    Worker->>Vector: Batch Upsert Embeddings (Chunks + Facts)
    Worker->>DB: Write Chunks & Facts (Linked to Memory)
    Worker->>DB: Update Memory Status (Approved/Active)
```

### Parallelized Retrieval (RAG)
Retrieval queries run exact relational Fact lookups and fuzzy Semantic Search in parallel to feed LLM contexts with ultra-low latency:

```mermaid
sequenceDiagram
    participant User
    participant API as FastAPI API
    participant RetSvc as RetrievalService
    participant Vector as Vector Store
    participant DB as Relational DB
    participant LLM as GenAI Model

    User->>API: Chat Query / RAG Trigger
    API->>RetSvc: search_memories(Query, project_id)
    
    par State Fact Lookups
        RetSvc->>Vector: Vector Search (Factual matches)
        RetSvc->>DB: SQL Filter (Valid & Non-superseded Facts)
    and Semantic Search
        RetSvc->>Vector: Vector Search (Chunk embeddings)
        RetSvc->>RetSvc: MMR Re-ranking (Filter redundant chunks)
    end
    
    RetSvc->>RetSvc: Merge Results (State Facts + Chunk text)
    RetSvc-->>API: Ranked Top-K Context Items
    
    API->>LLM: Generate Answer (Prompt + Merged Context)
    LLM-->>User: Streaming Response
```

---

## The LoCoMo Benchmark Evaluation

The **LoCoMo-10** (Long Conversational Memory) benchmark, introduced by Snap Research in *"Evaluating Very Long-Term Conversational Memory of LLM Agents" (2024)*, evaluates AI agent systems on long-term memory, factual consistency, temporal alignment, and multi-hop reasoning over lengthy, multi-session dialog flows (up to 32 sessions and 26,000 tokens per conversation).

### Performance Metrics (Memwyre vs. Flat Vector Systems)

| Evaluation Category | Test Description | Flat Vector RAG | Memwyre Engine |
| :--- | :--- | :---: | :---: |
| **Single-Hop Recall** | Direct retrieval of personal facts and values | 53.0% | **80.0%** |
| **Multi-Hop Reasoning** | Linking facts across distant chat sessions | 24.0% | **45.0%** |
| **Temporal Alignment** | Ordering events and identifying timeframe changes | 48.0% | **74.0%** |
| **Open-Domain Reasoning** | Contextual inferences and complex reasoning | 50.0% | **76.0%** |
| **Overall Accuracy** | Weighted average across all 1,540 test questions | 43.7% | **73.5%** |
| **Mean Token Size** | Average size of retrieved context sent to LLM prompt | ~26,000 | **~3,000** |

> [!TIP]
> **Context Compression**: Memwyre achieves a **88.5% context length reduction** (retrieving 3,000 tokens instead of the 26,000-token raw conversational dialog) while significantly outperforming flat vector indexing in accuracy.

### Architectural Enablers of LoCoMo Performance
1. **Dynamic Context Pruning**: Strips out conversational noise (filler words, greetings, and distractors) during chunk enrichment.
2. **Two-Stage Re-ranking**: Employs a broad, high-recall vector fetch stage followed by a Cross-Encoder re-ranker to pick only the most contextually relevant memory items.
3. **Ebbinghaus Logarithmic Recency Decay**: Automatically deprecates older user preferences or conflicting facts chronologically when newer entries override them.
4. **Adversarial Immunity**: Utilizes strict semantic containment, causing the retriever to fail cleanly and refuse hallucinations when queried on non-existent information.

---

## Database Schema & Multi-Tenancy

Memwyre uses a hybrid storage model: metadata, relational facts, and user credentials reside in SQL tables (PostgreSQL/SQLite), while document chunks and enriched fact strings are mirrored in vector databases (Pinecone/ChromaDB).

```
  +------------------+          +-------------------+          +------------------+
  |      Users       | 1      * |     Memories      | 1      * |      Chunks      |
  |------------------|----------|-------------------|----------|------------------|
  | id (PK)          |          | id (PK)           |          | id (PK)          |
  | email            |          | user_id (FK)      |          | memory_id (FK)   |
  +------------------+          | content           |          | content_text     |
           | 1                  | project_id        |          | metadata (JSON)  |
           |                    | status            |          +------------------+
           |                    +-------------------+
           | *                            | 1
  +------------------+                    |
  |      Facts       | *                  |
  |------------------|--------------------+
  | id (PK)          |
  | user_id (FK)     |
  | memory_id (FK)   |
  | subject          |  (e.g., "User")
  | predicate        |  (e.g., "lives_in")
  | object           |  (e.g., "Tokyo")
  | valid_from       |
  | valid_until      |  (Determines supersession)
  | is_superseded    |
  +------------------+
```

### Fact Supersession & Project Containerization
- **Supersession**: When a new fact matching the same `subject` and `predicate` is written (e.g. user moves from Berlin to Tokyo), the database marks the old record's `is_superseded` flag as true and updates `valid_until` to the current timestamp. This guarantees that temporal inquiries return state-accurate facts.
- **Containerization**: Every memory and vector contains a `project_id`. When querying, filters strictly enforce containment matching the current workspace's `project_id`, preventing leakage across different project environments.

---

## Installation & Setup

### Prerequisites
- Python 3.11 or 3.12 (UV package manager recommended)
- Node.js 18+ & npm
- Redis server (for background Celery tasks)
- PostgreSQL database (Optional; SQLite is used by default)

### 1. Backend API Setup
Navigate to the backend directory, initialize the environment, install dependencies, and start the FastAPI server:

```bash
cd backend

# Create virtual environment and install packages
uv venv
uv pip install -r requirements.txt

# Start the FastAPI server
uv run uvicorn app.main:app --reload
```
*API Swagger UI documentation will be available at `http://localhost:8000/docs`.*

### 2. Background Ingestion Worker
Ensure Redis is running, then start the Celery background worker to process ingestion queues:

```bash
cd backend
uv run celery -A app.celery_app worker --loglevel=info -P solo
```

### 3. Frontend Dashboard Setup
Install frontend packages and spin up the Vite development server:

```bash
cd frontend
npm install
npm run dev
```
*The web dashboard runs at `http://localhost:5173`.*

### 4. Chrome Extension Installation
1. Open Chrome and navigate to `chrome://extensions/`
2. Enable **Developer mode** (top-right toggle)
3. Click **Load unpacked** (top-left)
4. Select the `extension/` folder from the root of this project.
5. In the Web App, go to **Settings** -> **Copy Extension Token** and paste it into the Extension popup to link your session.

### 5. MCP Server Integration
#### Claude Desktop
Add the following to your Claude Desktop config (located at `%APPDATA%\Claude\claude_desktop_config.json` on Windows or `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "brain-vault": {
      "command": "python",
      "args": ["/path/to/memwyre/backend/mcp_server.py"]
    }
  }
}
```

#### Cursor / VS Code
Configure your editor's MCP settings to run the server via command line:
```bash
python /path/to/memwyre/backend/mcp_server.py
```

### 6. Node CLI Setup
Install dependencies and run the command line tool globally:

```bash
cd cli
npm install
node index.js --help
```

---

## Environment Configuration

Copy the example environment file in the `backend/` directory and configure the variables:

```bash
cp backend/.env.example backend/.env
```

Key environment parameters:

```env
# --- Base Secrets & Database ---
SECRET_KEY="your-strong-random-64-character-string"
DATABASE_URL="postgresql://postgres:password@localhost/brain-vault"

# --- Redis & Celery ---
CELERY_BROKER_URL="redis://localhost:6379/0"
REDIS_URL="redis://localhost:6379/0"

# --- Vector Database (Pinecone) ---
PINECONE_API_KEY="your-pinecone-api-key"
PINECONE_HOST="https://your-pinecone-index-host"
PINECONE_SPARSE_HOST="https://your-optional-sparse-index-host"

# --- LLM Providers & Embeddings ---
MEMORY_ENGINE_VERSION="v2"  # "v1" for NVIDIA, "v2" for Azure/OpenAI
AZURE_OPENAI_API_KEY="your-azure-key"
AZURE_OPENAI_ENDPOINT="https://your-resource-name.cognitiveservices.azure.com/"
AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT="text-embedding-3-small"

# --- V1 Compatibility (NVIDIA NIM) ---
EMBEDDING_API_KEY="your-nvidia-embedding-key"
LLM_API_KEY="your-nvidia-llm-key"
```

---

## License

This project is licensed under the Apache License, Version 2.0 (Apache-2.0). See the [LICENSE](LICENSE) and [NOTICE](NOTICE) files for details.
