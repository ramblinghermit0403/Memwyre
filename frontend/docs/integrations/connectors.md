---
title: Connecting Data Sources to Memwyre
description: Configure data connectors to sync Memwyre memory graphs automatically with Notion, GitHub, Google Drive, and more.
---
# Workspace Connectors

Synchronize your existing workspace knowledge bases with Memwyre. Connectors sync documents, issues, chat channels, and databases into your memory vault, keeping your context updated automatically.

---

## 1. Notion Sync

Bring your Notion pages and database tables into your vector store.

### Configuration
1. Go to your Memwyre dashboard and navigate to **Settings → Integrations → Notion**.
2. Click **Connect Notion**. This redirects you to the official Notion workspace authorisation screen.
3. Select the specific pages or workspaces you want Memwyre to access.
4. Click **Allow Access** to complete the authentication.

### Sync Details
* **Frequency**: Memwyre pulls updates from authorized pages every 6 hours.
* **Format**: Notion pages are parsed, converted into clean Markdown block arrays, and embedded as separate documents in your vault.

---

## 2. GitHub Connector

Keep your codebase references, commits, PRs, and issues in sync.

### Setup via Webhooks
Instead of full repository read access, Memwyre can sync context using lightweight webhooks:
1. In your GitHub Repository, go to **Settings → Webhooks → Add Webhook**.
2. Set the **Payload URL** to:
   `https://api.memwyre.tech/v1/webhooks/github`
3. Set **Content type** to `application/json`.
4. Paste your webhook secret (generated from your Memwyre dashboard integrations tab) into the **Secret** field.
5. Under events, select **"Let me select individual events"** and select:
   * [x] Pull Requests
   * [x] Issues
   * [x] Pushes / Commits
6. Click **Add webhook**.

---

## 3. Slack Connector

Index public team communications to resolve code questions later.

### Setup Steps
1. Navigate to **Integrations → Slack** on your dashboard.
2. Click **Add to Slack** and authorise the Memwyre bot.
3. Invite the bot into the channels you want indexed by sending a message in the channel:
   ```text
   /invite @Memwyre
   ```

### Privacy Filtering
* Memwyre **never** indexes Direct Messages (DMs) or private channels.
* Messages containing sensitive keyword markers (e.g. `[private]` or `[secret]`) are ignored by the parser.

---

## 4. Cloud Storage (Google Drive, OneDrive, S3)

Sync entire document folders, assets, or static manuals.

| Provider | Setup Method | Sync Schedule | Supported Extensions |
|---|---|---|---|
| **Google Drive** | OAuth Integration via Settings page | Every 24 hours | `.pdf`, `.docx`, `.txt`, `.gdoc` |
| **OneDrive** | Microsoft Graph App Authorization | Every 24 hours | `.pdf`, `.docx`, `.xlsx`, `.txt` |
| **S3 / R2 Buckets** | AWS IAM Credentials & Bucket Name | Real-time (SQS event) | `.pdf`, `.md`, `.json`, `.csv` |

### Setting up S3 Sync
Add your read-only IAM credentials to your configuration block or backend environment:
```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=secret...
AWS_REGION=us-east-1
S3_BUCKET_NAME=my-memwyre-vault
```
If you configure AWS S3 Event Notifications pointing to our SQS queues, new files placed in your bucket are indexed instantly.
