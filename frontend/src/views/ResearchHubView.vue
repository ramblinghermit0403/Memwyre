<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ RESEARCH / LAB INDEX</div>
          <div>MEMWYRE AUTHORITIES</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          The Research Hub <br />
          <span class="italic font-bold text-gray-900">Advancing AI <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Long-Term Memory.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          Memwyre Research Lab publishes studies, evaluations, and datasets exploring how entity graphs, pruning algorithms, and context compression solve statelessness in AI agent networks.
        </p>
      </div>

      <!-- Research Grid Layout -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 my-12 text-left">
        
        <!-- Document 1: LoCoMo Benchmark -->
        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm hover:border-gray-400 transition-all flex flex-col justify-between">
          <!-- Corner Brackets -->
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="space-y-4">
            <div class="text-[#D97757] font-mono text-xs uppercase font-bold">Evaluation Report &bull; Active</div>
            <h3 class="hero-serif text-2xl text-gray-900 font-bold">The LoCoMo Benchmark Report</h3>
            <p class="text-sm text-gray-500 leading-relaxed">
              Our core evaluation matrix checking long-context recall, entity traversal, and temporal consistency across 1,540 simulated developer query runs.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="text-xs font-semibold text-gray-400 font-mono">ACCURACY: 73.5% | HIT@10: 88.8%</span>
            <router-link to="/ai-memory-benchmark-locomo" class="text-xs font-bold text-[#D97757] hover:underline uppercase tracking-wider">Read Report &rarr;</router-link>
          </div>
        </div>

        <!-- Document 2: What is AI Memory -->
        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm hover:border-gray-400 transition-all flex flex-col justify-between">
          <!-- Corner Brackets -->
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="space-y-4">
            <div class="text-blue-500 font-mono text-xs uppercase font-bold">Guide &bull; Long-Form</div>
            <h3 class="hero-serif text-2xl text-gray-900 font-bold">What is AI Memory?</h3>
            <p class="text-sm text-gray-500 leading-relaxed">
              A 3,000-word comprehensive technical analysis exploring cognitive memory structures, entity graphs, vector decay formulas, and workspace agents.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="text-xs font-semibold text-gray-400 font-mono">LENGTH: 3,000 WORDS</span>
            <router-link to="/what-is-ai-memory" class="text-xs font-bold text-[#D97757] hover:underline uppercase tracking-wider">Read Guide &rarr;</router-link>
          </div>
        </div>

        <!-- Document 3: State of AI Memory 2026 -->
        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm hover:border-gray-400 transition-all flex flex-col justify-between">
          <!-- Corner Brackets -->
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="space-y-4">
            <div class="text-gray-400 font-mono text-xs uppercase font-bold">Whitepaper &bull; Trend analysis</div>
            <h3 class="hero-serif text-2xl text-gray-900 font-bold">State of AI Memory 2026</h3>
            <p class="text-sm text-gray-500 leading-relaxed">
              An inspection of context window explosion and why stateless attention buffers create substantial financial and latency overheads for enterprise codebases.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="text-xs font-semibold text-gray-400 font-mono">STATUS: PUBLISHED</span>
            <router-link to="/blog/state-of-ai-memory-2026" class="text-xs font-bold text-[#D97757] hover:underline uppercase tracking-wider">Read Article &rarr;</router-link>
          </div>
        </div>

        <!-- Document 4: Technical Papers & Experiments -->
        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm hover:border-gray-400 transition-all flex flex-col justify-between">
          <!-- Corner Brackets -->
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="space-y-4">
            <div class="text-emerald-600 font-mono text-xs uppercase font-bold">Studies &bull; Experimental</div>
            <h3 class="hero-serif text-2xl text-gray-900 font-bold">Retrieval &amp; Pruning Studies</h3>
            <p class="text-sm text-gray-500 leading-relaxed">
              Experimental results validating our mathematical decay functions: \(I(t) = I_0 \cdot e^{-\lambda t}\). Analyzing the correlation of memory reinforcement against query speed.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="text-xs font-semibold text-gray-400 font-mono">RETRIEVAL LATENCY: &lt; 300MS</span>
            <router-link to="/rag" class="text-xs font-bold text-[#D97757] hover:underline uppercase tracking-wider">View RAG Studies &rarr;</router-link>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="p-8 bg-[#050614] text-white rounded text-center my-12 relative overflow-hidden">
        <h3 class="hero-serif text-2xl sm:text-3xl mb-3">Advance Your AI Architecture</h3>
        <p class="text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Access our open source benchmark repositories, integrate Model Context Protocol memory servers, and build stateful agents.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/signup" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#e68a6c] text-white text-sm font-semibold rounded transition-colors shadow-sm">
            Join the Beta
          </router-link>
          <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
            Explore GitHub
          </a>
        </div>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import SiteFooter from '@/components/SiteFooter.vue';
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
}
</style>
