from langchain_openai import AzureOpenAIEmbeddings

try:
    embeddings = AzureOpenAIEmbeddings(
        api_key="fake-key",
        azure_endpoint="https://fake.cognitiveservices.azure.com/",
        api_version="2023-05-15",
        azure_deployment="text-embedding-3-small"
    )
    print("Success with api_version")
except Exception as e:
    import traceback
    traceback.print_exc()

try:
    embeddings = AzureOpenAIEmbeddings(
        api_key="fake-key",
        azure_endpoint="https://fake.cognitiveservices.azure.com/",
        openai_api_version="2023-05-15",
        azure_deployment="text-embedding-3-small"
    )
    print("Success with openai_api_version")
except Exception as e:
    import traceback
    traceback.print_exc()
