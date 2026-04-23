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


@router.get("/.well-known/oauth-authorization-server")
async def oauth_authorization_server():
    """
    RFC 8414 — OAuth 2.0 Authorization Server Metadata.
    Describes MemWyre's auth endpoints so agents know how to authenticate.
    """
    return JSONResponse(content={
        "issuer": "https://server.memwyre.tech",
        "authorization_endpoint": f"https://server.memwyre.tech{settings.API_V1_STR}/auth/oauth/google/login",
        "token_endpoint": f"https://server.memwyre.tech{settings.API_V1_STR}/auth/login",
        "registration_endpoint": f"https://server.memwyre.tech{settings.API_V1_STR}/auth/register",
        "scopes_supported": ["mcp:read", "mcp:write"],
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code", "password"],
        "token_endpoint_auth_methods_supported": ["client_secret_post"],
        "service_documentation": "https://memwyre.tech",
        "ui_locales_supported": ["en"],
        "code_challenge_methods_supported": [],
        "x_api_key_info": {
            "description": (
                "For programmatic / MCP access, generate a persistent API key "
                "from your dashboard at https://memwyre.tech/dashboard/settings. "
                "API keys use the prefix 'bv_sk_' and support Bearer auth."
            ),
            "prefix": "bv_sk_",
        },
    })


@router.get("/.well-known/openid-configuration")
async def openid_configuration():
    """
    OpenID Connect Discovery — minimal OIDC metadata.
    MemWyre delegates identity to Google; this document helps agents
    understand the auth flow.
    """
    return JSONResponse(content={
        "issuer": "https://server.memwyre.tech",
        "authorization_endpoint": f"https://server.memwyre.tech{settings.API_V1_STR}/auth/oauth/google/login",
        "token_endpoint": f"https://server.memwyre.tech{settings.API_V1_STR}/auth/login",
        "userinfo_endpoint": f"https://server.memwyre.tech{settings.API_V1_STR}/auth/verify",
        "scopes_supported": ["openid", "email", "profile"],
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code", "password"],
        "subject_types_supported": ["public"],
        "id_token_signing_alg_values_supported": ["HS256"],
        "token_endpoint_auth_methods_supported": ["client_secret_post"],
    })


@router.get("/.well-known/oauth-protected-resource")
async def oauth_protected_resource():
    """
    RFC 9728 — OAuth Protected Resource Metadata.
    Tells agents this resource requires auth and how to obtain tokens.
    """
    return JSONResponse(content={
        "resource": "https://server.memwyre.tech",
        "authorization_servers": ["https://server.memwyre.tech"],
        "scopes_supported": ["mcp:read", "mcp:write"],
        "bearer_methods_supported": ["header"],
        "resource_documentation": "https://memwyre.tech",
    })


@router.get("/.well-known/agent-skills/index.json")
async def agent_skills_index():
    """
    Agent Skills Discovery (Cloudflare RFC v0.2.0).
    Lists MemWyre's capabilities as discoverable agent skills.
    """
    return JSONResponse(content={
        "$schema": "https://agentskills.io/schema/v0.2.0/index.json",
        "name": "MemWyre",
        "description": "Personal Knowledge Base & Memory Layer for AI Agents",
        "url": "https://memwyre.tech",
        "skills": [
            {
                "name": "semantic-search",
                "type": "mcp-tool",
                "description": "Search across saved memories and documents using natural language queries.",
                "url": "https://server.memwyre.tech/mcp/",
            },
            {
                "name": "memory-management",
                "type": "mcp-tool",
                "description": "Save, update, delete, and list personal knowledge memories.",
                "url": "https://server.memwyre.tech/mcp/",
            },
            {
                "name": "document-retrieval",
                "type": "mcp-tool",
                "description": "Retrieve full content of uploaded documents (PDF, text, web pages).",
                "url": "https://server.memwyre.tech/mcp/",
            },
            {
                "name": "context-generation",
                "type": "mcp-tool",
                "description": "Generate prompts enriched with personal knowledge context.",
                "url": "https://server.memwyre.tech/mcp/",
            },
        ],
    })

