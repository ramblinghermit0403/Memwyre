// OpenClaw MemWyre Plugin
// Provides save_memory and search_memwyre tools for persistent context.

import { Type } from "@sinclair/typebox";

interface PluginConfig {
    apiKey?: string;
    hostUrl?: string;
}

export default async function setup(api: any, config: PluginConfig | undefined) {
    const cfg = config || {} as PluginConfig;
    const hostUrl = (cfg.hostUrl || "https://server.memwyre.tech").replace(/\/$/, "");
    const apiKey = cfg.apiKey || "";

    const checkConfigured = (): string | null => {
        if (!apiKey) {
            return "MemWyre plugin is not configured. Please set your apiKey in ~/.openclaw/openclaw.json under plugins.entries.openclaw-plugin.config.";
        }
        return null;
    };

    api.registerTool({
        name: "save_memory",
        description: "Save a new memory snippet to the MemWyre Vault. Use this tool when the user explicitly asks you to 'remember' something, 'save' a note, or when you encounter important information that should be persisted for future reference.",
        parameters: Type.Object({
            text: Type.String({ description: "The content of the memory or note to save." }),
            tags: Type.Optional(Type.Array(Type.String(), { description: "Optional list of tags." }))
        }),
        execute: async (args: { text: string; tags?: string[] }) => {
            const configError = checkConfigured();
            if (configError) return configError;
            try {
                const response = await fetch(`${hostUrl}/api/v1/llm/save_memory`, {
                    method: "POST",
                    headers: {
                        "Authorization": `Bearer ${apiKey}`,
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        content: args.text,
                        source_llm: "openclaw",
                        model_name: "openclaw-agent",
                        url: "openclaw CLI",
                        tags: args.tags || []
                    }),
                });

                if (!response.ok) {
                    const err = await response.text();
                    throw new Error(`Failed to save memory: ${response.status} ${err}`);
                }

                const data = (await response.json()) as any;
                return `Memory saved successfully to MemWyre Inbox with ID: ${data.id}`;
            } catch (error: any) {
                return `Error saving memory: ${error.message}`;
            }
        }
    });

    api.registerTool({
        name: "search_memwyre",
        description: "Search MemWyre for context or previous memories. Use this to retrieve notes, project specs, or any personal context before answering questions.",
        parameters: Type.Object({
            query: Type.String({ description: "The semantic search query." })
        }),
        execute: async (args: { query: string }) => {
            const configError = checkConfigured();
            if (configError) return configError;
            try {
                const response = await fetch(`${hostUrl}/api/v1/llm/retrieve_context`, {
                    method: "POST",
                    headers: {
                        "Authorization": `Bearer ${apiKey}`,
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        query: args.query,
                        limit_tokens: 2000
                    }),
                });

                if (!response.ok) {
                    const err = await response.text();
                    throw new Error(`Failed to search MemWyre: ${response.status} ${err}`);
                }

                const data = (await response.json()) as any;
                if (!data.context_text || data.context_text.trim() === "") {
                    return "No relevant memories found in MemWyre for this query.";
                }
                return `Found in MemWyre:\n${data.context_text}`;
            } catch (error: any) {
                return `Error searching MemWyre: ${error.message}`;
            }
        }
    });

    console.log("[MemWyre] OpenClaw plugin initialized successfully.");
}
