<template>
  <div class="flex justify-start gap-4">
    <div class="w-8 h-8 rounded-full bg-white border border-gray-200 shrink-0 mt-1 shadow-sm">
      <img src="/image.svg" alt="AI" />
    </div>
    <div class="max-w-[85%] min-w-0">
      <div class="bg-white/70 dark:bg-surface-2/40 dark:text-gray-100 px-5 py-4 rounded-xl text-sm md:text-base leading-relaxed text-gray-800 border border-gray-200/70 dark:border-gray-700/70">
        <ReasoningPanel :thinking-text="thinkingText" />

        <section class="mb-4">
          <p class="text-[11px] uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2 font-semibold">Answer</p>
          <div
            class="prose prose-sm max-w-none dark:prose-invert prose-headings:mb-2 prose-p:my-2 prose-ul:my-2 prose-ol:my-2 prose-li:my-0.5 prose-pre:my-3 prose-pre:p-3 prose-pre:rounded-lg prose-code:text-[0.9em] prose-table:block prose-table:overflow-x-auto"
            v-html="renderChatMarkdown(answerText)"
          ></div>
        </section>

        <section v-if="keyPoints.length > 0" class="mb-4">
          <p class="text-[11px] uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2 font-semibold">Key Points</p>
          <ul class="list-disc pl-5 space-y-1 text-sm text-gray-700 dark:text-gray-200">
            <li v-for="(point, idx) in keyPoints.slice(0, 5)" :key="`kp-${idx}`">{{ point }}</li>
          </ul>
        </section>

        <section v-if="actions.length > 0" class="mb-4">
          <p class="text-[11px] uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2 font-semibold">Actions</p>
          <ul class="list-disc pl-5 space-y-1 text-sm text-gray-700 dark:text-gray-200">
            <li v-for="(action, idx) in actions.slice(0, 5)" :key="`act-${idx}`">{{ action }}</li>
          </ul>
        </section>

        <section v-if="sourceRows.length > 0">
          <p class="text-[11px] uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2 font-semibold">Sources</p>
          <div class="space-y-1.5">
            <button
              v-for="(source, idx) in sourceRows"
              :key="`src-${idx}`"
              class="w-full text-left text-xs px-1 py-1 border-b border-gray-200 dark:border-gray-700 hover:text-[#D97757] transition-colors"
              @click="$emit('open-source', source)"
            >
              {{ source.title || source.id || source }}
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
