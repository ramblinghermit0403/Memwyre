from mcp_server import mcp

# Create the ASGI app for the dedicated MCP server
app = mcp.streamable_http_app()
