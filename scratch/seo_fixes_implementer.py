import os
import re

FRONTEND_DIR = r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend"
DOCS_DIR = os.path.join(FRONTEND_DIR, "docs")

# Mapping of file relative paths to custom descriptions and titles
DOCS_META = {
    "index.md": {
        "title": "Memwyre Documentation Overview",
        "description": "Get started with Memwyre, the universal persistent memory layer for AI agents, developer IDEs, and prompt workflows."
    },
    "use-cases.md": {
        "title": "Memwyre Core Use Cases",
        "description": "Explore core use cases for Memwyre, including codebase synchronization, personalized AI memory, and team workflows."
    },
    "self-hosting.md": {
        "title": "Self-Hosting Memwyre Guide",
        "description": "Learn how to host Memwyre locally or on your own private cloud using Docker Compose, PostgreSQL, and pgvector."
    },
    "how-it-works.md": {
        "title": "How Memwyre Works — Architecture",
        "description": "Understand the architectural concepts of Memwyre, including memory decay curves, graphs, profiles, and routing."
    },
    "rag-vs-memory.md": {
        "title": "RAG vs. Persistent AI Memory",
        "description": "Compare traditional RAG retrieval with Memwyre's persistent memory layer to see how entity profiling improves context relevance."
    },
    "benchmarks.md": {
        "title": "Memwyre Latency & Performance Benchmarks",
        "description": "Read the performance and latency benchmark report comparing Memwyre's retrieval with Mem0, Zep, and Supermemory."
    },
    "security.md": {
        "title": "Security & Data Privacy in Memwyre",
        "description": "Read about Memwyre security practices, including private memory vaults, data encryption, and local offline deployment."
    },
    "integrations/index.md": {
        "title": "Memwyre Integrations Overview",
        "description": "Browse available integrations for Memwyre, linking your memory vault to Claude, Cursor, VS Code, and browser extensions."
    },
    "integrations/browser-extension.md": {
        "title": "Memwyre Chrome/Edge Extension Setup",
        "description": "Learn how to install and use the Memwyre Chrome/Edge extension to capture web pages and chat context instantly."
    },
    "integrations/cli-installer.md": {
        "title": "CLI Auto-Installer Guide",
        "description": "Step-by-step instructions for running the Memwyre CLI installer to configure local MCP servers and developer hooks."
    },
    "integrations/connectors.md": {
        "title": "Connecting Data Sources to Memwyre",
        "description": "Configure data connectors to sync Memwyre memory graphs automatically with Notion, GitHub, Google Drive, and more."
    },
    "integrations/mcp-server.md": {
        "title": "Universal MCP Server Guide",
        "description": "Universal guide to connecting Memwyre to Model Context Protocol (MCP) clients like Claude Desktop, Cursor, and VS Code."
    },
    "integrations/mcp-server/claude.md": {
        "title": "Claude Desktop MCP Integration",
        "description": "Configure Memwyre as a local MCP server for Claude Desktop to maintain a persistent chat memory layer."
    },
    "integrations/mcp-server/cursor.md": {
        "title": "Cursor AI IDE MCP Integration",
        "description": "Configure Memwyre inside Cursor AI IDE to maintain persistent codebase memories across editing sessions."
    },
    "integrations/mcp-server/vscode.md": {
        "title": "VS Code MCP Agent Caching",
        "description": "Configure remote or local MCP memory gateway in VS Code for Cline, Roo-Code, and other developer agents."
    },
    "integrations/plugins/claude.md": {
        "title": "Claude Code CLI Lifecycle Hooks",
        "description": "Integrate Memwyre lifecycle hooks into Claude Code CLI to automatically save and retrieve terminal session memory."
    },
    "integrations/plugins/openclaw.md": {
        "title": "OpenClaw Persistent Memory Plugin",
        "description": "Install the Memwyre plugin for OpenClaw autonomous agents to query and persist memory graphs across agent runs."
    }
}

def update_docs():
    for rel_path, meta in DOCS_META.items():
        filepath = os.path.join(DOCS_DIR, rel_path.replace("/", "\\"))
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Update/Add Frontmatter
        if content.startswith("---"):
            # Existing frontmatter, let's update description and title
            match = re.match(r"^---([\s\S]*?)---", content)
            fm_content = match.group(1)
            body = content[match.end():]
            
            # Update title
            if "title:" in fm_content:
                fm_content = re.sub(r"title:.*", f"title: {meta['title']}", fm_content)
            else:
                fm_content += f"\ntitle: {meta['title']}"
                
            # Update description
            if "description:" in fm_content:
                fm_content = re.sub(r"description:.*", f"description: {meta['description']}", fm_content)
            else:
                fm_content += f"\ndescription: {meta['description']}"
                
            # Strip extra newlines
            fm_content = fm_content.strip()
            new_content = f"---\n{fm_content}\n---{body}"
        else:
            # No frontmatter, let's create it
            title = meta["title"]
            desc = meta["description"]
            frontmatter = f"---\ntitle: {title}\ndescription: {desc}\n---\n"
            new_content = frontmatter + content
            
        # 2. Fix local links in docs/index.md and docs/integrations/index.md
        if rel_path == "index.md":
            # docs/index.md fixes
            new_content = new_content.replace(
                "([Browser Extension](./integrations/browser-extension)",
                "([Browser Extension](./integrations/browser-extension/)"
            )
            new_content = new_content.replace(
                "([MCP Server](./integrations/mcp-server)",
                "([MCP Server](./integrations/mcp-server/)"
            )
            new_content = new_content.replace(
                "([OpenClaw Plugin](./integrations/plugins/openclaw)",
                "([OpenClaw Plugin](./integrations/plugins/openclaw/)"
            )
            new_content = new_content.replace(
                "([guide here](./integrations/browser-extension)",
                "([guide here](./integrations/browser-extension/)"
            )
            # Standard formats
            new_content = new_content.replace(
                "./integrations/browser-extension)",
                "./integrations/browser-extension/)"
            )
            new_content = new_content.replace(
                "./integrations/mcp-server)",
                "./integrations/mcp-server/)"
            )
            new_content = new_content.replace(
                "./integrations/plugins/openclaw)",
                "./integrations/plugins/openclaw/)"
            )
        elif rel_path == "integrations/index.md":
            # docs/integrations/index.md fixes
            new_content = new_content.replace(
                "([Browser Extension](./browser-extension)",
                "([Browser Extension](./browser-extension/)"
            )
            new_content = new_content.replace(
                "([IDEs & Agents (MCP Server)](./mcp-server)",
                "([IDEs & Agents (MCP Server)](./mcp-server/)"
            )
            new_content = new_content.replace(
                "([OpenClaw Plugin](./plugins/openclaw)",
                "([OpenClaw Plugin](./plugins/openclaw/)"
            )
            # Standard formats
            new_content = new_content.replace(
                "./browser-extension)",
                "./browser-extension/)"
            )
            new_content = new_content.replace(
                "./mcp-server)",
                "./mcp-server/)"
            )
            new_content = new_content.replace(
                "./plugins/openclaw)",
                "./plugins/openclaw/)"
            )
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Updated metadata and links for: {rel_path}")

if __name__ == "__main__":
    update_docs()
