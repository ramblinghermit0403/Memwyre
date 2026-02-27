<template>
  <div class="mt-6 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 shadow-sm overflow-hidden animate-fade-in">
    <div class="px-4 py-4 border-b border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800/50 flex items-center justify-between">
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
    <div class="border-b border-gray-200 dark:border-gray-700">
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

    <!-- Tab Content -->
    <div class="p-5 bg-white dark:bg-gray-900/50 min-h-[250px]">
      
      <!-- Claude Desktop -->
      <div v-show="activeTab === 'claude'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Add Memwyre to your Claude Desktop configuration file.
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
          Open Cursor Settings (<kbd class="px-1 py-0.5 bg-gray-100 dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded text-xs shadow-sm shadow-gray-200/50 dark:shadow-none">Ctrl/Cmd + Shift + J</kbd>), go to <strong>Features > MCP</strong>, and click <strong>+ Add New MCP Server</strong>.
          Set Name to <strong>Memwyre</strong> and Type to <strong>command</strong>.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
            <span>Command</span>
          </div>
          <div class="relative group">
            <div class="overflow-x-auto custom-scrollbar bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 shadow-sm p-3.5 pr-12">
               <code class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-nowrap select-all">{{ `npx -y mcp-remote http://server.memwyre.tech/mcp --header "Authorization:Bearer ${apiKey}"` }}</code>
            </div>
            <button @click="copy(`npx -y mcp-remote http://server.memwyre.tech/mcp --header \&#34;Authorization:Bearer ${apiKey}\&#34;`, 'cursor')" class="absolute top-[50%] -translate-y-[50%] right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.cursor" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- VS Code (Cline) -->
      <div v-show="activeTab === 'vscode'" class="space-y-4 animate-fade-in">
         <p class="text-sm text-gray-600 dark:text-gray-300">
          Add Memwyre to your Cline or RooCode configuration file in VS Code.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
          <div class="mb-2 flex items-start gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono break-all">
            <svg class="w-4 h-4 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <span>%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json</span>
          </div>
          <div class="relative group mt-3">
            <pre class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-pre-wrap overflow-x-auto p-3.5 bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 custom-scrollbar shadow-sm">{{ claudeConfig }}</pre>
            <button @click="copy(claudeConfig, 'vscode')" class="absolute top-2.5 right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.vscode" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Claude Code (CLI) -->
      <div v-show="activeTab === 'claudecode'" class="space-y-4 animate-fade-in">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Add Memwyre to Anthropic's terminal tool, <a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview" target="_blank" class="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 underline font-medium">Claude Code</a>.
        </p>
        <div class="bg-gray-50 dark:bg-gray-800/60 p-3 rounded-lg border border-gray-200 dark:border-gray-700">
           <div class="mb-2 flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 font-mono">
            <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
            <span>Terminal Command</span>
          </div>
          <div class="relative group">
            <div class="overflow-x-auto custom-scrollbar bg-white dark:bg-gray-900 rounded-md border border-gray-200 dark:border-gray-700 shadow-sm p-3.5 pr-12">
               <code class="text-[11px] sm:text-xs text-gray-800 dark:text-gray-200 font-mono whitespace-nowrap select-all">{{ `claude mcp add memwyre -- npx -y mcp-remote http://server.memwyre.tech/mcp --header "Authorization:Bearer ${apiKey}"` }}</code>
            </div>
            <button @click="copy(`claude mcp add memwyre -- npx -y mcp-remote http://server.memwyre.tech/mcp --header \&#34;Authorization:Bearer ${apiKey}\&#34;`, 'claudecode')" class="absolute top-[50%] -translate-y-[50%] right-2.5 p-1.5 bg-white dark:bg-gray-800 text-gray-400 hover:text-gray-800 dark:hover:text-white rounded-md opacity-0 group-hover:opacity-100 transition-all border border-gray-200 dark:border-gray-600 shadow-sm hover:shadow">
               <svg v-if="!copied.claudecode" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
               <svg v-else class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </button>
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
  }
});

defineEmits(['close']);

const activeTab = ref('claude');
const copied = ref({ claude: false, cursor: false, vscode: false, claudecode: false });

const tabs = [
  { id: 'claude', name: 'Claude Desktop' },
  { id: 'cursor', name: 'Cursor / Windsurf' },
  { id: 'vscode', name: 'VS Code' },
  { id: 'claudecode', name: 'Claude Code' }
];

// Computed JSON config for Claude/Cline
const claudeConfig = computed(() => {
  return `{
  "mcpServers": {
    "memwyre": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "http://server.memwyre.tech/mcp",
        "--header",
        "Authorization:Bearer ${props.apiKey}"
      ]
    }
  }
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
