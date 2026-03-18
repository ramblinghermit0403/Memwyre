<template>
  <div class="mt-3 pl-1 flex items-center gap-2 text-xs text-gray-400">
    <button @click="$emit('copy')" class="flex items-center gap-1 hover:text-gray-600 dark:hover:text-gray-200 transition-colors p-1 rounded">
      <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
      </svg>
      Copy
    </button>

    <span class="text-gray-300 dark:text-gray-700">|</span>

    <div class="flex items-center gap-1">
      <button @click="$emit('feedback', 'up')" class="hover:text-gray-600 dark:hover:text-gray-200 p-1 rounded transition-colors group">
        <svg class="w-4 h-4 group-active:scale-90 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
        </svg>
      </button>
      <button @click="$emit('feedback', 'down')" class="hover:text-gray-600 dark:hover:text-gray-200 p-1 rounded transition-colors group">
        <svg class="w-4 h-4 group-active:scale-90 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14H5.236a2 2 0 01-1.789-2.894l3.5-7A2 2 0 018.736 3h4.018a2 2 0 01.485.06l3.76.94m-7 10v5a2 2 0 002 2h.095c.5 0 .905-.405.905-.905 0-.714.211-1.412.608-2.006L17 13V4m-7 10h2m5-10h2a2 2 0 012 2v6a2 2 0 01-2 2h-2.5" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
defineEmits(['copy', 'feedback']);
</script>
