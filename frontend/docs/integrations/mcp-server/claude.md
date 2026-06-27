# Claude Desktop Setup

Connect Memwyre directly to the official Claude Desktop client to give Claude access to your centralized knowledge base.

## Configuration File Locations

Add the Memwyre server configuration to your `claude_desktop_config.json` file. Depending on your operating system, this file is located at:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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
