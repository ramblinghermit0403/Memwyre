/**
 * iconResolver.js
 * 
 * Utility functions for dynamically resolving SVG icons or favicons based on 
 * an item's tags, source string, or other metadata properties.
 * 
 * Includes built-in SVG representations for known AI agents/LLM integrations
 * (e.g. Antigravity, Cursor, Claude Code, OpenClaw, Codex)
 */

import antigravityIcon from '../assets/Google-Antigravity-Icon-Full-Color.png';
import claudeIcon from '../assets/claude-color.svg';
import geminiIcon from '../assets/gemini-color.svg';
import openaiIcon from '../assets/openai.svg';
import openclawIcon from '../assets/openclaw-color.svg';
import perplexityIcon from '../assets/perplexity-color.svg';

// SVG Strings for known AI clients
export const KNOWN_CLIENT_ICONS = {
    antigravity: { type: 'img', content: antigravityIcon },
    cursor: { type: 'svg', content: `<svg viewBox="0 0 24 24" fill="currentColor" class="w-full h-full text-indigo-500"><path d="M6.028 1.488A1.5 1.5 0 0 1 7.23 1.05l14 4a1.5 1.5 0 0 1 .465 2.59l-6.236 4.757 2.112 8.448a1.5 1.5 0 0 1-2.903.725l-2.434-9.736-6.684-1.215a1.5 1.5 0 0 1-1.077-2.155l3.555-6.977Z" /></svg>` },
    claude: { type: 'img', content: claudeIcon },
    'claude code': { type: 'img', content: claudeIcon },
    openclaw: { type: 'img', content: openclawIcon },
    perplexity: { type: 'img', content: perplexityIcon },
    codex: { type: 'svg', content: `<svg viewBox="0 0 24 24" fill="none" class="w-full h-full text-emerald-500" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>` },
    youtube: { type: 'svg', content: `<svg viewBox="0 0 24 24" fill="currentColor" class="w-full h-full text-red-600"><path d="M21.582,6.186c-0.23-0.86-0.908-1.538-1.768-1.768C18.254,4,12,4,12,4S5.746,4,4.186,4.418 c-0.86,0.23-1.538,0.908-1.768,1.768C2,7.746,2,12,2,12s0,4.254,0.418,5.814c0.23,0.86,0.908,1.538,1.768,1.768 C5.746,20,12,20,12,20s6.254,0,7.814-0.418c0.86-0.23,1.538-0.908,1.768-1.768C22,16.254,22,12,22,12S22,7.746,21.582,6.186z M10,15.464V8.536L16,12L10,15.464z"/></svg>` },
    chatgpt: { type: 'img', content: openaiIcon },
    gemini: { type: 'img', content: geminiIcon }
};

const DEFAULT_DOC_ICON = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" class="w-full h-full"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>`;
const DEFAULT_WEB_ICON = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" class="w-full h-full"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>`;

/**
 * Returns an object describing how the icon should be rendered.
 * @param {Object} item - The document, memory, or inbox item
 * @returns {Object} { type: 'svg' | 'img', content: string }
 */
export function getIconForSource(item) {
    if (!item) return { type: 'svg', content: DEFAULT_DOC_ICON };

    // 1. Check the source property FIRST (most reliable indicator)
    if (item.source) {
        const sourceStr = item.source.toLowerCase();

        // 1a. YouTube check
        if (sourceStr.includes('youtube.com') || sourceStr.includes('youtu.be')) {
            return KNOWN_CLIENT_ICONS.youtube;
        }

        // 1b. Known specific chatbot agents and apps
        if (sourceStr.includes('chatgpt') || sourceStr.includes('chat gpt') || sourceStr.includes('chat.openai.com')) {
            return KNOWN_CLIENT_ICONS.chatgpt;
        }
        if (sourceStr.includes('gemini') || sourceStr.includes('gemni') || sourceStr.includes('gemini.google.com')) {
            return KNOWN_CLIENT_ICONS.gemini;
        }
        if (sourceStr.includes('perplexity') || sourceStr.includes('perplexity.ai')) {
            return KNOWN_CLIENT_ICONS.perplexity;
        }
        if (sourceStr.includes('claude') || sourceStr.includes('anthropic')) {
            return KNOWN_CLIENT_ICONS.claude;
        }
        if (sourceStr.includes('cursor')) {
            return KNOWN_CLIENT_ICONS.cursor;
        }
        if (sourceStr.includes('openclaw')) {
            return KNOWN_CLIENT_ICONS.openclaw;
        }
        if (sourceStr.includes('codex')) {
            return KNOWN_CLIENT_ICONS.codex;
        }
        if (sourceStr.includes('antigravity') || sourceStr === 'mcp') {
            return KNOWN_CLIENT_ICONS.antigravity;
        }

        // 1c. Agent Drop Fallback
        if (sourceStr === 'agent_drop') {
            return { type: 'svg', content: DEFAULT_DOC_ICON };
        }

        // 1d. Try parsing as a URL for a favicon
        try {
            let urlString = item.source;
            if (!urlString.startsWith('http://') && !urlString.startsWith('https://')) {
                if (urlString.includes('.') && !urlString.includes(' ')) {
                    urlString = 'https://' + urlString;
                } else {
                    // Not a URL, fall through to tag check
                }
            }

            if (urlString.startsWith('http')) {
                const url = new URL(urlString);
                const domain = url.hostname;
                const faviconUrl = `https://www.google.com/s2/favicons?domain=${domain}&sz=64`;
                return { type: 'img', content: faviconUrl };
            }
        } catch (e) {
            // Not a valid URL, fall through to tag check
        }
    }

    // 2. Fallback: Check Tags for Known Integrations / MCP tools
    if (item.tags && Array.isArray(item.tags)) {
        const lowerTags = item.tags.map(t => typeof t === 'string' ? t.toLowerCase() : '');
        for (const [key, iconObj] of Object.entries(KNOWN_CLIENT_ICONS)) {
            if (lowerTags.includes(key)) {
                return iconObj;
            }
        }
    }

    // Default Fallback
    return { type: 'svg', content: DEFAULT_DOC_ICON };
}
