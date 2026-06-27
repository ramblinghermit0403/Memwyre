---
layout: page
title: Memwyre Blog
---

# Memwyre Blog
### Latest guides, insights, and engineering updates from the team building the universal memory layer for AI.

<div class="blog-grid">

  <div class="blog-card">
    <div class="blog-category">MCP SERVER</div>
    <h3 class="blog-title">How to Give Claude Desktop Persistent Memory using MCP</h3>
    <p class="blog-excerpt">Claude Desktop is powerful but stateless. Learn how to configure Memwyre as a local Model Context Protocol (MCP) server to store and query context across chat sessions.</p>
    <a href="./mcp-persistent-memory" class="blog-link">Read Guide →</a>
  </div>

  <div class="blog-card">
    <div class="blog-category">MCP SERVER</div>
    <h3 class="blog-title">How to Enable Persistent Codebase Memory in VS Code with MCP and Cline</h3>
    <p class="blog-excerpt">Give your VS Code AI agents (Cline, Roo-Code) a persistent memory layer. Step-by-step setup using the remote Memwyre MCP gateway.</p>
    <a href="./vscode-mcp-persistent-memory" class="blog-link">Read Guide →</a>
  </div>

  <div class="blog-card">
    <div class="blog-category">CLI PLUGINS</div>
    <h3 class="blog-title">Building Persistent Terminal Sessions: Claude Code Memory Ingestion</h3>
    <p class="blog-excerpt">Anthropic's Claude Code CLI is incredibly fast. Integrate Memwyre hooks to automatically inject project memory on launch and ingest transcripts on exit.</p>
    <a href="./claude-code-memory-ingestion" class="blog-link">Read Guide →</a>
  </div>

  <div class="blog-card">
    <div class="blog-category">CLI PLUGINS</div>
    <h3 class="blog-title">Persistent Memory for Autonomous Agents: OpenClaw and Memwyre</h3>
    <p class="blog-excerpt">Autonomous agent workflows suffer from amnesia. Learn how to load the Memwyre OpenClaw plugin and enable the agent to query and update your vault.</p>
    <a href="./openclaw-autonomous-memory" class="blog-link">Read Guide →</a>
  </div>

  <div class="blog-card">
    <div class="blog-category">COMPARISONS</div>
    <h3 class="blog-title">Cursor AI vs Claude Code: Managing Context and Memory in IDEs</h3>
    <p class="blog-excerpt">A technical breakdown comparing how Cursor AI and Claude Code manage workspace context, and how to extend both with Memwyre.</p>
    <a href="./cursor-vs-claude-code-context" class="blog-link">Read Guide →</a>
  </div>

  <div class="blog-card">
    <div class="blog-category">ARCHITECTURE</div>
    <h3 class="blog-title">RAG vs. AI Memory: Choosing the Right Approach for Long-Term Knowledge</h3>
    <p class="blog-excerpt">Why basic Vector RAG fails for developer workflows due to chunk fragmentation, and why entity-profile routing provides better context.</p>
    <a href="./rag-vs-memory-long-term-knowledge" class="blog-link">Read Guide →</a>
  </div>

</div>

<style>
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  margin-top: 32px;
  margin-bottom: 64px;
}

.blog-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.2s ease-in-out;
}

.blog-card:hover {
  transform: translateY(-4px);
  border-color: #D97757;
  background: rgba(255, 255, 255, 0.05);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.blog-category {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #D97757;
  margin-bottom: 12px;
  text-transform: uppercase;
}

.blog-title {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.4;
  margin: 0 0 12px 0;
  color: var(--vp-c-text-1);
}

.blog-excerpt {
  font-size: 14px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0 0 20px 0;
  flex-grow: 1;
}

.blog-link {
  font-size: 14px;
  font-weight: 600;
  color: #D97757;
  text-decoration: none;
  display: inline-block;
  transition: color 0.15s ease;
}

.blog-link:hover {
  color: #c05c3d;
}

/* Light mode overrides */
:root:not(.dark) .blog-card {
  background: rgba(0, 0, 0, 0.02);
  border: 1px solid rgba(0, 0, 0, 0.08);
}

:root:not(.dark) .blog-card:hover {
  background: rgba(0, 0, 0, 0.03);
}
</style>
