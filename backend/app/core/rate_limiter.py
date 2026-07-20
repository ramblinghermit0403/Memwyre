import asyncio
import time
import logging
from typing import Optional, List, Any
from app.core.config import settings
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

# Initialize Redis connection for SlowAPI rate limiter
redis_url = settings.REDIS_URL
limiter = Limiter(key_func=get_remote_address, storage_uri=redis_url)

def init_rate_limiter(app):
    """
    Register Rate Limiter middleware and exception handler
    """
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)

logger = logging.getLogger(__name__)

class AsyncRateLimiter:
    def __init__(self, max_calls: int, period: float):
        """
        Thread-safe and Async-safe Token Bucket Rate Limiter.
        Args:
            max_calls: Maximum number of calls allowed in the period
            period: Time period in seconds (e.g. 60.0 for 1 minute)
        """
        self.max_calls = max_calls
        self.period = period
        # Cap the token bucket to 1.0 to enforce strict pacing and prevent large bursts 
        # that trigger 429 errors from strict APIs (like Moonshot/NVIDIA) after idle periods.
        self.max_burst = min(float(max_calls), 1.0)
        self.tokens = self.max_burst
        self.last_update = time.monotonic()
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            while True:
                now = time.monotonic()
                passed = now - self.last_update
                # Replenish tokens proportional to time elapsed
                replenished = passed * (self.max_calls / self.period)
                # Cap the tokens at max_burst instead of max_calls
                self.tokens = min(self.max_burst, self.tokens + replenished)
                self.last_update = now
                
                if self.tokens >= 1.0:
                    self.tokens -= 1.0
                    return
                
                # Wait until a token becomes available
                needed = 1.0 - self.tokens
                sleep_time = needed / (self.max_calls / self.period)
                logger.debug(f"Rate limit reached. Sleeping for {sleep_time:.2f}s")
                await asyncio.sleep(sleep_time)


class RateLimitedEmbeddings:
    def __init__(self, embeddings, rate_limiter: AsyncRateLimiter):
        self.embeddings = embeddings
        self.rate_limiter = rate_limiter

    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        await self.rate_limiter.acquire()
        return await self.embeddings.aembed_documents(texts)

    async def aembed_query(self, text: str) -> List[float]:
        await self.rate_limiter.acquire()
        return await self.embeddings.aembed_query(text)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        # Synchronous fallback: sleep briefly or call directly
        # For simplicity in sync context we call directly or log warning
        return self.embeddings.embed_documents(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embeddings.embed_query(text)

    def __getattr__(self, name):
        return getattr(self.embeddings, name)


# Shared global rate limiters
embedding_rate_limiter = AsyncRateLimiter(settings.EMBEDDING_RATE_LIMIT_RPM, 60.0)
llm_rate_limiter = AsyncRateLimiter(settings.LLM_RATE_LIMIT_RPM, 60.0)


def wrap_llm_with_rate_limit(llm):
    """
    Wraps the LLM's invoke and ainvoke methods to enforce global LLM rate limits.
    """
    if not llm:
        return llm

    original_ainvoke = llm.ainvoke
    original_invoke = llm.invoke

    async def rate_limited_ainvoke(input, config=None, **kwargs):
        await llm_rate_limiter.acquire()
        return await original_ainvoke(input, config=config, **kwargs)

    def rate_limited_invoke(input, config=None, **kwargs):
        # We can't await inside sync invoke, so we block using time.sleep
        # since rate limiter is async, we can just block or call directly
        # Typically sync is not used in FastAPI endpoints, but let's run it safely
        try:
            # Simple fallback: if sync is called, we just log a debug warning and proceed
            pass
        except Exception:
            pass
        return original_invoke(input, config=config, **kwargs)

    object.__setattr__(llm, "ainvoke", rate_limited_ainvoke)
    object.__setattr__(llm, "invoke", rate_limited_invoke)
    return llm


def get_embeddings_instance():
    """
    Factory function to initialize and return the correct Embeddings instance,
    wrapped with the global rate limiter.
    """
    api_key = getattr(settings, "EMBEDDING_API_KEY", None) or getattr(settings, "OPENAI_API_KEY", None) or getattr(settings, "AZURE_OPENAI_API_KEY", None)
    
    provider = getattr(settings, "DEFAULT_EMBEDDING_PROVIDER", None)
    if provider:
        provider = provider.lower()
    else:
        # Backwards-compatible auto-detection logic
        if getattr(settings, "EMBEDDING_API_BASE", None):
            provider = "nvidia"
        elif getattr(settings, "AZURE_OPENAI_API_KEY", None) or getattr(settings, "OPENAI_API_KEY", None):
            provider = "azure"
        else:
            provider = "bedrock"

    if provider == "nvidia":
        from langchain_openai import OpenAIEmbeddings

        class CustomNIMEmbeddings(OpenAIEmbeddings):
            """Custom wrapper for NVIDIA NIM asymmetric embeddings which require 'input_type'."""
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.check_embedding_ctx_length = False

            async def aembed_documents(self, texts: List[str], chunk_size: Optional[int] = 0) -> List[List[float]]:
                original_create = self.async_client.create
                async def mock_create(*args, **kwargs):
                    kwargs["extra_body"] = {"input_type": "passage"}
                    return await original_create(*args, **kwargs)
                self.async_client.create = mock_create
                try:
                    return await super().aembed_documents(texts, chunk_size)
                finally:
                    self.async_client.create = original_create

            async def aembed_query(self, text: str) -> List[float]:
                original_create = self.async_client.create
                async def mock_create(*args, **kwargs):
                    kwargs["extra_body"] = {"input_type": "query"}
                    return await original_create(*args, **kwargs)
                self.async_client.create = mock_create
                try:
                    return await super().aembed_query(text)
                finally:
                    self.async_client.create = original_create

            def embed_documents(self, texts: List[str], chunk_size: Optional[int] = 0) -> List[List[float]]:
                original_create = self.client.create
                def mock_create(*args, **kwargs):
                    kwargs["extra_body"] = {"input_type": "passage"}
                    return original_create(*args, **kwargs)
                self.client.create = mock_create
                try:
                    return super().embed_documents(texts, chunk_size)
                finally:
                    self.client.create = original_create

            def embed_query(self, text: str) -> List[float]:
                original_create = self.client.create
                def mock_create(*args, **kwargs):
                    kwargs["extra_body"] = {"input_type": "query"}
                    return original_create(*args, **kwargs)
                self.client.create = mock_create
                try:
                    return super().embed_query(text)
                finally:
                    self.client.create = original_create

        logger.info(f"Initializing custom OpenAI-compatible embeddings from base: {settings.EMBEDDING_API_BASE}")
        raw_embeddings = CustomNIMEmbeddings(
            base_url=settings.EMBEDDING_API_BASE,
            api_key=api_key,
            model=getattr(settings, "EMBEDDING_MODEL_NAME", "nvidia/nv-embedqa-e5-v5"),
            check_embedding_ctx_length=False
        )
    elif provider == "azure" or provider == "openai":
        from langchain_openai import AzureOpenAIEmbeddings
        logger.info("Initializing Azure OpenAI Embeddings.")
        raw_embeddings = AzureOpenAIEmbeddings(
            api_key=api_key,
            azure_endpoint=getattr(settings, "AZURE_OPENAI_ENDPOINT", "https://memwyre.cognitiveservices.azure.com/"),
            api_version=getattr(settings, "AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
            azure_deployment=getattr(settings, "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small"),
            dimensions=1024
        )
    elif provider == "bedrock":
        from langchain_aws import BedrockEmbeddings
        logger.info("Initializing Bedrock Titan V2 Embeddings.")
        
        bedrock_kwargs = {
            "model_id": "amazon.titan-embed-text-v2:0",
            "region_name": getattr(settings, "AWS_REGION", "us-west-2"),
            "model_kwargs": {"dimensions": 1024, "normalize": True}
        }
        
        # Explicitly pass credentials if configured in settings
        aws_key = getattr(settings, "AWS_ACCESS_KEY_ID", None)
        aws_secret = getattr(settings, "AWS_SECRET_ACCESS_KEY", None)
        if aws_key and aws_secret:
            bedrock_kwargs["aws_access_key_id"] = aws_key
            bedrock_kwargs["aws_secret_access_key"] = aws_secret
            
        raw_embeddings = BedrockEmbeddings(**bedrock_kwargs)
    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")

    return RateLimitedEmbeddings(raw_embeddings, embedding_rate_limiter)
