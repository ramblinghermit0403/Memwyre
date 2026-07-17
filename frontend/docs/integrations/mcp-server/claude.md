---
title: "Claude Desktop MCP Integration"
description: "Configure Memwyre as a local MCP server for Claude Desktop to maintain a persistent chat memory layer."
---

## Configuration File Locations

Add the Memwyre server configuration to your `claude_desktop_config.json` file. Depending on your operating system, this file is located at:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

## Setup Options

### Option A: Cloud Remote Tunnel (Recommended)

This uses our hosted `mcp-remote` tunnel to execute commands securely against the Memwyre Cloud API.

1. Open your configuration file and add the `memwyre` server block:

```json
{
  "mcpServers": {
    "memwyre": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://server.memwyre.tech/mcp",
        "--header",
        "Authorization:Bearer your_api_key_here"
      ]
    }
  }
}
```

2. Replace `your_api_key_here` with the token generated from **Settings → API Keys** in the Memwyre web app.

### Option B: Local Python Instance

For fully self-hosted environments:

1. Download the `mcp_server.py` script.
2. Register the python script inside your configuration file:

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

## Verifying Connection

1. Close and completely restart your **Claude Desktop** application.
2. Once restarted, click on the **plug icon** at the bottom-right corner of the chat input box.
3. You should see `memwyre` listed as an active source, exposing tools like `search_memwyre` and `save_memory`.

---

## Detailed Parameter Reference

When configuring the `memwyre` server block in your JSON settings, the following parameters are parsed by the Claude Desktop application when spawning the MCP subprocess:

- **`command`**: The primary executable to launch. When using `npx`, Claude Desktop uses your local Node.js environment path to resolve the command.
- **`args`**: The array of CLI parameters passed directly to the command:
  - `-y`: Forces npm to run non-interactively and auto-install the `mcp-remote` client without prompting.
  - `mcp-remote`: The official Memwyre Client library for remote secure tunnel gateway connections.
  - `https://server.memwyre.tech/mcp`: The endpoint URL of the Memwyre Cloud MCP engine.
  - `--header`: Configures custom HTTP authorization headers.
  - `Authorization:Bearer your_api_key_here`: Passes your private authentication key securely.
- **`env`** (Optional for Option A, required for Option B): Specific environment variables supplied to the spawned subprocess.

---

## Technical Details: Exposed Tools & Parameters

Once the connection is established, Claude Desktop automatically queries the MCP server's schemas. Memwyre exposes the following tools directly into Claude's prompt execution scope:

1. **`search_memwyre`**:
   - **Description**: Queries the Memwyre Vault for matching semantic memories, context rules, and style guides.
   - **Arguments**: `query` (string, the semantic search string), `limit` (integer, maximum matching nodes to return).
   - **Usage**: Triggered when you ask Claude questions about past projects, configurations, or personal notes.
2. **`save_memory`**:
   - **Description**: Ingests new text segments, project constraints, or architectural updates into your memory graph.
   - **Arguments**: `content` (string, the raw text content to memorize), `tags` (array of strings, category tags for organization).
   - **Usage**: Triggered when you instruct Claude: "Remember that we changed our database port to 5432" or "Save this setup configuration".

---

## Troubleshooting & Debugging

If the Memwyre connection does not initialize, check the following common issues:

### 1. Inspecting Claude Desktop MCP Logs

Claude Desktop writes all subprocess stdout/stderr and JSON-RPC connection failures to a local log file. Check these paths for error details:

- **macOS**: `~/Library/Logs/Claude/mcp.log`
- **Windows**: `%APPDATA%\Claude\logs\mcp.log`

Common errors like `npx: command not found` indicate that the Node.js path is not accessible by the Claude Desktop GUI app environment. In this case, ensure Node.js is installed globally and added to your system path.

### 2. Testing NPX Manually

Before launching Claude, verify the remote client runs successfully in your local shell by running:

```bash
npx -y mcp-remote https://server.memwyre.tech/mcp --header "Authorization:Bearer YOUR_KEY"
```

If this succeeds, the console will print `Listening on stdio...` and wait for JSON-RPC messages. You can exit using `Ctrl+C`.