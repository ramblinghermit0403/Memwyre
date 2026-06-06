"""Check what dimension Azure text-embedding-3-small produces."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from openai import AzureOpenAI
from app.core.config import settings

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://memwyre.cognitiveservices.azure.com/",
    api_key=settings.AZURE_OPENAI_API_KEY,
)

response = client.embeddings.create(
    input="test",
    model="text-embedding-3-small"
)

dim = len(response.data[0].embedding)
print(f"Embedding dimension: {dim}")
