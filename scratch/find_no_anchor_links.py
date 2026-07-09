import os
from bs4 import BeautifulSoup

FRONTEND_DIR = r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend"

no_anchor_links = []

def scan_file(filepath):
    if not filepath.endswith(".vue") and not filepath.endswith(".md"):
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, "html.parser")
    for idx, a in enumerate(soup.find_all("a")):
        # Get text content
        text = a.get_text().strip()
        aria_label = a.get("aria-label") or a.get(":aria-label")
        href = a.get("href") or a.get(":href") or a.get("to") or a.get(":to")
        
        # If text is empty, check if there's an image with alt text
        has_alt = False
        images = a.find_all("img")
        for img in images:
            alt = img.get("alt") or img.get(":alt")
            if alt and alt.strip():
                has_alt = True
                
        # If no text, no aria-label, and no alt text on images, it has no anchor text
        if not text and not aria_label and not has_alt and href:
            # Find approximate line number
            lines = content.split("\n")
            line_num = 0
            href_str = str(href)
            for l_idx, line in enumerate(lines):
                if href_str in line:
                    line_num = l_idx + 1
                    break
            
            no_anchor_links.append({
                "file": os.path.relpath(filepath, FRONTEND_DIR),
                "line": line_num,
                "href": href,
                "html": str(a)[:100]
            })

for root, dirs, files in os.walk(os.path.join(FRONTEND_DIR, "src")):
    for f in files:
        scan_file(os.path.join(root, f))

for root, dirs, files in os.walk(os.path.join(FRONTEND_DIR, "docs")):
    if ".vitepress" in root or "cache" in root:
        continue
    for f in files:
        scan_file(os.path.join(root, f))

print(f"Found {len(no_anchor_links)} links with no anchor text:")
for item in no_anchor_links:
    print(f"File: {item['file']}:{item['line']} | target: {item['href']} | html: {item['html']}")
