from langchain_openai import AzureOpenAIEmbeddings

try:
    embeddings = AzureOpenAIEmbeddings(
        api_key="",
        azure_endpoint="https://fake.cognitiveservices.azure.com/",
        api_version="2023-05-15",
        azure_deployment="text-embedding-3-small"
    )
    print("Success with empty api_key")
except Exception as e:
    print(f"Exception with empty api_key: {e}")
