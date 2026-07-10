"""Test Azure OpenAI chat completion directly."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.core.config import settings

from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://memwyre.cognitiveservices.azure.com/",
    api_key=settings.AZURE_OPENAI_API_KEY,
)

# Try the deployment name from .env
deployment = settings.AZURE_OPENAI_DEPLOYMENT
print(f"Testing deployment: '{deployment}'")

try:
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": "Say hello in one word."}],
        max_tokens=10,
    )
    print(f"SUCCESS! Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"FAILED with deployment '{deployment}': {e}")

# Also try common alternative names
for alt in ["gpt-4o-mini", "gpt4o-mini", "gpt-4o-mini-deployment"]:
    if alt == deployment:
        continue
    try:
        response = client.chat.completions.create(
            model=alt,
            messages=[{"role": "user", "content": "Say hello in one word."}],
            max_tokens=10,
        )
        print(f"SUCCESS with '{alt}'! Response: {response.choices[0].message.content}")
        break
    except Exception as e:
        print(f"FAILED with '{alt}': {type(e).__name__}")
