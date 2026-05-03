# IDEs & Agents (MCP Server)

MemWyre provides a fully compliant **Model Context Protocol (MCP)** server. This allows your local AI agents, code editors, and desktop applications to seamlessly read from and write to your MemWyre vault.

## Overview

The Model Context Protocol (MCP) connects AI systems with external tools. By running the MemWyre MCP Server script locally, you give your favorite local agents (like Claude Desktop) or IDEs (like Cursor and VS Code) direct access to your centralized memory without needing to copy-paste context manually.

## Setup & Installation

The MemWyre MCP Server is distributed as a standalone Python script (`mcp_server.py`). You must configure your local environment to run this script.

### Prerequisites
1. **Python**: Ensure Python 3.10+ is installed on your machine.
2. **API Key**: Generate your `MEMWYRE_API_KEY` from the Settings page in the MemWyre web app.
3. **Dependencies**: If required by the distribution, ensure you install the necessary Python packages (e.g., `pip install mcp langchain` depending on the provided requirements).

### Step 1: Download the Server
Download the `mcp_server.py` file provided by MemWyre and save it to a secure location on your hard drive.

### Step 2: Configure Claude Desktop

Add the following configuration to your Claude Desktop config file (typically found at `~/Library/Application Support/Claude/claude_desktop_config.json` on Mac, or `%APPDATA%\Claude\claude_desktop_config.json` on Windows):

```json
{
  "mcpServers": {
    "brain-vault": {
      "command": "python",
      "args": ["/absolute/path/to/your/mcp_server.py"],
      "env": {
        "MEMWYRE_API_KEY": "your_api_key_here"
      }
    }
  }
}
```
*Make sure to replace `/absolute/path/to/your/mcp_server.py` with the actual path where you saved the script on your computer.*

### Step 3: Configure VS Code / Cursor

In your IDE's MCP client settings, configure a new server using the `python` command and point it to the script:

```bash
python /absolute/path/to/your/mcp_server.py
```
You will also need to add your `MEMWYRE_API_KEY` to the environment variables section within your IDE's MCP configuration panel.

## Capabilities

Once connected, your IDE or agent will have access to the following tools:
- **`search_memory(query, top_k)`**: Perform semantic searches across your knowledge base to retrieve highly relevant coding context.
- **`save_memory(text, tags)`**: Save new code snippets or architectural decisions directly into your MemWyre Inbox.
- **`get_document(doc_id)`**: Retrieve the full text of a specific saved document.
