# YouTube Ingestion

Memwyre can read directly from YouTube videos — no manual note-taking or transcript copying required.

## Overview

When you provide a YouTube URL, Memwyre automatically fetches the video's transcript, title, and description in the background. Hours of video content become instantly searchable, semantic text inside your memory vault.

## How It Works

1. **Paste the link** — Drop a YouTube URL into the Memwyre chat, or save it as a new memory from your Inbox.
2. **Automatic extraction** — Memwyre fetches the English transcript (manual captions or auto-generated).
3. **Semantic storage** — The transcript is chunked and embedded into your vault. You can then ask questions like:

   > *"What was the main takeaway from that machine learning video I saved yesterday?"*

   Memwyre answers using exact quotes from the video.

## Supported URL Formats

| Format | Example |
|---|---|
| Standard watch URL | `youtube.com/watch?v=...` |
| YouTube Shorts | `youtube.com/shorts/...` |
| Short link | `youtu.be/...` |
| Embedded iframe URL | `youtube.com/embed/...` |

## Tips

- Videos with **manually created captions** produce better quality memories than auto-generated ones.
- If a video has no English captions available, ingestion will be skipped and you'll see an error in your Inbox.
- Long videos (1 hour+) may take a few seconds longer to process.
