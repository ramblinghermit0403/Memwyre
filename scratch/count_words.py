import os
import re

FILES = [
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\src\views\products\ConnectorsView.vue",
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\src\views\products\McpView.vue",
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\src\views\products\PluginsView.vue",
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\src\views\products\MemoryGraphView.vue",
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\docs\integrations\mcp-server\claude.md",
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\docs\integrations\mcp-server\cursor.md",
    r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\docs\integrations\mcp-server\vscode.md"
]

def count_words(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return 0
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Strip HTML tags
    clean_html = re.sub(r"<[^>]+>", " ", content)
    # Strip frontmatter
    if filepath.endswith(".md") and clean_html.startswith("---"):
        parts = clean_html.split("---", 2)
        if len(parts) >= 3:
            clean_html = parts[2]
            
    # Extract words
    words = re.findall(r"\b\w+\b", clean_html)
    return len(words)

for fp in FILES:
    count = count_words(fp)
    status = "PASS" if count >= 500 else "FAIL"
    print(f"[{status}] {os.path.basename(fp)}: {count} words")
