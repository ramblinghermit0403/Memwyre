import asyncio
from app.services.retrieval_service import RetrievalService

async def classify_and_report(service, cid, old_type, query, semaphore):
    async with semaphore:
        try:
            result = await service._classify_hop(query)
            return (cid, old_type, query, result)
        except Exception as e:
            return (cid, old_type, query, f"ERROR: {e}")

async def run_tests():
    service = RetrievalService()
    
    filename = "router_dataset_subset.txt"
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
        old_type = lines[i+1] 
        query = lines[i+2]
        i += 4
        
        cases.append((case_id, old_type, query))

    print(f"--- Router Classification Report ({len(cases)} queries) ---")
    
    semaphore = asyncio.Semaphore(10)
    tasks = [classify_and_report(service, c[0], c[1], c[2], semaphore) for c in cases]
    results = await asyncio.gather(*tasks)
    
    with open("router_subset_report.txt", "w") as out:
        out.write(f"ID | Original Label | Predicted Label | Query\n")
        out.write("-" * 80 + "\n")
        
        for cid, old_type, query, result in results:
            out.write(f"{cid} | {old_type} | {result} | {query}\n")
            print(f"{cid} [{old_type}] -> {result}")

    print(f"\nReport saved to router_subset_report.txt")

if __name__ == "__main__":
    asyncio.run(run_tests())
