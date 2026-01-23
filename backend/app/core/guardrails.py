import re
from fastapi import HTTPException

# Basic Guardrails
class GuardRails:
    def __init__(self):
        # Allow listing risky terms to block
        self.blocked_terms = [
            # "ignore all previous instructions", # Prompt injection common phrase
            # "system prompt",
        ]
        
    def validate_input(self, text: str):
        """
        Validate input for safety and constraints.
        """
        if len(text) > 10000:
             raise HTTPException(status_code=400, detail="Input text too long (max 10000 chars)")
             
        # Check for injection patterns (Basic)
        lower_text = text.lower()
        for term in self.blocked_terms:
            if term in lower_text:
                raise HTTPException(status_code=400, detail="Input contains blocked terms.")
                
        return True

    def validate_output(self, text: str):
        """
        Validate output (if needed).
        """
        return True

guardrails = GuardRails()
