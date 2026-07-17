---
title: "Cursor AI IDE MCP Integration"
description: "Configure Memwyre inside Cursor AI IDE to maintain persistent codebase memories across editing sessions."
---

## Setup Steps

1. Open **Cursor Settings** (gear icon in the top right, or `Ctrl + Shift + J` / `Cmd + Shift + J`).
2. Go to **Features** and scroll down to the **MCP** section.
3. Click **\+ Add New MCP Server**.
4. Enter the details for the server configuration:
   - **Name**: `Memwyre`
   - **Type**: `command`
   - **Command / Args**:
     ```bash
     npx -y mcp-remote https://server.memwyre.tech/mcp --header "Authorization:Bearer your_api_key_here"
     ```
5. Replace `your_api_key_here` with your Memwyre API Key.
6. Click **Save**.

## Using Memwyre in Cursor

Once registered, Cursor automatically detects the available tools.

- Type `@Memwyre` or ask Cursor's chat assistant: _"Search my memory for X"_
- The assistant will execute `search_memwyre` and pull the matching memories into your prompt context.

---

## Detailed Configuration Options

When setting up the MCP server in the Cursor settings UI, you are prompted to configure three key fields:

1. **Name**: A unique identifier for the server inside Cursor's registry (we recommend `Memwyre` or `memwyre-mcp`).
2. **Type**: Select `command`. This tells Cursor to spawn a local subprocess. Under the hood, Cursor launches this command using your operating system's default shell environment, mapping the standard input and standard output streams directly to the JSON-RPC interface.
3. **Command / Args**: The command line string. It uses `npx` to auto-fetch the latest `mcp-remote` client package and connect to our secure websocket API gateway at `https://server.memwyre.tech/mcp`.

---

## Best Practices: Codebase Context & Project Profiles

Using Memwyre inside Cursor provides a powerful, persistent context layer that survives when you close your IDE or switch branches. Here is how to optimize the integration:

- **Semantic Scope Matching**: When you ask a question in Cursor Chat or Composer, the LLM parses the current query. If it detects references to environment setup, styling rules, or API paths, it automatically invokes the `search_memwyre` tool. It retrieves relevant conventions from your vault and injects them as system prompts.
- **Project-Specific Memories**: To organize your memories, use custom tags when adding guidelines via the Web Dashboard (e.g. `[react, tailwind, typescript]`). When Cursor queries the vault, the matching engine uses these tags to retrieve only the rules appropriate for the files currently open in your workspace.
- **Workspace Profiles**: Maintain distinct profiles for personal projects vs corporate codebases by configuring separate API tokens for different workspaces.

---

## Troubleshooting Cursor Connection Issues

If the Memwyre server fails to show a green status dot or is stuck in an error loop:

### 1. Stuck on "Connecting"

- **Cause**: This usually means Cursor is unable to resolve the `npx` executable in its environment path.
- **Fix**: Verify that Node.js is installed globally on your machine. Open a terminal and run `node -v` and `npx -v`. If they are not found, install the Node.js package. On Windows, make sure to restart Cursor after modifying your system environment variables.

### 2. Status Dot is Red ("Error")

- **Cause**: Typically indicates an invalid or expired API authorization token, or a network firewall blocking outbound WebSocket traffic.
- **Fix**: Double check that the token copy-pasted into the `--header "Authorization:Bearer YOUR_KEY"` string matches exactly and has no trailing spaces. You can generate a fresh token by going to the Memwyre web dashboard and navigating to **Settings → API Keys**.

### 3. Force Reloading the MCP Server

If you update your configuration parameters, Cursor may not reload the process automatically. Click the **Refresh / Reload** icon next to the Memwyre entry in Cursor Settings \> Features \> MCP to restart the subprocess.