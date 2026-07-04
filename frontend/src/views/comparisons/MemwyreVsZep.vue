<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ COMPARISONS / MEMWYRE VS ZEP</div>
          <div>COMPILATION DATE: JUNE 2026</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          Memwyre vs Zep <br />
          <span class="italic font-medium text-gray-900">Active Workspace Memory vs <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Session History.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          A deep dive comparison of developer workspace graph integration versus backend database chat history retention systems.
        </p>
      </div>

      <!-- Comparison Matrix Table -->
      <div class="border border-dashed border-gray-300 rounded p-6 bg-[#FDFCFB] my-10 relative text-left">
        <!-- Corner Brackets -->
        <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
          <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
          <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
        </div>

        <h3 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-6">Feature Comparison Matrix</h3>
        <div class="overflow-x-auto">
          <table class="w-full text-sm text-left text-gray-500">
            <thead class="text-xs uppercase bg-gray-100 text-gray-700 border-b border-gray-200 font-mono">
              <tr>
                <th scope="col" class="px-6 py-4">Capability</th>
                <th scope="col" class="px-6 py-4 bg-[#D97757]/5 text-gray-950 font-bold">Memwyre</th>
                <th scope="col" class="px-6 py-4">Zep (Chat History Engine)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 text-gray-700">
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Primary Focus</td>
                <td class="px-6 py-4 font-bold text-[#D97757] bg-[#D97757]/5">Client-side Workspace Context &amp; Graph Entities</td>
                <td class="px-6 py-4">Backend Session Logs &amp; Chat History Summaries</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Retrieval Latency</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Sub-300ms</td>
                <td class="px-6 py-4">580ms+ average</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Knowledge Network</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Entity relationships linked across projects</td>
                <td class="px-6 py-4">Isolated session logs &amp; chat vectors</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Pruning Logic</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Dynamic forgetting curves (formula-based decay)</td>
                <td class="px-6 py-4">Automatic session summarization (flat summaries)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Developer Integrations</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">MCP client/server, Cursor, VSCode, CLI hooks</td>
                <td class="px-6 py-4">SDKs (Python/JS) for application backend only</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">LoCoMo score</td>
                <td class="px-6 py-4 font-bold text-[#D97757] bg-[#D97757]/5">70.0% Accuracy</td>
                <td class="px-6 py-4">50.2% Accuracy</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Core Architectural Differences -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 py-10 text-left">
        <div class="space-y-4">
          <h3 class="hero-serif text-2xl text-gray-900">The Zep Approach</h3>
          <p class="text-gray-600 leading-relaxed text-sm">
            Zep is a backend session management database designed for building chat apps. When a user chats with your support bot, Zep indexes the conversation history, extracts simple metadata, and generates summaries of old sessions.
          </p>
          <p class="text-gray-600 leading-relaxed text-sm">
            This is perfect for customer support pipelines where a bot needs to remember that "Alice bought a red shirt yesterday." However, Zep is not designed to sit in a local terminal or IDE editor. It cannot compile project entities or track code modifications in real time, nor does it have client-side integrations.
          </p>
        </div>
        <div class="space-y-4">
          <h3 class="hero-serif text-2xl text-gray-900">The Memwyre Approach</h3>
          <p class="text-gray-600 leading-relaxed text-sm">
            Memwyre focuses on developer workspace context. It bridges local developer clients (VS Code, Cursor, terminals) to a centralized graph memory model. It models coding rules, schema edits, and terminal error resolutions.
          </p>
          <p class="text-gray-600 leading-relaxed text-sm">
            Instead of simply summarizing chat lines, Memwyre constructs entites (e.g. database names, libraries, conventions) and tracks how they evolve. The memory retrieves sub-300ms, preserving your API context buffer sizes.
          </p>
        </div>
      </div>

      <!-- CTA -->
      <div class="p-8 bg-[#050614] text-white rounded text-center my-12 relative overflow-hidden">
        <h3 class="hero-serif text-2xl sm:text-3xl mb-3">Upgrade to Stateful AI Memory</h3>
        <p class="text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Experience sub-300ms graph retrieval and official developer plugins that align context across all your editor sessions.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/signup" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#e68a6c] text-white text-sm font-semibold rounded transition-colors shadow-sm">
            Start Free
          </router-link>
          <router-link to="/ai-memory-benchmark-locomo" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
            View Benchmark Data
          </router-link>
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
