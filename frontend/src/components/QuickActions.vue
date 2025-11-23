<template>
  <div class="h-full flex flex-col justify-center items-center bg-white dark:bg-gray-800 p-6">
    <button 
      @click="createNewMemory" 
      class="w-full py-4 px-6 bg-indigo-600 hover:bg-indigo-700 text-white text-lg font-medium rounded-lg shadow-md transition-transform transform hover:scale-105 flex items-center justify-center space-x-3 mb-4"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
      </svg>
      <span>Create New Memory</span>
    </button>
    
    <button 
      @click="goToPromptGenerator" 
      class="w-full py-4 px-6 bg-purple-600 hover:bg-purple-700 text-white text-lg font-medium rounded-lg shadow-md transition-transform transform hover:scale-105 flex items-center justify-center space-x-3"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
      </svg>
      <span>Generate Prompt</span>
    </button>
    <p class="mt-4 text-sm text-gray-500 dark:text-gray-400 text-center">
      Open the full-screen editor to write and format your memories with Markdown.
    </p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const createNewMemory = () => {
  router.push('/editor/new');
};

const goToPromptGenerator = () => {
  router.push('/prompts');
};
</script>
