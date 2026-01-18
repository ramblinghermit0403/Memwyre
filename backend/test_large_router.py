import asyncio
from app.services.retrieval_service import RetrievalService

async def run_tests():
    service = RetrievalService()
    
    with open("router_dataset.txt", "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        
    # Dataset format:
    # ID
    # Type
    # Query
    # Status (ignored)
    
    # Parse into (Query, ExpectedType)
    cases = []
    i = 0
    while i < len(lines):
        if not lines[i].startswith("conv-"):
            i += 1
            continue
            
        case_id = lines[i]
        case_type = lines[i+1].lower()
        query = lines[i+2]
        # Skip status line
        i += 4
        
        expected_hop = "SINGLE" if "single" in case_type else "MULTI"
        cases.append((case_id, query, expected_hop, case_type))

    print(f"--- Testing Router on {len(cases)} queries ---")
    
    failures = 0
    for cid, query, expected, ctype in cases:
        try:
            # Check if it's async
            if asyncio.iscoroutinefunction(service._classify_hop):
                result = await service._classify_hop(query)
            else:
                result = service._classify_hop(query)
        except Exception as e:
            result = f"ERROR: {e}"
            
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL": 
            failures += 1
            print(f"[{status}] {cid} ({ctype})")
            print(f"  Query: {query}")
            print(f"  Exp: {expected}, Got: {result}")
        else:
            # print(f"[PASS] {cid}")
            pass
            
    print(f"\nFinal Results: {len(cases) - failures}/{len(cases)} Passed")
    print(f"Total Failures: {failures}")

if __name__ == "__main__":
    asyncio.run(run_tests())
