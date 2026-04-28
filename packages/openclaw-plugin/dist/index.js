/**
 * MemWyre Plugin for OpenClaw
 * Provides persistent memory and context retrieval tools.
 *
 * Tools:
 *   - save_memory:    Save a note/memory to the MemWyre Vault.
 *   - search_memwyre: Search the MemWyre Vault for relevant context.
 */
import { readFileSync } from "node:fs";
import { Type } from "@sinclair/typebox";
// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
/**
 * Wrap a plain string in the structured content format OpenClaw tools must return.
 */
function toolResult(text) {
    return {
        content: [{ type: "text", text }],
        details: {}
    };
}
/**
 * Strip JSON keys from free-text that the OpenClaw message parser might
 * misinterpret as reasoning / role blocks, crashing the agent.
 */
function sanitize(raw) {
    return raw
        .replace(/"role"\s*:/gi, '"_role":')
        .replace(/"reasoning"\s*:/gi, '"_reasoning":')
        .replace(/"thought"\s*:/gi, '"_thought":')
        .replace(/"content"\s*:/gi, '"_content":');
}
// ---------------------------------------------------------------------------
// Plugin Definition
// ---------------------------------------------------------------------------
const memwyrePlugin = {
    id: "openclaw-plugin",
    name: "MemWyre",
    description: "Persistent memory and context retrieval for OpenClaw, powered by MemWyre.",
    configSchema: {
        type: "object",
        properties: {
            apiKey: {
                type: "string",
                description: "Your MemWyre API Key (starts with bv_sk_)",
            },
            hostUrl: {
                type: "string",
                description: "MemWyre server URL",
                default: "https://server.memwyre.tech",
            },
        },
        required: ["apiKey"],
        additionalProperties: false,
    },
    register(api) {
        const config = (api.pluginConfig || {});
        const hostUrl = (config.hostUrl || "https://server.memwyre.tech").replace(/\/$/, "");
        const apiKey = config.apiKey || "";
        const headers = {
            "Content-Type": "application/json",
            ...(apiKey ? { Authorization: `Bearer ${apiKey}` } : {}),
        };
        // Loop-protection state
        let lastSearchQuery = "";
        // -----------------------------------------------------------------------
        // Tool: save_memory
        // -----------------------------------------------------------------------
        api.registerTool((ctx) => ({
            name: "save_memory",
            label: "Save Memory",
            description: "Save a new memory snippet to the MemWyre Vault. " +
                "Use when the user asks you to 'remember' something, " +
                "'save' a note, or when you encounter important information " +
                "that should be persisted for future reference.",
            parameters: Type.Object({
                text: Type.String({
                    description: "The content of the memory or note to save."
                }),
                tags: Type.Optional(Type.Array(Type.String(), {
                    description: "Optional list of tags."
                }))
            }),
            async execute(_id, params) {
                if (!apiKey) {
                    return toolResult("MemWyre plugin is not configured. " +
                        "Set your apiKey under plugins.entries.openclaw-plugin.config in openclaw.json.");
                }
                const text = String(params.text || "");
                const tags = Array.isArray(params.tags) ? params.tags.map(String) : [];
                try {
                    const res = await fetch(`${hostUrl}/api/v1/llm/save_memory`, {
                        method: "POST",
                        headers,
                        body: JSON.stringify({
                            content: text,
                            source_llm: "openclaw",
                            model_name: "openclaw-agent",
                            url: "openclaw",
                            tags,
                        }),
                    });
                    if (!res.ok) {
                        return toolResult(`Failed to save memory (HTTP ${res.status}). Move on to the next step.`);
                    }
                    const data = (await res.json());
                    return toolResult(`Memory saved to MemWyre Inbox (ID: ${data.id || "unknown"}).`);
                }
                catch {
                    return toolResult("Network error while saving memory. Move on to the next step.");
                }
            }
        }), { name: "save_memory" });
        // -----------------------------------------------------------------------
        // Tool: search_memwyre
        // -----------------------------------------------------------------------
        api.registerTool((ctx) => ({
            name: "search_memwyre",
            label: "Search MemWyre",
            description: "Search MemWyre for context or previous memories. " +
                "Use this to retrieve notes, project specs, or personal context " +
                "before answering questions that may require prior knowledge.",
            parameters: Type.Object({
                query: Type.String({
                    description: "The semantic search query."
                })
            }),
            async execute(_id, params) {
                if (!apiKey) {
                    return toolResult("MemWyre plugin is not configured. " +
                        "Set your apiKey under plugins.entries.openclaw-plugin.config in openclaw.json.");
                }
                const query = String(params.query || "");
                if (query === lastSearchQuery) {
                    return toolResult("Duplicate query — you already searched for this. " +
                        "Do not search again. Proceed with what you have.");
                }
                try {
                    const res = await fetch(`${hostUrl}/api/v1/llm/retrieve_context`, {
                        method: "POST",
                        headers,
                        body: JSON.stringify({ query, limit_tokens: 2000 }),
                    });
                    if (!res.ok) {
                        return toolResult(`Failed to search MemWyre (HTTP ${res.status}). ` +
                            "Stop searching and inform the user.");
                    }
                    const data = (await res.json());
                    lastSearchQuery = query;
                    const raw = data.context_text?.trim();
                    if (!raw) {
                        return toolResult("No relevant memories found in MemWyre for this query.");
                    }
                    return toolResult(`Found in MemWyre:\n${sanitize(raw)}`);
                }
                catch {
                    return toolResult("Network error while searching MemWyre. Stop searching and inform the user.");
                }
            }
        }), { name: "search_memwyre" });
        api.logger.info(`[MemWyre] plugin v${pluginVersion} initialised (host: ${hostUrl})`);
    },
};
// ---------------------------------------------------------------------------
// Version helper
// ---------------------------------------------------------------------------
let pluginVersion = "unknown";
try {
    const pkg = JSON.parse(readFileSync(new URL("../package.json", import.meta.url), "utf8"));
    pluginVersion = pkg.version || "unknown";
}
catch {
    // silently ignore — version string is informational only
}
export default memwyrePlugin;
