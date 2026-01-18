
import asyncio
import sys
import os
from datetime import datetime

# Add backend to path
sys.path.append(os.getcwd())

from app.services.llm_service import llm_service

async def main():
    # Simulate the scenario
    # Conversation Date: 8th May 2023
    ref_date = datetime(2023, 5, 8, 12, 0, 0) # Noon
    
    text = "Caroline attended the lgbtq event yesterday."
    
    print(f"--- Testing Date Resolution ---")
    print(f"Reference Date: {ref_date}")
    print(f"Text: '{text}'")
    
    facts = await llm_service.extract_facts_from_text(text, reference_date=ref_date)
    
    for f in facts:
        print(f"Fact: {f.get('subject')} {f.get('predicate')} {f.get('object')}")
        print(f"Valid From: {f.get('valid_from')}")
        
        # Check correctness
        v_from = f.get('valid_from')
        if "2023-05-07" in str(v_from):
             print("RESULT: CORRECT (May 7th)")
        elif "2023-05-06" in str(v_from):
             print("RESULT: FAILURE (May 6th - Off by one!)")
        else:
             print(f"RESULT: UNEXPECTED ({v_from})")

if __name__ == "__main__":
    asyncio.run(main())
