#!/usr/bin/env node
import * as p from '@clack/prompts';
import pc from 'picocolors';
import fs from 'fs';
import path from 'path';
import os from 'os';
import open from 'open';
import express from 'express';
import toml from '@iarna/toml';

const MEMWYRE_MCP_URL_NATIVE = 'https://server.memwyre.tech/mcp';

// Helper to determine paths
const getAppData = () => process.env.APPDATA || (process.platform === 'darwin' ? path.join(os.homedir(), 'Library', 'Application Support') : path.join(os.homedir(), '.config'));

const IDE_CONFIGS = {
  'cursor': {
    name: 'Cursor',
    clientName: 'Cursor',
    getPath: () => path.join(os.homedir(), '.cursor', 'mcp.json'),
    getSettings: (token) => ({
      command: 'npx',
      args: ['-y', 'mcp-remote', MEMWYRE_MCP_URL_NATIVE, '--header', `Authorization:Bearer ${token}`]
    })
  },
  'vscode': {
    name: 'VS Code',
    clientName: 'VS Code',
    getPath: () => {
      return path.join(getAppData(), 'Code', 'User', 'mcp.json');
    },
    getSettings: (token) => ({
      type: 'stdio',
      command: 'npx',
      args: ['-y', 'mcp-remote', MEMWYRE_MCP_URL_NATIVE, '--header', `Authorization:Bearer ${token}`]
    })
  },
  'claude': {
    name: 'Claude Desktop',
    clientName: 'Claude Desktop',
    getPath: () => path.join(getAppData(), 'Claude', 'claude_desktop_config.json'),
    getSettings: (token) => ({
      command: 'npx',
      args: ['-y', 'mcp-remote', MEMWYRE_MCP_URL_NATIVE, '--header', `Authorization:Bearer ${token}`]
    })
  },
  'codex': {
    name: 'Codex',
    clientName: 'Codex',
    getPath: () => path.join(os.homedir(), '.codex', 'config.toml'),
    getSettings: (token) => ({
      enabled: true,
      url: MEMWYRE_MCP_URL_NATIVE,
      http_headers: {
        Authorization: `Bearer ${token}`
      }
    })
  },
  'claudecode': {
    name: 'Claude Code',
    clientName: 'Claude Code',
    execute: async (token) => {
      const { exec } = await import('child_process');
      const util = await import('util');
      const execAsync = util.promisify(exec);
      await execAsync(`claude mcp add memwyre -- npx -y mcp-remote ${MEMWYRE_MCP_URL_NATIVE} --header "Authorization:Bearer ${token}"`);
    }
  },
  'antigravity': {
    name: 'Antigravity',
    clientName: 'Antigravity',
    getPath: () => path.join(os.homedir(), '.gemini', 'config', 'mcp_config.json'),
    getSettings: (token) => ({
      command: 'npx',
      args: ['-y', 'mcp-remote', MEMWYRE_MCP_URL_NATIVE, '--header', `Authorization:Bearer ${token}`]
    })
  }
};

async function authenticate(clientName) {
  return new Promise((resolve, reject) => {
    const app = express();
    let server;
    
    app.get('/callback', (req, res) => {
      const token = req.query.token;
      if (token) {
        res.send('<html><body style="font-family: sans-serif; text-align: center; padding: 50px;"><h2>Authentication Successful!</h2><p>You can close this tab and return to your terminal.</p></body></html>');
        resolve(token);
        setTimeout(() => server.close(), 1000);
      } else {
        res.status(400).send('Missing token');
        reject(new Error('Missing token in callback'));
        setTimeout(() => server.close(), 1000);
      }
    });

    server = app.listen(0, async () => {
      const port = server.address().port;
      const redirectUri = `http://localhost:${port}/callback`;
      // Use production URL or fallback to localhost for development
      const frontendUrl = process.env.MEMWYRE_FRONTEND_URL || 'https://memwyre.tech';
      const authUrl = `${frontendUrl}/login?cli_port=${port}&client=${encodeURIComponent(clientName)}`;
      
      p.log.info(`Opening your browser to authenticate with Memwyre...`);
      await open(authUrl);
    });
  });
}

async function updateMcpConfig(ideKey, token) {
  const ide = IDE_CONFIGS[ideKey];
  
  if (ide.execute) {
    p.log.info(`Executing CLI installation for ${ide.name}...`);
    try {
      await ide.execute(token);
      p.log.success(`Successfully configured ${pc.cyan(ide.name)}`);
    } catch (e) {
      throw new Error(`Failed to configure ${ide.name}: ${e.message}`);
    }
    return;
  }

  const configPath = ide.getPath();
  const isToml = configPath.endsWith('.toml');
  const isVSCode = ide.clientName === 'VS Code';
  const rootKey = isToml ? 'mcp_servers' : (isVSCode ? 'servers' : 'mcpServers');
  
  let config = { [rootKey]: {} };
  
  if (fs.existsSync(configPath)) {
    try {
      const content = fs.readFileSync(configPath, 'utf8');
      if (isToml) {
        config = toml.parse(content);
        if (!config.mcp_servers) config.mcp_servers = {};
      } else {
        config = JSON.parse(content);
        if (!config[rootKey]) config[rootKey] = {};
      }
    } catch (e) {
      p.log.warn(`Could not parse existing config at ${configPath}. Overwriting.`);
    }
  } else {
    // Ensure directory exists
    const dir = path.dirname(configPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
  }
  
  if (isToml) {
    config[rootKey]['memwyre'] = ide.getSettings(token);
    fs.writeFileSync(configPath, toml.stringify(config), 'utf8');
  } else {
    config[rootKey]['memwyre'] = ide.getSettings(token)[rootKey]?.memwyre || ide.getSettings(token);
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');
  }
  
  p.log.success(`Successfully configured ${pc.cyan(ide.name)} at ${configPath}`);
}

async function main() {
  p.intro(pc.bgCyan(pc.black(' Memwyre MCP Installer ')));

  const args = process.argv.slice(2);
  let selectedIde = null;

  // Simple argument parsing, e.g., --cursor, --claude, --vscode, --codex
  const argMap = {
    '--cursor': 'cursor',
    '--claude': 'claude',
    '--vscode': 'vscode',
    '--codex': 'codex',
    '--claudecode': 'claudecode',
    '--antigravity': 'antigravity'
  };

  for (const arg of args) {
    if (argMap[arg.toLowerCase()]) {
      selectedIde = argMap[arg.toLowerCase()];
      break;
    } else if (arg.startsWith('--client=')) {
      selectedIde = arg.split('=')[1].toLowerCase();
      break;
    } else if (arg === '-codex') {
      selectedIde = 'codex';
      break;
    }
  }

  if (!selectedIde || !IDE_CONFIGS[selectedIde]) {
    selectedIde = await p.select({
      message: 'Which IDE would you like to configure?',
      options: [
        { value: 'cursor', label: 'Cursor', hint: 'recommended' },
        { value: 'claude', label: 'Claude Desktop' },
        { value: 'vscode', label: 'VS Code' },
        { value: 'codex', label: 'Codex' },
        { value: 'claudecode', label: 'Claude Code' },
        { value: 'antigravity', label: 'Antigravity' }
      ],
    });

    if (p.isCancel(selectedIde)) {
      p.cancel('Operation cancelled.');
      process.exit(0);
    }
  } else {
    p.log.step(`Auto-selected IDE: ${IDE_CONFIGS[selectedIde].name}`);
  }

  const s = p.spinner();
  const ideInfo = IDE_CONFIGS[selectedIde];

  try {
    s.start(`Waiting for authentication for ${ideInfo.name}...`);
    const token = await authenticate(ideInfo.clientName);
    s.stop(`Authenticated successfully!`);

    await updateMcpConfig(selectedIde, token);
    
    p.outro(pc.green('Memwyre is now connected! Please restart your IDE.'));
    process.exit(0);
  } catch (err) {
    s.stop(`Installation failed.`);
    p.log.error(err.message);
    process.exit(1);
  }
}

main().catch(console.error);
