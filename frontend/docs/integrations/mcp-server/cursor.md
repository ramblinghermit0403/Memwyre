# Cursor Setup

Enable the Memwyre MCP Server inside Cursor to inject your personal memory directly into your code generation and editing process.

## Setup Steps

1. Open **Cursor Settings** (gear icon in the top right, or `Ctrl + Shift + J` / `Cmd + Shift + J`).
2. Go to **Features** and scroll down to the **MCP** section.
3. Click **+ Add New MCP Server**.
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
* Type `@Memwyre` or ask Cursor's chat assistant: *"Search my memory for X"*
* The assistant will execute `search_memwyre` and pull the matching memories into your prompt context.
