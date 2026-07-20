<template>
  <div class="mt-2.5 flex items-center justify-between text-xs text-gray-400 font-mono">
    <div class="flex items-center space-x-2">
      <button
        @click="$emit('copy')"
        class="inline-flex items-center space-x-1 px-2 py-1 rounded-md bg-gray-100/70 dark:bg-gray-800/60 hover:bg-gray-200 dark:hover:bg-gray-700/80 hover:text-gray-700 dark:hover:text-gray-200 transition-all cursor-pointer"
        title="Copy response"
      >
        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
        </svg>
        <span>Copy</span>
      </button>

      <span class="text-gray-300 dark:text-gray-700">•</span>

      <div class="flex items-center space-x-1">
        <button
          @click="$emit('feedback', 'up')"
          class="p-1 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-emerald-500 transition-colors cursor-pointer"
          title="Good response"
        >
          <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
          </svg>
        </button>
        <button
          @click="$emit('feedback', 'down')"
          class="p-1 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-red-500 transition-colors cursor-pointer"
          title="Poor response"
        >
          <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14H5.236a2 2 0 01-1.789-2.894l3.5-7A2 2 0 018.736 3h4.018a2 2 0 01.485.06l3.76.94m-7 10v5a2 2 0 002 2h.095c.5 0 .905-.405.905-.905 0-.714.211-1.412.608-2.006L17 13V4m-7 10h2m5-10h2a2 2 0 012 2v6a2 2 0 01-2 2h-2.5" />
          </svg>
        </button>
      </div>
    </div>

    <span class="text-[10px] text-gray-400/80 dark:text-gray-500 px-2 py-0.5 rounded bg-gray-100/50 dark:bg-gray-800/40">
      Kimi K2.5 (Bedrock)
    </span>
  </div>
</template>

<script setup>
defineEmits(['copy', 'feedback']);
</script>
