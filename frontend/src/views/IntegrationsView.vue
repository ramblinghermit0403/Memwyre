<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />
    
    <main class="flex-1 overflow-hidden w-full max-w-4xl mx-auto py-10 px-4 sm:px-6 lg:px-8 flex flex-col h-full">
      <div class="flex-none">
          <div class="mb-8">
            <h1 class="text-3xl font-bold text-gray-900 dark:text-text-primary">Integrations</h1>
          </div>
      </div>

      <!-- Scrollable Content Area -->
      <div class="flex-1 overflow-y-auto min-h-0 pr-2 custom-scrollbar">
          <div class="bg-white dark:bg-surface shadow rounded-lg px-8 py-8 border border-gray-100 dark:border-border animate-fade-in">
               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-text-primary mb-2">Integrations Ecosystem</h3>
               <p class="text-sm text-gray-500 dark:text-text-secondary mb-8">Connect MemWyre with your favorite tools and agents.</p>
               
               <!-- Integrations Showcase Grid -->
               <div v-for="category in integrationCategories" :key="category.name" class="mb-10">
                   <div class="flex items-center justify-between mb-4">
                       <h4 class="text-md font-semibold text-gray-900 dark:text-text-primary">{{ category.name }}</h4>
                       <div class="flex gap-2">
                           <button class="p-1 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300">
                               <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>
                           </button>
                           <button class="p-1 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300">
                               <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
                           </button>
                       </div>
                   </div>
                   
                   <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                       <div v-for="item in category.items" :key="item.id" class="flex flex-col bg-gray-50 dark:bg-[#1C1F26] rounded-xl p-5 border border-gray-100 dark:border-gray-800 relative transition-transform hover:scale-[1.02] hover:shadow-md cursor-pointer">
                           <!-- Docs Badge -->
                           <div v-if="item.hasDocs" class="absolute top-4 right-4 flex items-center text-gray-500 dark:text-gray-400 text-xs font-medium">
                               <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                               Docs
                           </div>
                           
                           <!-- Logo -->
                           <div class="h-10 w-10 mb-4 flex items-center justify-center rounded-lg" :class="item.bgColor || 'bg-gray-200 dark:bg-gray-800'">
                               <img v-if="item.icon" :src="item.icon" class="w-6 h-6 object-contain" :class="{'invert dark:invert-0': item.invert}" />
                               <svg v-else class="w-6 h-6 text-gray-500 dark:text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                           </div>
                           
                           <!-- Title & PRO badge -->
                           <div class="flex items-center gap-2 mb-2">
                               <h3 class="font-semibold text-gray-900 dark:text-gray-100 text-sm">{{ item.name }}</h3>
                               <span v-if="item.isPro" class="px-1.5 py-0.5 text-[10px] uppercase font-bold tracking-wider rounded border border-[#0066FF] text-[#0066FF] dark:text-[#3388FF] dark:border-[#3388FF]">PRO</span>
                           </div>
                           
                           <!-- Description -->
                           <p class="text-xs text-gray-500 dark:text-gray-400 mb-6 flex-grow line-clamp-3 leading-relaxed">
                               {{ item.desc }}
                           </p>
                           
                           <!-- Action Button -->
                           <div class="flex justify-end mt-auto">
                               <button 
                                 class="px-4 py-1.5 rounded-full text-xs font-medium transition-colors flex items-center shadow-sm"
                                 :class="item.btnText === 'Connect' ? 'bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700' : 'bg-[#0F172A] dark:bg-black border border-transparent text-white hover:bg-gray-800 dark:hover:bg-gray-900'"
                                 @click.stop="handleConnectClientClick(item)"
                               >
                                   <svg v-if="item.isLightning" class="w-3.5 h-3.5 mr-1 text-blue-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.381z" clip-rule="evenodd" /></svg>
                                   {{ item.btnText }}
                               </button>
                           </div>
                       </div>
                   </div>
               </div>

               <template v-if="false">
               <hr class="border-gray-100 dark:border-border my-10" />

               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-text-primary mb-2">Connected LLM Clients</h3>
               <p class="text-sm text-gray-500 dark:text-text-secondary mb-6">Manage external LLM providers and their permissions.</p>
               
               <!-- Keys List -->
               <div class="space-y-3 mb-8" v-if="keys.length > 0">
                    <div v-for="key in keys" :key="key.id" class="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg border border-gray-200 dark:border-gray-600">
                      <div class="flex items-center gap-3">
                        <div class="p-2 bg-white dark:bg-gray-600 rounded-md shadow-sm">
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" /></svg>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-medium text-gray-900 dark:text-text-primary capitalize">{{ key.provider }}</span>
                            <div class="flex gap-2 mt-0.5">
                                <span v-if="key.permissions.read" class="text-[10px] uppercase font-bold tracking-wider text-black dark:text-white">Read</span>
                                <span v-if="key.permissions.write" class="text-[10px] uppercase font-bold tracking-wider text-black dark:text-white">Write</span>
                            </div>
                        </div>
                      </div>
                      <button @click="deleteKey(key.id)" class="text-gray-400 hover:text-red-600 dark:text-gray-500 dark:hover:text-red-400 p-2 transition-colors">
                          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                      </button>
                    </div>
               </div>
               
                   <!-- API Keys Management -->
                   <div class="mb-8">
                       <div class="flex items-center justify-between mb-4">
                           <h4 class="text-sm font-medium text-gray-900 dark:text-text-primary">Your API Keys</h4>
                       </div>
                       
                       <!-- Empty State -->
                       <div v-if="apiKeys.length === 0" class="text-center py-8 bg-gray-50 dark:bg-gray-700/30 rounded-lg border-2 border-dashed border-gray-200 dark:border-gray-600">
                           <svg class="mx-auto h-10 w-10 text-gray-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" /></svg>
                           <h3 class="text-sm font-medium text-gray-900 dark:text-text-primary">No API Keys Found</h3>
                           <p class="mt-1 text-sm text-gray-500 dark:text-gray-400 max-w-sm mx-auto mb-5">Click "Connect" on an integration above to generate an API key.</p>
                       </div>

                       <!-- List -->
                       <div v-else class="space-y-3">
                            <div v-for="key in apiKeys" :key="key.id" class="flex items-center justify-between p-3 bg-white dark:bg-gray-700 rounded-lg border border-gray-200 dark:border-gray-600 shadow-sm transition-all hover:shadow-md">
                                <div class="flex items-center gap-3">
                                    <div class="p-2 bg-gray-100 dark:bg-gray-600 rounded-md">
                                        <svg class="w-5 h-5 text-gray-500 dark:text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" /></svg>
                                    </div>
                                    <div>
                                        <div class="flex items-center gap-2">
                                            <span class="font-medium text-gray-900 dark:text-text-primary">{{ key.name }}</span>
                                            <span v-if="!key.is_active" class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-gray-200 dark:bg-gray-600 text-gray-600 dark:text-gray-300">REVOKED</span>
                                        </div>
                                        <div class="text-xs text-gray-500 dark:text-text-secondary font-mono mt-0.5 flex items-center gap-2">
                                            <span>{{ key.prefix }} • Created {{ new Date(key.created_at).toLocaleDateString() }}</span>
                                        </div>
                                    </div>
                                </div>
                                <button @click="revokeKeyConfirm(key.id)" class="text-gray-400 hover:text-red-600 dark:text-gray-500 dark:hover:text-red-400 p-2 transition-colors" title="Revoke Key">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                </button>
                            </div>
                       </div>
                   </div>

               <div class="mt-10 pt-8 border-t border-gray-100 dark:border-border">
                  <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-text-primary mb-2">Browser Extension Auth</h3>
                  <p class="text-sm text-gray-500 dark:text-text-secondary mb-6">Use this token to log in to the Brain Vault extension.</p>
                  
                  <div class="flex items-center gap-4">
                     <button @click="copyToken" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] transition-colors">
                       <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
                       <span v-if="tokenCopied">Copied!</span>
                       <span v-else>Copy Token</span>
                     </button>
                  </div>
               </div>
               </template>
          </div>
      </div>
    </main>
    
    <ConfirmationModal
      :is-open="showDeleteModal"
      title="Remove Key"
      message="Are you sure you want to remove this API key? This action cannot be undone."
      confirm-text="Remove"
      :loading="deletingKey"
      @confirm="confirmDeleteKey"
      @cancel="showDeleteModal = false"
    />
    
    <!-- Integration Modal -->
    <div v-if="showIntegrationModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6" @click.self="closeIntegrationModal">
        <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-sm transition-opacity" @click="closeIntegrationModal"></div>
        <div class="relative bg-white dark:bg-gray-800 rounded-xl shadow-xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col animate-fade-in">
            <div class="px-5 py-4 border-b border-gray-100 dark:border-gray-700 flex justify-between items-center bg-gray-50/50 dark:bg-gray-800/50">
                <div class="flex items-center gap-3">
                    <div class="h-8 w-8 flex items-center justify-center rounded-lg" :class="selectedIntegration?.bgColor || 'bg-gray-200'">
                        <img v-if="selectedIntegration?.icon" :src="selectedIntegration?.icon" class="w-5 h-5 object-contain" :class="{'invert dark:invert-0': selectedIntegration?.invert}" />
                    </div>
                    <div>
                        <h3 class="text-base font-semibold text-gray-900 dark:text-white">Connect to {{ selectedIntegration?.name }}</h3>
                    </div>
                </div>
                <button @click="closeIntegrationModal" class="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300 p-1 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
                </button>
            </div>
            
            <div class="p-5 overflow-y-auto custom-scrollbar">
                <div v-if="isExistingKey" class="mb-5 bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg border border-blue-200 dark:border-blue-800/50">
                    <h4 class="text-sm font-medium text-blue-800 dark:text-blue-300 flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        Existing API Key Found
                    </h4>
                    <p class="text-xs text-blue-700 dark:text-blue-400 mt-1">You already have an API key named "{{ selectedIntegration?.name }}". For security, we cannot show you the full secret again. If you lost it, you can generate a new one.</p>
                    <button @click="generateKeyForIntegration(selectedIntegration.name, true)" class="mt-3 px-3 py-1.5 bg-white dark:bg-gray-800 text-blue-600 dark:text-blue-400 border border-blue-200 dark:border-blue-700 rounded text-xs font-medium hover:bg-blue-50 dark:hover:bg-gray-700 transition-colors shadow-sm">
                        <LoadingLogo v-if="generatingKey" size="sm" class="w-3 h-3 inline mr-1" />
                        Regenerate Key
                    </button>
                </div>

                <div v-if="!isExistingKey && integrationApiKey !== '<YOUR_API_KEY>'" class="mb-5 bg-green-50 dark:bg-green-900/20 p-4 rounded-lg border border-green-200 dark:border-green-800/50">
                    <h4 class="text-sm font-medium text-green-800 dark:text-green-300 flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                        API Key Generated
                    </h4>
                    <p class="text-xs text-green-700 dark:text-green-400 mt-1 mb-2">Please copy the command below. You won't be able to see the API key again after you close this popup.</p>
                </div>

                <McpConnectionGuide 
                    :apiKey="integrationApiKey" 
                    :initialTab="mapIntegrationToTab(selectedIntegration?.id)"
                    :hideHeader="true"
                    :hideTabs="true"
                    @close="closeIntegrationModal"
                    class="!mt-0 shadow-none border-none rounded-none"
                />
            </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import api from '../services/api';
import apiKeysService from '../services/apiKeys'; 
import NavBar from '../components/NavBar.vue';
import ConfirmationModal from '../components/ConfirmationModal.vue';
import McpConnectionGuide from '../components/McpConnectionGuide.vue';
import { useToast } from 'vue-toastification';
import LoadingLogo from '@/components/common/LoadingLogo.vue';

const authStore = useAuthStore();
const toast = useToast();

const keys = ref([]);
const newKey = ref({
  provider: 'openai',
  api_key: '',
  permissions: { read: true, write: false, auto_save: false }
});
const tokenCopied = ref(false);

const integrationCategories = ref([
  {
    name: 'MCP Client Connections',
    items: [
      { id: 'cursor', name: 'Cursor', desc: 'One-click MCP install in Cursor', btnText: 'Connect', hasDocs: true, bgColor: 'bg-black dark:bg-black', icon: 'https://unpkg.com/@lobehub/icons-static-svg@latest/icons/cursor.svg', invert: true },
      { id: 'claude-desktop', name: 'Claude Desktop', desc: 'Connect supermemory in Claude Desktop', btnText: 'Connect', hasDocs: true, bgColor: 'bg-[#D97757]/10 dark:bg-[#D97757]/20', icon: 'https://unpkg.com/@lobehub/icons-static-svg@latest/icons/claude-color.svg' },
      { id: 'vscode', name: 'VS Code', desc: 'Native MCP support for VS Code', btnText: 'Connect', bgColor: 'bg-blue-500/10 dark:bg-blue-500/20', icon: '/src/assets/vscode.svg' },
      { id: 'antigravity', name: 'Antigravity', desc: 'Integrate directly into the Antigravity system', btnText: 'Connect', hasDocs: true, bgColor: 'bg-white dark:bg-white', icon: 'https://unpkg.com/@lobehub/icons-static-svg@latest/icons/antigravity-color.svg' },
      { id: 'codex', name: 'Codex', desc: 'Persistent memory for the Codex CLI — free on every plan', btnText: 'Connect', hasDocs: true, bgColor: 'bg-[#10A37F]/10 dark:bg-[#10A37F]/20', icon: 'https://unpkg.com/@lobehub/icons-static-svg@latest/icons/codex-color.svg' }
    ]
  },
  {
    name: 'Plugins',
    items: [
      { id: 'claude-code', name: 'Claude Code', isPro: true, desc: 'Remembers your conventions, decisions, and project context', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-[#D97757]/10 dark:bg-[#D97757]/20', icon: '/src/assets/claude-color.svg' },
      { id: 'opencode', name: 'OpenCode', isPro: true, desc: 'Long-term memory for your OpenCode sessions', btnText: 'Upgrade', isLightning: true, hasDocs: true, bgColor: 'bg-gray-200 dark:bg-gray-700', icon: 'https://unpkg.com/@lobehub/icons-static-svg@latest/icons/opencode.svg' },
      { id: 'openclaw', name: 'OpenClaw', isPro: true, desc: 'Add persistent memory to autonomous OpenClaw agent sessions', btnText: 'Upgrade', isLightning: true, hasDocs: true, bgColor: 'bg-[#FF3366]/10 dark:bg-[#FF3366]/20', icon: '/src/assets/openclaw-color.svg' }
    ]
  },
  {
    name: 'Knowledge bases',
    items: [
      { id: 'gdrive', name: 'Google Drive', isPro: true, desc: 'Sync Docs, Sheets and Slides into your memory', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-gray-100 dark:bg-white/10', icon: '/src/assets/google-drive.svg' },
      { id: 'notion', name: 'Notion', isPro: true, desc: 'Import Notion pages and databases', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-white dark:bg-black', icon: '/src/assets/notion-svgrepo-com.svg' },
      { id: 'onedrive', name: 'OneDrive', isPro: true, desc: 'Bring in Office documents from OneDrive', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-blue-500/10 dark:bg-blue-500/20', icon: '/src/assets/onedrive.svg' }
    ]
  }
]);

// Loading States
const addingKey = ref(false);
const deletingKey = ref(false);

// API Keys Logic
const apiKeys = ref([]);
const generatingKey = ref(false);

// Modal State
const showIntegrationModal = ref(false);
const selectedIntegration = ref(null);
const integrationApiKey = ref("<YOUR_API_KEY>");
const isExistingKey = ref(false);

const closeIntegrationModal = () => {
    showIntegrationModal.value = false;
    selectedIntegration.value = null;
};

const mapIntegrationToTab = (id) => {
    if (id === 'claude-desktop') return 'claude';
    if (id === 'cursor') return 'cursor';
    if (id === 'vscode') return 'vscode';
    if (id === 'claude-code') return 'claudecode';
    if (id === 'codex') return 'codex';
    if (id === 'antigravity') return 'antigravity';
    if (id === 'openclaw') return 'openclaw';
    if (id === 'opencode') return 'opencode';
    if (id === 'windsurf') return 'windsurf';
    return 'claude';
};

const handleConnectClientClick = async (item) => {
    selectedIntegration.value = item;
    
    const existingKey = apiKeys.value.find(k => k.name.toLowerCase() === item.name.toLowerCase() && k.is_active);
    
    if (existingKey) {
        integrationApiKey.value = "<YOUR_API_KEY>";
        isExistingKey.value = true;
        showIntegrationModal.value = true;
    } else {
        isExistingKey.value = false;
        await generateKeyForIntegration(item.name);
    }
};

const loadApiKeys = async () => {
    try {
        const res = await apiKeysService.listKeys();
        apiKeys.value = res.data;
    } catch (err) {
        console.error("Failed to list keys", err);
    }
};

const generateKeyForIntegration = async (name, isRegenerate = false) => {
    generatingKey.value = true;
    try {
        if (isRegenerate) {
            const existingKey = apiKeys.value.find(k => k.name.toLowerCase() === name.toLowerCase() && k.is_active);
            if (existingKey) {
                await apiKeysService.revokeKey(existingKey.id);
            }
        }
        
        const res = await apiKeysService.createKey(name);
        integrationApiKey.value = res.data.key;
        isExistingKey.value = false;
        showIntegrationModal.value = true;
        toast.success("API Key generated successfully");
        loadApiKeys();
    } catch (err) {
        toast.error("Failed to generate key");
    } finally {
        generatingKey.value = false;
    }
};

const loadKeys = async () => {
  try {
    const res = await api.get('/user/llm-keys');
    keys.value = res.data;
  } catch (err) {
    console.error(err);
  }
};

const keyToDelete = ref(null);
const showDeleteModal = ref(false);

const deleteKey = (id) => {
  keyToDelete.value = id;
  showDeleteModal.value = true;
};

const revokeKeyConfirm = (id) => {
  keyToDelete.value = id;
  showDeleteModal.value = true;
};

const confirmDeleteKey = async () => {
    if (!keyToDelete.value) return;
    deletingKey.value = true;
    try {
        const isUserKey = apiKeys.value.some(k => k.id === keyToDelete.value);

        if (isUserKey) {
             await apiKeysService.revokeKey(keyToDelete.value);
             loadApiKeys();
        } else {
             await api.delete(`/user/llm-keys/${keyToDelete.value}`);
             loadKeys();
        }
        
        toast.success("Key removed");
        showDeleteModal.value = false;
        keyToDelete.value = null;
    } catch (err) {
        toast.error("Failed to remove key");
    } finally {
        deletingKey.value = false;
    }
};

const copyToken = async () => {
  if (!authStore.token) {
    return toast.error("No token available");
  }
  try {
    await navigator.clipboard.writeText(authStore.token);
    tokenCopied.value = true;
    toast.success("Token copied");
    setTimeout(() => {
      tokenCopied.value = false;
    }, 2000);
  } catch (err) {
    toast.error("Failed to copy token");
  }
};

// Initial load
loadKeys();
loadApiKeys();
</script>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
