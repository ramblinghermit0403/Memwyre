import os
import re
import urllib.parse
from bs4 import BeautifulSoup

FRONTEND_DIR = r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend"
SRC_DIR = os.path.join(FRONTEND_DIR, "src")
DOCS_DIR = os.path.join(FRONTEND_DIR, "docs")
BLOG_DIR = os.path.join(SRC_DIR, "assets", "blog")

ROUTES = {
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
    "/docs/integrations/plugins/openclaw/",
    "/dashboard", "/inbox", "/projects", "/settings", "/integrations", "/prompts",
    "/map", "/chat", "/billing", "/admin", "/admin/bypass", "/retrieval-visualizer",
    "/redeem", "/slides", "/login", "/signup"
}

all_issues = []

def find_line_number(content, attr_name, attr_val):
    # Search for something like: to="/path" or href="/path" or :to="path" or :href="path"
    # Escaping value
    escaped_val = re.escape(attr_val)
    pattern = rf'{attr_name}\s*=\s*["\']\s*{escaped_val}\s*["\']'
    match = re.search(pattern, content)
    if match:
        return content[:match.start()].count("\n") + 1
    
    # Try dynamic binding syntax e.g. :to="'/path'"
    pattern_dyn = rf':?{attr_name}\s*=\s*["\']\s*\'?{escaped_val}\'?\s*["\']'
    match_dyn = re.search(pattern_dyn, content)
    if match_dyn:
        return content[:match_dyn.start()].count("\n") + 1
        
    return 0

def audit_link(file_path, line_num, source_route, target_url, link_text):
    if not target_url or target_url == "None" or target_url.startswith("`") or target_url.startswith("post.") or target_url.startswith("item.") or "{{" in target_url:
        return
        
    if target_url.startswith("mailto:") or target_url.startswith("tel:") or target_url.startswith("#"):
        return
        
    parsed = urllib.parse.urlparse(target_url)
    if parsed.scheme and parsed.netloc:
        if "memwyre.tech" in parsed.netloc:
            target_url = parsed.path
            if parsed.fragment:
                target_url += "#" + parsed.fragment
        else:
            return
            
    # Resolve relative link
    resolved_path = target_url
    if not target_url.startswith("/"):
        if source_route.startswith("/docs/"):
            base = source_route
        elif source_route.startswith("/blog/") and source_route != "/blog":
            base = "/blog/"
        else:
            base = "/"
        resolved_path = urllib.parse.urljoin(base, target_url)
        
    path_only = resolved_path.split("?")[0].split("#")[0]
    
    # Check if target route is valid
    is_valid = False
    redirect_reason = None
    
    if path_only in ROUTES:
        is_valid = True
        # Check redirect
        if path_only.startswith("/docs"):
            if not path_only.endswith("/"):
                redirect_reason = f"Redirects to {path_only}/ (VitePress requires trailing slash)"
        else:
            if path_only != "/" and path_only.endswith("/"):
                redirect_reason = f"Redirects to {path_only[:-1]} (SPA strips trailing slash)"
    elif path_only + "/" in ROUTES:
        is_valid = True
        redirect_reason = f"Redirects to {path_only}/ (VitePress requires trailing slash)"
    elif path_only.endswith("/") and path_only[:-1] in ROUTES:
        is_valid = True
        redirect_reason = f"Redirects to {path_only[:-1]} (SPA strips trailing slash)"
    elif path_only.startswith("/blog/") and path_only.count("/") == 2:
        slug = path_only.split("/")[-1]
        if os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md")):
            is_valid = True
            
    if not is_valid:
        # Check if it is a static file
        pub_file = os.path.join(FRONTEND_DIR, "public", path_only.lstrip("/"))
        if os.path.exists(pub_file) and os.path.isfile(pub_file):
            return
            
        all_issues.append({
            "file": os.path.relpath(file_path, FRONTEND_DIR),
            "line": line_num,
            "type": "Broken Link",
            "anchor": link_text,
            "target": target_url,
            "resolved": resolved_path,
            "severity": "High"
        })
    elif redirect_reason:
        all_issues.append({
            "file": os.path.relpath(file_path, FRONTEND_DIR),
            "line": line_num,
            "type": "Redirecting Link (301)",
            "anchor": link_text,
            "target": target_url,
            "resolved": resolved_path,
            "description": redirect_reason,
            "severity": "High"
        })

# Parse markdown file line by line
def parse_markdown(file_path, route):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split("\n")
    for idx, line in enumerate(lines):
        line_num = idx + 1
        # Find md links [Text](URL)
        md_links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", line)
        for text, url in md_links:
            audit_link(file_path, line_num, route, url.strip(), text.strip())
            
        # Find HTML href links
        html_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', line, re.IGNORECASE)
        for url, inner in html_links:
            text = re.sub(r'<[^>]+>', '', inner).strip()
            audit_link(file_path, line_num, route, url.strip(), text)

# Parse vue file with BeautifulSoup and locate lines
def parse_vue(file_path, route):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, "html.parser")
    
    # 1. router-link elements
    for rl in soup.find_all(["router-link", "routerlink"]):
        to_val = rl.get("to") or rl.get(":to")
        if to_val:
            text = rl.get_text().strip()
            line_num = find_line_number(content, "to", str(to_val))
            audit_link(file_path, line_num, route, str(to_val), text)
            
    # 2. a href elements
    for a in soup.find_all("a"):
        href_val = a.get("href") or a.get(":href")
        if href_val:
            text = a.get_text().strip()
            line_num = find_line_number(content, "href", str(href_val))
            audit_link(file_path, line_num, route, str(href_val), text)

# 1. Walk Docs
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
            parse_markdown(filepath, route)

# 2. Walk Blog
for f in os.listdir(BLOG_DIR):
    if f.endswith(".md"):
        filepath = os.path.join(BLOG_DIR, f)
        route = "/blog" if f == "index.md" else f"/blog/{f[:-3]}"
        parse_markdown(filepath, route)

# 3. Walk Vue views
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

views_dir = os.path.join(SRC_DIR, "views")
for rel, route in views_mapping.items():
    fp = os.path.join(views_dir, rel.replace("/", "\\"))
    if os.path.exists(fp):
        parse_vue(fp, route)

# Parse navbar and footer
parse_vue(os.path.join(SRC_DIR, "components", "SiteNavBar.vue"), "[SiteNavBar]")
parse_vue(os.path.join(SRC_DIR, "components", "SiteFooter.vue"), "[SiteFooter]")

# Deduplicate issues
unique_issues = []
seen = set()
for issue in all_issues:
    key = (issue["file"], issue["line"], issue["target"])
    if key not in seen:
        seen.add(key)
        unique_issues.append(issue)

# Write to JSON
import json
with open(r"c:\Users\himan\OneDrive\Documents\brain_vault\scratch\detailed_broken_links.json", "w", encoding="utf-8") as f:
    json.dump(unique_issues, f, indent=2)

print(f"Total Unique Issues Found: {len(unique_issues)}")
for issue in unique_issues:
    desc = issue.get("description", "")
    print(f"[{issue['severity']}] {issue['type']} in {issue['file']}:{issue['line']} -> target: {issue['target']} (text: '{issue['anchor']}') {desc}")
