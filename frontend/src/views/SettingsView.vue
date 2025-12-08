<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-300">
    <nav class="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <div class="flex-shrink-0 flex items-center">
              <h1 class="text-xl font-bold text-blue-600">Brain Vault</h1>
            </div>
            <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
              <router-link to="/" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                Dashboard
              </router-link>
              <a href="#" class="border-blue-600 text-gray-900 dark:text-white inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                Settings & Export
              </a>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <ThemeToggle />
            <button @click="logout" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 px-3 py-2 rounded-md text-sm font-medium">
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>

    <div class="py-10">
      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold leading-tight text-gray-900 dark:text-white">
            Settings & Export
          </h1>
        </div>
      </header>
      <main>
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
          <div class="px-4 py-8 sm:px-0 space-y-6">
            
            <!-- Preferences Section -->
            <div class="bg-white dark:bg-gray-800 shadow-sm sm:rounded-lg p-6 border border-gray-100 dark:border-gray-700 transition-colors duration-300">
              <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">Preferences</h3>
              <div class="mt-4 space-y-4">
                <div class="flex items-center justify-between">
                  <div>
                    <span class="text-sm font-medium text-gray-900 dark:text-white">Auto-Approve New Memories</span>
                    <p class="text-sm text-gray-500 dark:text-gray-400">Automatically add created memories to the vector store without review.</p>
                  </div>
                  <button 
                    @click="toggleAutoApprove" 
                    :class="settings.auto_approve ? 'bg-indigo-600' : 'bg-gray-200 dark:bg-gray-700'" 
                    class="relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    <span 
                      aria-hidden="true" 
                      :class="settings.auto_approve ? 'translate-x-5' : 'translate-x-0'" 
                      class="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200"
                    ></span>
                  </button>
                </div>
              </div>
            </div>

            <!-- API Keys Section -->
            <div class="bg-white dark:bg-gray-800 shadow-sm sm:rounded-lg p-6 border border-gray-100 dark:border-gray-700 transition-colors duration-300">
              <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">Connected LLM Clients</h3>
              <div class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                <p>Manage external LLM providers and their permissions.</p>
              </div>
              
              <!-- Existing Keys List -->
              <div class="mt-4 space-y-3" v-if="keys.length > 0">
                <div v-for="key in keys" :key="key.id" class="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                  <div class="flex items-center gap-2">
                    <span class="font-medium text-gray-900 dark:text-white capitalize">{{ key.provider }}</span>
                    <span class="text-xs px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300" v-if="key.permissions.read">Read Access</span>
                  </div>
                  <button @click="deleteKey(key.id)" class="text-red-600 hover:text-red-800 dark:hover:text-red-400 text-sm">Remove</button>
                </div>
              </div>

              <!-- Add New Key -->
              <div class="mt-6 border-t border-gray-200 dark:border-gray-600 pt-4">
                <h4 class="text-sm font-medium text-gray-900 dark:text-white mb-3">Add New Connection</h4>
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Provider</label>
                    <select v-model="newKey.provider" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                      <option value="openai">OpenAI</option>
                      <option value="anthropic">Anthropic</option>
                      <option value="gemini">Google Gemini</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">API Key</label>
                    <input type="password" v-model="newKey.api_key" class="mt-1 block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white" placeholder="sk-..." />
                  </div>
                </div>
                <!-- Permissions Toggles (Simplified) -->
                <div class="mt-4 flex items-center gap-4">
                  <label class="inline-flex items-center">
                    <input type="checkbox" v-model="newKey.permissions.read" class="rounded border-gray-300 text-blue-600 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                    <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Allow Read</span>
                  </label>
                  <label class="inline-flex items-center">
                    <input type="checkbox" v-model="newKey.permissions.write" class="rounded border-gray-300 text-blue-600 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                    <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Allow Write</span>
                  </label>
                  <label class="inline-flex items-center">
                    <input type="checkbox" v-model="newKey.permissions.auto_save" class="rounded border-gray-300 text-blue-600 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                    <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Auto-Save (No Inbox)</span>
                  </label>
                </div>
                
                <div class="mt-4">
                  <button @click="addKey" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                    Connect Provider
                  </button>
                </div>
              </div>
            </div>

            <!-- Extension Auth Section -->
            <div class="bg-white dark:bg-gray-800 shadow-sm sm:rounded-lg p-6 border border-gray-100 dark:border-gray-700 transition-colors duration-300">
              <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">Browser Extension Auth</h3>
              <div class="mt-2 max-w-xl text-sm text-gray-500 dark:text-gray-400">
                <p>Use this token to log in to the Brain Vault Browser Extension.</p>
              </div>
              <div class="mt-5 flex space-x-4">
                <button @click="copyToken" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition-colors duration-200">
                  <span v-if="tokenCopied">Copied!</span>
                  <span v-else>Copy Extension Token</span>
                </button>
                <button @click="restartTour" class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 shadow-sm text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                  Restart Tour
                </button>
              </div>
            </div>

            <!-- Export Section -->
            <div class="bg-white dark:bg-gray-800 shadow-sm sm:rounded-lg p-6 border border-gray-100 dark:border-gray-700 transition-colors duration-300">
              <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">Export Data</h3>
              <div class="mt-2 max-w-xl text-sm text-gray-500 dark:text-gray-400">
                <p>Download your entire knowledge base.</p>
              </div>
              <div class="mt-5 flex space-x-4">
                <button @click="exportData('json')" class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 shadow-sm text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                  Export JSON
                </button>
                <button @click="exportData('md')" class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 shadow-sm text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                  Export Markdown
                </button>
              </div>
            </div>

          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import api from '../services/api';
import ThemeToggle from '../components/ThemeToggle.vue';
import { useToast } from 'vue-toastification';

const authStore = useAuthStore();
const router = useRouter();
const toast = useToast();
const keys = ref([]);
const settings = ref({ auto_approve: true });
const newKey = ref({
  provider: 'openai',
  api_key: '',
  permissions: { read: true, write: false, auto_save: false }
});

const loadSettings = async () => {
  try {
    const res = await api.get('/user/settings');
    settings.value = { ...settings.value, ...res.data };
  } catch (err) {
    console.error(err);
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

const addKey = async () => {
  if (!newKey.value.api_key) return toast.error("API Key required");
  try {
    await api.post('/user/llm-keys', newKey.value);
    toast.success("Key added");
    newKey.value.api_key = ""; // clear
    loadKeys();
  } catch (err) {
    toast.error("Failed to add key");
  }
};

const deleteKey = async (id) => {
  if (!confirm("Remove this key?")) return;
  try {
    await api.delete(`/user/llm-keys/${id}`);
    toast.success("Key removed");
    loadKeys();
  } catch (err) {
    toast.error("Failed to remove key");
  }
};

// Initial load
loadKeys();
loadSettings();

const exportData = async (format) => {
  try {
    const response = await api.get(`/export/${format}`, { responseType: 'blob' });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `brain_vault_export.${format}`);
    document.body.appendChild(link);
    link.click();
    toast.success(`Exported as ${format.toUpperCase()}`);
    toast.success(`Exported as ${format.toUpperCase()}`);
  } catch (error) {
    toast.error('Export failed');
  }
};

const tokenCopied = ref(false);

const copyToken = async () => {
  if (!authStore.token) {
    return toast.error("No token available");
  }
  try {
    await navigator.clipboard.writeText(authStore.token);
    tokenCopied.value = true;
    toast.success("Token copied to clipboard");
    setTimeout(() => {
      tokenCopied.value = false;
    }, 2000);
  } catch (err) {
    console.error("Copy failed", err);
    toast.error("Failed to copy token");
  }
};

const restartTour = () => {
    localStorage.removeItem('tour_completed');
    toast.info("Tour reset. Returning to Dashboard...");
    setTimeout(() => router.push('/'), 1000);
};
</script>
