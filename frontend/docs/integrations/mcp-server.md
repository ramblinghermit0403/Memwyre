---
title: Universal MCP Server Guide
description: Universal guide to connecting Memwyre to Model Context Protocol (MCP) clients like Claude Desktop, Cursor, and VS Code.
---
# IDEs & Agents — MCP Server

Memwyre provides a fully compliant **Model Context Protocol (MCP)** server. This lets your local AI agents, code editors, and desktop apps seamlessly read from and write to your Memwyre vault.

## Overview

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open standard that connects AI systems with external tools and data sources. By running the Memwyre MCP Server locally, you give your IDE or agent (Claude Desktop, Cursor, VS Code, etc.) direct access to your centralised memory — no more copy-pasting context manually.

## Prerequisites

Before you begin, make sure you have:

- **Python 3.10+** installed on your machine.
- Your **`MEMWYRE_API_KEY`** — generate one from **Settings → API Keys** in the Memwyre web app.
- The `mcp_server.py` script downloaded to a permanent location on your hard drive.

## Connection Protocols

Memwyre supports two connection protocols for Model Context Protocol (MCP):
1. **Remote HTTP Tunneling (Recommended)**: Utilizes the `mcp-remote` utility to tunnel commands to our secure cloud endpoint (`https://server.memwyre.tech/mcp`).
2. **Local Python Execution**: Runs the `mcp_server.py` file locally on your machine using Python, executing local SQLite vector updates.

---

## Setup Configurations

### 1. Claude Desktop (Remote)
Add this server block to your Claude configuration file:
* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "memwyre": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer your_token_here"]
    }
  }
}
```

### 2. VS Code & Cursor (Remote)
In your IDE settings panel, register the MCP server as:
* **Command**: `npx`
* **Args**: `["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer your_token_here"]`

### 3. Local Python Script Setup
If running fully self-hosted, download `mcp_server.py` and invoke it directly:
```json
{
  "mcpServers": {
    "memwyre-local": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server.py"],
      "env": {
        "MEMWYRE_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

---

## Available Tools

Once connected, your IDE or agent will have access to the following tools:

<details>
<summary><b><code>search_memwyre</code></b> (Primary Search)</summary>

The most important tool for retrieving context. It performs a semantic search across your entire vault.

- **Parameters:**
  - `query` (Required): Your search terms or question.
  - `purpose` (Optional): Hint for context formatting. Options: `general`, `code`, or `summary`.
</details>

<details>
<summary><b><code>save_memory</code></b> (Capture Context)</summary>

Save new information or notes directly into your Memwyre Inbox.

- **Parameters:**
  - `text` (Required): The content you want to save.
  - `tags` (Optional): A list of tags to categorize the memory (e.g. `["project-x", "todo"]`).
  - `source` (Optional): Origin of the memory (defaults to `mcp`).
</details>

<details>
<summary><b><code>approve_memory</code></b> (Approve Ingestion)</summary>

Approve a pending memory in the Inbox and begin its ingestion process.

- **Parameters:**
  - `memory_id` (Required): The ID of the memory, starting with `mem_` (e.g. `mem_123`).
</details>

<details>
<summary><b><code>discard_memory</code></b> (Discard from Inbox)</summary>

Discard a pending memory from the Inbox.

- **Parameters:**
  - `memory_id` (Required): The ID of the memory, starting with `mem_` (e.g. `mem_123`).
</details>

<details>
<summary><b><code>generate_prompt</code></b> (Prompt Engineering)</summary>

Retrieves relevant context and wraps it in a pre-formatted prompt for an LLM.

- **Parameters:**
  - `query` (Required): The topic to generate a prompt for.
  - `template` (Optional): The prompt structure. Options: `standard`, `code`, or `summary`.
</details>

<details>
<summary><b><code>get_document</code></b> (Full Text Retrieval)</summary>

Retrieve the entire content of a specific document (PDF, Doc, or Web Page) by its ID.

- **Parameters:**
  - `doc_id` (Required): The numeric ID of the document (e.g. `123`).
</details>

<details>
<summary><b><code>list_memories</code></b> (Discovery)</summary>

List the most recent memories and documents added to your vault.

- **Parameters:**
  - `limit` (Optional): Number of items to return (default: 10).
  - `offset` (Optional): Pagination offset.
</details>

<details>
<summary><b><code>get_inbox</code></b> (Pending Review)</summary>

Lists all memories currently in your "Inbox" status that are awaiting review or confirmation.
</details>

<details>
<summary><b><code>update_memory</code></b> (Edit)</summary>

Update the content of an existing memory snippet.

- **Parameters:**
  - `memory_id` (Required): The ID of the memory, starting with `mem_` (e.g. `mem_45`).
  - `content` (Required): The new text content.
</details>

<details>
<summary><b><code>delete_memory</code></b> (Cleanup)</summary>

Permanently remove a memory or document from your vault.

- **Parameters:**
  - `memory_id` (Required): The ID of the item, starting with `mem_` or `doc_` (e.g. `doc_12`).
</details>

<details>
<summary><b><code>search_by_date</code></b> (Chronological Search)</summary>

Find memories created within a specific timeframe.

- **Parameters:**
  - `start_date` (Required): Start date in `YYYY-MM-DD` format.
  - `end_date` (Optional): End date in `YYYY-MM-DD` format.
</details>

<details>
<summary><b><code>get_all_tags</code></b> (Taxonomy)</summary>

Retrieve a comprehensive list of all tags currently used across your entire memory vault.
</details>

---

## Troubleshooting

**Claude Desktop doesn't show the Memwyre tools.**  
Check that the `command` path resolves correctly — try `python3` instead of `python` on macOS/Linux if deploying local scripts, or confirm your `npx` command executes correctly in your shell.

**`MEMWYRE_API_KEY` environment variable not found.**  
For local server python deployments, ensure the key is set inside the `env` block of your config file, not as a system environment variable. For remote instances, ensure your Bearer token in the header argument is valid.
