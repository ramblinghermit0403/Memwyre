---
title: VS Code MCP Agent Caching
description: Configure remote or local MCP memory gateway in VS Code for Cline, Roo-Code, and other developer agents.
---
# VS Code Setup

To use Model Context Protocol (MCP) inside VS Code, you can use popular AI agent extensions like **Cline**, **Roo-Code**, or **Devins**.

## Setup via Cline / Roo-Code

1. Install the **Cline** or **Roo-Code** extension from the VS Code Marketplace.
2. Open the extension panel in the sidebar.
3. Click the **Settings (gear icon)** at the top right of the extension panel.
4. Scroll down to the **MCP Mode** section and enable it.
5. Edit your extension's MCP configuration settings:
   - **Cline**: click **Edit MCP Config** (opens `cline_mcp_settings.json`).
   - Add the following block:
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
6. Save the configuration file. Cline/Roo-Code will automatically start the server.

## Verification

In the extension's MCP dashboard tab, you will see `memwyre` listed as connected with 10+ active tools. The agent is now ready to query your database for contextual code references!

---

## Configuration Settings File Paths

Depending on the extension you are using, the configuration settings are stored in your VS Code user application data folders. You can edit them directly in the IDE or open the files at these physical locations:

* **Cline Settings Path**:
  * **macOS**: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
  * **Windows**: `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`
  * **Linux**: `~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
* **Roo-Code Settings Path**:
  * Replace `saoudrizwan.claude-dev` in the paths above with the Roo-Code storage directory `roodev.roo-cline`.

---

## Agent Integration: Cline & Roo-Code Workflows

Autonomous coding agents (like Cline and Roo-Code) operate by recursively executing tasks in a loop: reading files, running terminal commands, and editing code. Integrating Memwyre into these workflows provides key benefits:

* **Long-Term Debugging History**: If Cline encounters a compiler error, it queries the memory vault using `search_memwyre` to see if a similar error was solved in a past session. This saves significant developer time by preventing the agent from repeating the same debugging loops.
* **Architectural Guardrails**: You can store your project's architectural guidelines (such as styling conventions, design patterns, or test coverages) directly in your Memwyre Vault. The agent queries these rules on startup and applies them automatically during file edits.
* **Token Optimization**: Since the agent retrieves context dynamically through the MCP tool, it does not need to read the entire workspace into its system prompt, keeping token usage low and preventing context window exhaustion.

---

## Troubleshooting VS Code Connection Errors

If the Memwyre server fails to show a healthy connection in the extension settings tab:

### 1. NPX Client Install Failures
If you see installation error logs in the extension output console, it usually means the extension is unable to find the global Node/npx installation.
* **Fix**: Verify that Node.js is accessible in your environment path by opening the VS Code integrated terminal and running `npx -v`. If it is not found, install Node.js and restart VS Code.

### 2. Authorization Token Issues
Ensure the API authorization key has been copied correctly. You can test your key by making a curl request in your terminal:
```bash
curl -H "Authorization: Bearer YOUR_KEY" https://server.memwyre.tech/api/v1/health
```
If this health check succeeds, the token is valid and the issue lies in your JSON formatting.

### 3. Restarting the Server Process
If the connection is lost or settings change, you can force-restart the subprocess:
* Open the Cline/Roo-Code panel.
* Click the **MCP** tab at the bottom of the panel.
* Locate the `memwyre` entry and click the **Restart / Refresh** icon.
