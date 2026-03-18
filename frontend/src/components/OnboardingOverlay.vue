<template>
  <Teleport to="body">
    <div class="relative z-[9999]" aria-labelledby="modal-title" role="dialog" aria-modal="true" @click.self="finishOnboarding">
      <div class="fixed inset-0 bg-gray-500/75 transition-opacity" aria-hidden="true"></div>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto" @click.self="finishOnboarding">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0" @click.self="finishOnboarding">
          <div class="relative transform overflow-hidden rounded-lg bg-white dark:bg-elevated text-left shadow-2xl transition-all sm:my-8 sm:w-full sm:max-w-2xl border border-gray-200 dark:border-gray-700 animate-in fade-in zoom-in-95 duration-200">
            <div class="bg-white dark:bg-elevated px-4 pb-4 pt-5 sm:p-10 sm:pb-8">
              <div class="sm:flex sm:items-center mb-10">
                <div class="mx-auto flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-12 sm:w-12">
                  <i class="fa-solid fa-wand-magic-sparkles text-xl text-blue-600"></i>
                </div>
                <div class="mt-4 text-center sm:ml-5 sm:mt-0 sm:text-left">
                  <h3 class="text-xl font-bold leading-6 text-gray-900 dark:text-white" id="modal-title">Welcome to MemWyre</h3>
                  <div class="mt-2">
                    <p class="text-sm text-gray-500 dark:text-gray-400">Save your first AI interaction to get started.</p>
                  </div>
                </div>
              </div>

              <div class="flex items-center justify-between border-b border-gray-100 dark:border-gray-800 pb-6 mb-8 mt-2">
                <div v-for="step in 3" :key="step" class="flex items-center gap-3">
                  <div :class="[
                    'w-8 h-8 rounded-full flex items-center justify-center text-sm font-semibold border transition-colors',
                    currentStep > step ? 'bg-[#D97757] text-white border-[#D97757] shadow-sm' :
                    currentStep === step ? 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white border-gray-300 dark:border-gray-600 ring-2 ring-gray-100 dark:ring-gray-800 ring-offset-1' :
                    'bg-transparent text-gray-400 border-gray-200 dark:border-gray-700'
                  ]">
                    <i v-if="currentStep > step" class="fa-solid fa-check text-xs"></i>
                    <span v-else>{{ step }}</span>
                  </div>
                  <span :class="['text-sm font-medium hidden sm:block transition-colors', currentStep >= step ? 'text-gray-900 dark:text-white' : 'text-gray-400']">
                    {{ getStepTitle(step) }}
                  </span>
                </div>
              </div>

              <div v-if="currentStep === 1" class="space-y-8 animate-in fade-in slide-in-from-right-4 duration-500">
                <div class="text-center sm:text-left">
                  <h4 class="text-xl font-semibold text-gray-900 dark:text-white">Save your first AI interaction</h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Choose one action to start your timeline.</p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                  <button v-for="action in firstActions" :key="action.id" @click="selectedAction = action.id" :class="[
                    'p-4 rounded-xl border transition-all focus:outline-none focus:ring-2 focus:ring-gray-900 dark:focus:ring-gray-100 text-left',
                    selectedAction === action.id
                      ? 'border-gray-900 dark:border-gray-100 bg-gray-50 dark:bg-gray-800 ring-1 ring-gray-900 dark:ring-gray-100 shadow-sm'
                      : 'border-gray-200 dark:border-gray-700 bg-white dark:bg-elevated hover:bg-gray-50 dark:hover:bg-gray-800'
                  ]">
                    <div class="font-semibold text-gray-900 dark:text-white">{{ action.name }}</div>
                    <div class="text-xs text-gray-500 dark:text-gray-400 mt-1">{{ action.desc }}</div>
                  </button>
                </div>
              </div>

              <div v-else-if="currentStep === 2" class="space-y-8 animate-in fade-in slide-in-from-right-4 duration-500">
                <div class="text-center sm:text-left">
                  <h4 class="text-xl font-semibold text-gray-900 dark:text-white">Install the Extension</h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Capture web context seamlessly into your workspace.</p>
                </div>

                <div class="bg-gray-50 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700 p-10 text-center rounded-xl">
                  <i class="fa-brands fa-chrome text-5xl text-gray-400 dark:text-gray-500 mx-auto mb-6 block"></i>
                  <a href="#" target="_blank" class="inline-flex justify-center items-center gap-2 w-full rounded-lg bg-white dark:bg-gray-700 px-6 py-3 text-sm font-bold text-gray-900 dark:text-white shadow-sm ring-1 ring-inset ring-gray-300 dark:ring-gray-600 hover:bg-gray-50 dark:hover:bg-gray-600 sm:w-auto transition-colors">
                    Add to Chrome
                  </a>
                </div>
              </div>

              <div v-else-if="currentStep === 3" class="space-y-8 animate-in fade-in slide-in-from-right-4 duration-500">
                <div class="text-center sm:text-left">
                  <h4 class="text-xl font-semibold text-gray-900 dark:text-white">Ready to explore?</h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Weï¿½ll open your timeline focused on today.</p>
                </div>

                <div class="bg-blue-50/50 dark:bg-blue-900/10 border border-blue-100 dark:border-blue-900/30 p-12 text-center rounded-xl">
                  <i class="fa-regular fa-compass text-6xl text-blue-500 mx-auto mb-5 block"></i>
                  <p class="text-gray-700 dark:text-gray-300 text-sm font-medium">See your AI interactions, projects, and reusable context in one place.</p>
                </div>
              </div>
            </div>

            <div class="bg-gray-50 dark:bg-gray-700/50 px-6 py-4 sm:flex sm:flex-row-reverse sm:px-10">
              <template v-if="currentStep === 1">
                <button type="button" class="inline-flex w-full justify-center rounded-lg bg-[#D97757] px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-[#C4654A] sm:ml-3 sm:w-auto disabled:opacity-50 transition-colors" @click="startFirstAction" :disabled="!selectedAction">Continue</button>
              </template>

              <template v-else-if="currentStep === 2">
                <button type="button" class="inline-flex w-full justify-center rounded-lg bg-[#D97757] px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-[#C4654A] sm:ml-3 sm:w-auto transition-colors" @click="nextStep">I've installed it</button>
                <button type="button" class="mt-3 inline-flex w-full justify-center rounded-lg bg-white dark:bg-gray-800 px-5 py-2.5 text-sm font-bold text-gray-700 dark:text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 dark:ring-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 sm:mt-0 sm:w-auto transition-colors" @click="nextStep">Skip</button>
              </template>

              <template v-else-if="currentStep === 3">
                <button type="button" class="inline-flex items-center gap-2 w-full justify-center rounded-lg bg-[#D97757] px-5 py-2.5 text-sm font-bold text-white shadow-sm hover:bg-[#C4654A] sm:ml-3 sm:w-auto transition-colors" @click="startTour">Open Timeline</button>
                <button type="button" class="mt-3 inline-flex w-full justify-center rounded-lg bg-white dark:bg-gray-800 px-5 py-2.5 text-sm font-bold text-gray-700 dark:text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 dark:ring-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 sm:mt-0 sm:w-auto transition-colors" @click="finishOnboarding">Iï¿½ll explore on my own</button>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();
const router = useRouter();
const currentStep = ref(1);
const selectedAction = ref(null);

const firstActions = [
  { id: 'prompt', name: 'Save a prompt', desc: 'Start with a reusable prompt.' },
  { id: 'conversation', name: 'Save a conversation', desc: 'Store an AI exchange.' },
  { id: 'web', name: 'Save a web page', desc: 'Capture external context.' },
];

const getStepTitle = (step) => {
  switch (step) {
    case 1: return 'First Action';
    case 2: return 'Extension';
    case 3: return 'Timeline';
    default: return 'Setup';
  }
};

const nextStep = () => {
  currentStep.value += 1;
};

const actionRoute = (actionId) => {
  if (actionId === 'prompt') return '/editor/new?interaction_type=prompt&source_app=chatgpt';
  if (actionId === 'conversation') return '/editor/new?interaction_type=conversation&source_app=claude';
  return '/editor/new?interaction_type=web_snippet&source_app=web';
};

const startFirstAction = () => {
  authStore.completeOnboarding();
  localStorage.setItem('tour_completed', 'true');
  router.push(actionRoute(selectedAction.value));
};

const finishOnboarding = () => {
  localStorage.setItem('tour_completed', 'true');
  authStore.completeOnboarding();
  if (router.currentRoute.value.path !== '/dashboard') {
    router.push('/dashboard?view=today');
  }
};

const startTour = () => {
  localStorage.removeItem('tour_completed');
  authStore.completeOnboarding();
  router.push('/dashboard?view=today');
};
</script>
