/**
 * iconResolver.js — Extension port of the web app's icon engine.
 * No bundler/imports needed. Attach to window for use in sidepanel.js.
 *
 * Match order: source string → tag lookup → URL favicon → default doc icon.
 */

(function () {

  // Inline SVGs for non-image icons
  const SVG_CURSOR = `<svg viewBox="0 0 24 24" fill="currentColor" style="color:#6366f1;width:100%;height:100%"><path d="M6.028 1.488A1.5 1.5 0 0 1 7.23 1.05l14 4a1.5 1.5 0 0 1 .465 2.59l-6.236 4.757 2.112 8.448a1.5 1.5 0 0 1-2.903.725l-2.434-9.736-6.684-1.215a1.5 1.5 0 0 1-1.077-2.155l3.555-6.977Z" /></svg>`;
  const SVG_CODEX  = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" style="color:#10b981;width:100%;height:100%"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>`;
  const SVG_YT     = `<svg viewBox="0 0 24 24" fill="currentColor" style="color:#ef4444;width:100%;height:100%"><path d="M21.582,6.186c-0.23-0.86-0.908-1.538-1.768-1.768C18.254,4,12,4,12,4S5.746,4,4.186,4.418c-0.86,0.23-1.538,0.908-1.768,1.768C2,7.746,2,12,2,12s0,4.254,0.418,5.814c0.23,0.86,0.908,1.538,1.768,1.768C5.746,20,12,20,12,20s6.254,0,7.814-0.418c0.86-0.23,1.538-0.908,1.768-1.768C22,16.254,22,12,22,12S22,7.746,21.582,6.186zM10,15.464V8.536L16,12L10,15.464z"/></svg>`;
  const SVG_WEB    = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" style="width:100%;height:100%;opacity:0.5"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>`;
  const SVG_DOC    = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" style="width:100%;height:100%;opacity:0.5"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>`;

  // Known clients — img entries use the Google favicon service so no bundled assets needed.
  const KNOWN = {
    chatgpt:      { type: 'img', content: 'https://www.google.com/s2/favicons?domain=chatgpt.com&sz=64' },
    claude:       { type: 'img', content: 'https://www.google.com/s2/favicons?domain=claude.ai&sz=64' },
    gemini:       { type: 'img', content: 'https://www.google.com/s2/favicons?domain=gemini.google.com&sz=64' },
    perplexity:   { type: 'img', content: 'https://www.google.com/s2/favicons?domain=perplexity.ai&sz=64' },
    openclaw:     { type: 'img', content: 'https://www.google.com/s2/favicons?domain=openclaw.dev&sz=64' },
    antigravity:  { type: 'img', content: 'https://www.google.com/s2/favicons?domain=google.com&sz=64' },
    cursor:       { type: 'svg', content: SVG_CURSOR },
    codex:        { type: 'svg', content: SVG_CODEX },
    youtube:      { type: 'svg', content: SVG_YT },
  };

  /**
   * Returns { type: 'svg'|'img', content: string } for a given item.
   * Matches the web app's getIconForSource signature exactly.
   */
  function getIconForSource(item) {
    if (!item) return { type: 'svg', content: SVG_DOC };

    let rawSource = item.source;
    if (item.source_app && (item.source_app.startsWith('http') || item.source_app.includes('.'))) {
      rawSource = item.source_app;
    }

    const src = (rawSource || '').toLowerCase();

    if (src) {
      // YouTube
      if (src.includes('youtube.com') || src.includes('youtu.be')) return KNOWN.youtube;
      // ChatGPT / OpenAI
      if (src.includes('chatgpt') || src.includes('chat gpt') || src.includes('chat.openai.com')) return KNOWN.chatgpt;
      // Gemini
      if (src.includes('gemini') || src.includes('gemni') || src.includes('gemini.google.com')) return KNOWN.gemini;
      // Perplexity
      if (src.includes('perplexity')) return KNOWN.perplexity;
      // Claude / Anthropic
      if (src.includes('claude') || src.includes('anthropic')) return KNOWN.claude;
      // Cursor
      if (src.includes('cursor')) return KNOWN.cursor;
      // OpenClaw
      if (src.includes('openclaw')) return KNOWN.openclaw;
      // Codex
      if (src.includes('codex')) return KNOWN.codex;
      // Antigravity / MCP
      if (src.includes('antigravity') || src === 'mcp') return KNOWN.antigravity;
      // Agent Drop
      if (src === 'agent_drop') return { type: 'svg', content: SVG_DOC };

      // Generic URL → Google favicon service
      try {
        let urlStr = typeof rawSource === 'string' ? rawSource : '';
        if (!urlStr.startsWith('http://') && !urlStr.startsWith('https://')) {
          if (urlStr.includes('.') && !urlStr.includes(' ')) urlStr = 'https://' + urlStr;
        }
        if (urlStr.startsWith('http')) {
          const domain = new URL(urlStr).hostname;
          return { type: 'img', content: `https://www.google.com/s2/favicons?domain=${domain}&sz=64` };
        }
      } catch (_) { /* not a URL, fall through */ }
    }

    // Tag-based lookup (same as web app)
    if (item.tags && Array.isArray(item.tags)) {
      const lowerTags = item.tags.map(t => (typeof t === 'string' ? t.toLowerCase() : ''));
      for (const [key, iconObj] of Object.entries(KNOWN)) {
        if (lowerTags.includes(key)) return iconObj;
      }
    }

    return { type: 'svg', content: SVG_DOC };
  }

  // Expose globally
  window.getIconForSource = getIconForSource;
  window.KNOWN_CLIENT_ICONS = KNOWN;

})();
