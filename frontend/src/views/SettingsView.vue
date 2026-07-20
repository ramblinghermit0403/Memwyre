<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />
    
    <main class="flex-1 overflow-hidden w-full max-w-4xl mx-auto py-10 px-4 sm:px-6 lg:px-8 flex flex-col h-full">
      <div class="flex-none">
          <div class="mb-8">
            <h1 class="text-3xl font-bold text-gray-900 dark:text-text-primary">Settings</h1>
          </div>

          <!-- Tab Header -->
          <div class="border-b border-gray-200 dark:border-border mb-8 overflow-x-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:'none'] [scrollbar-width:'none']">
              <nav class="-mb-px flex space-x-8">
                  <button 
                    @click="activeTab = 'general'"
                    :class="activeTab === 'general' ? 'border-[#D97757] text-[#D97757]' : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'"
                    class="whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm transition-colors"
                  >
                      General
                  </button>
              </nav>
          </div>
      </div>

      <!-- Scrollable Content Area -->
      <div class="flex-1 overflow-y-auto min-h-0 pr-2 custom-scrollbar">
          <!-- General Tab -->
          <div v-show="activeTab === 'general'" class="bg-white dark:bg-surface shadow rounded-lg px-8 py-8 border border-gray-100 dark:border-border animate-fade-in relative">
               
               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white mb-6">Appearance</h3>
               <div class="space-y-6 mb-8">
                   <div class="flex items-center justify-between">
                      <div>
                        <span class="text-sm font-medium text-gray-900 dark:text-white">Theme</span>
                        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Customize the look and feel of your workspace.</p>
                      </div>
                      <ThemeToggle />
                   </div>
               </div>
               
               <hr class="border-gray-100 dark:border-border mb-8" />

               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white mb-6">Preferences</h3>
               <div class="space-y-6">
                    <!-- Auto-Approve Toggle -->
                    <div class="flex items-center justify-between">
                       <div>
                        <span class="text-sm font-medium text-gray-900 dark:text-white">Auto-Approve New Memories</span>
                        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Automatically add created memories to the vector store without manual review.</p>
                      </div>
                      <button 
                        @click="toggleAutoApprove" 
                        :class="settings.auto_approve ? 'bg-[#D97757]' : 'bg-gray-200 dark:bg-gray-700'" 
                        class="relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757]"
                      >
                        <span 
                          aria-hidden="true" 
                          :class="settings.auto_approve ? 'translate-x-5' : 'translate-x-0'" 
                          class="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200"
                        ></span>
                      </button>
                    </div>
                    
                    <hr class="border-gray-100 dark:border-border" />
                    <hr class="border-gray-100 dark:border-border" />
                    
                    <!-- Account Info -->
                    <div>
                       <h4 class="text-sm font-medium text-gray-900 dark:text-text-primary mb-4">Account</h4>
                       <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                           <div class="sm:col-span-4">
                               <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email address</label>
                               <div class="flex items-center gap-3">
                                   <input type="email" disabled :value="authStore.user?.email || 'user@example.com'" class="bg-gray-50 dark:bg-gray-700 block w-full sm:max-w-md sm:text-sm border-gray-300 dark:border-gray-600 rounded-md py-2 px-3 text-gray-500 dark:text-gray-400 cursor-not-allowed">
                                   <span v-if="authStore.user?.is_verified" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
                                       Verified
                                   </span>
                                   <span v-else class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200">
                                       Unverified
                                   </span>
                               </div>
                               <div v-if="authStore.user && !authStore.user.is_verified" class="mt-3">
                                   <p class="text-sm text-red-600 dark:text-red-400 mb-2">You must verify your email address to access core features.</p>
                                   <button @click="resendVerification" :disabled="resendingEmail" class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-md shadow-sm text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] disabled:opacity-50 disabled:cursor-not-allowed hover:cursor-pointer">
                                       <svg v-if="resendingEmail" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                                       {{ resendingEmail ? 'Sending...' : 'Resend Verification Email' }}
                                   </button>
                               </div>
                           </div>
                       </div>
                    </div>
               </div>

                    <!-- Hidden Form -->
                    <div v-if="false">
                        <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 mb-4">
                          <div>
                            <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-1">Provider</label>
                            <div class="relative">
                                <select v-model="newKey.provider" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-[#D97757] focus:border-[#D97757] sm:text-sm rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white appearance-none">
                                  <option value="openai">OpenAI</option>
                                  <option value="anthropic">Anthropic</option>
                                  <option value="gemini">Google Gemini</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 dark:text-gray-400">
                                     <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                                </div>
                            </div>
                          </div>
                          <div>
                            <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-1">API Key</label>
                            <input type="password" v-model="newKey.api_key" class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-[#D97757] focus:border-[#D97757] sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white py-2 px-3" placeholder="sk-..." />
                          </div>
                        </div>
                        
                        <div class="flex items-center gap-6 mb-6">
                           <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="newKey.permissions.read" class="rounded border-gray-300 text-black shadow-sm focus:border-[#D97757] focus:ring focus:ring-[#D97757] focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                            <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Allow Read</span>
                          </label>
                          <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="newKey.permissions.write" class="rounded border-gray-300 text-black shadow-sm focus:border-[#D97757] focus:ring focus:ring-[#D97757] focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                            <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Allow Write</span>
                          </label>
                        </div>
                        
                        <button 
                            @click="addKey" 
                            :disabled="addingKey"
                            class="w-full sm:w-auto inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] transition-colors disabled:opacity-70 disabled:cursor-not-allowed gap-2"
                        >
                            <LoadingLogo v-if="addingKey" size="sm" class="w-4 h-4" :isWhite="true" />
                            {{ addingKey ? 'Connecting...' : 'Connect Provider' }}
                        </button>
                    </div>


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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import api from '../services/api';
import apiKeysService from '../services/apiKeys'; // Import Service
import NavBar from '../components/NavBar.vue';
import ThemeToggle from '../components/ThemeToggle.vue';
import ConfirmationModal from '../components/ConfirmationModal.vue';
import McpConnectionGuide from '../components/McpConnectionGuide.vue';
import { useToast } from 'vue-toastification';
import { writeScopedBoolean } from '../utils/onboardingState';

import LoadingLogo from '@/components/common/LoadingLogo.vue';

const authStore = useAuthStore();
const router = useRouter();
const toast = useToast();

const activeTab = ref('general');
const keys = ref([]);
const settings = ref({ auto_approve: true });
const newKey = ref({
  provider: 'openai',
  api_key: '',
  permissions: { read: true, write: false, auto_save: false }
});
const tokenCopied = ref(false);

const integrationCategories = ref([
  {
    name: 'MCP',
    items: [
      { id: 'cursor', name: 'Cursor', desc: 'One-click MCP install in Cursor', btnText: 'Connect', hasDocs: true, bgColor: 'bg-black dark:bg-black', icon: '/src/assets/cursor_CUBE_2D_DARK.svg', invert: true },
      { id: 'claude-desktop', name: 'Claude Desktop', desc: 'Connect supermemory in Claude Desktop', btnText: 'Connect', hasDocs: true, bgColor: 'bg-[#D97757]/10 dark:bg-[#D97757]/20', icon: '/src/assets/claude-color.svg' },
      { id: 'chatgpt', name: 'ChatGPT', desc: 'Apps via ChatGPT developer mode', btnText: 'Connect', hasDocs: true, bgColor: 'bg-[#10A37F]/10 dark:bg-white', icon: '/src/assets/openai.svg' },
      { id: 'vscode', name: 'VS Code', desc: 'Native MCP support for VS Code', btnText: 'Connect', bgColor: 'bg-blue-500/10 dark:bg-blue-500/20' }
    ]
  },
  {
    name: 'Plugins',
    items: [
      { id: 'claude-code', name: 'Claude Code', isPro: true, desc: 'Remembers your conventions, decisions, and project context', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-[#D97757]/10 dark:bg-[#D97757]/20', icon: '/src/assets/claude-color.svg' },
      { id: 'codex', name: 'Codex', desc: 'Persistent memory for the Codex CLI — free on every plan', btnText: 'Connect', hasDocs: true, bgColor: 'bg-blue-500/10 dark:bg-blue-500/20' },
      { id: 'opencode', name: 'OpenCode', isPro: true, desc: 'Long-term memory for your OpenCode sessions', btnText: 'Upgrade', isLightning: true, hasDocs: true, bgColor: 'bg-gray-200 dark:bg-gray-700' },
      { id: 'openclaw', name: 'OpenClaw', isPro: true, desc: 'Add persistent memory to autonomous OpenClaw agent sessions', btnText: 'Upgrade', isLightning: true, hasDocs: true, bgColor: 'bg-[#FF3366]/10 dark:bg-[#FF3366]/20', icon: '/src/assets/openclaw-color.svg' }
    ]
  },
  {
    name: 'Knowledge bases',
    items: [
      { id: 'gdrive', name: 'Google Drive', isPro: true, desc: 'Sync Docs, Sheets and Slides into your memory', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-gray-100 dark:bg-white/10' },
      { id: 'notion', name: 'Notion', isPro: true, desc: 'Import Notion pages and databases', btnText: 'Upgrade', isLightning: true, bgColor: 'bg-white dark:bg-black', icon: '/src/assets/notion-svgrepo-com.svg' }
    ]
  }
]);

const resendingEmail = ref(false);

const resendVerification = async () => {
    if (resendingEmail.value) return;
    resendingEmail.value = true;
    try {
        await api.post('/auth/resend-verification');
        toast.success("Verification email sent! Please check your inbox.");
    } catch (err) {
        toast.error(err.response?.data?.detail || "Failed to resend email.");
    } finally {
        resendingEmail.value = false;
    }
};

// Loading States
const addingKey = ref(false);
const deletingKey = ref(false);

// API Keys Logic
const apiKeys = ref([]);
const showAddKeyForm = ref(false);
const newKeyName = ref("");
const generatingKey = ref(false);
const justGeneratedKey = ref(null);
const keyCopied = ref(false);
const showGuideForKey = ref(null);
const showGlobalGuide = ref(false);

const handleConnectClientClick = () => {
    if (apiKeys.value.length === 0) {
        // Prompt them to create a key first
        showAddKeyForm.value = true;
        toast.info("Please generate an API key first to connect your client.");
    } else {
        // Show the generic global guide
        showGlobalGuide.value = true;
        // Scroll into view
        setTimeout(() => {
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        }, 100);
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

const generateKey = async () => {
    if (!newKeyName.value) return;
    generatingKey.value = true;
    try {
        const res = await apiKeysService.createKey(newKeyName.value);
        justGeneratedKey.value = res.data.key;
        showGuideForKey.value = res.data.key;
        toast.success("API Key generated successfully");
        newKeyName.value = "";
        showAddKeyForm.value = false;
        loadApiKeys();
    } catch (err) {
        toast.error("Failed to generate key");
    } finally {
        generatingKey.value = false;
    }
};

const copyGeneratedKey = async () => {
    if (justGeneratedKey.value) {
        await navigator.clipboard.writeText(justGeneratedKey.value);
        keyCopied.value = true;
        toast.success("Key copied to clipboard");
        setTimeout(() => keyCopied.value = false, 2000);
    }
};

const toggleAutoApprove = async () => {
  const newVal = !settings.value.auto_approve;
  settings.value.auto_approve = newVal;
  try {
    await api.patch('/user/settings', { auto_approve: newVal });
    toast.success("Settings updated");
  } catch (err) {
    settings.value.auto_approve = !newVal; // revert
    toast.error("Failed to update settings");
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

const loadSettings = async () => {
  try {
    const res = await api.get('/user/settings');
    settings.value = { ...settings.value, ...res.data };
  } catch (err) {
    console.error(err);
  }
};

const addKey = async () => {
  if (!newKey.value.api_key) return toast.error("API Key required");
  addingKey.value = true;
  try {
    await api.post('/user/llm-keys', newKey.value);
    toast.success("Key added");
    newKey.value.api_key = ""; // clear
    loadKeys();
  } catch (err) {
    toast.error("Failed to add key");
  } finally {
    addingKey.value = false;
  }
};

const keyToDelete = ref(null);
const showDeleteModal = ref(false);

const deleteKey = (id) => {
  keyToDelete.value = id;
  showDeleteModal.value = true;
};

const confirmDeleteKey = async () => {
    if (!keyToDelete.value) return;
    deletingKey.value = true;
    try {
        // HACK: Differentiate based on where it was called from. 
        // Ideally we'd have separate modals or pass a type.
        // Checking if ID exists in apiKeys list vs llm-keys list could work, 
        // but IDs might collide if integers.
        // For MVP, we'll try to delete from User Keys first, if not found then LLM keys?
        // BETTER: Check if it's in `apiKeys` array
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

const restartTour = () => {
    if (authStore.user?.id) {
        writeScopedBoolean(localStorage, authStore.user.id, 'tour_completed', false);
        writeScopedBoolean(localStorage, authStore.user.id, 'tour_requested', true);
    } else {
        localStorage.removeItem('tour_completed');
        localStorage.setItem('tour_requested', 'true');
    }
    toast.info("Tour reset. Returning to Dashboard...");
    setTimeout(() => router.push('/dashboard'), 1000);
};

// Initial load
loadKeys();
loadSettings();
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
