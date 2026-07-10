import os
import re
import shutil
import subprocess

# Paths
DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "docs"))
WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tmp", "wiki"))
WIKI_REPO_URL = "https://github.com/ramblinghermit0403/Memwyre.wiki.git"

def clean_wiki_dir():
    if os.path.exists(WIKI_DIR):
        print(f"Cleaning existing wiki dir: {WIKI_DIR}")
        shutil.rmtree(WIKI_DIR)
    os.makedirs(WIKI_DIR, exist_ok=True)

def clone_wiki():
    print(f"Cloning Wiki repository from {WIKI_REPO_URL}...")
    try:
        subprocess.run(["git", "clone", WIKI_REPO_URL, WIKI_DIR], check=True)
    except subprocess.CalledProcessError:
        print("\n[ERROR] Failed to clone wiki repo. Please make sure you have initialized the Wiki")
        print("on GitHub by going to https://github.com/ramblinghermit0403/Memwyre/wiki")
        print("and clicking 'Create the first page' and saving it.")
        exit(1)

def get_flattened_name(rel_path):
    """
    Translates e.g. 'integrations/browser-extension.md' -> 'integrations-browser-extension.md'
    and 'index.md' -> 'Home.md' or 'integrations-index.md'.
    """
    rel_path = rel_path.replace("\\", "/")
    if rel_path == "index.md":
        return "Home.md"
    
    parts = rel_path.split("/")
    if parts[-1] == "index.md":
        parts[-1] = "index"
    
    return "-".join(parts)

def rewrite_markdown_links(content, current_rel_dir):
    """
    Finds Markdown links e.g. [Link](../integrations/mcp-server) or [Link](./security.md)
    and rewrites them to the flat wiki target file names (without .md extension, as GitHub Wiki supports both).
    """
    # Pattern to match: [text](path)
    def link_replacer(match):
        text = match.group(1)
        link = match.group(2)
        
        # Skip external links and anchors
        if link.startswith("http://") or link.startswith("https://") or link.startswith("#") or link.startswith("mailto:"):
            return match.group(0)
        
        # Split anchor if present
        anchor = ""
        if "#" in link:
            link, anchor = link.split("#", 1)
            anchor = "#" + anchor
            
        # Resolve relative path against the source file directory
        resolved_path = os.path.normpath(os.path.join(current_rel_dir, link)).replace("\\", "/")
        
        # If it doesn't end with .md, VitePress auto-resolves it. We should assume it points to .md.
        if not resolved_path.endswith(".md"):
            resolved_path += ".md"
            
        # Clean relative prefixes like "./" or "../" at the beginning of resolved path
        resolved_path = resolved_path.lstrip("./").lstrip("/")
        
        # Get the flat wiki name
        flat_name = get_flattened_name(resolved_path)
        # Strip .md for cleaner wiki link
        if flat_name.endswith(".md"):
            flat_name = flat_name[:-3]
            
        return f"[{text}]({flat_name}{anchor})"

    # Match [text](link) where link doesn't contain spaces and parenthesis match
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, link_replacer, content)

def sync_files():
    print("Flattening and copying VitePress Markdown docs to Wiki...")
    markdown_files = []
    
    for root, dirs, files in os.walk(DOCS_DIR):
        # Skip internal directories
        if ".vitepress" in root or "public" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, DOCS_DIR)
                flat_name = get_flattened_name(rel_path)
                
                dest_path = os.path.join(WIKI_DIR, flat_name)
                
                with open(src_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Rewrite links
                rel_dir = os.path.dirname(rel_path)
                modified_content = rewrite_markdown_links(content, rel_dir)
                
                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(modified_content)
                
                print(f"  Copying: {rel_path} -> {flat_name}")
                markdown_files.append((rel_path, flat_name))
                
    return markdown_files

def generate_sidebar():
    print("Generating Wiki Sidebar (_Sidebar.md)...")
    sidebar_content = """### Getting Started
* [[Home]]
* [[Use Cases|use-cases]]
* [[Self-Hosting|self-hosting]]

### Concepts
* [[How It Works|how-it-works]]
* [[RAG vs. Memory|rag-vs-memory]]
* [[Benchmarks|benchmarks]]
* [[Security & Privacy|security]]

### Integrations
* [[Browser Extension|integrations-browser-extension]]
* [[CLI Auto-Installer|integrations-cli-installer]]
* [[MCP Server|integrations-mcp-server]]
* [[Connectors|integrations-connectors]]
* [[OpenClaw Plugin|integrations-plugins-openclaw]]
* [[Claude Code Plugin|integrations-plugins-claude]]
"""
    
    sidebar_path = os.path.join(WIKI_DIR, "_Sidebar.md")
    with open(sidebar_path, "w", encoding="utf-8") as f:
        f.write(sidebar_content)
    print("  Sidebar created.")

def commit_and_push():
    print("Committing and pushing Wiki updates...")
    try:
        subprocess.run(["git", "add", "."], cwd=WIKI_DIR, check=True)
        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], cwd=WIKI_DIR, capture_output=True, text=True)
        if not status.stdout.strip():
            print("No changes to sync.")
            return
            
        subprocess.run(["git", "commit", "-m", "docs: sync with VitePress docs"], cwd=WIKI_DIR, check=True)
        subprocess.run(["git", "push", "origin", "master"], cwd=WIKI_DIR, check=True)
        print("\n[SUCCESS] Wiki successfully updated!")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Git operation failed: {e}")

if __name__ == "__main__":
    clean_wiki_dir()
    clone_wiki()
    sync_files()
    generate_sidebar()
    commit_and_push()
