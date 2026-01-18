import asyncio
from app.services.retrieval_service import RetrievalService

async def classify_and_verify(service, cid, query, expected, semaphore):
    async with semaphore:
        try:
            result = await service._classify_hop(query)
            # Map result back to 2-way for this dataset comparison if needed, 
            # OR better: Map expected from dataset to new labels.
            # Strategy: Map dataset "SINGLE" -> "EPISODIC_SINGLE", "MULTI" -> "MULTI_HOP"
            
            status = "PASS" if result == expected else "FAIL"
            
            # Allow FACT as a valid substitute for EPISODIC_SINGLE if the query was labeled SINGLE?
            # User said FACT is strict. Let's strict match first.
            if result == "FACT" and expected == "EPISODIC_SINGLE":
                 status = "FAIL (FACT)" # Interesting to note
                 
            return (cid, query, expected, result, status)
        except Exception as e:
            return (cid, query, expected, f"ERROR: {e}", "FAIL")

async def run_tests():
    service = RetrievalService()
    
    filename = "router_dataset_v3_strict.txt"
    try:
        with open(filename, "r") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    cases = []
    i = 0
    while i < len(lines):
        if not lines[i].startswith("conv-"):
            i += 1
            continue
            
        case_id = lines[i]
        expected_hop = lines[i+1] # Now strictly FACT, EPISODIC_SINGLE, or MULTI_HOP
        query = lines[i+2]
        i += 4
        
        cases.append((case_id, query, expected_hop))
        
    print(f"--- Testing Router (Tri-State Strict) on {len(cases)} queries (Parallel) ---")
    
    semaphore = asyncio.Semaphore(10)
    tasks = [classify_and_verify(service, c[0], c[1], c[2], semaphore) for c in cases]
    results = await asyncio.gather(*tasks)
    
    with open("router_results_tristate.txt", "w") as out:
        out.write(f"--- Router Verification Results (Tri-State) ---\n\n")
        
        failures = 0
        for cid, query, expected, result, status in results:
            out.write(f"[{status}] {cid}\n")
            out.write(f"  Query: {query}\n")
            out.write(f"  Exp: {expected}, Got: {result}\n\n")
            
            if status != "PASS":
                failures += 1
                print(f"[{status}] {cid}")
                print(f"  Query: {query}")
                print(f"  Exp: {expected}, Got: {result}")
        
        out.write(f"\nFinal Results: {len(cases) - failures}/{len(cases)} Passed\n")
        out.write(f"Total Failures: {failures}\n")
    
    print(f"\nResults saved to router_results_tristate.txt")
    print(f"Final Results: {len(cases) - failures}/{len(cases)} Passed")
    print(f"Total Failures: {failures}")

if __name__ == "__main__":
    asyncio.run(run_tests())
