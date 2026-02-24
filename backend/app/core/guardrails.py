import re
from fastapi import HTTPException

# Basic Guardrails
class GuardRails:
    def __init__(self):
        # Compiled regex patterns for fast matching against common injection techniques
        self.injection_patterns = [
            re.compile(r"ignore\s+(all\s+)?previous\s+(instructions|directives|prompts)", re.IGNORECASE),
            re.compile(r"disregard\s+(all\s+)?previous", re.IGNORECASE),
            re.compile(r"you\s+are\s+now\s+(a\s+)?(dan|developer|unrestricted|god)", re.IGNORECASE),
            re.compile(r"(reveal|print|show|output)\s+(your\s+)?(system\s+prompt|initial\s+instructions|core\s+directives)", re.IGNORECASE),
            re.compile(r"forget\s+(everything|all\s+rules|your\s+instructions)", re.IGNORECASE),
            re.compile(r"do\s+anything\s+now", re.IGNORECASE)
        ]
        
    def validate_input(self, text: str):
        """
        Validate input for safety and constraints.
        """
        if len(text) > 10000:
             raise HTTPException(status_code=400, detail="Input text too long (max 10000 chars)")
             
        # Check against injection regex patterns
        for pattern in self.injection_patterns:
            if pattern.search(text):
                raise HTTPException(status_code=400, detail="Input violates safety policy (Injection detected).")
                
        return True

    def validate_output(self, text: str):
        """
        Validate output (if needed).
        """
        return True

guardrails = GuardRails()
