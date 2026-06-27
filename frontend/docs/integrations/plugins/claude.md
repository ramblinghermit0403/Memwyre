# Claude Code Plugin

Integrate Memwyre directly with Anthropic's **Claude Code** terminal agent interface to provide persistent, cross-session memory and automatic transcript ingestion.

## Overview

Claude Code is a command-line tool that allows you to interact with Claude directly in your terminal. By default, Claude Code has no long-term memory of past tasks. The Memwyre Claude Plugin bridges this gap:

1. **Context Injection (`SessionStart`)**: When you launch Claude Code, the plugin automatically retrieves relevant past memories matching your current project folder and injects them as start context.
2. **Session Archival (`Stop` / `SessionEnd`)**: When you exit Claude Code, the plugin parses your session transcript and automatically uploads it to Memwyre, saving new insights and code updates for future sessions.

## Installation

### 1. Install the Package
Install the Memwyre Claude Plugin globally:
```bash
npm install -g @memwyre/claude-memwyre
```

### 2. Register Plugin Hooks in Claude Code
Register the plugin by editing your Claude Code configuration directory (typically located at `~/.claude/`):

Open `~/.claude/hooks.json` (create it if it doesn't exist) and add the hooks block pointing to the installed script:
```json
{
  "description": "Memwyre: Persistent autonomous memory",
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "node \"/path/to/global/node_modules/@memwyre/claude-memwyre/dist/inject-memory.cjs\"",
            "timeout": 30
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "node \"/path/to/global/node_modules/@memwyre/claude-memwyre/dist/capture-session.cjs\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Configuration

Ensure the following environment variables are set in your shell session before launching Claude Code:

```bash
export MEMWYRE_API_KEY="your_api_key_here"
export MEMWYRE_API_URL="https://server.memwyre.tech"  # Use http://127.0.0.1:8000 for local self-hosting
```
