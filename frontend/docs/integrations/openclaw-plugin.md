# OpenClaw Plugin

This plugin enables the **OpenClaw** autonomous agent framework to seamlessly use MemWyre as its persistent memory and context engine. 

## Overview

If you use OpenClaw for autonomous tasks, this plugin bridges the gap between OpenClaw's transient session state and MemWyre's long-term memory. The agent can recall previous sessions, look up project documentation, and automatically save its own insights back to your vault.

## Capabilities

Once configured, the OpenClaw agent will have access to the following tools:
- **`save_memory`**: Saves a new memory/note directly into your MemWyre Inbox. The agent can use this to document its findings.
- **`search_memwyre`**: Performs semantic search across your MemWyre Vault to retrieve past context, code snippets, or instructions.

## Setup & Installation

You can install the plugin directly via the OpenClaw CLI or NPM.

1. **Install the Plugin**:
   ```bash
   openclaw plugins install @memwyre/openclaw-plugin
   ```

2. **Configure OpenClaw**:
   Add the following to your OpenClaw settings file (usually `~/.openclaw/config.json`):

   ```json
   "plugins": {
       "entries": {
         "openclaw-plugin": {
           "enabled": true,
           "config": {
             "apiKey": "bv_sk_your_api_key_here",
             "hostUrl": "https://server.memwyre.tech"
           }
         }
       }
   }
   ```
   *Note: Generate your API key from the MemWyre web interface under Settings > API Keys.*

### Important: Agent Tool Profile

To ensure the tools are injected into your OpenClaw agent session, you **must set your agent tool profile to `full` or `coding`**. If your profile is set to standard or bare minimum, OpenClaw may artificially disable these custom memory plugins to save tokens.
