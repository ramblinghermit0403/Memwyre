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
            
        if not context:
            return "I couldn't find any relevant information in your Brain Vault to answer that. Please try adding more memories or documents related to your specific question."

        context_str = "\n\n".join(context)
        system_prompt = (
            "You are the Brain Vault AI, a personal knowledge assistant. "
            "Use ONLY the following Context to answer the user's question. "
            "If the answer is not explicitly supported by the Context, state that you do not have enough information. "
            "Do not hallucinate or use outside knowledge unless it is general definitions to help explain the context.\n\n"
            f"Context:\n{context_str}"
        )
        
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
