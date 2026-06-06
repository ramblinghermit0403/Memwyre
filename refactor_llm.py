import os
import re

path = r"backend\app\services\llm_service_v2.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove Bedrock blocks
# A bedrock block typically looks like:
#        used_bedrock = False
#        try:
#             ...
#             used_bedrock = True
#        except Exception as e:
#             ...
#             pass
#        
#        if not used_bedrock:

# Using regex to remove the bedrock try-except block
pattern = re.compile(r"([ \t]*)used_bedrock\s*=\s*False\s*try:.*?except Exception as e:.*?pass\s*if not used_bedrock:", re.DOTALL)
content = pattern.sub(r"\1", content)

# 2. Replace gpt-3.5-turbo with gpt-4o-mini
content = content.replace("gpt-3.5-turbo", "gpt-4o-mini")

# 3. Replace instance name
content = content.replace("llm_service = LLMService()", "llm_service_v2 = LLMService()")

# 4. In generate_response, force provider
res_pattern = re.compile(r'(async def generate_response.*?:\n.*?\n.*?\n\s*pass)', re.DOTALL)
content = res_pattern.sub(r'\1\n        provider = "openai"\n        api_key = api_key or self.openai_api_key', content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done refactoring llm_service_v2.py")
