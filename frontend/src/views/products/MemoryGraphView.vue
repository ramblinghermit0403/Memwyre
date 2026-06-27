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
          <div>/ PRODUCTS / MEMORY GRAPH</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              Memories that<br class="hidden sm:block" />
              <span class="inline-block italic font-medium">remember <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">each other.</span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              A living knowledge graph where memories connect to other memories. Automatic extraction, intelligent relationships, and built-in forgetting — no manual work required.
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
                  Build Memory Graph →
                </router-link>
                <a href="/docs/graph/overview" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  Read Documentation
                </a>
              </div>
            </div>
          </div>

          <!-- Interactive Node-Link SVG Diagram -->
          <div class="border border-dashed border-gray-300 bg-white p-8 relative flex flex-col justify-center min-h-[300px]">
            <!-- corner brackets -->
            <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-gray-400"></div>
            <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-gray-400"></div>
            <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-gray-400"></div>
            <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-gray-400"></div>

            <div class="relative w-full max-w-xs mx-auto aspect-square flex items-center justify-center">
              <svg class="absolute inset-0 w-full h-full" viewBox="0 0 100 100" fill="none">
                <!-- Lines connecting nodes -->
                <line x1="50" y1="50" x2="20" y2="30" stroke="#D97757" stroke-width="1.5" opacity="0.6" />
                <line x1="50" y1="50" x2="80" y2="30" stroke="#D97757" stroke-width="1.5" opacity="0.6" />
                <line x1="50" y1="50" x2="50" y2="85" stroke="#D97757" stroke-width="1.5" opacity="0.6" />
                <line x1="20" y1="30" x2="80" y2="30" stroke="#D97757" stroke-width="1.5" stroke-dasharray="2 2" opacity="0.4" />
                
                <!-- Center: Primary Memory Node -->
                <circle cx="50" cy="50" r="8" fill="#D97757" class="animate-pulse" />
                <text x="50" y="63" font-family="monospace" font-size="5" font-weight="bold" fill="#000" text-anchor="middle">User Node</text>

                <!-- Outlying Nodes -->
                <circle cx="20" cy="30" r="5" fill="#474747" />
                <circle cx="80" cy="30" r="5" fill="#474747" />
                <circle cx="50" cy="85" r="5" fill="#474747" />
              </svg>
            </div>
            <div class="text-[10px] uppercase tracking-widest font-mono font-bold text-gray-400 text-center mt-6">evolving memory nodes</div>
          </div>
        </div>
      </div>

      <!-- 2. THE PROBLEM / USE CASE -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">The Disconnect</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Triplet graphs don't scale.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'Triplet Overhead', body: 'Classic entity-relation triplets (Subject-Predicate-Object) result in highly fragmented databases. Writing schemas manually is tedious.' },
            { title: 'Slow Queries', body: 'Graph queries requiring deep recursive traversals (joins) lead to exponential latency increases as nodes scale.' },
            { title: 'No Temporal Decoupling', body: 'Triplets preserve historical facts forever without context-aware forgetting, cluttering the prompt windows over time.' }
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
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Architecture</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Add content. The graph builds itself.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-5 space-y-8">
            <div v-for="(step, idx) in [
              { title: 'Extract Facts', body: 'Isolates discrete Subject-Predicate-Object triplets from ingested memory content using parallel LLM analysis.' },
              { title: 'Supersede Contradictions', body: 'Identifies conflicting states (e.g. location or email) and marks old facts as superseded in the database.' },
              { title: 'Temporal Decay', body: 'Sets valid_until timestamps on facts, ensuring old or temporary context decays and does not clutter prompts.' }
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
              <span>Fact Database Schema Model</span>
              <span>JSON</span>
            </div>
            <pre class="text-xs sm:text-sm font-mono overflow-x-auto text-gray-700 leading-relaxed"><code>{
  <span class="text-[#D97757]">"id"</span>: <span class="text-[#2B7FFF]">142</span>,
  <span class="text-[#D97757]">"subject"</span>: <span class="text-[#2B7FFF]">"User"</span>,
  <span class="text-[#D97757]">"predicate"</span>: <span class="text-[#2B7FFF]">"prefers"</span>,
  <span class="text-[#D97757]">"object"</span>: <span class="text-[#2B7FFF]">"dark mode UI styling"</span>,
  <span class="text-[#D97757]">"is_superseded"</span>: <span class="text-[#2B7FFF]">false</span>,
  <span class="text-[#D97757]">"valid_from"</span>: <span class="text-[#2B7FFF]">"2026-06-18T10:00:00Z"</span>,
  <span class="text-[#D97757]">"valid_until"</span>: <span class="text-[#2B7FFF]">null</span>
}</code></pre>
          </div>
        </div>
      </div>

      <!-- 4. THREE WAY CONNECTIONS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Graph Relations</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Three ways memories connect.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="rel in [
            { name: 'Updates', desc: 'Overwrites outdated or contradicted facts dynamically to prevent stale responses.', border: 'border-l-4 border-l-red-500' },
            { name: 'Extends', desc: 'Builds upon existing nodes by adding granular contextual details and links.', border: 'border-l-4 border-l-[#D97757]' },
            { name: 'Derives', desc: 'Synthesizes high-level insights by correlating multiple historical episodes.', border: 'border-l-4 border-l-blue-500' }
          ]" :key="rel.name" :class="['p-6 border border-gray-200 rounded bg-white', rel.border]">
            <div class="font-bold text-gray-900 text-lg mb-1">{{ rel.name }}</div>
            <p class="text-xs text-gray-500 leading-relaxed">{{ rel.desc }}</p>
          </div>
        </div>
      </div>

      <!-- 5. BOTTOM CTA -->
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
          Build a long-term memory that logically updates and evolves over time.
        </p>
        <router-link to="/signup" class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Initialize Memory Graph
        </router-link>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
// Memory Graph view component logic
import SiteFooter from '@/components/SiteFooter.vue';
</script>
