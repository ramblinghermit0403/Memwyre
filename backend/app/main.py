from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import auth, retrieval, llm, documents, memory, export, prompts, llm_api, inbox, user_keys, ws, settings as user_settings
from app.db.base import Base
from app.db.session import engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for AI Brain Vault - Personal Knowledge Base",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(retrieval.router, prefix=f"{settings.API_V1_STR}/retrieval", tags=["retrieval"])
app.include_router(llm.router, prefix=f"{settings.API_V1_STR}/llm", tags=["llm"])
app.include_router(documents.router, prefix=f"{settings.API_V1_STR}/documents", tags=["documents"])
app.include_router(memory.router, prefix=f"{settings.API_V1_STR}/memory", tags=["memory"])
app.include_router(export.router, prefix=f"{settings.API_V1_STR}/export", tags=["export"])
app.include_router(prompts.router, prefix=f"{settings.API_V1_STR}/prompts", tags=["prompts"])
app.include_router(llm_api.router, prefix=f"{settings.API_V1_STR}/llm", tags=["llm-api"])
app.include_router(inbox.router, prefix=f"{settings.API_V1_STR}/inbox", tags=["inbox"])
app.include_router(user_keys.router, prefix=f"{settings.API_V1_STR}/user", tags=["user-keys"])
app.include_router(user_settings.router, prefix=f"{settings.API_V1_STR}/user", tags=["user-settings"])
app.include_router(ws.router, prefix="/ws", tags=["websocket"])

@app.on_event("startup")
async def startup_event():
    # Start background tasks
    from app.services.dedupe_job import dedupe_service
    from app.db.session import SessionLocal
    import asyncio
    
    # We run it as a background task
    asyncio.create_task(dedupe_service.run_periodic_check(SessionLocal))

@app.get("/")
async def root():
    return {"message": "Welcome to AI Brain Vault API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
