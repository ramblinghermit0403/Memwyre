import asyncio
from app.services.retrieval_service import RetrievalService

async def classify_and_verify(service, cid, query, expected, semaphore):
    async with semaphore:
        try:
            result = await service._classify_hop(query)
            status = "PASS" if result == expected else "FAIL"
            return (cid, query, expected, result, status)
        except Exception as e:
            return (cid, query, expected, f"ERROR: {e}", "FAIL")

async def run_tests():
    service = RetrievalService()
    
    filename = "router_dataset_v2.txt"
    try:
        with open(filename, "r") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    cases = []
    i = 0
    # Process 4 lines at a time
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
        cases.append((case_id, query, expected_hop))

    print(f"--- Testing Router on {len(cases)} queries (Parallel) ---")
    
    semaphore = asyncio.Semaphore(10)  # Limit concurrency to 10
    tasks = [classify_and_verify(service, c[0], c[1], c[2], semaphore) for c in cases]
    results = await asyncio.gather(*tasks)
    
    with open("router_results.txt", "w") as out:
        out.write(f"--- Router Verification Results ({len(cases)} queries) ---\n\n")
        
        failures = 0
        for cid, query, expected, result, status in results:
            out.write(f"[{status}] {cid}\n")
            out.write(f"  Query: {query}\n")
            out.write(f"  Exp: {expected}, Got: {result}\n\n")
            
            if status == "FAIL":
                failures += 1
                print(f"[{status}] {cid}") # Keep printing failures to console for quick feedback
        
        out.write(f"\nFinal Results: {len(cases) - failures}/{len(cases)} Passed\n")
        out.write(f"Total Failures: {failures}\n")
    
    print(f"\nResults saved to router_results.txt")
    print(f"Final Results: {len(cases) - failures}/{len(cases)} Passed")
    print(f"Total Failures: {failures}")

if __name__ == "__main__":
    asyncio.run(run_tests())
