<template>
  <div class="relative min-h-screen bg-white dark:bg-[#0c0c0c] pt-28 pb-20 overflow-hidden font-sans">
    <!-- Grid Blueprint background line effects (consistent with landing/blog pages) -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.03] dark:opacity-[0.05]">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:40px_40px]"></div>
    </div>

    <!-- Global Vertical Grid Lines (matching landing/blog pages) -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
      <!-- Breadcrumb & Header -->
      <div class="mb-16 text-left">
        <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 mb-6 px-1">
          / RESEARCH & STUDIES
        </div>
        <h1 class="hero-serif text-4xl md:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] dark:text-white mb-6">
          The Research Hub <br />
          <span class="italic font-medium">Advancing AI <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Long-Term Memory.</span></span>
        </h1>
        <p class="text-base sm:text-lg text-[#4B5563] dark:text-gray-400 max-w-2xl font-normal leading-relaxed">
          Memwyre Research Lab publishes studies, evaluations, and datasets exploring how entity graphs, pruning algorithms, and context compression solve statelessness in AI agent networks.
        </p>

        <!-- Command Installer Codeblock in Hero -->
        <div class="relative bg-zinc-50 dark:bg-zinc-900 border border-dashed border-zinc-200 dark:border-zinc-800 rounded-none p-3.5 font-mono text-[11px] sm:text-xs text-zinc-600 dark:text-zinc-400 flex items-center justify-between gap-3 max-w-sm mt-4 select-none">
          <div class="flex items-center gap-1.5 overflow-x-auto whitespace-nowrap scrollbar-none select-all py-0.5">
            <span class="text-[#D97757] select-none font-bold">$</span>
            <span>npx -y install-memwyre</span>
          </div>
          <button 
            @click="copyCommand('npx -y install-memwyre')" 
            class="text-[#D97757] hover:text-[#C4654A] font-semibold text-[10px] sm:text-xs tracking-wider uppercase shrink-0 transition-colors cursor-pointer select-none"
          >
            {{ copiedText === 'npx -y install-memwyre' ? 'Copied' : 'Copy' }}
          </button>
        </div>
      </div>

      <!-- Grid of Cards (2 columns layout matching blog aesthetics) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        <article 
          v-for="paper in papers" 
          :key="paper.title"
          class="group relative flex flex-col justify-between p-8 bg-white dark:bg-[#111] border border-gray-200 dark:border-gray-800/80 rounded-xl hover:border-[#D97757] dark:hover:border-[#D97757] transition-all duration-300 shadow-[0_4px_20px_rgba(0,0,0,0.02)] dark:shadow-none hover:shadow-[0_8px_30px_rgba(217,119,87,0.06)] hover:-translate-y-1"
        >
          <div>
            <!-- Cover Image (minimal, aspect-ratio 2:1) -->
            <div class="w-full aspect-[2/1] rounded-lg overflow-hidden mb-6 bg-gray-50 border border-gray-100 dark:bg-zinc-900/30 dark:border-zinc-800/80 flex items-center justify-center">
              <img 
                :src="paper.cover" 
                :alt="paper.title" 
                class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-300"
              />
            </div>

            <div class="flex items-center justify-between mb-4">
              <span class="text-xs font-bold uppercase tracking-wider text-[#D97757]">
                {{ paper.category }}
              </span>
              <span class="text-xs text-gray-400 dark:text-gray-500 font-light">
                {{ paper.readTime }}
              </span>
            </div>
            
            <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-3 group-hover:text-[#D97757] transition-colors duration-200 leading-snug">
              <router-link :to="paper.link">
                {{ paper.title }}
              </router-link>
            </h2>
            
            <p class="text-[14px] text-gray-500 dark:text-gray-400 font-light leading-relaxed mb-6">
              {{ paper.excerpt }}
            </p>
          </div>

          <div class="flex items-center justify-between mt-auto pt-4 border-t border-gray-100 dark:border-gray-900">
            <span class="text-xs text-gray-400 dark:text-gray-500 font-mono font-semibold uppercase">
              {{ paper.date }}
            </span>
            <router-link 
              :to="paper.link"
              class="inline-flex items-center gap-1 text-sm font-semibold text-[#D97757] hover:text-[#c05c3d] transition-colors duration-150"
            >
              Read Report
              <svg class="w-4 h-4 transform group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
        </article>
      </div>

      <!-- CTA (matching branding with dashed borders and corners) -->
      <div class="p-8 sm:p-12 border border-dashed border-gray-300 dark:border-zinc-800 bg-white dark:bg-[#111] rounded-xl text-center my-16 relative overflow-hidden">
        <!-- Corner Brackets -->
        <div class="absolute top-2 left-2 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
        <div class="absolute top-2 right-2 w-3 h-3 pointer-events-none border-t-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
        <div class="absolute bottom-2 left-2 w-3 h-3 pointer-events-none border-b-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
        <div class="absolute bottom-2 right-2 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>

        <h3 class="hero-serif text-3xl mb-3 text-gray-950 dark:text-white">Advance Your AI Architecture</h3>
        <p class="text-gray-500 dark:text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Access our open source benchmark repositories, integrate Model Context Protocol memory servers, and build stateful agents.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/signup" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#c05c3d] text-white text-sm font-semibold rounded-lg transition-colors shadow-sm">
            Join the Beta
          </router-link>
          <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank" class="px-6 py-2.5 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 hover:bg-gray-100 dark:hover:bg-zinc-800 text-gray-700 dark:text-gray-300 text-sm font-semibold rounded-lg transition-colors">
            Explore GitHub
          </a>
        </div>
      </div>
    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import SiteFooter from '@/components/SiteFooter.vue';

const copiedText = ref('');
const copyCommand = (cmd) => {
  navigator.clipboard.writeText(cmd);
  copiedText.value = cmd;
  setTimeout(() => {
    copiedText.value = '';
  }, 2000);
};

const papers = [
  {
    category: 'Evaluation Report',
    title: 'The LoCoMo Benchmark Report',
    excerpt: 'Our core evaluation matrix checking long-context recall, entity traversal, and temporal consistency across 1,540 simulated developer query runs.',
    readTime: 'Active',
    date: 'ACCURACY: 73.5% | HIT@10: 88.8%',
    link: '/research/ai-memory-benchmark-locomo',
    cover: '/blog-covers/ai-memory-benchmark-locomo.png'
  }
];
</script>


