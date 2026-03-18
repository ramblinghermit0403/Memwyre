<template>
  <div class="flex justify-start gap-3">
    <div class="w-8 h-8 rounded-full bg-white dark:bg-surface border border-gray-200 dark:border-gray-700 shrink-0 mt-1 flex items-center justify-center">
      <span class="w-1.5 h-1.5 rounded-full bg-[#D97757] animate-pulse"></span>
    </div>

    <div class="max-w-[85%] min-w-0">
      <div class="flex items-center justify-between gap-3">
        <p class="text-[11px] uppercase tracking-wide text-gray-500 dark:text-gray-400 font-semibold">Agent Timeline</p>
        <button
          class="text-[11px] text-gray-500 hover:text-gray-700 dark:hover:text-gray-300 transition-colors"
          @click="$emit('toggle')"
        >
          {{ expanded ? 'Collapse' : 'Expand' }}
        </button>
      </div>

      <p v-if="waitingForFirstStep" class="mt-1 text-xs text-gray-500 dark:text-gray-400">
        Waiting for first step...
      </p>

      <template v-else-if="steps.length > 0">
        <p v-if="!expanded" class="mt-1 text-xs text-gray-600 dark:text-gray-300">
          {{ summaryLine }}
        </p>

        <ul v-else class="mt-3 pl-1 border-l border-gray-200 dark:border-gray-700">
          <li
            v-for="step in steps"
            :key="`${turnId}-${step.step}`"
            class="relative pl-4 pb-5 last:pb-1"
          >
            <span
              class="absolute -left-[5px] top-[7px] w-2 h-2 rounded-full"
              :class="dotClass(step.status)"
            ></span>
            <div class="min-w-0 flex flex-col gap-1">
              <div class="flex items-start justify-between gap-3">
                <p class="text-xs text-gray-700 dark:text-gray-200">{{ step.label }}</p>
                <span class="text-[10px] text-gray-400 dark:text-gray-500 shrink-0">{{ formatTime(step.timestamp) }}</span>
              </div>
              <p v-if="metaText(step.meta)" class="text-[11px] text-gray-500 dark:text-gray-400">
                {{ metaText(step.meta) }}
              </p>
            </div>
          </li>
        </ul>
      </template>
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
  return `${latestStep.value.label} | ${completedCount}/${props.steps.length} done`;
});

const dotClass = (status) => {
  if (status === 'failed') return 'bg-red-500';
  if (status === 'active') return 'bg-amber-500 animate-pulse';
  if (status === 'completed') return 'bg-green-500';
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
