---
title: "Openclaw"
description: "Install the Memwyre plugin for OpenClaw autonomous agents to query and persist memory graphs across agent runs."
---

# OpenClaw Plugin

Add persistent, long-term memory to your **OpenClaw** autonomous agent sessions using Memwyre as the memory and context engine.

## Overview

OpenClaw agents operate within a single session and lose context when that session ends. This plugin bridges the gap — giving your agent access to Memwyre's vault so it can recall previous sessions, look up project documentation, and save its own findings for future runs.

## Available Tools

Once configured, the OpenClaw agent can use the following Memwyre tools:

| Tool | Description |
| --- | --- |
| `save_memory` | Save a new memory or note into your Memwyre Inbox. |
| `search_memwyre` | Run a semantic search across your Memwyre Vault. |

## Installation

The plugin (Version **2.0.14**) can be installed globally or linked locally for custom development runs:

### Option A: Standard CLI Install

```bash
openclaw plugins install @memwyre/openclaw-plugin@2.0.14
```

### Option B: Local Linking (Development)

If modifying the plugin source, link the package manually:

1. Navigate to the plugin folder:
   ```bash
   cd openclaw-plugin
   npm install
   ```
2. Link the package to your local OpenClaw workspace:
   ```bash
   openclaw plugins install .
   ```

## Configuration

Add the following to your OpenClaw settings file (typically `~/.openclaw/config.json`):

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

> Generate your API key from **Settings → API Keys** in the Memwyre web app.

## Important: Agent Tool Profile

To ensure the Memwyre tools are injected into your agent session, **set your agent tool profile to `full` or `coding`**.

If your profile is set to `standard` or `minimal`, OpenClaw may disable custom memory plugins to reduce token usage.