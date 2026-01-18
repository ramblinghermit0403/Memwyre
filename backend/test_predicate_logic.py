import asyncio
import sys
import os

# Ensure backend directory is in path
sys.path.append(os.getcwd())

from app.services.retrieval_service import retrieval_service

async def test_logic():
    output_lines = []
    
    def log(msg):
        print(msg)
        output_lines.append(str(msg))

    from app.services.llm_service import llm_service
    log(f"API Key present: {bool(llm_service.api_key)}")
    if llm_service.api_key:
         log(f"API Key start: {llm_service.api_key[:4]}...")

    log("--- Testing Hop Classification ---")
    single_hop_q = "Where do I live?"
    multi_hop_q = "Who replaced the CEO and then resigned?"
    
    log(f"Query: '{single_hop_q}' -> Hop: {retrieval_service._classify_hop(single_hop_q)}")
    log(f"Query: '{multi_hop_q}' -> Hop: {retrieval_service._classify_hop(multi_hop_q)}")
    
    log("\n--- Testing Predicate Extraction (Rule-Based) ---")
    queries = [
        ("Where do I live?", "lives_in"),
        ("Who is my employer?", "works_at"),
        ("Where was I born?", "born_in"),
        ("Who am I married to?", "married_to"),
        ("What job do I have?", "job_title"),
        ("Where did I move to?", "moved_to"),
        ("Who is my friend?", "friends_with"),
        ("What do I own?", "owns"),
        ("What did I achieve?", "achieved"),
        ("When did I join?", "joined"),
        ("When did I leave?", "left"),
        ("Where am I from?", "from"),
        ("Where is it located?", "located_in"),
        ("Who is my partner?", "partner_of")
    ]
    
    for q, expected in queries:
        preds = await retrieval_service._extract_predicates(q)
        log(f"Query: '{q}' -> Predicates: {preds}")
        # Relaxed check since some return multiple
        if expected in preds:
             log(f"  [PASS] Found '{expected}'")
        else:
             log(f"  [FAIL] Expected '{expected}'")

    log("\n--- Testing Predicate Extraction (LLM Fallback) ---")
    # A query that shouldn't match simple keywords but implies a predicate
    # "Where do I hang my hat?" -> implies residence -> lives_in
    llm_q = "Where do I sleep at night?" 
    log(f"Query: '{llm_q}'")
    
    # DEBUG: Call generate_predicate directly - REMOVED
    preds = await retrieval_service._extract_predicates(llm_q)
    log(f"  -> Predicates: {preds}")

    preds = await retrieval_service._extract_predicates(llm_q)
    log(f"  -> Predicates: {preds}")
    
    if "lives_in" in preds:
    # ... rest of file
        log("  [PASS] LLM correctly identified 'lives_in'")
    else:
        log("  [WARN] LLM might not have identified 'lives_in' or returned something else.")
        
    with open("verification_results.log", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    asyncio.run(test_logic())
