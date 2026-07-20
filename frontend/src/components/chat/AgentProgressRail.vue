<template>
  <div class="flex justify-start my-2">
    <div class="max-w-[85%] min-w-0">
      <div class="bg-white/80 dark:bg-surface-2/60 border border-gray-200/80 dark:border-gray-800 rounded-xl p-3 shadow-xs transition-all">
        <div class="flex items-center justify-between gap-3">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-semibold text-gray-700 dark:text-gray-200 tracking-wide uppercase">Agent Progress</span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-500 font-mono">
              {{ steps.filter(s => s.status === 'completed').length }}/{{ steps.length || 1 }}
            </span>
          </div>
          <button
            class="text-[11px] text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 font-medium transition-colors"
            @click="$emit('toggle')"
          >
            {{ expanded ? 'Collapse' : 'Details' }}
          </button>
        </div>

        <p v-if="waitingForFirstStep" class="mt-1.5 text-xs text-gray-500 dark:text-gray-400 font-mono">
          Waiting for agent response...
        </p>

        <template v-else-if="steps.length > 0">
          <p v-if="!expanded" class="mt-1.5 text-xs text-gray-600 dark:text-gray-300 font-mono truncate">
            {{ summaryLine }}
          </p>

          <ul v-else class="mt-3 pl-1 space-y-2 border-t border-gray-100 dark:border-gray-800 pt-2.5">
            <li
              v-for="step in steps"
              :key="`${turnId}-${step.step}`"
              class="flex items-start justify-between text-xs min-w-0"
            >
              <div class="flex items-center space-x-2 min-w-0">
                <span
                  class="w-1.5 h-1.5 rounded-full shrink-0"
                  :class="dotClass(step.status)"
                ></span>
                <span class="text-gray-700 dark:text-gray-200 font-medium truncate">{{ step.label }}</span>
                <span v-if="metaText(step.meta)" class="text-[10px] text-gray-400 dark:text-gray-500 font-mono">
                  ({{ metaText(step.meta) }})
                </span>
              </div>
              <span class="text-[10px] text-gray-400 dark:text-gray-500 shrink-0 font-mono">{{ formatTime(step.timestamp) }}</span>
            </li>
          </ul>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  steps: { type: Array, default: () => [] },
  expanded: { type: Boolean, default: false },
  turnId: { type: String, default: '' },
  waitingForFirstStep: { type: Boolean, default: false },
});

defineEmits(['toggle']);

const latestStep = computed(() => {
  if (!props.steps.length) return null;
  const active = props.steps.find((s) => s.status === 'active');
  return active || props.steps[props.steps.length - 1];
});

const summaryLine = computed(() => {
  const completedCount = props.steps.filter((s) => s.status === 'completed').length;
  if (!latestStep.value) return `${completedCount} steps completed`;
  return `${latestStep.value.label} (${completedCount}/${props.steps.length})`;
});

const dotClass = (status) => {
  if (status === 'failed') return 'bg-red-500';
  if (status === 'active') return 'bg-amber-500 animate-pulse';
  if (status === 'completed') return 'bg-emerald-500';
  return 'bg-gray-300 dark:bg-gray-600';
};

const formatTime = (timestamp) => {
  if (!timestamp) return '';
  return new Intl.DateTimeFormat('en-US', {
    hour: '2-digit',
    minute: '2-digit'
  }).format(new Date(timestamp));
};

const metaText = (meta) => {
  if (!meta || typeof meta !== 'object') return '';
  const parts = [];
  if (typeof meta.result_count === 'number') parts.push(`${meta.result_count} results`);
  if (typeof meta.source_count === 'number') parts.push(`${meta.source_count} sources`);
  if (meta.model) parts.push(meta.model);
  if (meta.error) parts.push('error');
  return parts.join(' | ');
};
</script>
