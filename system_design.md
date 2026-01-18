# System Design - Brain Vault (Current Architecture)

## 1. High-Level Architecture (Component View)

```mermaid
flowchart TB
    subgraph Client_Side [Client Side]
        Browser["WebApp (Vue.js)"]
        Extension["Chrome Extension"]
    end

    subgraph Load_Balancer [Ingress]
        Nginx["Reverse Proxy / LB"]
    end

    subgraph Backend_Core [Backend API (FastAPI)]
        Auth_Mod["Auth & Users"]
        Mem_Mod["Memory Management"]
        Ret_Mod["Retrieval Service"]
        LLM_Mod["LLM Service"]
    end

    subgraph Background_Workers [Celery Workers]
        Ingest_Worker["Ingestion Worker"]
        Dedupe_Worker["Deduplication Worker"]
    end

    subgraph Data_Persistence [Data Layer]
        Postgres[("PostgreSQL - Users, Facts, Chunks")]
        Pinecone[("Pinecone - Vector Index")]
        Redis[("Redis - Celery Broker")]
    end
    
    subgraph External_Services [AI Providers]
        Bedrock["AWS Bedrock (Nova Pro / Titan v2)"]
        OpenAI["OpenAI (GPT-4o)"]
        Gemini["Google Gemini"]
    end

    Browser -->|HTTPS| Nginx
    Extension -->|HTTPS| Nginx
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

## 2. Core Workflows

### 2.1 Advanced Ingestion Pipeline
The ingestion process is asynchronous and heavily enriched using LLMs.

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Worker as Celery Worker
    participant LLM as Bedrock/LLM
    participant Vector as Pinecone
    participant DB as PostgreSQL

    User->>API: POST /memory (Content)
    API->>DB: Save Memory (Raw)
    API->>Worker: Dispatch Ingest Task
    API-->>User: 202 Accepted
    
    Note over Worker: Background Processing
    Worker->>LLM: Metadata Extraction (Title, Tags)
    Worker->>Worker: Semantic Chunking (Titan v2 Embeddings)
    
    loop Parallel Enrichment
        Worker->>LLM: Enrich Chunk (Summary, Q&A, Entities)
        Worker->>LLM: Extract Atomic Facts (Subject-Predicate-Object)
    end
    
    Worker->>Vector: Batch Upsert (Enriched Chunks + Facts)
    Worker->>DB: Save Chunks & Facts (Linked to Memory)
    Worker->>DB: Update Memory Status (Active)
```

### 2.2 Parallelized Retrieval (RAG)
Retrieval combines exact Fact lookups with fuzzy Semantic Search in parallel for low latency.

```mermaid
sequenceDiagram
    participant User
    participant API
    participant RetSvc as RetrievalService
    participant Vector as Pinecone
    participant DB as PostgreSQL
    participant LLM as GenAI

    User->>API: Chat Query
    API->>RetSvc: search_memories(Query)
    
    par State Search (Facts)
        RetSvc->>Vector: Vector Search (Facts)
        RetSvc->>DB: SQL Filter (Valid Facts)
    and Semantic Search (Memories)
        RetSvc->>Vector: Vector Search (Chunks)
        RetSvc->>RetSvc: MMR Re-ranking (Lambda=0.7)
    end
    
    RetSvc->>RetSvc: Merge Results (State + Semantic)
    RetSvc-->>API: Top-K Context
    
    API->>LLM: Generate Answer(Prompt + Context)
    LLM-->>User: Response
```

## 3. Database Schema (Key Entities)

```mermaid
erDiagram
    Users ||--o{ Memories : "owns"
    Users ||--o{ Facts : "owns"
    
    Memories ||--o{ Chunks : "contains"
    Memories ||--o{ Facts : "source"
    Chunks ||--o{ Facts : "exact_source"

    Users {
        string id PK
        string email
    }

    Memories {
        int id PK
        int user_id FK
        text content
        datetime created_at
        string status
    }

    Chunks {
        int id PK
        int memory_id FK
        text content_text
        json metadata
        string embedding_id
    }

    Facts {
        int id PK
        int user_id FK
        string subject
        string predicate
        string object
        datetime valid_from
        datetime valid_until
        boolean is_superseded
    }
```

## 4. Technology Stack (Current)

```json
{
  "system": "Brain Vault",
  "layers": [
    {
      "name": "Backend",
      "tech": ["FastAPI", "Python 3.12+", "Celery", "SQLAlchemy (Async)"],
      "deployment": "Uvicorn"
    },
    {
      "name": "AI / ML",
      "embeddings": "Amazon Titan Text v2 (via Boto3)",
      "inference": ["AWS Bedrock (Nova Pro)", "OpenAI (GPT-4o)", "Gemini 1.5 Pro"],
      "vector_db": "Pinecone (Serverless)"
    },
    {
      "name": "Data",
      "primary_db": "PostgreSQL",
      "queue": "Redis"
    }
  ]
}
```
