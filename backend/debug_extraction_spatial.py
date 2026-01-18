import asyncio
from app.services.llm_service import llm_service
from datetime import datetime

async def test_extraction():
    test_text = "Caroline painted the painting on the beach on 29 dec."
    print(f"Input: {test_text}")
    
    # Use strict today for consistent relative date testing if needed, but here date is explicitish (29 Dec)
    facts = await llm_service.extract_facts_from_text(test_text, reference_date=datetime(2023, 12, 30))
    
    print("\nExtracted Facts:")
    found_location = False
    for f in facts:
        print(f" - [{f.get('valid_from')}] {f.get('subject')} {f.get('predicate')} {f.get('object')}")
        
        # Check if 'beach' is in object or predicate
        obj = f.get('object', '').lower()
        pred = f.get('predicate', '').lower()
        if 'beach' in obj or 'beach' in pred:
            found_location = True
            
    if found_location:
        print("\nSUCCESS: Location 'beach' preserved.")
    else:
        print("\nFAIL: Location 'beach' lost.")

if __name__ == "__main__":
    asyncio.run(test_extraction())
