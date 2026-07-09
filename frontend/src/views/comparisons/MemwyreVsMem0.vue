<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ COMPARISONS / MEMWYRE VS MEM0</div>
          <div>COMPILATION DATE: JUNE 2026</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          Memwyre vs Mem0 <br />
          <span class="italic font-medium text-gray-900">Graph Memory vs <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Flat Key-Value.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          An architectural comparison of long-term AI context retention systems. Compare entity relationship structures, retrieval latencies, and client-side developer plugin integrations.
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
                <th scope="col" class="px-6 py-4 bg-[#D97757]/5 text-gray-950 font-bold">Memwyre (Graph Memory)</th>
                <th scope="col" class="px-6 py-4">Mem0 (Key-Value Vector)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 text-gray-700">
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Retrieval Latency</td>
                <td class="px-6 py-4 font-bold text-[#D97757] bg-[#D97757]/5">Sub-300ms</td>
                <td class="px-6 py-4">420ms+ average</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Knowledge Representation</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Hierarchical Entity Graph + Vector Linkage</td>
                <td class="px-6 py-4">Flat Semantic Vectors (Key-Value list)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">Forgetting &amp; Decay Curve</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Active exponential decay based on usage frequency</td>
                <td class="px-6 py-4">Manual deletions or simple overwrite updates</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">MCP Native Support</td>
                <td class="px-6 py-4 font-bold text-emerald-600 bg-[#D97757]/5">Yes (Official client and server configurations)</td>
                <td class="px-6 py-4">No (Requires custom wrapper)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">IDE Plugins</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950">Cursor, VS Code, Claude Code CLI, OpenClaw</td>
                <td class="px-6 py-4">None (Focuses on API/SDK layers)</td>
              </tr>
              <tr>
                <td class="px-6 py-4 font-bold text-gray-900">LoCoMo Score</td>
                <td class="px-6 py-4 font-bold text-[#D97757] bg-[#D97757]/5">70.0% Accuracy</td>
                <td class="px-6 py-4">54.5% Accuracy</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Core Architectural Differences -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 py-10 text-left">
        <div class="space-y-4">
          <h3 class="hero-serif text-2xl text-gray-900">The Limitations of Flat Vectors (Mem0)</h3>
          <p class="text-gray-600 leading-relaxed text-sm">
            Mem0 stores memories as flat semantic lists. For example, if you say "I prefer tab spacing of 2 for Vue files," it converts that string to an embedding and saves it. When you query later, it fetches matching sentences.
          </p>
          <p class="text-gray-600 leading-relaxed text-sm">
            While this is ideal for simple user profile flags (e.g. "User likes dark mode"), it struggles with codebase dependency graphs. It has no structural knowledge of how entities relate. If file A depends on module B, a flat search cannot resolve multi-hop logic without bringing in excessive unrelated vectors.
          </p>
        </div>
        <div class="space-y-4">
          <h3 class="hero-serif text-2xl text-gray-900">The Power of Entity Graph Memory (Memwyre)</h3>
          <p class="text-gray-600 leading-relaxed text-sm">
            Memwyre extracts entities and defines their relations as directed graph connections. If a developer edits a mock DB file, Memwyre links the developer node, the database config node, and the API mock routes node together.
          </p>
          <p class="text-gray-600 leading-relaxed text-sm">
            During retrieval, Memwyre traverses the graph connections, resolving temporal updates and multi-session issues. old stale memories decay automatically, while reinforced concepts stay warm.
          </p>
        </div>
      </div>

      <!-- Setup Comparison -->
      <div class="border border-gray-200 rounded p-6 bg-white my-10 text-left">
        <h3 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-6">Setup Comparison</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 font-mono text-xs">
          <div>
            <div class="text-gray-400 font-bold mb-2 uppercase">Mem0 (Python API Setup)</div>
            <pre class="bg-gray-50 border border-gray-200 rounded p-4 overflow-x-auto"><code>from mem0 import Memory
m = Memory()
m.add("Prefers React", user_id="alice")
# Flat retrieval list
m.get_all(user_id="alice")</code></pre>
          </div>
          <div>
            <div class="text-[#D97757] font-bold mb-2 uppercase">Memwyre (MCP Integration config)</div>
            <pre class="bg-gray-50 border border-gray-200 rounded p-4 overflow-x-auto"><code>{
  "mcpServers": {
    "memwyre": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer KEY"]
    }
  }
}</code></pre>
          </div>
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
          <router-link to="/research/ai-memory-benchmark-locomo" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
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
