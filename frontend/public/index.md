# Memwyre — Your Digital Brain for AI

Memwyre is a **personal knowledge base and memory layer** that works across every AI tool you use — Claude, ChatGPT, Gemini, Copilot, and more.

## What is Memwyre?

Memwyre captures, organizes, and retrieves your knowledge so AI agents can use your personal context to give better answers.

### Key Features

- **Omnipresent Overlay** — Save memories from any AI chat with a single click via the browser extension.
- **Contextual Chat** — Ask questions and get answers grounded in your personal knowledge base.
- **Cross-Post** — Send context from one AI to another seamlessly.
- **MCP Server** — Connect your vault to Claude Desktop, Cursor, or any MCP-compatible agent.
- **Semantic Search** — Find anything in your vault using natural language.
- **Document Ingestion** — Upload PDFs, text files, YouTube links, and web pages.
- **Smart Inbox** — Triage and organize incoming memories before they enter your vault.
- **Projects** — Organize your knowledge into focused workspaces.
- **Export** — Export your knowledge as Markdown, JSON, or PDF.

## For AI Agents

Memwyre exposes an [MCP Server](https://memwyre.tech/.well-known/mcp.json) with the following tools:

| Tool | Description |
|---|---|
| `search_memwyre` | Semantic search across saved memories and documents |
| `save_memory` | Save a new memory snippet to the vault |
| `list_memories` | List recent memories and documents |
| `get_document` | Retrieve full document content by ID |
| `get_inbox` | Get pending memories in the inbox |
| `update_memory` | Update an existing memory |
| `delete_memory` | Delete a memory or document |
| `search_by_date` | Find memories within a date range |
| `get_all_tags` | List all tags in the knowledge base |
| `generate_prompt` | Generate a prompt with retrieved context |

### Connecting

1. Get an API key from [memwyre.tech/dashboard/settings](https://memwyre.tech/dashboard/settings)
2. Connect via MCP at `https://server.memwyre.tech/mcp/`
3. Authenticate with `Authorization: Bearer bv_sk_YOUR_KEY`

## Links

- **Homepage**: [memwyre.tech](https://memwyre.tech)
- **API Docs**: [server.memwyre.tech/api/v1/openapi.json](https://server.memwyre.tech/api/v1/openapi.json)
- **MCP Server Card**: [memwyre.tech/.well-known/mcp.json](https://memwyre.tech/.well-known/mcp.json)
- **Privacy Policy**: [memwyre.tech/privacy-policy](https://memwyre.tech/privacy-policy)
- **Terms**: [memwyre.tech/terms](https://memwyre.tech/terms)
