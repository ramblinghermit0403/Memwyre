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
