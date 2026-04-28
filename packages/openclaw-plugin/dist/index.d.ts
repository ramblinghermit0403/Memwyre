/**
 * MemWyre Plugin for OpenClaw
 * Provides persistent memory and context retrieval tools.
 *
 * Tools:
 *   - save_memory:    Save a note/memory to the MemWyre Vault.
 *   - search_memwyre: Search the MemWyre Vault for relevant context.
 */
import type { OpenClawPluginApi } from "openclaw/plugin-sdk";
declare const memwyrePlugin: {
    id: string;
    name: string;
    description: string;
    configSchema: {
        type: string;
        properties: {
            apiKey: {
                type: string;
                description: string;
            };
            hostUrl: {
                type: string;
                description: string;
                default: string;
            };
        };
        required: string[];
        additionalProperties: boolean;
    };
    register(api: OpenClawPluginApi): void;
};
export default memwyrePlugin;
