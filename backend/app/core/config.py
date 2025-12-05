from pydantic_settings import BaseSettings

import os

# Database
# Use absolute path to ensure it works regardless of CWD (e.g. when run from Claude Desktop)
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Brain Vault"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "YOUR_SECRET_KEY_HERE"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = f"sqlite:///{os.path.join(BASE_DIR, 'brain_vault.db')}"
    
    # Vector DB
    CHROMA_DB_PATH: str = os.path.join(BASE_DIR, "chroma_db")

    # LLM Keys
    OPENAI_API_KEY: str = "OPENAI_API_KEY"
    GEMINI_API_KEY: str = "GEMINI_API_KEY"
    
    class Config:
        env_file = ".env"

settings = Settings()
