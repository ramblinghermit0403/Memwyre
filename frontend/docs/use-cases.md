---
title: "Use Cases"
description: "Explore core use cases for Memwyre, including codebase synchronization, personalized AI memory, and team workflows."
---

## 1. Coding & IDE Context Sync

- **The Workflow**: Synchronizing codebase architectures, framework versions, styling conventions, API keys, and architectural decisions with your local IDE (e.g. Cursor, VS Code, or Claude Desktop).
- **Why Memwyre Helps**: Instead of manually uploading context files or copy-pasting setup steps, Memwyre's MCP server streams the exact codebase details to the LLM in the background. As configuration keys or dependencies update, the memory layer updates itself, preventing the AI from referencing outdated APIs.

---

## 2. Research & Knowledge Caching

- **The Workflow**: Saving documentations, research papers, web articles, or technical guides during deep research sessions.
- **Why Memwyre Helps**: Using the Browser Extension, you can capture full pages, selected paragraphs, or articles. Memwyre cleans page noise and index them semantically. When you draft articles or code implementation plans, you can query your vault directly for relevant insights.

---

## 3. Persistent Memory for Autonomous Agents

- **The Workflow**: Equipping autonomous software agents (e.g. OpenClaw sessions or command-line scripts) with long-term memory across runs.
- **Why Memwyre Helps**: Standard agents are stateless and start from zero on every execution, losing task progress or previous decisions. By interfacing via our API or plugin connectors, agents read and write task checkpoints to a persistent graph, enabling continual learning.

---

## 4. Media & Transcripts Digest

- **The Workflow**: Ingesting meeting transcripts, audio files, or YouTube video records to query specific topics or discussions.
- **Why Memwyre Helps**: You can feed video links or raw audio transcripts directly to Memwyre. The background worker parses the transcripts, extracts key facts, and embeds them. You can then prompt: _"what did we decide about the hosting server during the meeting?"_ and get precise facts.

---

## 5. Unified Knowledge Connectors

- **The Workflow**: Searching across scattered repositories like Google Drive, Notion workspaces, and local folders in a single query.
- **Why Memwyre Helps**: Our workspace connectors automatically sync pages and files into your vault. Memwyre creates unified entity profiles across these tools, resolving relationships dynamically so your queries aggregate all relevant sources seamlessly.