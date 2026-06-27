/**
 * Memwyre Plugin for OpenClaw
 * Provides persistent memory and context retrieval tools.
 *
 * Tools:
 *   - save_memory:    Save a note/memory to the Memwyre Vault.
 *   - search_memwyre: Search the Memwyre Vault for relevant context.
 */

import { readFileSync } from "node:fs";
import { Type } from "@sinclair/typebox";
import type { OpenClawPluginApi } from "openclaw/plugin-sdk";

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/** 
 * Wrap a plain string in the structured content format OpenClaw tools must return. 
 */
function toolResult(text: string) {
    return {
        content: [{ type: "text" as const, text }],
        details: {}
    };
}

/**
 * Strip JSON keys from free-text that the OpenClaw message parser might
 * misinterpret as reasoning / role blocks, crashing the agent.
 */
function sanitize(raw: string): string {
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
    name: "Memwyre",
    description: "Persistent memory and context retrieval for OpenClaw, powered by Memwyre.",
    configSchema: {
        type: "object",
        properties: {
            apiKey: {
                type: "string",
                description: "Your Memwyre API Key (starts with bv_sk_)",
            },
            hostUrl: {
                type: "string",
                description: "Memwyre server URL",
                default: "https://server.memwyre.tech",
            },
        },
        required: ["apiKey"],
        additionalProperties: false,
    },

    register(api: OpenClawPluginApi) {
        const config = (api.pluginConfig || {}) as { apiKey?: string; hostUrl?: string };
        const hostUrl = (config.hostUrl || "https://server.memwyre.tech").replace(/\/$/, "");
        const apiKey = config.apiKey || "";

        const headers: Record<string, string> = {
            "Content-Type": "application/json",
            ...(apiKey ? { Authorization: `Bearer ${apiKey}` } : {}),
        };

        // Loop-protection state
        let lastSearchQuery = "";

        // -----------------------------------------------------------------------
        // Tool: save_memory
        // -----------------------------------------------------------------------
        api.registerTool(
            (ctx) => ({
                name: "save_memory",
                label: "Save Memory",
                description:
                    "Save a new memory snippet to the Memwyre Vault. " +
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

                async execute(_id: string, params: Record<string, unknown>) {
                    if (!apiKey) {
                        return toolResult(
                            "Memwyre plugin is not configured. " +
                            "Set your apiKey under plugins.entries.openclaw-plugin.config in openclaw.json.",
                        );
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

                        const data = (await res.json()) as { id?: string };
                        return toolResult(`Memory saved to Memwyre Inbox (ID: ${data.id || "unknown"}).`);
                    } catch {
                        return toolResult("Network error while saving memory. Move on to the next step.");
                    }
                }
            }),
            { name: "save_memory" }
        );

        // -----------------------------------------------------------------------
        // Tool: search_memwyre
        // -----------------------------------------------------------------------
        api.registerTool(
            (ctx) => ({
                name: "search_memwyre",
                label: "Search Memwyre",
                description:
                    "Search Memwyre for context or previous memories. " +
                    "Use this to retrieve notes, project specs, or personal context " +
                    "before answering questions that may require prior knowledge.",
                parameters: Type.Object({
                    query: Type.String({
                        description: "The semantic search query."
                    })
                }),

                async execute(_id: string, params: Record<string, unknown>) {
                    if (!apiKey) {
                        return toolResult(
                            "Memwyre plugin is not configured. " +
                            "Set your apiKey under plugins.entries.openclaw-plugin.config in openclaw.json.",
                        );
                    }

                    const query = String(params.query || "");

                    if (query === lastSearchQuery) {
                        return toolResult(
                            "Duplicate query — you already searched for this. " +
                            "Do not search again. Proceed with what you have.",
                        );
                    }

                    try {
                        const res = await fetch(`${hostUrl}/api/v1/llm/retrieve_context`, {
                            method: "POST",
                            headers,
                            body: JSON.stringify({ query, limit_tokens: 2000 }),
                        });

                        if (!res.ok) {
                            return toolResult(
                                `Failed to search Memwyre (HTTP ${res.status}). ` +
                                "Stop searching and inform the user.",
                            );
                        }

                        const data = (await res.json()) as { context_text?: string };
                        lastSearchQuery = query;

                        const raw = data.context_text?.trim();
                        if (!raw) {
                            return toolResult("No relevant memories found in Memwyre for this query.");
                        }

                        return toolResult(`Found in Memwyre:\n${sanitize(raw)}`);
                    } catch {
                        return toolResult(
                            "Network error while searching Memwyre. Stop searching and inform the user.",
                        );
                    }
                }
            }),
            { name: "search_memwyre" }
        );

        api.logger.info(`[Memwyre] plugin v${pluginVersion} initialised (host: ${hostUrl})`);
    },
};

// ---------------------------------------------------------------------------
// Version helper
// ---------------------------------------------------------------------------

let pluginVersion = "unknown";
try {
    const pkg = JSON.parse(
        readFileSync(new URL("../package.json", import.meta.url), "utf8"),
    );
    pluginVersion = pkg.version || "unknown";
} catch {
    // silently ignore — version string is informational only
}

export default memwyrePlugin;
