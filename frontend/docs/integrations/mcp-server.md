# IDEs & Agents — MCP Server

Memwyre provides a fully compliant **Model Context Protocol (MCP)** server. This lets your local AI agents, code editors, and desktop apps seamlessly read from and write to your Memwyre vault.

## Overview

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open standard that connects AI systems with external tools and data sources. By running the Memwyre MCP Server locally, you give your IDE or agent (Claude Desktop, Cursor, VS Code, etc.) direct access to your centralised memory — no more copy-pasting context manually.

## Prerequisites

Before you begin, make sure you have:

- **Python 3.10+** installed on your machine.
- Your **`MEMWYRE_API_KEY`** — generate one from **Settings → API Keys** in the Memwyre web app.
- The `mcp_server.py` script downloaded to a permanent location on your hard drive.

## Setup

### Step 1 — Download the Server Script

Download `mcp_server.py` from your [Memwyre dashboard](https://memwyre.tech) and save it somewhere stable (e.g. `~/memwyre/mcp_server.py`).

### Step 2 — Configure Claude Desktop

Add the following block to your Claude Desktop config file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "memwyre": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server.py"],
      "env": {
        "MEMWYRE_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

> Replace `/absolute/path/to/mcp_server.py` with the actual path where you saved the file.

### Step 3 — Configure VS Code or Cursor

In your IDE's MCP client settings, add a new server entry pointing to the script:

```bash
python /absolute/path/to/mcp_server.py
```

Set `MEMWYRE_API_KEY` in the environment variables section of your IDE's MCP configuration panel.

## Available Tools

Once connected, your IDE or agent will have access to:

| Tool | Description |
|---|---|
| `search_memory(query, top_k)` | Semantic search across your entire knowledge base. |
| `save_memory(text, tags)` | Save a new snippet or note directly into your Memwyre Inbox. |
| `get_document(doc_id)` | Retrieve the full text of a specific saved document. |

## Troubleshooting

**Claude Desktop doesn't show the Memwyre tools.**  
Check that the `command` path resolves correctly — try `python3` instead of `python` on macOS/Linux.

**`MEMWYRE_API_KEY` environment variable not found.**  
Make sure the key is set inside the `env` block of your config file, not as a system environment variable.
