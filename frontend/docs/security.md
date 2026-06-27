# Security & Privacy

Privacy is not an afterthought — it is the core design philosophy of Memwyre. As your unified memory layer, Memwyre handles sensitive codebase structures, credentials, and personal notes. This page details our security architecture and data governance practices.

---

## 1. The Zero-Knowledge Standard

Our primary mandate is that **your data belongs to you**. In cloud-connected setups, Memwyre uses a Zero-Knowledge design for prompt evaluation and context retrieval:

* **No Query Logging**: Your search queries, generated prompts, and context payloads are evaluated in-memory and never logged to permanent disk storage on our servers.
* **On-the-Fly Processing**: Documents and code snippets sent for vectorization are processed immediately and saved to your isolated database instance. Raw file contents are not archived in flat files or accessible by third parties.
* **Local Processing Options**: When running self-hosted, 100% of the ingestion, vectorization, and inference is kept within your local network. No external API calls are made.

---

## 2. Data Encryption

Memwyre enforces industry-standard encryption protocols at every lifecycle stage of your data:

### Token Authorization & Session Expiration
* Client connections are authenticated using JSON Web Tokens (JWT) signed via the `HS256` algorithm.
* **Access Tokens**: Expire after **15 minutes** to minimize leakage vectors.
* **Refresh Tokens**: Expire after **30 days** before requiring a new login challenge.
* **Rate Limits**: Free tier accounts are capped at a token quota threshold of **100,000 tokens daily** (`MAX_DAILY_TOKENS`), backed by Redis-based token buckets.
* **Bot Defenses**: External entry points (like signup/login pages) validate requests against Cloudflare Turnstile CAPTCHA checks.

### In Transit
* All API connections between client platforms (the Chrome Extension, CLI, MCP Server, and IDEs) and the Memwyre server require HTTPS.
* We enforce **TLS 1.3** (with TLS 1.2 fallback) for all network endpoints, protecting your data against interception or man-in-the-middle attacks.

### At Rest
* Vector embeddings and metadata indices stored in our cloud databases are encrypted using **AES-256**.
* API tokens and service integration credentials (e.g., Notion, GitHub secrets) are double-encrypted using a salted key-derivation function before storage.

---

## 3. Workspace Sandboxing

When you connect local IDEs (like Cursor or VS Code) to your Memwyre MCP Server, your model gains high-speed search capabilities. To prevent cross-project context leakages:

* **Workspace Boundaries**: The MCP server restricts search scopes to the active project folder. An AI agent working on a personal project cannot retrieve context from a work codebase unless explicitly configured.
* **Path Filtering**: You can declare paths or pattern exclusions (similar to `.gitignore` files) inside your workspace configurations to prevent the indexing of sensitive directories (like `.env`, `.git`, or `node_modules`).
* **Process Isolation**: The local MCP process runs under standard user-level permissions. It cannot scan systemic network directories or read from disks outside of your workspace folder without permission.

---

## 4. Third-Party AI Integrations

When using Memwyre to inject context into chat interfaces (e.g. ChatGPT, Claude.ai, or Gemini):

* The browser extension injects retrieved context directly into the browser's DOM textarea before submission.
* The data is processed by the AI vendor (OpenAI, Anthropic, Google) under their standard enterprise privacy policies. Memwyre does not store or intercept the final LLM response.
* For maximum security, we recommend opting out of data training within your respective OpenAI, Anthropic, or Google account settings.
