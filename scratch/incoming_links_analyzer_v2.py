import os
import re
import urllib.parse
from bs4 import BeautifulSoup

FRONTEND_DIR = r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend"
SRC_DIR = os.path.join(FRONTEND_DIR, "src")
DOCS_DIR = os.path.join(FRONTEND_DIR, "docs")
BLOG_DIR = os.path.join(SRC_DIR, "assets", "blog")

ROUTES = [
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

in_links = {r: 0 for r in ROUTES}
in_link_sources = {r: [] for r in ROUTES}

def add_link(source_route, link_url):
    if not link_url or link_url == "None":
        return
        
    # Ignore absolute links that aren't ours, mailto, tel, hashes
    if link_url.startswith("mailto:") or link_url.startswith("tel:") or link_url.startswith("#"):
        return
        
    parsed = urllib.parse.urlparse(link_url)
    if parsed.scheme and parsed.netloc:
        if "memwyre.tech" in parsed.netloc:
            link_url = parsed.path
        else:
            return
            
    # Resolve relative links
    if not link_url.startswith("/"):
        if source_route.startswith("/docs/"):
            base = source_route
        elif source_route.startswith("/blog/") and source_route != "/blog":
            base = "/blog/"
        else:
            base = "/"
        link_url = urllib.parse.urljoin(base, link_url)
        
    path = link_url.split("?")[0].split("#")[0]
    
    # Check match in routes
    if path in in_links:
        in_links[path] += 1
        in_link_sources[path].append(source_route)
    elif path + "/" in in_links:
        in_links[path + "/"] += 1
        in_link_sources[path + "/"].append(source_route)
    elif path.endswith("/") and path[:-1] in in_links:
        in_links[path[:-1]] += 1
        in_link_sources[path[:-1]].append(source_route)
    elif path.startswith("/blog/") and path.count("/") == 2:
        # Dynamic blog routes
        in_links.setdefault(path, 0)
        in_link_sources.setdefault(path, [])
        in_links[path] += 1
        in_link_sources[path].append(source_route)

# 1. Parse Docs Markdown files
for root, dirs, filenames in os.walk(DOCS_DIR):
    if ".vitepress" in root or "cache" in root or "node_modules" in root:
        continue
    for f in filenames:
        if f.endswith(".md"):
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, DOCS_DIR).replace("\\", "/")
            if rel_path == "index.md":
                route = "/docs/"
            else:
                route = "/docs/" + rel_path[:-3] + "/"
                if route.endswith("/index/"):
                    route = route[:-6]
            
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                
            # Extract links
            md_links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", content)
            for text, url in md_links:
                add_link(route, url.strip())
            html_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>', content, re.IGNORECASE)
            for url in html_links:
                add_link(route, url.strip())

# 2. Parse Blog Markdown files
for f in os.listdir(BLOG_DIR):
    if f.endswith(".md"):
        filepath = os.path.join(BLOG_DIR, f)
        route = "/blog" if f == "index.md" else f"/blog/{f[:-3]}"
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        md_links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", content)
        for text, url in md_links:
            add_link(route, url.strip())
        html_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>', content, re.IGNORECASE)
        for url in html_links:
            add_link(route, url.strip())

# 3. Parse Vue Views & Layouts & Components
# Walk through src/views and src/components
for root, dirs, filenames in os.walk(SRC_DIR):
    for f in filenames:
        if f.endswith(".vue"):
            filepath = os.path.join(root, f)
            # Find route name
            route = "component:" + f
            # If it maps to a route, use it
            rel = os.path.relpath(filepath, os.path.join(SRC_DIR, "views")).replace("\\", "/")
            views_mapping = {
                "LandingPage.vue": "/",
                "UseCaseView.vue": "/use-cases",
                "PricingView.vue": "/pricing",
                "PrivacyPolicyView.vue": "/privacy-policy",
                "TermsView.vue": "/terms",
                "products/ConnectorsView.vue": "/connectors",
                "products/McpView.vue": "/mcp",
                "products/PluginsView.vue": "/plugins",
                "products/RagView.vue": "/rag",
                "products/MemoryGraphView.vue": "/memory-graph",
                "products/PersonalAppView.vue": "/personal",
                "products/ExtensionView.vue": "/extension",
                "BlogListView.vue": "/blog",
                "BlogPostView.vue": "/blog/:slug",
                "WhatIsAiMemoryView.vue": "/what-is-ai-memory",
                "LocomoBenchmarkView.vue": "/ai-memory-benchmark-locomo",
                "ResearchHubView.vue": "/research",
                "comparisons/MemwyreVsMem0.vue": "/memwyre-vs-mem0",
                "comparisons/MemwyreVsSupermemory.vue": "/memwyre-vs-supermemory",
                "comparisons/MemwyreVsZep.vue": "/memwyre-vs-zep",
                "integrations/ChatgptMemoryView.vue": "/chatgpt-memory",
                "integrations/ClaudeMemoryView.vue": "/claude-memory",
                "integrations/CursorMemoryView.vue": "/cursor-memory",
                "integrations/McpMemoryView.vue": "/mcp-memory",
                "LoginView.vue": "/login",
                "RegisterView.vue": "/signup",
                "VerifyEmailView.vue": "/verify-email",
                "ForgotPasswordView.vue": "/forgot-password",
                "ResetPasswordView.vue": "/reset-password",
                "SettingsView.vue": "/settings",
                "IntegrationsView.vue": "/integrations",
                "PromptGeneratorView.vue": "/prompts",
                "MemoryMapView.vue": "/map",
                "ChatView.vue": "/chat",
                "BillingView.vue": "/billing",
                "AdminInsightsView.vue": "/admin",
                "AdminBypassView.vue": "/admin/bypass",
                "RetrievalVisualizerView.vue": "/retrieval-visualizer",
                "RedeemView.vue": "/redeem",
                "SlideGalleryView.vue": "/slides"
            }
            if rel in views_mapping:
                route = views_mapping[rel]
            elif f == "SiteNavBar.vue":
                route = "[SiteNavBar]"
            elif f == "SiteFooter.vue":
                route = "[SiteFooter]"
                
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                
            soup = BeautifulSoup(content, "html.parser")
            for rl in soup.find_all(["router-link", "routerlink"]):
                to_val = rl.get("to") or rl.get(":to")
                add_link(route, str(to_val))
            for a in soup.find_all("a"):
                href_val = a.get("href") or a.get(":href")
                add_link(route, str(href_val))

# Filter out components from sources and print results
orphaned = []
one_link = []
others = []

for r in ROUTES:
    cnt = in_links[r]
    # Filter sources to only unique routes (SPA, docs, blogs)
    sources = list(set([s for s in in_link_sources[r] if not s.startswith("component:")]))
    
    # If it is linked from SiteNavBar or SiteFooter, it's linked from "global template" which is present on all pages
    # Let's count that as linked from everywhere
    is_global = "[SiteNavBar]" in in_link_sources[r] or "[SiteFooter]" in in_link_sources[r]
    
    # Calculate effective in-links count
    effective_cnt = len(sources)
    if is_global:
        effective_cnt += 1 # represent template link
        
    if effective_cnt == 0:
        orphaned.append((r, sources, is_global))
    elif effective_cnt == 1:
        one_link.append((r, sources, is_global))
    else:
        others.append((r, cnt, sources, is_global))

print(f"\n--- REVISED LINK COUNTS ---")
print(f"Orphaned pages (0 in-links) [{len(orphaned)}]:")
for r, src, global_link in sorted(orphaned):
    print(f"  - {r}")

print(f"\nPages with only one in-link [{len(one_link)}]:")
for r, src, global_link in sorted(one_link):
    g_str = " + Global Nav/Footer" if global_link else ""
    print(f"  - {r} (Linked from: {src}{g_str})")

print(f"\nWell linked pages [{len(others)}]:")
for r, cnt, src, global_link in sorted(others):
    g_str = " + Global Nav/Footer" if global_link else ""
    print(f"  - {r} (In-links count: {cnt}, unique pages: {src}{g_str})")
