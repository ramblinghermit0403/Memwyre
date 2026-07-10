"""Check if langchain AzureOpenAIEmbeddings supports dimensions param."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.core.config import settings

from langchain_openai import AzureOpenAIEmbeddings

embed = AzureOpenAIEmbeddings(
    api_key=settings.AZURE_OPENAI_API_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version="2024-12-01-preview",
    azure_deployment="text-embedding-3-small",
    dimensions=512
)

import asyncio
result = asyncio.run(embed.aembed_query("test"))
print(f"Dimension with dimensions=512: {len(result)}")
