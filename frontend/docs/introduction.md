# Introduction

**Memwyre** is a universal memory layer for AI — a persistent, searchable knowledge vault that sits between you and every AI tool you use.

Instead of re-explaining your projects to ChatGPT, losing context when a Claude session ends, or copy-pasting the same background notes into every prompt, Memwyre remembers it for you. Automatically.

## What Problem Does It Solve?

Modern AI tools are powerful, but stateless. Every new conversation starts from zero. Memwyre fixes this by giving you one place to store, organise, and retrieve knowledge — then injecting the right context into any AI session on demand.

## How It Works

```
  You ──► Memwyre Vault ──► Any AI Tool
            ▲
  Browser / IDE / YouTube / Web Pages
```

1. **Capture** — Save memories from the browser extension, MCP server, chat, or by pasting URLs (YouTube videos, web articles, etc.).
2. **Organise** — Memories land in your Inbox, where you can review, tag, and promote them to your long-term Vault.
3. **Retrieve** — Memwyre's semantic search surfaces the most relevant memories for any question. Your IDE, agent, or the Memwyre chat all have access.

## Core Concepts

| Concept | Description |
|---|---|
| **Vault** | Your long-term knowledge store. Semantically indexed and always searchable. |
| **Inbox** | A staging area for new captures before they're reviewed and promoted. |
| **Memory** | A single unit of knowledge — a note, snippet, transcript, or article. |
| **Document** | A longer, structured piece of content stored and retrieved as a whole. |
| **MCP Server** | A local Python process that exposes your vault to IDEs and AI agents. |

## Choose Your Path

Not sure where to start? Pick the setup that fits your workflow:

- 🌐 **Just browsing the web / using ChatGPT?** → [Browser Extension](./integrations/browser-extension)
- 💻 **Using Cursor, VS Code, or Claude Desktop?** → [MCP Server](./integrations/mcp-server)
- 🤖 **Running autonomous agents with OpenClaw?** → [OpenClaw Plugin](./integrations/openclaw-plugin)
- 🎥 **Want to ingest YouTube videos or web articles?** → [YouTube Ingestion](./features/youtube-ingestion) · [Web Ingestion](./features/web-ingestion)

## Quick Start (60 seconds)

1. Sign up at [memwyre.tech](https://memwyre.tech).
2. Install the browser extension ([guide here](./integrations/browser-extension)).
3. Go to **Settings → Copy Extension Token** and paste it into the extension.
4. Browse to any AI site — Memwyre is ready.
