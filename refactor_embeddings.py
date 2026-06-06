import os
import re

# 1. Update config.py
config_path = r"backend\app\core\config.py"
with open(config_path, "r", encoding="utf-8") as f:
    config_content = f.read()

if "AZURE_OPENAI_EMBEDDING_DEPLOYMENT" not in config_content:
    config_content = config_content.replace(
        'AZURE_OPENAI_DEPLOYMENT: str = "gpt-4o-mini"',
        'AZURE_OPENAI_DEPLOYMENT: str = "gpt-4o-mini"\n    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = "text-embedding-3-small"'
    )
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_content)


# 2. Update vector_store_v2.py
vs_path = r"backend\app\services\vector_store_v2.py"
with open(vs_path, "r", encoding="utf-8") as f:
    vs_content = f.read()

vs_content = vs_content.replace('vector_store = VectorStore()', 'vector_store_v2 = VectorStore()')
vs_content = vs_content.replace('self.bedrock_embeddings', 'self.embeddings')

embed_import = """            from langchain_aws import BedrockEmbeddings
            self.embeddings = BedrockEmbeddings(
                model_id="amazon.titan-embed-text-v2:0",
                region_name=os.getenv("AWS_REGION", "us-east-1")
            )
            logger.info("Initialized Bedrock Titan v2 Embeddings locally.")"""
new_embed = """            from langchain_openai import AzureOpenAIEmbeddings
            self.embeddings = AzureOpenAIEmbeddings(
                api_key=getattr(settings, "AZURE_OPENAI_API_KEY", getattr(settings, "OPENAI_API_KEY", "")),
                azure_endpoint=getattr(settings, "AZURE_OPENAI_ENDPOINT", "https://memwyre.cognitiveservices.azure.com/"),
                api_version=getattr(settings, "AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
                azure_deployment=getattr(settings, "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")
            )
            logger.info("Initialized Azure OpenAI Embeddings locally.")"""

vs_content = vs_content.replace(embed_import, new_embed)
vs_content = vs_content.replace("Bedrock embeddings not initialized", "Azure embeddings not initialized")
vs_content = vs_content.replace("Bedrock Async Embedding Failed", "Azure Async Embedding Failed")
vs_content = vs_content.replace("from langchain_aws import BedrockEmbeddings", "from langchain_openai import AzureOpenAIEmbeddings")

with open(vs_path, "w", encoding="utf-8") as f:
    f.write(vs_content)


# 3. Update ingestion_v2.py
ingest_path = r"backend\app\services\ingestion_v2.py"
with open(ingest_path, "r", encoding="utf-8") as f:
    ing_content = f.read()

ing_content = ing_content.replace('self.bedrock_embeddings', 'self.embeddings')
ing_content = ing_content.replace('Bedrock Batched Embedding failed', 'Azure Batched Embedding failed')
ing_content = ing_content.replace('from langchain_aws import BedrockEmbeddings', 'from langchain_openai import AzureOpenAIEmbeddings')

ing_embed_import = """            self.embeddings = BedrockEmbeddings(
                model_id="amazon.titan-embed-text-v2:0",
                region_name=os.getenv("AWS_REGION", "us-east-1")
            )"""
new_ing_embed = """            self.embeddings = AzureOpenAIEmbeddings(
                api_key=getattr(settings, "AZURE_OPENAI_API_KEY", getattr(settings, "OPENAI_API_KEY", "")),
                azure_endpoint=getattr(settings, "AZURE_OPENAI_ENDPOINT", "https://memwyre.cognitiveservices.azure.com/"),
                api_version=getattr(settings, "AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
                azure_deployment=getattr(settings, "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")
            )"""

ing_content = ing_content.replace(ing_embed_import, new_ing_embed)
with open(ingest_path, "w", encoding="utf-8") as f:
    f.write(ing_content)


# 4. Update imports in V2 files
v2_files = [
    r"backend\app\services\dedupe_job_v2.py",
    r"backend\app\services\retrieval_service_v2.py",
    r"backend\app\worker_v2.py",
    r"backend\app\services\ingestion_v2.py"
]

for fp in v2_files:
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("from app.services.vector_store import vector_store", "from app.services.vector_store_v2 import vector_store_v2 as vector_store")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)

print("Refactoring complete.")
