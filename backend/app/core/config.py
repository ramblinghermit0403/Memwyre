from pydantic_settings import BaseSettings, SettingsConfigDict

import os
import warnings
from typing import List, Optional

# Database
# Use absolute path to ensure it works regardless of CWD (e.g. when run from Claude Desktop)
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Settings(BaseSettings):
    PROJECT_NAME: str = "MemWyre"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "YOUR_SECRET_KEY_HERE"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    
    # CORS — comma-separated origins, or "*" for dev
    CORS_ORIGINS: str = "*"

    @property
    def cors_origin_list(self) -> List[str]:
        """Parse CORS_ORIGINS into a list."""
        if self.CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]

    # Auth Overrides
    ADMIN_EMAILS: str = ""
    WHITELISTED_DOMAINS: str = ""

    @property
    def admin_email_list(self) -> List[str]:
        return [e.strip().lower() for e in self.ADMIN_EMAILS.split(",") if e.strip()]

    @property
    def whitelisted_domain_list(self) -> List[str]:
        return [d.strip().lower() for d in self.WHITELISTED_DOMAINS.split(",") if d.strip()]
    
    # AWS Services
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_REGION: str = "us-east-1"
    AWS_SES_SENDER_EMAIL: Optional[str] = None

    # Cloudflare Turnstile
    TURNSTILE_SECRET_KEY: Optional[str] = None

    # YouTube Proxy (for bypassing IP bans on cloud servers)
    YOUTUBE_PROXY_URL: Optional[str] = None

    # Database
    # Default to sqlite if not set in .env
    DATABASE_URL: Optional[str] = None
    
    @property
    def assemble_db_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"sqlite:///{os.path.join(BASE_DIR, 'brain_vault.db')}"
    
    # Vector DB (Pinecone)
    PINECONE_API_KEY: str = ""
    PINECONE_ENV: str = "gcp-starter"
    PINECONE_HOST: str = ""

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    REDIS_URL: str = "redis://localhost:6379/0"

    # LLM Keys
    OPENAI_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    GEMINI_API_KEY: Optional[str] = None

    # OAuth
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GITHUB_CLIENT_ID: Optional[str] = None
    GITHUB_CLIENT_SECRET: Optional[str] = None
    FRONTEND_URL: str = "http://localhost:5173"
    BACKEND_URL: str = "http://localhost:8000"

    # Retrieval Config
    ENABLE_BM25_FILTER: bool = True
    MAX_DAILY_TOKENS: int = 100_000
    
    # Dual Index Support
    PINECONE_SPARSE_HOST: Optional[str] = None

    # Dodo Payments
    DODO_PAYMENTS_API_KEY: Optional[str] = None
    DODO_WEBHOOK_SECRET: Optional[str] = None
    DODO_PRODUCT_ID: Optional[str] = None
    DODO_ENVIRONMENT: str = "test_mode"  # "test_mode" or "live_mode"

    # Feature Gating
    DEV_MODE: bool = False  # True = bypass all subscription checks
    FREE_MEMORY_LIMIT: int = 0
    FREE_DOCUMENT_LIMIT: int = 0
    FREE_CHAT_LIMIT: int = 0
    MAX_CHARS_PER_MEMORY: int = 25000
    MAX_CHARS_PER_DOC_FREE: int = 0
    MAX_CHARS_PER_DOC_PRO: int = 500000

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        extra="ignore"
    )

settings = Settings()

# Warn if default secret key is in use
if settings.SECRET_KEY == "YOUR_SECRET_KEY_HERE":
    warnings.warn(
        "⚠️  Using default SECRET_KEY — set a strong SECRET_KEY in .env for production!",
        stacklevel=2,
    )
