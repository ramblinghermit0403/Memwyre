# Persistent Memory for Autonomous Agents: OpenClaw and Memwyre Integration

Autonomous coding agents are shifting from simple prompt-based assistants to goal-driven systems that execute multiple files, run tests, and self-correct. **OpenClaw** is a prominent open-source autonomous agent framework that excels at executing complex, multi-step workflows.

However, because autonomous agents run in isolated sessions, they suffer from a major limitation: **they operate with short-term amnesia**. Every time you launch a new OpenClaw task, the agent has no memory of past runs, previously discovered codebase patterns, or bugs it already fixed.

By integrating the **Memwyre OpenClaw Plugin**, you can give your autonomous agents a shared, persistent long-term memory vault. 

---

## State Management and the Context Exhaustion Dilemma

In long-running autonomous agent loops, managing state is one of the hardest challenges. 

### Why Context Windows Fail
If an agent relies on pure conversational history (short-term memory), its context window fills up rapidly. For every step the agent takes—reading a file, running a shell command, checking a compiler warning—the log is appended to its history.
- Within 15 to 20 turns, the context window can exceed 50,000 tokens.
- **Cost Explosion**: The agent repeats the entire history on every new step, causing token costs to compound quadratically.
- **Attention Degradation**: As the prompt grows longer, LLMs suffer from "lost-in-the-middle" syndrome, failing to recall facts buried in the middle of the context window.

### The Memory Solution: Recency-Aware Scoring
Instead of loading the entire log history, Memwyre enables OpenClaw to run a background tool loop that retrieves only the exact facts relevant to the active sub-task.

To prevent stale context from overwhelming the agent, the plugin ranks memories using a temporal decay function:
\[ S = \text{Similarity} \times e^{-\lambda t} \]

Where:
- \(\text{Similarity}\) is the cosine similarity between the query embedding and the memory record.
- \(\lambda\) is the decay rate (regulating how quickly old memories fade).
- \(t\) is the elapsed time (number of days or sessions since the memory was last updated or accessed).

This guarantees that if the agent queries for "database credentials," recent staging updates automatically rank higher than deprecated local docker profiles.

---

## Plugin Tool Schema

Once loaded, the `@memwyre/openclaw-plugin` exposes two core tools to the OpenClaw reasoning loop. The agent selects these tools using standard JSON schemas:

### 1. `search_memwyre`
Allows the agent to execute a semantic vector search across the workspace memories.

```json
{
  "name": "search_memwyre",
  "description": "Search the persistent memory vault for relevant context, preferences, or codebase decisions.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search term or query string to find in the memory vault."
      },
      "limit": {
        "type": "integer",
        "description": "Maximum number of memories to return (default 5).",
        "default": 5
      }
    },
    "required": ["query"]
  }
}
```

### 2. `save_memory`
Allows the agent to write a new finding or guideline back to the database.

```json
{
  "name": "save_memory",
  "description": "Save an important technical finding, decision, or user preference to the memory vault.",
  "parameters": {
    "type": "object",
    "properties": {
      "content": {
        "type": "string",
        "description": "The exact fact or guideline to store."
      },
      "importance": {
        "type": "integer",
        "description": "An importance rating from 1 to 5 (5 being critical, e.g. credentials or syntax rules).",
        "default": 3
      }
    },
    "required": ["content"]
  }
}
```

---

## Installation & Configuration

### 1. Install the Plugin
You can install the official plugin (Version **2.0.14**) directly using the OpenClaw CLI:

```bash
openclaw plugins install @memwyre/openclaw-plugin@2.0.14
```

### 2. Configure Settings
Add the plugin configuration settings to your OpenClaw configuration file (typically located at `~/.openclaw/config.json`):

```json
{
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
}
```

*Be sure to replace `bv_sk_your_api_key_here` with your API key generated from settings in your Memwyre web dashboard.*

### 3. Select the Correct Agent Tool Profile
To ensure custom memory plugins are injected into the agent session, **set your agent tool profile to `full` or `coding`**. 

> **Important**: If your profile is set to `standard` or `minimal`, OpenClaw may disable custom plugins to save token overhead, preventing the agent from utilizing the memory tools.

---

## Auto-Compaction: Preventing Memory Bloat

An autonomous agent can generate hundreds of logs in a day. If every detail was written as a separate memory, the database would quickly get cluttered with duplicate and contradictory records.

Memwyre runs an **Auto-Compaction** loop:
1. **Deduplication**: When a new memory is saved, the plugin checks for high cosine similarity matches in the vault. If a similar memory exists (e.g., "build runs on port 8080" vs "configured backend port to 8080"), it merges them into a single record.
2. **Conflict Resolution**: If the new memory contradicts an old one (e.g., "swapped Postgres backend for SQLite for testing"), the plugin updates the record and flags the older fact as inactive or archived.

This background reconciliation ensures that your agent always operates on a clean, high-signal codebase index.

---

## Conclusion

Integrating Memwyre with OpenClaw transforms autonomous agents from simple, stateless executors into continuous, learning co-developers. 

Equip your autonomous agents with long-term memory at [memwyre.tech](https://memwyre.tech).

