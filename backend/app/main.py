from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import auth, retrieval, llm, documents, memory, export, prompts, llm_api, inbox, user_keys, ws, settings as user_settings, feedback, chat_api, ingest, billing, admin, admin_bypass, bypass, projects, context, discovery, plugin
from app.db.base import Base
from app.db.session import engine
import app.models # Register models
import sys
import os

# Import MCP server for mounting
_mcp_server = None
try:
    if os.getcwd() not in sys.path:
        sys.path.append(os.getcwd())
    from mcp_server import mcp as _mcp_server
except Exception as e:
    print(f"Failed to import MCP Server: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle manager."""
    # --- Startup ---
    from app.services.dedupe_job import dedupe_service
    from app.db.session import AsyncSessionLocal
    from app.services.websocket import manager
    import asyncio

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Start background tasks
    asyncio.create_task(dedupe_service.run_periodic_check(AsyncSessionLocal))
    asyncio.create_task(manager.start_redis_listener())

    # App is running
    yield

    # --- Shutdown (if needed) ---


app = FastAPI(
    title="MemWyre",
    description="Backend API for MemWyre - Personal Knowledge Base",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# CORS Configuration
if settings.cors_origin_list == ["*"]:
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=r".*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Requires-Subscription"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Requires-Subscription"],
    )

# Rate Limiter
from app.core.rate_limiter import init_rate_limiter
init_rate_limiter(app)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(retrieval.router, prefix=f"{settings.API_V1_STR}/retrieval", tags=["retrieval"])
app.include_router(llm.router, prefix=f"{settings.API_V1_STR}/llm", tags=["llm"])
app.include_router(documents.router, prefix=f"{settings.API_V1_STR}/documents", tags=["documents"])
app.include_router(ingest.router, prefix=f"{settings.API_V1_STR}/ingest", tags=["ingest"])
app.include_router(memory.router, prefix=f"{settings.API_V1_STR}/memory", tags=["memory"])
app.include_router(projects.router, prefix=f"{settings.API_V1_STR}/projects", tags=["projects"])
app.include_router(context.router, prefix=f"{settings.API_V1_STR}/context", tags=["context"])
app.include_router(export.router, prefix=f"{settings.API_V1_STR}/export", tags=["export"])
app.include_router(prompts.router, prefix=f"{settings.API_V1_STR}/prompts", tags=["prompts"])

app.include_router(llm_api.router, prefix=f"{settings.API_V1_STR}/llm", tags=["llm-api"])
app.include_router(inbox.router, prefix=f"{settings.API_V1_STR}/inbox", tags=["inbox"])
app.include_router(user_keys.router, prefix=f"{settings.API_V1_STR}/user", tags=["user-keys"])
app.include_router(user_settings.router, prefix=f"{settings.API_V1_STR}/user", tags=["user-settings"])
app.include_router(feedback.router, prefix=f"{settings.API_V1_STR}/feedback", tags=["feedback"])
app.include_router(chat_api.router, prefix=f"{settings.API_V1_STR}/chat", tags=["chat"])

from app.routers import user_api_keys
app.include_router(user_api_keys.router, prefix=f"{settings.API_V1_STR}/user", tags=["api-keys"])
app.include_router(plugin.router, prefix=f"{settings.API_V1_STR}/plugin", tags=["plugin"])
app.include_router(ws.router, prefix="/ws", tags=["websocket"])
app.include_router(billing.router, prefix=f"{settings.API_V1_STR}/billing", tags=["billing"])
app.include_router(admin.router, prefix=f"{settings.API_V1_STR}/admin", tags=["admin"])
app.include_router(admin_bypass.router, prefix=f"{settings.API_V1_STR}/admin/bypass", tags=["admin-bypass"])
app.include_router(bypass.router, prefix=f"{settings.API_V1_STR}/bypass", tags=["bypass"])

# Agent-Readiness: .well-known discovery endpoints (mounted at root, not under /api/v1)
app.include_router(discovery.router)

@app.get("/")
async def root(request: Request):
    link_header = '</.well-known/api-catalog>; rel="api-catalog", </.well-known/mcp.json>; rel="mcp-server-card"'
    accept = request.headers.get("accept", "")

    if "text/markdown" in accept:
        md_content = (
            "# MemWyre API\n\n"
            "Personal Knowledge Base & Memory Layer for AI Agents.\n\n"
            "## MCP Server\n\n"
            "Connect via Streamable HTTP at `https://server.memwyre.tech/mcp/`\n\n"
            "See [/.well-known/mcp.json](/.well-known/mcp.json) for full capabilities.\n\n"
            "## API Documentation\n\n"
            f"OpenAPI spec: [{settings.API_V1_STR}/openapi.json]({settings.API_V1_STR}/openapi.json)\n"
        )
        return PlainTextResponse(
            content=md_content,
            media_type="text/markdown",
            headers={"Link": link_header},
        )

    return JSONResponse(
        content={"message": "Welcome to MemWyre API", "status": "running"},
        headers={"Link": link_header},
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
