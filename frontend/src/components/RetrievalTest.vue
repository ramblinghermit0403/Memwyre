~<template>
  <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-lg rounded-xl border border-gray-100 dark:border-gray-700 transition-all duration-200 hover:shadow-xl h-full flex flex-col">
    <div class="p-6 flex-1 flex flex-col">
      <div class="flex items-center mb-6">
        <div class="h-10 w-10 rounded-full bg-green-100 dark:bg-green-900 flex items-center justify-center mr-4">
          <svg class="h-6 w-6 text-green-600 dark:text-green-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
        <div>
          <h3 class="text-lg font-bold text-gray-900 dark:text-white">Ask Your Brain Vault</h3>
          <p class="text-sm text-gray-500 dark:text-gray-400">Retrieve information from your documents</p>
        </div>
      </div>
      
      <div class="space-y-4 flex-1 flex flex-col">
        <!-- Provider Selection -->
        <div>
          <label for="provider" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">LLM Provider</label>
          <select v-model="provider" id="provider" class="block w-full border-gray-300 dark:border-gray-600 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white">
            <option value="openai">OpenAI (GPT-3.5)</option>
            <option value="gemini">Google Gemini</option>
          </select>
        </div>

        <div class="relative">
          <input type="text" v-model="query" @keyup.enter="search" class="block w-full pl-4 pr-12 py-3 border-gray-300 dark:border-gray-600 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm transition-colors duration-200 bg-white dark:bg-gray-700 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400" placeholder="Ask a question..." />
          <div class="absolute inset-y-0 right-0 flex items-center pr-3">
            <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
            </svg>
          </div>
        </div>
        
        <button @click="search" :disabled="!query || loading" class="w-full flex justify-center items-center px-4 py-3 border border-transparent text-sm font-medium rounded-lg shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200">
          <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ loading ? 'Thinking...' : 'Ask Question' }}
        </button>

        <div v-if="response" class="mt-6 flex-1 overflow-y-auto max-h-96 custom-scrollbar">
          <div class="bg-gray-50 dark:bg-gray-700/50 rounded-lg p-4 border border-gray-200 dark:border-gray-600">
            <h4 class="text-sm font-bold text-gray-900 dark:text-white mb-2 flex items-center">
              <svg class="h-4 w-4 mr-2 text-green-600 dark:text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Answer ({{ provider === 'gemini' ? 'Gemini' : 'OpenAI' }})
            </h4>
            <div class="text-gray-700 dark:text-gray-300 text-sm whitespace-pre-wrap leading-relaxed">
              {{ response }}
            </div>
          </div>
          
          <div v-if="context && context.length" class="mt-4">
            <h4 class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-2">Sources</h4>
            <ul class="space-y-2">
              <li v-for="(ctx, index) in context" :key="index" class="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded p-2 text-xs text-gray-600 dark:text-gray-400 shadow-sm">
                {{ ctx.substring(0, 150) }}...
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import api from '../services/api';

const query = ref('');
const loading = ref(false);
const response = ref('');
const context = ref([]);
const provider = ref('gemini'); // Default to Gemini

const search = async () => {
  if (!query.value) return;

  loading.value = true;
  response.value = '';
  context.value = [];

  try {
    // Get API key from localStorage based on provider
    const apiKey = provider.value === 'gemini' 
      ? localStorage.getItem('gemini_key') 
      : localStorage.getItem('openai_key');

    if (!apiKey) {
      response.value = `Error: Please set your ${provider.value === 'gemini' ? 'Gemini' : 'OpenAI'} API key in Settings.`;
      loading.value = false;
      return;
    }

    const res = await api.post('/llm/chat', {
      query: query.value,
      provider: provider.value,
      api_key: apiKey,
      top_k: 3
    });
    
    response.value = res.data.response;
    context.value = res.data.context;
  } catch (error) {
    response.value = 'Error: ' + (error.response?.data?.detail || error.message);
  } finally {
    loading.value = false;
  }
};
</script>
