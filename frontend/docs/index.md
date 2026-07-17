---
title: "Overview"
description: "Get started with Memwyre, the universal persistent memory layer for AI agents, developer IDEs, and prompt workflows."
---

Instead of re-explaining your projects to ChatGPT, losing context when a Claude session ends, or copy-pasting the same background notes into every prompt, Memwyre remembers it for you. Automatically.

## What Problem Does It Solve?

Modern AI tools are powerful, but stateless. Every new conversation starts from zero. Memwyre fixes this by giving you one place to store, organise, and retrieve knowledge — then injecting the right context into any AI session on demand.

## How It Works

```text
  You ──► Memwyre Vault ──► Any AI Tool
            ▲
  Browser / IDE / YouTube / Web Pages
```

1. **Capture** — Save text blocks, URLs, articles, and chats from the browser extension, native connectors, or the CLI installer.
2. **Organise** — Incoming captures land in your Inbox, where you can review, tag, and promote them. Background tasks chunk documents and extract key facts.
3. **Retrieve** — Memwyre's hybrid engine queries both relational facts and vector indexes (using MMR and Cross-Encoder reranking) to inject precise context.

## Core Concepts

| Concept | Description | Database Model |
| --- | --- | --- |
| **Memory** | A single unit of raw ingested text — a note, snippet, article, or video transcript. | `Memory` |
| **Chunk** | A segmented slice of a larger document, vectorized for dense retrieval. | `Chunk` |
| **Fact** | An extracted atomic statement (subject-predicate-object) representing a current, stateful truth. | `Fact` |
| **Entity Profile** | A compiled metadata profile representing a unique project or person, matched deterministically on query boundaries. | `EntityProfile` |
| **MCP Server** | A standard Model Context Protocol interface exposing search and ingestion tools to client IDEs. | - |

## Choose Your Path

Not sure where to start? Pick the setup that fits your workflow:

- 🌐 **Just browsing the web / using ChatGPT?** → [Browser Extension](./integrations/browser-extension)
- 💻 **Using Cursor, VS Code, or Claude Desktop?** → [MCP Server](./integrations/mcp-server)
- 🤖 **Running autonomous agents with OpenClaw?** → [OpenClaw Plugin](./integrations/plugins/openclaw)

## Quick Start (60 seconds)

1. Sign up at [memwyre.tech](https://memwyre.tech).
2. Install the browser extension ([guide here](./integrations/browser-extension)).
3. Go to **Settings → Copy Extension Token** and paste it into the extension.
4. Browse to any AI site — Memwyre is ready.