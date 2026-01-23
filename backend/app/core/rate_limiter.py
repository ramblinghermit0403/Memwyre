from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.core.config import settings
import redis

# Initialize Redis connection
# We can use the same Redis instance as Celery
redis_url = settings.REDIS_URL

# Create Limiter instance
# key_func=get_remote_address uses the IP address of the client
limiter = Limiter(key_func=get_remote_address, storage_uri=redis_url)

def init_rate_limiter(app):
    """
    Register Rate Limiter middleware and exception handler
    """
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)
