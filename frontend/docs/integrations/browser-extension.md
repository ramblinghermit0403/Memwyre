---
title: Memwyre Chrome/Edge Extension Setup
description: Learn how to install and use the Memwyre Chrome/Edge extension to capture web pages and chat context instantly.
---
# Browser Extension

Connect your second brain directly to your browser. The Memwyre browser extension lets you capture content, save notes, and seamlessly inject memory into AI tools like ChatGPT, Claude, and Gemini — without leaving your current tab.

## Installation

The Memwyre extension is built on **Manifest V3** and distributed as a standalone ZIP file. Install it manually using Chrome or Edge's built-in Developer Mode (no Chrome Web Store account required).

### Manifest Specifications (Version 1.1.1)
* **API Version**: Manifest V3
* **Required Permissions**:
  * `activeTab`: To read context from the currently open browser tab.
  * `storage`: To securely cache authentication tokens and settings locally.
  * `sidePanel`: Exposes the sidebar interface for search and vault discovery.
  * `contextMenus`: Adds right-click triggers like "Save to Memwyre".
* **Host Permissions**: Limited to `https://server.memwyre.tech/*` and `https://memwyre.tech/*` to preserve user privacy.

### Step 1 — Download & Extract

1. Download the `extension.zip` file from your [Memwyre dashboard](https://memwyre.tech) or the direct link provided to you.
2. Extract the ZIP into a permanent folder on your computer. **Do not move or delete this folder** after loading the extension — doing so will break it.

### Step 2 — Load into Chrome or Edge

1. Open your browser and navigate to the Extensions page:
   - **Chrome**: `chrome://extensions/`
   - **Edge**: `edge://extensions/`
2. Toggle **Developer mode** ON (top-right corner).
3. Click **Load unpacked**.
4. Select the folder you extracted in Step 1.

The Memwyre icon will now appear in your browser toolbar. ✅

## Authentication & Setup

Before saving memories, you need to link the extension to your account:

1. Click the Memwyre icon in your toolbar to open the side panel.
2. Open [memwyre.tech](https://memwyre.tech) and go to **Settings**.
3. Click **"Copy Extension Token"**.
4. Paste the token into the extension popup when prompted.

## Features

Once installed and authenticated, you get:

| Feature | Description |
|---|---|
| **AI Site Integration** | Native adapters inject memory into `chatgpt.com`, `claude.ai`, `gemini.google.com`, and **`perplexity.ai`**. |
| **Turndown Serialization** | Integrates **`turndown.min.js`** to convert HTML page scopes into clean, formatted Markdown on the client-side before sync. |
| **One-Click Capture** | Highlight any text, right-click, and select **"Save to Memwyre"**. |
| **Side Panel Search** | Search your vault or review your Inbox directly from the sidebar. |

## Troubleshooting

**The extension doesn't appear after loading it.**  
Make sure Developer Mode is enabled and that you selected the correct unzipped folder (not the ZIP file itself).

**My token isn't being accepted.**  
Regenerate your token from **Settings → Extension Token** and paste it again. Tokens expire after 30 days.
