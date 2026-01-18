from botocore.config import Config

# Shared AWS Configuration
# Increase pool size to handle parallel embedding and LLM calls in worker
AWS_CONFIG = Config(
    max_pool_connections=50,
    retries={
        'max_attempts': 3,
        'mode': 'standard'
    }
)
