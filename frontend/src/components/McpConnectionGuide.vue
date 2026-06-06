<template>
  <div class="mt-6 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 shadow-sm overflow-hidden animate-fade-in">
    <div v-if="!hideHeader" class="px-4 py-4 border-b border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800/50 flex items-center justify-between">
      <div>
        <h3 class="text-sm font-semibold text-gray-900 dark:text-white">MCP Connection Guide</h3>
        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Connect Memwyre to your local AI clients using this new key.</p>
      </div>
      <button @click="$emit('close')" class="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300">
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <!-- Client Tabs -->
    <div v-if="!hideTabs" class="border-b border-gray-200 dark:border-gray-700">
      <nav class="-mb-px flex" aria-label="Tabs">
        <button 
          v-for="tab in tabs" 
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            activeTab === tab.id 
              ? 'border-black text-black dark:border-white dark:text-white' 
              : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300',
            'flex-1 py-3 px-1 text-center border-b-2 font-medium text-xs transition-colors'
          ]"
        >
          {{ tab.name }}
        </button>
      </nav>
    </div>

    <!-- Sub Tabs: One-Line vs Manual -->
    <div class="px-5 pt-4 pb-0 bg-white dark:bg-gray-900/50">
      <div class="flex border-b border-gray-200 dark:border-gray-700 gap-4">
        <button 
          @click="setupMode = 'oneline'"
          :class="setupMode === 'oneline' ? 'border-[#D97757] text-[#D97757]' : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300'"
          class="pb-2 px-1 text-xs font-medium border-b-2 transition-colors"
        >
          One-Line Setup
        </button>
        <button 
          @click="setupMode = 'manual'"
          :class="setupMode === 'manual' ? 'border-[#D97757] text-[#D97757]' : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300'"
          class="pb-2 px-1 text-xs font-medium border-b-2 transition-colors"
        >
          Manual Configuration
        </button>
      </div>
    </div>

    <!-- Tab Content -->
    <div class="p-5 bg-white dark:bg-gray-900/50 min-h-[250px]">
      
      <!-- One-Line Mode -->
      <div v-show="setupMode === 'oneline'" class="space-y-4 animate-fade-in">
        <p v-if="activeTab !== 'openclaw'" class="text-sm text-gray-600 dark:text-gray-300">
          The easiest way to connect. Just run this command in your terminal. It will automatically detect your IDE, log you in, and inject the configuration securely.
        </p>
        <p v-else class="text-sm text-gray-600 dark:text-gray-300">
          Install the Memwyre plugin directly through the OpenClaw CLI.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
            <span>{{ activeTab === 'openclaw' ? 'OpenClaw Plugin Install' : 'Interactive CLI Installer' }}</span>
          </div>
          <div class="relative group">
            <div class="overflow-x-auto custom-scrollbar bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 shadow-sm p-3.5 pr-12">
               <code class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-nowrap select-all">{{ activeTab === 'openclaw' ? 'openclaw plugins install @memwyre/openclaw-plugin' : `npx -y install-memwyre --${activeTab}` }}</code>
            </div>
            <button @click="copy(activeTab === 'openclaw' ? 'openclaw plugins install @memwyre/openclaw-plugin' : `npx -y install-memwyre --${activeTab}`, 'oneline')" class="absolute top-[50%] -translate-y-[50%] right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.oneline" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Manual Mode -->
      <div v-show="setupMode === 'manual'">
      
      <!-- Claude Desktop -->
      <div v-show="activeTab === 'claude'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Open Claude Desktop, go to <strong>Settings > Developer</strong>, and click <strong>Edit Config</strong>. Add the Memwyre server configuration inside the <code>"mcpServers"</code> object.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
          <div class="mb-2 flex items-start gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono break-all">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>%APPDATA%\Claude\claude_desktop_config.json (Windows)<br>~/Library/Application Support/Claude/claude_desktop_config.json (Mac)</span>
          </div>
          <div class="relative group mt-3">
            <pre class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-pre-wrap overflow-x-auto p-3.5 bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 custom-scrollbar shadow-sm">{{ claudeConfig }}</pre>
            <button @click="copy(claudeConfig, 'claude')" class="absolute top-2.5 right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.claude" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Cursor -->
      <div v-show="activeTab === 'cursor'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Go to the <strong>Settings</strong> > <strong>Open tools and MCPs</strong> > click on <strong>New MCP server</strong>. Add the code below to the config file under the key <code>"mcpServers"</code>.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>~/.cursor/mcp.json</span>
          </div>
          <div class="relative group mt-3">
            <pre class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-pre-wrap overflow-x-auto p-3.5 bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 custom-scrollbar shadow-sm">{{ cursorConfig }}</pre>
            <button @click="copy(cursorConfig, 'cursor')" class="absolute top-2.5 right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.cursor" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- VS Code -->
      <div v-show="activeTab === 'vscode'" class="space-y-4 animate-fade-in">
         <p class="text-sm text-gray-600 dark:text-gray-300">
          Open VS Code and edit the <code>mcp.json</code> file in your VS Code User directory. Add the Memwyre server configuration inside the <code>"servers"</code> object.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
          <div class="mb-2 flex items-start gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono break-all">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>%APPDATA%\Code\User\mcp.json</span>
          </div>
          <div class="relative group mt-3">
            <pre class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-pre-wrap overflow-x-auto p-3.5 bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 custom-scrollbar shadow-sm">{{ vscodeConfig }}</pre>
            <button @click="copy(vscodeConfig, 'vscode')" class="absolute top-2.5 right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.vscode" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Claude Code (CLI) -->
      <div v-show="activeTab === 'claudecode'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Run the following command in your terminal where you use <a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview" target="_blank" class="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 underline font-medium">Claude Code</a> to automatically inject the Memwyre MCP configuration.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
            <span>Terminal Command</span>
          </div>
          <div class="relative group">
            <div class="overflow-x-auto custom-scrollbar bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 shadow-sm p-3.5 pr-12">
               <code class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-nowrap select-all">{{ `claude mcp add memwyre -- npx -y mcp-remote https://server.memwyre.tech/mcp --header "Authorization:Bearer ${apiKey}"` }}</code>
            </div>
            <button @click="copy(`claude mcp add memwyre -- npx -y mcp-remote https://server.memwyre.tech/mcp --header \&#34;Authorization:Bearer ${apiKey}\&#34;`, 'claudecode')" class="absolute top-[50%] -translate-y-[50%] right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.claudecode" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-if="!copied.claudecode" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Codex -->
      <div v-show="activeTab === 'codex'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Open <strong>Settings</strong> > click on <strong>MCP Servers</strong> on the left sidebar > click on <strong>Add MCP Server</strong>.
          <br><br>
          • Name the server: <strong>Memwyre</strong><br>
          • Select: <strong>Streamable HTTP</strong><br>
          • Enter Server URL: <code>https://server.memwyre.tech/mcp</code>
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>Header: Authorization</span>
          </div>
          <div class="relative group mt-2">
            <div class="overflow-x-auto custom-scrollbar bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 shadow-sm p-3.5 pr-12">
               <code class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-nowrap select-all">{{ `Bearer ${apiKey}` }}</code>
            </div>
            <button @click="copy(`Bearer ${apiKey}`, 'codex')" class="absolute top-[50%] -translate-y-[50%] right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.codex" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Finally, hit <strong>Save</strong>.
        </p>
      </div>

      <!-- Antigravity -->
      <div v-show="activeTab === 'antigravity'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Open the Antigravity configuration file located at <strong><code>~/.gemini/config/mcp_config.json</code></strong> and add the Memwyre server configuration inside the <strong><code>"mcpServers"</code></strong> object.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>~/.gemini/config/mcp_config.json</span>
          </div>
          <div class="relative group mt-3">
            <pre class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-pre-wrap overflow-x-auto p-3.5 bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 custom-scrollbar shadow-sm">{{ antigravityConfig }}</pre>
            <button @click="copy(antigravityConfig, 'antigravity')" class="absolute top-2.5 right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.antigravity" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>
      <!-- OpenClaw -->
      <div v-show="activeTab === 'openclaw'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Open the OpenClaw configuration file located at <code>~/.openclaw/config.json</code> and add the Memwyre plugin configuration under the <code>"plugins.entries"</code> object.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
          <div class="mb-2 flex items-start gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono break-all">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>~/.openclaw/config.json</span>
          </div>
          <div class="relative group mt-3">
            <pre class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-pre-wrap overflow-x-auto p-3.5 bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 custom-scrollbar shadow-sm">{{ openclawConfig }}</pre>
            <button @click="copy(openclawConfig, 'openclaw')" class="absolute top-2.5 right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.openclaw" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  apiKey: {
    type: String,
    required: true
  },
  initialTab: {
    type: String,
    default: 'claude'
  },
  hideHeader: {
    type: Boolean,
    default: false
  },
  hideTabs: {
    type: Boolean,
    default: false
  }
});

defineEmits(['close']);

const activeTab = ref(props.initialTab || 'claude');
const setupMode = ref('oneline');
const copied = ref({ claude: false, cursor: false, vscode: false, claudecode: false, codex: false, antigravity: false, openclaw: false, oneline: false });

const tabs = [
  { id: 'claude', name: 'Claude Desktop' },
  { id: 'cursor', name: 'Cursor' },
  { id: 'vscode', name: 'VS Code' },
  { id: 'claudecode', name: 'Claude Code' },
  { id: 'codex', name: 'Codex' },
  { id: 'antigravity', name: 'Antigravity' },
  { id: 'openclaw', name: 'OpenClaw' }
];

// Computed JSON config for OpenClaw
const openclawConfig = computed(() => {
  return `"openclaw-plugin": {
  "enabled": true,
  "config": {
    "apiKey": "${props.apiKey}",
    "hostUrl": "https://server.memwyre.tech"
  }
}`;
});

// Computed JSON config for Cursor
const cursorConfig = computed(() => {
  return `{
  "memwyre": {
    "command": "npx",
    "args": [
      "-y",
      "mcp-remote",
      "https://server.memwyre.tech/mcp",
      "--header",
      "Authorization:Bearer ${props.apiKey}"
    ]
  }
}`;
});

// Computed JSON config for Claude Desktop (Stdio wrapper)
const claudeConfig = computed(() => {
  return `"memwyre": {
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "https://server.memwyre.tech/mcp",
    "--header",
    "Authorization:Bearer ${props.apiKey}"
  ]
}`;
});

// Computed JSON config for Antigravity
const antigravityConfig = computed(() => {
  return `"memwyre": {
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "https://server.memwyre.tech/mcp",
    "--header",
    "Authorization:Bearer ${props.apiKey}"
  ]
}`;
});

// Computed JSON config for VS Code
const vscodeConfig = computed(() => {
  return `"memwyre": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "https://server.memwyre.tech/mcp",
    "--header",
    "Authorization:Bearer ${props.apiKey}"
  ]
}`;
});

const copy = async (text, tab) => {
  try {
    await navigator.clipboard.writeText(text);
    copied.value[tab] = true;
    setTimeout(() => { copied.value[tab] = false; }, 2000);
  } catch (err) {
    console.error('Failed to copy', err);
  }
};
</script>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Thinner scrollbar override for code blocks */
.custom-scrollbar::-webkit-scrollbar {
    height: 4px;
    width: 4px;
}
</style>
