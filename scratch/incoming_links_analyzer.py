import json

report_file = r"c:\Users\himan\OneDrive\Documents\brain_vault\scratch\seo_audit_results.json"

with open(report_file, "r", encoding="utf-8") as rf:
    data = json.load(rf)

# All indexable routes
routes = [
    "/", "/use-cases", "/pricing", "/privacy-policy", "/terms", "/connectors", 
    "/mcp", "/plugins", "/rag", "/memory-graph", "/personal", "/extension",
    "/blog", "/blog/mcp-persistent-memory", "/blog/cursor-vs-claude-code-context",
    "/blog/rag-vs-memory-long-term-knowledge", "/blog/vscode-mcp-persistent-memory",
    "/blog/claude-code-memory-ingestion", "/blog/openclaw-autonomous-memory",
    "/blog/state-of-ai-memory-2026", "/what-is-ai-memory", "/ai-memory-benchmark-locomo",
    "/research", "/memwyre-vs-mem0", "/memwyre-vs-supermemory", "/memwyre-vs-zep",
    "/chatgpt-memory", "/claude-memory", "/cursor-memory", "/mcp-memory",
    "/docs/", "/docs/use-cases/", "/docs/self-hosting/", "/docs/how-it-works/",
    "/docs/rag-vs-memory/", "/docs/benchmarks/", "/docs/security/", "/docs/integrations/",
    "/docs/integrations/browser-extension/", "/docs/integrations/cli-installer/",
    "/docs/integrations/connectors/", "/docs/integrations/mcp-server/",
    "/docs/integrations/mcp-server/claude/", "/docs/integrations/mcp-server/cursor/",
    "/docs/integrations/mcp-server/vscode/", "/docs/integrations/plugins/claude/",
    "/docs/integrations/plugins/openclaw/"
]

in_links = {r: 0 for r in routes}
in_link_sources = {r: [] for r in routes}

# Traverse all links in all pages
for page in data.get("pages", []):
    source_route = page["route"]
    for link in page.get("links", []):
        url = link["url"]
        
        # Normalize relative links for resolving
        if not url.startswith("/") and not url.startswith("http") and not url.startswith("#") and not url.startswith("mailto") and not url.startswith("tel"):
            # Resolve relative
            if source_route.startswith("/docs/"):
                base = source_route
            elif source_route.startswith("/blog/") and source_route != "/blog":
                base = "/blog/"
            else:
                base = "/"
            import urllib.parse
            url = urllib.parse.urljoin(base, url)
            
        path = url.split("?")[0].split("#")[0]
        
        # Check standard normalized variations
        if path.startswith("https://memwyre.tech"):
            path = path.replace("https://memwyre.tech", "")
            
        if path in in_links:
            in_links[path] += 1
            in_link_sources[path].append(source_route)
        elif path + "/" in in_links:
            in_links[path + "/"] += 1
            in_link_sources[path + "/"].append(source_route)
        elif path.endswith("/") and path[:-1] in in_links:
            in_links[path[:-1]] += 1
            in_link_sources[path[:-1]].append(source_route)

print("\n--- INCOMING LINK COUNTS FOR PAGES ---")
orphaned = []
one_link = []
others = []

for r in routes:
    cnt = in_links[r]
    sources = list(set(in_link_sources[r]))
    if cnt == 0:
        orphaned.append((r, cnt, sources))
    elif cnt == 1:
        one_link.append((r, cnt, sources))
    else:
        others.append((r, cnt, sources))

print(f"\nOrphaned pages (0 in-links) [{len(orphaned)}]:")
for r, cnt, src in sorted(orphaned):
    print(f"  - {r}")

print(f"\nPages with only one in-link [{len(one_link)}]:")
for r, cnt, src in sorted(one_link):
    print(f"  - {r} (Linked from: {src})")

print(f"\nWell linked pages [{len(others)}]:")
for r, cnt, src in sorted(others):
    print(f"  - {r} ({cnt} in-links)")
