import os
import re
import urllib.parse
from bs4 import BeautifulSoup

FRONTEND_DIR = r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend"
PUBLIC_DIR = os.path.join(FRONTEND_DIR, "public")
SRC_DIR = os.path.join(FRONTEND_DIR, "src")
DOCS_DIR = os.path.join(FRONTEND_DIR, "docs")
BLOG_DIR = os.path.join(SRC_DIR, "assets", "blog")

# Valid SPA routes (without trailing slash, except root)
SPA_ROUTES = {
    "/", "/use-cases", "/pricing", "/privacy-policy", "/terms", "/connectors", 
    "/mcp", "/plugins", "/rag", "/memory-graph", "/personal", "/extension",
    "/blog", "/blog/mcp-persistent-memory", "/blog/cursor-vs-claude-code-context",
    "/blog/rag-vs-memory-long-term-knowledge", "/blog/vscode-mcp-persistent-memory",
    "/blog/claude-code-memory-ingestion", "/blog/openclaw-autonomous-memory",
    "/blog/state-of-ai-memory-2026", "/what-is-ai-memory", "/ai-memory-benchmark-locomo",
    "/research", "/memwyre-vs-mem0", "/memwyre-vs-supermemory", "/memwyre-vs-zep",
    "/chatgpt-memory", "/claude-memory", "/cursor-memory", "/mcp-memory",
    "/login", "/signup", "/verify-email", "/forgot-password", "/reset-password",
    "/settings", "/integrations", "/prompts", "/map", "/chat", "/billing", 
    "/admin", "/admin/bypass", "/retrieval-visualizer", "/redeem", "/slides"
}

# Valid Docs routes (with trailing slash)
DOCS_ROUTES = {
    "/docs/", "/docs/use-cases/", "/docs/self-hosting/", "/docs/how-it-works/",
    "/docs/rag-vs-memory/", "/docs/benchmarks/", "/docs/security/", "/docs/integrations/",
    "/docs/integrations/browser-extension/", "/docs/integrations/cli-installer/",
    "/docs/integrations/connectors/", "/docs/integrations/mcp-server/",
    "/docs/integrations/mcp-server/claude/", "/docs/integrations/mcp-server/cursor/",
    "/docs/integrations/mcp-server/vscode/", "/docs/integrations/plugins/claude/",
    "/docs/integrations/plugins/openclaw/"
}

ALL_ROUTES = SPA_ROUTES.union(DOCS_ROUTES)

def get_word_count(text):
    # Strip HTML tags and markdown formatting basic style
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def scan_files():
    files_to_check = []
    
    # 1. Add docs markdown files
    for root, dirs, filenames in os.walk(DOCS_DIR):
        if ".vitepress" in root or "cache" in root or "node_modules" in root:
            continue
        for f in filenames:
            if f.endswith(".md"):
                filepath = os.path.join(root, f)
                # Determine route
                rel_path = os.path.relpath(filepath, DOCS_DIR).replace("\\", "/")
                if rel_path == "index.md":
                    route = "/docs/"
                else:
                    route = "/docs/" + rel_path[:-3] + "/"
                    # Special handles for nested index
                    if route.endswith("/index/"):
                        route = route[:-6]
                files_to_check.append({
                    "type": "doc",
                    "path": filepath,
                    "route": route
                })
                
    # 2. Add blog posts
    for f in os.listdir(BLOG_DIR):
        if f.endswith(".md"):
            filepath = os.path.join(BLOG_DIR, f)
            if f == "index.md":
                route = "/blog"
            else:
                route = f"/blog/{f[:-3]}"
            files_to_check.append({
                "type": "blog",
                "path": filepath,
                "route": route
            })

    # 3. Add Vue views (SPA routes)
    # We will map standard view files to their routes
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
    for rel_view, route in views_mapping.items():
        filepath = os.path.join(views_dir, rel_view.replace("/", "\\"))
        if os.path.exists(filepath):
            files_to_check.append({
                "type": "vue",
                "path": filepath,
                "route": route
            })
            
    # Also add standard layouts and components that contain links
    files_to_check.append({
        "type": "component",
        "path": os.path.join(SRC_DIR, "components", "SiteNavBar.vue"),
        "route": "SiteNavBar"
    })
    files_to_check.append({
        "type": "component",
        "path": os.path.join(SRC_DIR, "components", "SiteFooter.vue"),
        "route": "SiteFooter"
    })
    
    return files_to_check

def check_link(link, current_route):
    # Normalize link
    if not link:
        return "empty", None
        
    # Ignore mailto, tel, anchor hashes (internal to page)
    if link.startswith("mailto:") or link.startswith("tel:"):
        return "external", None
    if link.startswith("#"):
        return "hash", link
        
    # Check if external
    parsed = urllib.parse.urlparse(link)
    if parsed.scheme and parsed.netloc:
        if "memwyre.tech" in parsed.netloc:
            # It's an absolute link to our own domain
            path = parsed.path
            if parsed.fragment:
                path += "#" + parsed.fragment
            link = path
        else:
            return "external", None
            
    # Normalize relative links relative to current route
    if not link.startswith("/"):
        # Resolve relative path
        if current_route.startswith("/docs/"):
            # Docs are directories with trailing slashes, so they are folders
            base = current_route
        elif current_route.startswith("/blog/") and current_route != "/blog":
            # e.g., /blog/mcp-persistent-memory. Resolve relative to /blog/
            base = "/blog/"
        else:
            base = "/"
        
        # Simple resolution
        resolved = urllib.parse.urljoin(base, link)
        link = resolved
        
    # Split hash and query
    path_only = link.split("?")[0].split("#")[0]
    hash_part = "#" + link.split("#")[1] if "#" in link else ""
    
    # Check if static file in public
    if path_only != "/":
        pub_file = os.path.join(PUBLIC_DIR, path_only.lstrip("/"))
        if os.path.exists(pub_file) and os.path.isfile(pub_file):
            return "static", path_only
            
    # Check if route is valid
    if path_only in ALL_ROUTES:
        # Check if it causes redirect due to trailing slash mismatch
        if path_only.startswith("/docs"):
            if not path_only.endswith("/"):
                return "redirect_to_slash", path_only
        else:
            if path_only != "/" and path_only.endswith("/"):
                return "redirect_to_no_slash", path_only
        return "ok", path_only + hash_part
    
    # Special handle for dynamic routes
    if path_only.startswith("/blog/") and path_only.count("/") == 2:
        slug = path_only.split("/")[-1]
        if os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md")):
            return "ok", path_only
            
    return "broken", link

def analyze_file(file_info):
    filepath = file_info["path"]
    route = file_info["route"]
    file_type = file_info["type"]
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    word_count = get_word_count(content)
    has_h1 = False
    meta_description = ""
    links = []
    
    # Parse headings and links
    if file_type in ("doc", "blog"):
        # Check H1 in markdown
        if re.search(r"^#\s+.*", content, re.MULTILINE) or re.search(r"<h1>.*</h1>", content, re.IGNORECASE):
            has_h1 = True
            
        # Extract title from frontmatter
        title_match = re.search(r"^title:\s*(.*)", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else os.path.basename(filepath)
        
        # Find markdown links [Text](URL)
        md_links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", content)
        for text, url in md_links:
            links.append({"text": text.strip(), "url": url.strip(), "line": content[:content.find(f"({url})")].count("\n") + 1})
            
        # Find HTML links in markdown
        html_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
        for url, inner in html_links:
            text = re.sub(r'<[^>]+>', '', inner).strip()
            links.append({"text": text, "url": url.strip(), "line": content[:content.find(url)].count("\n") + 1})
            
        # Extract meta description from frontmatter or text
        desc_match = re.search(r"^description:\s*(.*)", content, re.MULTILINE)
        if desc_match:
            meta_description = desc_match.group(1).strip()
            
    elif file_type in ("vue", "component"):
        # Vue files
        soup = BeautifulSoup(content, "html.parser")
        
        # Check H1
        if soup.find("h1"):
            has_h1 = True
            
        # Find router-links
        for rl in soup.find_all(["router-link", "routerlink"]):
            to_val = rl.get("to") or rl.get(":to")
            text = rl.get_text().strip()
            links.append({"text": text, "url": str(to_val), "line": 0})
            
        # Find normal links
        for a in soup.find_all("a"):
            href_val = a.get("href") or a.get(":href")
            text = a.get_text().strip()
            links.append({"text": text, "url": str(href_val), "line": 0})
            
    return {
        "path": filepath,
        "filename": os.path.basename(filepath),
        "route": route,
        "type": file_type,
        "word_count": word_count,
        "has_h1": has_h1,
        "meta_description": meta_description,
        "links": links
    }

def main():
    files = scan_files()
    analyzed_results = []
    
    for f_info in files:
        try:
            res = analyze_file(f_info)
            analyzed_results.append(res)
        except Exception as e:
            print(f"Error analyzing {f_info['path']}: {e}")
            
    # Compile Audit Results
    broken_links = []
    redirect_links = []
    no_anchor_links = []
    low_word_count_pages = []
    missing_h1_pages = []
    duplicate_metas = {}
    
    # Store page information by route
    pages_report = []
    
    for res in analyzed_results:
        route = res["route"]
        if res["type"] == "component":
            route = f"[{res['route']}]"
            
        # Check H1
        if not res["has_h1"] and res["type"] in ("doc", "blog", "vue"):
            missing_h1_pages.append(res)
            
        # Check Word Count
        if res["word_count"] < 250 and res["type"] in ("doc", "blog", "vue"):
            low_word_count_pages.append(res)
            
        # Check Meta Description from seo.js or page
        # In our case we will fetch from PUBLIC_ROUTE_SEO (via manual check later or if extracted)
        desc = res["meta_description"]
        if desc:
            duplicate_metas.setdefault(desc, []).append(res["route"])
            
        # Check links
        for l in res["links"]:
            url = l["url"]
            text = l["text"]
            
            # Skip empty or bound values like variables
            if not url or url == "None" or url.startswith("`") or url.startswith("post.slug") or "{{" in url or "post" in url or "link" in url:
                continue
                
            status, resolved = check_link(url, res["route"])
            
            link_info = {
                "source_page": route,
                "source_file": res["filename"],
                "link_url": url,
                "resolved_url": resolved,
                "text": text,
                "status": status
            }
            
            if status == "broken":
                broken_links.append(link_info)
            elif status in ("redirect_to_slash", "redirect_to_no_slash"):
                redirect_links.append(link_info)
                
            if not text and status != "hash" and status != "external" and res["type"] != "component":
                # Check if it has an image or icon instead
                no_anchor_links.append(link_info)
                
        pages_report.append({
            "route": route,
            "filename": res["filename"],
            "word_count": res["word_count"],
            "has_h1": res["has_h1"],
            "type": res["type"],
            "links_count": len(res["links"])
        })
        
    # Output to report files
    import json
    report = {
        "pages": pages_report,
        "broken_links": broken_links,
        "redirect_links": redirect_links,
        "no_anchor_links": no_anchor_links,
        "low_word_count_pages": [{"route": p["route"], "file": p["filename"], "words": p["word_count"]} for p in low_word_count_pages],
        "missing_h1_pages": [{"route": p["route"], "file": p["filename"]} for p in missing_h1_pages],
        "duplicate_metas": {k: v for k, v in duplicate_metas.items() if len(v) > 1}
    }
    
    report_file = r"c:\Users\himan\OneDrive\Documents\brain_vault\scratch\seo_audit_results.json"
    with open(report_file, "w", encoding="utf-8") as rf:
        json.dump(report, rf, indent=2)
        
    print(f"Audit completed. Report written to {report_file}")
    print(f"Found {len(broken_links)} broken links.")
    print(f"Found {len(redirect_links)} redirect links.")
    print(f"Found {len(no_anchor_links)} no-anchor links.")
    print(f"Found {len(low_word_count_pages)} low word count pages.")
    print(f"Found {len(missing_h1_pages)} missing H1 pages.")

if __name__ == "__main__":
    main()
