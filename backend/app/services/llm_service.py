from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import google.generativeai as genai
from app.core.config import settings

class LLMService:
    def __init__(self):
        # Initialize with dummy key if not present to avoid startup error, 
        # but requests will fail if key is missing.
        self.openai_api_key = "OPENAI_API_KEY" 
        # In a real app, we'd fetch from settings or user input.
        
    async def generate_response(self, query: str, context: List[str], provider: str = "openai", api_key: Optional[str] = None) -> str:
        if not api_key:
            return "Error: API Key is required."

        context_str = "\n\n".join(context)
        system_prompt = f"You are a helpful assistant. Use the following context to answer the user's question.\n\nContext:\n{context_str}"
        
        if provider == "openai":
            try:
                llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")
                messages = [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=query)
                ]
                response = await llm.ainvoke(messages)
                return response.content
            except Exception as e:
                return f"OpenAI Error: {str(e)}"

        elif provider == "gemini":
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                prompt = f"{system_prompt}\n\nUser Question: {query}"
                
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                return f"Gemini Error: {str(e)}"

        elif provider == "claude":
            # Placeholder for Claude integration
            return "Claude integration not yet implemented."
        else:
            return "Unsupported provider."

llm_service = LLMService()
