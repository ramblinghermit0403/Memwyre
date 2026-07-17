---
title: "Self-Hosting"
description: "Learn how to host Memwyre locally or on your own private cloud using Docker Compose, PostgreSQL, and pgvector."
---

## Architecture Overview

A self-hosted Memwyre deployment consists of four primary components:

1. **Backend API (`memwyre-backend`)**: The core FastAPI/Python service handling ingestion, search pipelines, and client requests.
2. **Celery Worker (`celery-worker`)**: Resolves background tasks such as parsing web documents, downloading YouTube transcripts, and rebuilding relationship edges.
3. **Database (`postgres` with `pgvector`)**: Stores relational structured data and high-dimensional semantic vector embeddings.
4. **Cache & Queue (`redis`)**: Serves as the message broker for Celery and caching layer for rapid API queries.

```text
                  ┌──────────────────────┐
                  │    Client / IDE      │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   memwyre-backend    │
                  └─────┬──────────┬─────┘
                        │          │
                        ▼          ▼
                  ┌──────────┐ ┌──────────┐
                  │ postgres │ │  redis   │
                  └──────────┘ └────┬─────┘
                                    │
                                    ▼
                  ┌──────────────────────┐
                  │    celery-worker     │
                  └──────────────────────┘
```

---

## Docker Compose Quickstart

Create a `docker-compose.yml` file in your installation directory:

```yaml
version: '3.8'

services:
  db:
    image: pgvector/pgvector:pg16
    container_name: memwyre-db
    environment:
      POSTGRES_DB: memwyre
      POSTGRES_USER: memwyre_user
      POSTGRES_PASSWORD: super_secure_db_password
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U memwyre_user -d memwyre"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: memwyre-redis
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

  backend:
    image: ramblinghermit0403/memwyre-backend:latest
    container_name: memwyre-backend
    environment:
      - DATABASE_URL=postgresql://memwyre_user:super_secure_db_password@db:5432/memwyre
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=generate_a_random_jwt_secret_here
      - EMBEDDING_MODEL=nomic-embed-text
      - OLLAMA_HOST=http://host.docker.internal:11434
      - LLM_PROVIDER=ollama
      - LLM_MODEL=llama3
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

  worker:
    image: ramblinghermit0403/memwyre-backend:latest
    container_name: memwyre-worker
    command: celery -A app.worker worker --loglevel=info
    environment:
      - DATABASE_URL=postgresql://memwyre_user:super_secure_db_password@db:5432/memwyre
      - REDIS_URL=redis://redis:6379/0
      - EMBEDDING_MODEL=nomic-embed-text
      - OLLAMA_HOST=http://host.docker.internal:11434
      - LLM_PROVIDER=ollama
      - LLM_MODEL=llama3
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

volumes:
  pgdata:
  redisdata:
```

---

## Environment Variables

Configure these variables inside your `.env` file or docker-compose block:

| Variable | Description | Default / Example |
| --- | --- | --- |
| `DATABASE_URL` | SQLAlchemy-compatible connection string. If omitted, Memwyre defaults to local SQLite. | `postgresql://user:pass@db:5432/db` or `sqlite:///brain_vault.db` |
| `REDIS_URL` | Redis URL used for celery message passing and query cache. | `redis://redis:6379/0` |
| `SECRET_KEY` | Hex token used to sign authentication JWT keys. | `3a5d8f...` (Use `openssl rand -hex 32`) |
| `DEV_MODE` | If set to `True`, subscription checks are bypassed (unlimited usage gating). | `False` |
| `FREE_MEMORY_LIMIT` | Maximum memories allowed for a free user account. | `50` |
| `FREE_DOCUMENT_LIMIT` | Maximum documents allowed for a free user account. | `10` |
| `FREE_CHAT_LIMIT` | Maximum chats allowed for a free user account. | `30` |
| `MAX_CHARS_PER_MEMORY` | Character limit threshold for a single memory unit. | `25000` |
| `TURNSTILE_SECRET_KEY` | Cloudflare Turnstile token used for bot challenge validations. | `0x4AAAAAA...` |
| `DODO_PAYMENTS_API_KEY` | API authorization token for Dodo Payments gateway. | `dp_live_...` |
| `LLM_PROVIDER` | Language model platform. Options: `ollama`, `openai`, `anthropic`. | `ollama` |
| `LLM_MODEL` | Main inference model for relationship parsing and summarization. | `llama3` or `gpt-4o-mini` |
| `EMBEDDING_MODEL` | Model used to generate vector dimensions for retrieval. | `nomic-embed-text` |
| `OLLAMA_HOST` | Host URL pointing to your local Ollama runtime. | `http://host.docker.internal:11434` |

---

## Local LLM Setup (Ollama)

To run a zero-cloud setup, route all embedding and extraction tasks to [Ollama](https://ollama.com).

### Step 1: Install & Launch Ollama

Install Ollama on your host system (macOS, Windows, or Linux). Ensure Ollama runs locally by verifying:

```bash
curl http://localhost:11434/api/tags
```

### Step 2: Download Required Models

Memwyre requires a dense vector embedding model and an inference model. Pull them using the CLI:

```bash
# Pull the semantic embedding model (768 dimensions)
ollama pull nomic-embed-text

# Pull the inference model for memory graph extraction
ollama pull llama3
```

### Step 3: Run Docker Containers

Ensure `extra_hosts` is mapped to `host.docker.internal:host-gateway` in your `docker-compose.yml` so that Docker containers can contact your host's Ollama port (`11434`).

Spin up your cluster:

```bash
docker-compose up -d
```

### Step 4: Verify Local Connection

Inspect logs to verify that Memwyre connects to Ollama successfully during startup:

```bash
docker logs memwyre-backend
```

If you see vector dimension initialisation messages pointing to `nomic-embed-text`, your offline memory vault is up and running! 🚀