<template>
  <div v-if="thinkingText" class="mb-4">
    <div class="rounded-xl border border-gray-200/80 dark:border-gray-800 bg-gray-50/60 dark:bg-gray-900/40 p-2.5 transition-all">
      <button
        @click="isOpen = !isOpen"
        class="w-full flex items-center justify-between text-xs text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200 transition-colors"
      >
        <div class="flex items-center space-x-2">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-purple-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-purple-500"></span>
          </span>
          <span class="font-medium tracking-wide">Thinking Process</span>
        </div>
        <div class="flex items-center space-x-1.5 text-[11px] text-gray-400 dark:text-gray-500">
          <span>{{ isOpen ? 'Hide' : 'Show Details' }}</span>
          <svg
            class="w-3.5 h-3.5 transition-transform duration-200"
            :class="{ 'rotate-180': isOpen }"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </button>

      <div
        v-show="isOpen"
        class="mt-2.5 pt-2.5 border-t border-gray-200/60 dark:border-gray-800 text-xs leading-relaxed text-gray-600 dark:text-gray-300 font-mono"
      >
        <div
          class="prose prose-xs max-w-none dark:prose-invert prose-p:my-1 prose-pre:my-2 prose-pre:p-2.5 prose-pre:rounded-lg opacity-90"
          v-html="renderChatMarkdown(thinkingText)"
        ></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { renderChatMarkdown } from '../../utils/chatMarkdown';

defineProps({
  thinkingText: { type: String, default: '' },
});

const isOpen = ref(false);
</script>
