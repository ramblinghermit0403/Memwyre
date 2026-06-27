# CLI Auto-Installer

Setup your local developer environment in seconds. The Memwyre CLI installer handles authentication, creates configuration templates, and configures MCP servers for your favorite IDEs automatically.

---

## Quickstart

Run the following command in your terminal to initialize Memwyre locally:

```bash
npx -y install-memwyre
```

This interactive CLI script automates the installation process, removing the need for manual configuration.

---

## Authentication & OAuth Callback Flow

The installer handles the OAuth handshake securely using a local loopback handler:

```
┌──────────────┐      1. Start Loopback       ┌──────────────┐
│  Local CLI   ├─────────────────────────────►│ Local Port   │
│  Installer   │                              │ (Randomized) │
└──────┬───────┘                              └──────┬───────┘
       │                                             ▲
       │ 2. Open Web Browser                         │ 4. HTTP POST
       ▼                                             │    Bearer Token
┌──────────────┐      3. User logs in         ┌──────┴───────┐
│ memwyre.tech │─────────────────────────────►│ Web App Auth │
│ /login       │                              │ Dashboard    │
└──────────────┘                              └──────────────┘
```

1. **Local Server Start**: The script starts a temporary, lightweight Express server on an ephemeral port (e.g. `http://localhost:50310`).
2. **Browser Redirection**: The script opens your default web browser and redirects you to the authentication page:
   `https://memwyre.tech/login?cli_port=50310`
3. **Authentication**: You sign in with Google, GitHub, or email.
4. **Token Delivery**: Once authenticated, the web application sends the secure Bearer Token to the local loopback address (`http://localhost:50310/callback`).
5. **Config Write**: The CLI captures the token, writes it to your global configurations (like `mcp.json` and `claude_desktop_config.json`), and shuts down the loopback listener.

---

## What the Installer Does

The CLI script detects your installed developer applications and automatically maps the connection configurations for you using `mcp-remote` (a lightweight utility that tunnels MCP requests directly over HTTP to the Memwyre secure cloud server).

For each application, it writes the following configuration:

### 1. Cursor
* **Configuration Path**: `~/.cursor/mcp.json`
* **JSON Structure**:
  ```json
  "memwyre": {
    "command": "npx",
    "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer <token>"]
  }
  ```

### 2. VS Code (MCP Client)
* **Configuration Path**: `%APPDATA%\Code\User\mcp.json` (Windows) or `~/Library/Application Support/Code/User/mcp.json` (macOS)
* **JSON Structure**:
  ```json
  "memwyre": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer <token>"]
  }
  ```

### 3. Claude Desktop
* **Configuration Path**: `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)
* **JSON Structure**:
  ```json
  "mcpServers": {
    "memwyre": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer <token>"]
    }
  }
  ```

### 4. Codex
* **Configuration Path**: `~/.codex/config.toml`
* **TOML Structure**:
  ```toml
  [mcp_servers.memwyre]
  enabled = true
  url = "https://server.memwyre.tech/mcp"
  http_headers = { Authorization = "Bearer <token>" }
  ```

### 5. Claude Code
* **Action**: Executes the Claude CLI registration command directly in your shell:
  ```bash
  claude mcp add memwyre -- npx -y mcp-remote https://server.memwyre.tech/mcp --header "Authorization:Bearer <token>"
  ```

### 6. Antigravity
* **Configuration Path**: `~/.gemini/config/mcp_config.json`
* **JSON Structure**:
  ```json
  "memwyre": {
    "command": "npx",
    "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer <token>"]
  }
  ```

---

## Troubleshooting

### Port Conflict Error
If the script fails to start the callback listener, you may see:
```text
Error: listen EADDRINUSE: address already in use 127.0.0.1:XXXX
```
* **Solution**: The script automatically attempts to find an open port, but firewall rules or VPN clients can block local loopback binds. Disable active VPNs or corporate proxy configurations during authentication.

### Token Expiration Warning
If your IDE displays authentication errors:
* Run the installer again (`npx -y install-memwyre`) to renew your token and update configuration files automatically.
* Alternatively, generate an API key from your web dashboard and manually set it as `MEMWYRE_API_KEY` in your client's environment block.
