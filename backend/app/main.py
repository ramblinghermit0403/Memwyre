from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import auth, retrieval, llm, documents, memory, export, prompts, llm_api, inbox, user_keys, ws, settings as user_settings, feedback, chat_api, ingest, billing
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

    # Initialize MCP session manager (required for Streamable HTTP transport)
    if _mcp_server:
        async with _mcp_server.session_manager.run():
            yield  # App is running
    else:
        yield  # App is running without MCP

    # --- Shutdown (if needed) ---


app = FastAPI(
    title="MemWyre",
    description="Backend API for MemWyre - Personal Knowledge Base",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# CORS Configuration
# Note: allow_origins=["*"] + allow_credentials=True is invalid per CORS spec
# and causes WebSocket upgrades to be rejected with 403.
# When using wildcard, we use allow_origin_regex instead.
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
app.include_router(ws.router, prefix="/ws", tags=["websocket"])
app.include_router(billing.router, prefix=f"{settings.API_V1_STR}/billing", tags=["billing"])

# Mount MCP Server (Streamable HTTP) - MUST be LAST since mount("/") is a catch-all
# This allows remote connections (e.g. Cursor, Claude Desktop) via /mcp
if _mcp_server:
    # streamable_http_app() creates its own /mcp sub-route, so mount at root
    # Final endpoint: http://host:8000/mcp
    app.mount("/", _mcp_server.streamable_http_app())
    print("Mounted MCP Streamable HTTP Server at /mcp")


@app.get("/")
async def root():
    return {"message": "Welcome to MemWyre API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

