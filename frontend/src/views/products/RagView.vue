<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- 1. HERO SECTION -->
      <div class="pt-2 pb-10 sm:pb-12">
        <!-- Breadcrumb -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ PRODUCTS / RAG ENGINE</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              Search that<br class="hidden sm:block" />
              <span class="inline-block italic font-medium">actually <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">understands.</span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              Hybrid search with sub-300ms latency. Multi-modal RAG for PDFs, images, videos, and web pages. Context-aware reranking that surfaces what matters.
            </p>
            
            <!-- Buttons with technical grid brackets -->
            <div class="relative inline-flex p-3 mt-4 sm:mt-6 border border-dashed border-gray-300 rounded max-w-max z-20">
              <!-- Corner Brackets (Crosshairs) -->
              <div class="absolute -top-2 -left-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -top-2 -right-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-2 -left-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-2 -right-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>

              <!-- Content (Buttons) -->
              <div class="flex flex-row items-center justify-start gap-3 sm:gap-4">
                <router-link to="/signup"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-[#050614] text-white font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md text-xs sm:text-sm inline-flex items-center justify-center gap-2">
                  Access RAG API →
                </router-link>
                <a href="/docs/rag/retrieval" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  Read API Reference
                </a>
              </div>
            </div>
          </div>

          <!-- Interactive Latency Chart -->
          <div class="border border-dashed border-gray-300 bg-white p-8 relative flex flex-col justify-center min-h-[300px]">
            <!-- corner brackets -->
            <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-gray-400"></div>
            <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-gray-400"></div>
            <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-gray-400"></div>
            <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-gray-400"></div>

            <div class="space-y-4 max-w-md mx-auto w-full">
              <div class="flex items-center justify-between font-mono text-[10px] text-gray-400">
                <span>RAG LATENCY BENCHMARK</span>
                <span>LOWER IS BETTER</span>
              </div>
              
              <div class="space-y-3 pt-2">
                <div>
                  <div class="flex justify-between text-xs font-bold font-mono mb-1">
                    <span>Standard RAG (Dense Vector)</span>
                    <span class="text-gray-500">1,240ms</span>
                  </div>
                  <div class="w-full h-3 bg-gray-200 rounded">
                    <div class="h-full bg-gray-400 rounded-l" style="width: 80%"></div>
                  </div>
                </div>
                
                <div>
                  <div class="flex justify-between text-xs font-bold font-mono mb-1">
                    <span>Memwyre Hybrid-RAG</span>
                    <span class="text-[#D97757]">240ms</span>
                  </div>
                  <div class="w-full h-3 bg-gray-200 rounded">
                    <div class="h-full bg-[#D97757] rounded-l" style="width: 20%"></div>
                  </div>
                </div>
              </div>
            </div>
            <div class="text-[10px] uppercase tracking-widest font-mono font-bold text-gray-400 text-center mt-6">benchmark query speed</div>
          </div>
        </div>
      </div>

      <!-- 2. THE PROBLEM / USE CASE -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">The Disconnect</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Traditional RAG is broken.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'Lost in Chunks', body: 'Standard parsing breaks paragraphs midway. AI misses crucial context when relevant information is split across chunk boundaries.' },
            { title: 'Similarity is not Relevance', body: 'Vector cosine similarity indexes synonyms but fails to verify actual semantic relevance, yielding noisy LLM inputs.' },
            { title: 'Slow at Scale', body: 'As repositories grow, dense vector index scans slow down. Sub-second recall becomes impossible without complex database tuning.' }
          ]" :key="idx" class="p-6 border border-gray-200 rounded-lg bg-white shadow-sm hover:border-[#D97757]/40 transition-colors">
            <div class="text-xs tracking-wider font-mono font-bold text-gray-400 mb-4">0{{ idx + 1 }} . PROBLEM</div>
            <h3 class="text-lg font-bold text-gray-900 mb-2">{{ problem.title }}</h3>
            <p class="text-sm text-gray-500 leading-relaxed">{{ problem.body }}</p>
          </div>
        </div>
      </div>

      <!-- 3. TECHNICAL DETAILS / HOW IT WORKS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">RAG Pipeline</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            RAG, reimagined from scratch.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-5 space-y-8">
            <div v-for="(step, idx) in [
              { title: 'Semantic Sentence Chunking', body: 'Groups sentences dynamically using cosine similarity of adjacent sentence embeddings, preventing split ideas.' },
              { title: 'LLM Contextual Enrichment', body: 'Enriches every chunk with AI-generated summaries, entity lists, and Q&As to improve search matches.' },
              { title: 'Multi-View Retrieval', body: 'Supports vector search (semantic), current truth facts (state), time-based memory logs (episodic), or hybrid unified recall (auto).' }
            ]" :key="idx" class="flex gap-4">
              <div class="w-8 h-8 rounded-full border border-gray-300 text-sm font-bold font-mono flex items-center justify-center shrink-0 text-[#D97757] bg-white">
                {{ idx + 1 }}
              </div>
              <div>
                <h4 class="font-bold text-gray-900 mb-1">{{ step.title }}</h4>
                <p class="text-sm text-gray-500 leading-relaxed">{{ step.body }}</p>
              </div>
            </div>
          </div>

          <div class="lg:col-span-7 border border-gray-200 rounded-lg overflow-hidden bg-gray-50 p-6">
            <div class="flex items-center justify-between border-b border-gray-200 pb-3 mb-4 font-mono text-xs text-gray-400">
              <span>POST /api/v1/retrieval/search</span>
              <span>JavaScript</span>
            </div>
            <pre class="text-xs sm:text-sm font-mono overflow-x-auto text-gray-700 leading-relaxed"><code><span class="text-[#0452db]">const</span> response = <span class="text-[#0452db]">await</span> <span class="text-[#0452db]">fetch</span>(<span class="text-[#2B7FFF]">"https://server.memwyre.tech/api/v1/retrieval/search"</span>, {
  method: <span class="text-[#2B7FFF]">"POST"</span>,
  headers: {
    <span class="text-[#2B7FFF]">"Authorization"</span>: <span class="text-[#2B7FFF]">"Bearer bv_sk_your_api_key_here"</span>,
    <span class="text-[#2B7FFF]">"Content-Type"</span>: <span class="text-[#2B7FFF]">"application/json"</span>
  },
  body: JSON.stringify({
    query: <span class="text-[#2B7FFF]">"find error codes for deployment"</span>,
    view: <span class="text-[#2B7FFF]">"auto"</span>, <span class="text-[#888888]">// semantic, state, episodic, or auto</span>
    top_k: <span class="text-[#2B7FFF]">5</span>
  })
});
<span class="text-[#0452db]">const</span> results = <span class="text-[#0452db]">await</span> response.json();</code></pre>
          </div>
        </div>
      </div>

      <!-- 4. SUPPORTED FORMATS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Ingestion</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Understand any format.
          </h2>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          <div v-for="format in [
            { name: 'Text / Markdown', desc: '.txt, .md, .mdx files', iconClass: 'fa-regular fa-file-lines' },
            { name: 'PDFs & Epubs', desc: 'Embedded text extraction', iconClass: 'fa-regular fa-file-pdf' },
            { name: 'Web Pages / URLs', desc: 'CSS-stripped clean text', iconClass: 'fa-solid fa-globe' },
            { name: 'Images', desc: 'OCR & visual parsing', iconClass: 'fa-regular fa-file-image' },
            { name: 'Audio', desc: 'Automatic transcription', iconClass: 'fa-regular fa-file-audio' },
            { name: 'Video', desc: 'Frame semantic indexing', iconClass: 'fa-regular fa-file-video' },
            { name: 'Google Docs', desc: 'Drive sync document format', logo: driveLogo },
            { name: 'CSV / JSON', desc: 'Structured schema records', iconClass: 'fa-solid fa-file-code' }
          ]" :key="format.name" class="p-4 border border-gray-200 rounded bg-white hover:border-[#D97757]/30 transition-colors flex items-center gap-3">
            <img v-if="format.logo" :src="format.logo" class="w-6 h-6 shrink-0" :alt="format.name" />
            <div v-else-if="format.iconClass" class="w-6 h-6 shrink-0 flex items-center justify-center text-gray-500 text-lg">
              <i :class="format.iconClass"></i>
            </div>
            <div>
              <div class="font-bold text-gray-900 text-sm mb-0.5">{{ format.name }}</div>
              <div class="text-xs text-gray-400">{{ format.desc }}</div>
            </div>
          </div>
        </div>
      </div>

      <div class="border border-dashed border-gray-300 rounded-none p-12 text-center bg-white relative my-12 sm:my-16 overflow-hidden">
        <!-- corner brackets -->
        <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-gray-400"></div>
        <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-gray-400"></div>
        <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-gray-400"></div>
        <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-gray-400"></div>

        <h3 class="hero-serif text-2xl sm:text-3xl lg:text-4xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-4">
          Context infrastructure for AI agents.
        </h3>
        <p class="text-sm text-gray-500 max-w-md mx-auto mb-6">
          Upgrade your retrieval stack. Get started with sub-300ms semantic RAG queries.
        </p>
        <router-link to="/signup" class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Initialize RAG Engine
        </router-link>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import driveLogo from '@/assets/google-drive.svg';
import SiteFooter from '@/components/SiteFooter.vue';
</script>
