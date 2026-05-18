<template>
  <div class="min-h-screen bg-white text-[#191919] font-sans selection:bg-[#D97757] selection:text-white">
    <nav class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-black/5 px-6 py-4">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <router-link to="/portfolio" class="flex items-center gap-2 font-bold text-gray-600 hover:text-black transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          Back to Portfolio
        </router-link>
        <div class="font-bold text-xl tracking-tight hidden sm:block">{{ project?.title }}</div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-6 py-12 sm:py-20">
      <div v-if="project" class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-start">
        <!-- Left Side: Content -->
        <div class="lg:col-span-6 lg:sticky lg:top-28 animate-in fade-in slide-in-from-left-4 duration-700">
          <div class="flex items-center gap-6 mb-8 animate-in fade-in slide-in-from-left-4 duration-700">
            <div class="shrink-0">
              <img v-if="project.icon && project.icon.startsWith('/')" :src="project.icon" :alt="project.title" class="w-16 h-16 object-contain" />
              <span v-else class="text-4xl">{{ project.icon || '🚀' }}</span>
            </div>
            <h1 class="text-4xl sm:text-5xl font-extrabold tracking-tight text-gray-900">{{ project.title }}</h1>
          </div>

          <div class="flex flex-wrap gap-2 mb-8">
            <span v-for="tag in project.tags" :key="tag" class="px-3 py-1 bg-[#D97757]/10 text-[#D97757] text-xs font-bold rounded-full">
              {{ tag }}
            </span>
          </div>

          <p class="text-xl text-gray-600 leading-relaxed mb-10 font-medium italic">
            {{ project.description }}
          </p>

          <div class="flex flex-wrap gap-4 mb-12">
            <a v-if="project.github" :href="project.github" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 bg-black text-white font-bold rounded-xl hover:bg-gray-800 transition-all shadow-md hover:scale-105">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" /></svg>
              GitHub
            </a>
            <a v-if="project.demo" :href="project.demo" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 bg-white text-black font-bold rounded-xl border border-black/10 hover:bg-black/5 transition-all hover:border-black/20 shadow-sm">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
              Live Demo
            </a>
          </div>

          <div class="mb-12">
            <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-6">Tech Stack</h2>
            <div class="flex flex-wrap gap-3">
              <span v-for="t in project.tech" :key="t" class="px-4 py-2 bg-[#f7f6f3] border border-black/5 rounded-full text-sm font-medium text-gray-700">
                {{ t }}
              </span>
            </div>
          </div>

          <div class="prose prose-lg max-w-none prose-headings:text-gray-900 prose-headings:font-extrabold prose-p:text-gray-600 prose-p:leading-relaxed prose-li:text-gray-600 prose-strong:text-gray-900 prose-a:text-[#D97757] prose-img:rounded-2xl">
            <div v-html="renderedContent"></div>
          </div>
        </div>

        <!-- Right Side: Vertical Images -->
        <div class="lg:col-span-6 space-y-10 animate-in fade-in slide-in-from-right-4 duration-700 delay-200">
          <div v-if="project.images && project.images.length > 0" class="space-y-12">
            <div v-for="(img, idx) in project.images" :key="idx" class="w-full">
              <img :src="img" class="w-full h-auto object-contain rounded-xl sm:rounded-2xl portfolio-image-crop" :alt="`Screenshot ${idx + 1}`" />
            </div>
          </div>
          <div v-else class="h-96 rounded-3xl bg-[#f7f6f3] border border-dashed border-gray-300 flex items-center justify-center text-gray-400 italic">
            No screenshots available for this project.
          </div>
        </div>
      </div>
      
      <div v-else class="text-center py-20">
        <h1 class="text-2xl font-bold text-gray-400">Project not found</h1>
        <router-link to="/portfolio" class="text-[#D97757] font-bold mt-4 inline-block hover:underline">Return to Portfolio</router-link>
      </div>
    </main>

    <footer class="border-t border-black/5 py-12 text-center text-gray-400 text-sm">
      <div class="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row justify-between items-center gap-4">
        <p>© 2026 Himansh Shivhare. All rights reserved.</p>
        <div class="flex gap-6">
          <a href="#" class="hover:text-black transition-colors">Twitter</a>
          <a href="#" class="hover:text-black transition-colors">GitHub</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { projects } from '../data/projects';
import { Marked } from 'marked';

const route = useRoute();
const projectId = route.params.id;

const project = computed(() => projects.find(p => p.id === projectId));

const marked = new Marked();

const renderedContent = computed(() => {
  if (!project.value || !project.value.longDescription) return '';
  return marked.parse(project.value.longDescription);
});
</script>

<style scoped>
.animate-in {
  animation-duration: 0.7s;
  animation-fill-mode: both;
}

.delay-200 {
  animation-delay: 200ms;
}

@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slide-in-from-left {
  from { transform: translateX(-1rem); }
  to { transform: translateX(0); }
}

@keyframes slide-in-from-right {
  from { transform: translateX(1rem); }
  to { transform: translateX(0); }
}

.fade-in { animation-name: fade-in; }
.slide-in-from-left-4 { animation-name: slide-in-from-left; }
.slide-in-from-right-4 { animation-name: slide-in-from-right; }

:deep(.prose h2) {
  margin-top: 2.5rem;
  margin-bottom: 1.25rem;
  font-size: 1.875rem;
  border-bottom: 1px solid rgba(0,0,0,0.05);
  padding-bottom: 0.5rem;
}

:deep(.prose h3) {
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

:deep(.prose p) {
  margin-bottom: 1.5rem;
}

:deep(.prose ul) {
  list-style-type: disc;
  padding-left: 1.5rem;
  margin-bottom: 1.5rem;
}

:deep(.prose li) {
  margin-bottom: 0.5rem;
}

/* Custom scrollbar for sticky left column if content is too long */
.lg\:sticky {
  max-height: calc(100vh - 120px);
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
}

.lg\:sticky::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
}
</style>
