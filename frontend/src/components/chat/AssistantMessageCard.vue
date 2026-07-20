<template>
  <div class="flex justify-start my-2">
    <div class="max-w-[85%] min-w-0">
      <div class="bg-white/90 dark:bg-surface-2/70 backdrop-blur-md dark:text-gray-100 px-5 py-4 rounded-2xl rounded-tl-xs text-sm md:text-base leading-relaxed text-gray-800 border border-gray-200/80 dark:border-gray-700/80 shadow-xs">
        <ReasoningPanel :thinking-text="thinkingText" />

        <section class="mb-4">
          <p class="text-[11px] uppercase tracking-wider text-gray-400 dark:text-gray-400 mb-2 font-semibold font-mono">Answer</p>
          <div
            class="prose prose-sm max-w-none dark:prose-invert prose-headings:mb-2 prose-p:my-2 prose-ul:my-2 prose-ol:my-2 prose-li:my-0.5 prose-pre:my-3 prose-pre:p-3 prose-pre:rounded-xl prose-code:text-[0.9em] prose-table:block prose-table:overflow-x-auto"
            v-html="renderChatMarkdown(answerText)"
          ></div>
        </section>

        <section v-if="keyPoints.length > 0" class="mb-4">
          <p class="text-[11px] uppercase tracking-wider text-gray-400 dark:text-gray-400 mb-2 font-semibold font-mono">Key Points</p>
          <ul class="list-disc pl-5 space-y-1 text-sm text-gray-700 dark:text-gray-200">
            <li v-for="(point, idx) in keyPoints.slice(0, 5)" :key="`kp-${idx}`">{{ point }}</li>
          </ul>
        </section>

        <section v-if="actions.length > 0" class="mb-4">
          <p class="text-[11px] uppercase tracking-wider text-gray-400 dark:text-gray-400 mb-2 font-semibold font-mono">Actions</p>
          <ul class="list-disc pl-5 space-y-1 text-sm text-gray-700 dark:text-gray-200">
            <li v-for="(action, idx) in actions.slice(0, 5)" :key="`act-${idx}`">{{ action }}</li>
          </ul>
        </section>

        <section v-if="sourceRows.length > 0" class="pt-3 border-t border-gray-200/60 dark:border-gray-700/60">
          <p class="text-[11px] uppercase tracking-wider text-gray-400 dark:text-gray-400 mb-2 font-semibold font-mono">Sources</p>
          <div class="flex flex-wrap gap-1.5">
            <button
              v-for="(source, idx) in sourceRows"
              :key="`src-${idx}`"
              class="inline-flex items-center space-x-1.5 text-xs px-2.5 py-1 rounded-lg bg-gray-100 dark:bg-gray-800/80 border border-gray-200/60 dark:border-gray-700 hover:border-[#D97757] hover:text-[#D97757] dark:hover:text-[#D97757] transition-all cursor-pointer truncate max-w-xs"
              @click="$emit('open-source', source)"
            >
              <svg class="w-3 h-3 text-gray-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <span class="truncate">{{ source.title || source.id || source }}</span>
            </button>
          </div>
        </section>
      </div>

      <MessageActions @copy="$emit('copy')" @feedback="(type) => $emit('feedback', type)" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import MessageActions from './MessageActions.vue';
import ReasoningPanel from './ReasoningPanel.vue';
import { splitChatContent, renderChatMarkdown } from '../../utils/chatMarkdown';

const props = defineProps({
  message: { type: Object, required: true },
});

defineEmits(['copy', 'feedback', 'open-source']);

const parsedContent = computed(() => splitChatContent(props.message?.content || ''));

const thinkingText = computed(() => {
  return parsedContent.value.reasoningText;
});

const answerText = computed(() => {
  return parsedContent.value.answerText;
});

const lines = computed(() =>
  answerText.value
    .split('\n')
    .map((l) => l.trim())
    .filter(Boolean)
);

const keyPoints = computed(() =>
  lines.value.filter((line) => /^([-*]|\d+\.)\s+/.test(line)).map((line) => line.replace(/^([-*]|\d+\.)\s+/, ''))
);

const actions = computed(() =>
  lines.value.filter((line) => /^(next|action|todo|should|try|consider)\b/i.test(line))
);

const sourceRows = computed(() => {
  const src = props.message?.sources;
  return Array.isArray(src) ? src : [];
});
</script>
