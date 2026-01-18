import re

def categorize(query):
    q = query.lower()
    
    # FACT rules
    # "is X married", "where does X live", "status", "job", "identity", "pets names"
    facts = ["relationship status", "identity", "pets names", "children names", "where does", "what is", "who is"]
    # Check if it looks like a stable state question
    # "What is Caroline's identity?" -> FACT
    if any(f in q for f in facts) and "when" not in q and "did" not in q:
        return "FACT"
    
    # MULTI_HOP rules
    # Explicit joins
    joins = ["before", "after", "since", "while", "during", "later", "then"]
    if any(j in q for j in joins):
        return "MULTI_HOP"
    
    # "How long" is usually Multi (temporal arithmetic)
    if "how long" in q:
        return "MULTI_HOP"
        
    # "How many times" -> Counts across chunks -> Multi? User said: "counts... -> EPISODIC_SINGLE"
    # Wait, user said "EPISODIC_SINGLE ... counts". 
    # But later examples: "How many times has X gone to Y across years?" -> MULTI.
    # "How many children...?" -> FACT/EPISODIC?
    # Let's stick to "How long" -> MULTI.
    # "How many times" -> EPISODIC (simple count) or MULTI (complex)?
    # User example for MULTI: "How many times has X gone to Y across years?"
    # Let's default "How many" to EPISODIC_SINGLE unless it has "across" or "years".
    
    # Events -> EPISODIC_SINGLE
    # "When did", "What did", "Where has"
    if "when did" in q or "what did" in q or "where has" in q or "which events" in q:
        return "EPISODIC_SINGLE"
        
    return "EPISODIC_SINGLE"

def process_file():
    with open("router_dataset_v2.txt", "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        
    with open("router_dataset_v3_strict.txt", "w") as out:
        i = 0
        while i < len(lines):
            if not lines[i].startswith("conv-"):
                i += 1
                continue
            
            if i+3 >= len(lines):
                break
                
            cid = lines[i]
            query = lines[i+2]
            status = lines[i+3]
            
            # Apply new strict categorization
            new_label = categorize(query)
            
            out.write(f"{cid}\n")
            out.write(f"{new_label}\n")
            out.write(f"{query}\n")
            out.write(f"{status}\n")
            
            i += 4

if __name__ == "__main__":
    process_file()
