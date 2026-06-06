from app.core.config import settings
print(f"AZURE_OPENAI_API_KEY: {'[SET]' if settings.AZURE_OPENAI_API_KEY else '[MISSING]'}")
print(f"OPENAI_API_KEY: {'[SET]' if settings.OPENAI_API_KEY else '[MISSING]'}")
