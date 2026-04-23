"""
Discovery endpoints for agent-readiness.

Serves .well-known metadata so AI agents can discover MemWyre's
API catalog and MCP server capabilities without manual configuration.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.config import settings

router = APIRouter(tags=["discovery"])


@router.get("/.well-known/api-catalog")
async def api_catalog():
    """
    RFC 9264 API Catalog — points agents to the OpenAPI specification.
    """
    return JSONResponse(
        content={
            "linkset": [
                {
                    "anchor": settings.BACKEND_URL,
                    "item": [
                        {
                            "href": f"{settings.BACKEND_URL}{settings.API_V1_STR}/openapi.json",
                            "type": "application/vnd.oai.openapi+json;version=3.1",
                        }
                    ],
                }
            ]
        },
        media_type="application/linkset+json",
    )


@router.get("/.well-known/mcp.json")
@router.get("/.well-known/mcp/server-card.json")
@router.get("/.well-known/mcp/server-cards.json")
async def mcp_server_card():
    """
    MCP Server Card — advertises MemWyre's MCP capabilities, tools,
    transport type, and authentication requirements.
    """
    return JSONResponse(content={
        "name": "MemWyre",
        "description": (
            "Personal Knowledge Base & Memory Layer for AI Agents. "
            "Save, search, and retrieve memories, documents, and "
            "contextual knowledge across any LLM."
        ),
        "version": "1.0.0",
        "homepage": "https://memwyre.tech",
        "logo": "https://memwyre.tech/apple-touch-icon.png",
        "contact": {
            "email": "support@memwyre.tech",
        },
        "transport": {
            "type": "streamable-http",
            "url": "https://server.memwyre.tech/mcp/",
        },
        "authentication": {
            "type": "bearer",
            "description": (
                "Generate an API key from your MemWyre dashboard at "
                "https://memwyre.tech/dashboard/settings. "
                "Pass it as a Bearer token in the Authorization header."
            ),
            "token_prefix": "bv_sk_",
        },
        "capabilities": {
            "tools": True,
            "resources": True,
            "prompts": True,
        },
        "tools": [
            {"name": "search_memwyre", "description": "Semantic search across your saved memories, documents, and notes."},
            {"name": "save_memory", "description": "Save a new memory snippet to your MemWyre Vault."},
            {"name": "list_memories", "description": "List recent memories and documents."},
            {"name": "get_document", "description": "Retrieve the full content of a specific document by ID."},
            {"name": "get_inbox", "description": "Get list of pending memories in the Inbox."},
            {"name": "update_memory", "description": "Update the content of an existing memory."},
            {"name": "delete_memory", "description": "Delete a memory or document by ID."},
            {"name": "search_by_date", "description": "Find memories created within a specific date range."},
            {"name": "get_all_tags", "description": "Get a list of all tags used in your knowledge base."},
            {"name": "generate_prompt", "description": "Generate a prompt with retrieved context from your memories."},
        ],
    })
