<template>
  <div v-if="thinkingText" class="mb-4">
    <button
      @click="isOpen = !isOpen"
      class="inline-flex items-center gap-1.5 text-xs text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 transition-colors"
    >
      <svg
        class="w-3 h-3 transition-transform duration-150"
        :class="{ 'rotate-90': isOpen }"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
      <span>Thinking</span>
    </button>

    <div
      v-show="isOpen"
      class="mt-2 pl-4 border-l border-gray-200 dark:border-gray-700 text-sm text-gray-600 dark:text-gray-400 bg-gradient-to-r from-gray-50/80 to-transparent dark:from-surface/30 px-3 py-2 rounded-r-lg"
    >
      <div
        class="prose prose-sm max-w-none dark:prose-invert prose-p:mb-2 prose-li:my-0.5 prose-pre:my-3 prose-pre:p-3 prose-pre:rounded-lg italic opacity-85"
        v-html="renderChatMarkdown(thinkingText)"
      ></div>
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
