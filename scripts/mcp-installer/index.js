#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log("======================================");
console.log(" MemWyre MCP Universal Installer ");
console.log("======================================\n");

// Dynamically resolve the absolute path to the backend directory
const installerDir = __dirname;
const backendDir = path.resolve(installerDir, '..', '..', 'backend');

// Configuration payload for MemWyre MCP Server
const memwyreConfig = {
    command: "uv",
    args: ["run", "mcp_server.py"],
    cwd: backendDir,
    env: {} // Allows inheriting user environment variables
};

// Merge standard configuration structure
function mergeConfig(existingConfig) {
    if (!existingConfig.mcpServers) {
        existingConfig.mcpServers = {};
    }
    existingConfig.mcpServers["memwyre"] = memwyreConfig;
    return existingConfig;
}

// Utility to read, merge, and save JSON gracefully
function configureFile(clientName, filePath) {
    console.log(`Checking ${clientName} configuration...`);
    try {
        if (!fs.existsSync(filePath)) {
            // Create directories recursively if missing
            const dir = path.dirname(filePath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
            }
            // Initialize empty config file
            fs.writeFileSync(filePath, JSON.stringify({ mcpServers: {} }, null, 2));
            console.log(`  Created new config file at ${filePath}`);
        }

        const data = fs.readFileSync(filePath, 'utf8');
        let config = {};
        try {
            config = data.trim() === "" ? {} : JSON.parse(data);
        } catch (e) {
            console.warn(`  [Warning] Could not parse existing JSON in ${filePath}. Resetting config.`);
        }
        
        const newConfig = mergeConfig(config);
        fs.writeFileSync(filePath, JSON.stringify(newConfig, null, 2));
        console.log(`  \x1b[32m\u2713 Successfully installed for ${clientName}\x1b[0m\n`);
    } catch (error) {
        console.error(`  \x1b[31m\u2717 Failed to configure ${clientName}: ${error.message}\x1b[0m\n`);
    }
}

const APPDATA = process.env.APPDATA;
const USERPROFILE = process.env.USERPROFILE;

// 1. Cursor Native MCP
if (USERPROFILE) configureFile("Cursor (Native)", path.join(USERPROFILE, '.cursor', 'mcp.json'));

// 2. Cursor Roo-Code & Cline Extensions
if (APPDATA) {
    configureFile("Cursor Roo-Code", path.join(APPDATA, 'Cursor', 'User', 'globalStorage', 'rooveterinaryinc.roo-cline', 'settings', 'cline_mcp_settings.json'));
    configureFile("Cursor Claude-Dev", path.join(APPDATA, 'Cursor', 'User', 'globalStorage', 'saoudrizwan.claude-dev', 'settings', 'cline_mcp_settings.json'));
}

// 3. Windsurf
if (USERPROFILE) configureFile("Windsurf", path.join(USERPROFILE, '.codeium', 'windsurf', 'mcp_config.json'));

// 4. Claude Desktop
if (APPDATA) configureFile("Claude Desktop", path.join(APPDATA, 'Claude', 'claude_desktop_config.json'));

// 5. Antigravity Codex
if (USERPROFILE) configureFile("Antigravity Codex", path.join(USERPROFILE, '.gemini', 'antigravity', 'mcp.json'));

// 6. Claude Code (CLI)
console.log("Checking Claude Code (CLI)...");
try {
    execSync("claude --version", { stdio: 'ignore' });
    console.log("  Claude Code CLI detected. Adding MemWyre...");
    // The '--' escapes args being passed directly to uv
    execSync(`claude mcp add memwyre uv -- run --directory "${backendDir}" mcp_server.py`, { stdio: 'inherit' });
    console.log(`  \x1b[32m\u2713 Successfully installed for Claude Code\x1b[0m\n`);
} catch (e) {
    console.log("  \x1b[33m- Claude Code CLI not found or failed. Skipping.\x1b[0m\n");
}

console.log("======================================");
console.log(" Installation Complete!");
console.log(" You may need to restart your IDEs or clients to load the new server.");
console.log("======================================\n");
