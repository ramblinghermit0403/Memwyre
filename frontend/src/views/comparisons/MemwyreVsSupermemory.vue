<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ COMPARISONS / MEMWYRE VS SUPERMEMORY</div>
          <div>COMPILATION DATE: JUNE 2026</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          Memwyre vs Supermemory <br />
          <span class="italic font-medium text-gray-900">Developer Context vs <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Personal Bookmarks.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          Compare the engineering requirements for developer-first memory networks against bookmark retrieval search engines. Understand how Memwyre's latency-optimized backend suits active agent loops.
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
                <th scope="col" class="px-6 py-4">Supermemory</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 text-gray-700">
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Primary Focus</td>
                <td class="px-6 py-4 font-bold text-[#D97757] bg-[#D97757]/5">Developer workflows &amp; Agent context</td>
                <td class="px-6 py-4">Personal bookmarks &amp; Web curation</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Retrieval Speed</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Sub-300ms latency (pruning &amp; graph cache)</td>
                <td class="px-6 py-4">600ms - 1.2s (Heavy text embedding search)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Knowledge Type</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Active multi-hop graph nodes &amp; variables</td>
                <td class="px-6 py-4">Flat static page clips &amp; files</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Decay Curve</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Exponential forgetting curve pruning</td>
                <td class="px-6 py-4">None (Permanent archive storage)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">IDE Plugins</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Cursor, VS Code, Claude Code CLI, OpenClaw</td>
                <td class="px-6 py-4">None (Chrome Extension web page clip only)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">LoCoMo score</td>
                <td class="px-6 py-4 font-bold text-[#D97757] bg-[#D97757]/5">70.0% Accuracy</td>
                <td class="px-6 py-4">46.8% Accuracy</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Core Architectural Differences -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 py-10 text-left">
        <div class="space-y-4">
          <h3 class="hero-serif text-2xl text-gray-900">The Supermemory Approach</h3>
          <p class="text-gray-600 leading-relaxed text-sm">
            Supermemory operates primarily as a web clipper and bookmark manager for AI users. It takes Twitter bookmarks, saved web pages, and uploaded PDFs, chunks them, and stores them in a vector index so you can ask a chatbot questions about your bookmarks.
          </p>
          <p class="text-gray-600 leading-relaxed text-sm">
            While this is great for organizing research articles and reading lists, it lacks the low-latency guarantees and active lifecycle integrations needed for active terminal or IDE agent sessions. Bookmarked links do not track active git diff changes, environment variables, or developer dependencies.
          </p>
        </div>
        <div class="space-y-4">
          <h3 class="hero-serif text-2xl text-gray-900">The Memwyre Approach</h3>
          <p class="text-gray-600 leading-relaxed text-sm">
            Memwyre is designed from the ground up for software engineering. It connects natively to developer CLI hooks and Model Context Protocol (MCP) clients, reading active codebase structures, workspace decisions, and project constraints.
          </p>
          <p class="text-gray-600 leading-relaxed text-sm">
            Memwyre's latency is optimized to remain under 300ms, making it suitable for inline context injection in agentic loop scripts. It prunes old error statements automatically, keeping your context buffer clean and efficient.
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
