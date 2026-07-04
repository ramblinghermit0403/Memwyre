<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ INTEGRATIONS / CURSOR</div>
          <div>V2.0 STABLE</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          Cursor Memory <br />
          <span class="italic font-medium text-gray-900">Long-Term Context for <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Cursor AI IDE.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          Connect your Cursor Composer and Chat environments to your personal memory vault. Inject style rules, remember architectural patterns, and speed up composer code generations.
        </p>
      </div>

      <!-- Main Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 py-12 text-left">
        
        <!-- Details Column -->
        <div class="lg:col-span-7 space-y-8">
          <div class="space-y-4">
            <h3 class="hero-serif text-2xl text-gray-900">Accelerate Your Cursor Composer Workflows</h3>
            <p class="text-gray-600 leading-relaxed text-sm">
              Cursor is one of the most powerful developer editors, utilizing agent loops (Cursor Composer) to edit multiple files concurrently. However, Composer sessions consume a massive volume of tokens when reading codebases, leading to high latency and cost.
            </p>
            <p class="text-gray-600 leading-relaxed text-sm">
              Memwyre optimizes your Cursor setup. By indexing your design decisions, guidelines, and conventions into our memory graph, Cursor's LLM retrieves only the exact context it needs, bypassing large index scans. The result is a sub-300ms retrieval speed that keeps Composer runs fast and focused.
            </p>
          </div>

          <div class="space-y-4">
            <h4 class="font-mono text-xs uppercase font-bold text-gray-400">Core Integrations</h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Composer Context Injection</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Automatically inject coding rules, database schemas, and API constraints into Composer sessions.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Sub-300ms Cache</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Save money on index rebuilding. Memwyre local cache answers key structural questions instantly.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Automatic Entity Merging</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">When saving memories, Memwyre links them directly to Cursor codebase references (files, symbols).</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Active Forgetting</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Prunes out intermediate logs and command errors from the composer buffer to avoid cluttering attention.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Setup/Code Column -->
        <div class="lg:col-span-5">
          <div class="border border-dashed border-gray-300 rounded p-6 bg-[#FDFCFB] relative space-y-6">
            <!-- Corner Brackets -->
            <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>

            <h4 class="text-xs uppercase font-mono font-bold text-gray-400">Cursor MCP Setup</h4>
            <p class="text-xs text-gray-500">
              Add the Memwyre server in Cursor settings:
            </p>
            
            <ol class="list-decimal pl-4 space-y-3 text-xs text-gray-600">
              <li>Open <strong>Cursor Settings</strong> -> <strong>Features</strong> -> <strong>MCP</strong>.</li>
              <li>Click <strong>+ Add New MCP Server</strong>.</li>
              <li>Configure with:
                <ul class="list-disc pl-4 mt-1 space-y-1">
                  <li><strong>Name</strong>: <code>memwyre</code></li>
                  <li><strong>Type</strong>: <code>command</code></li>
                  <li><strong>Command</strong>: <code class="bg-gray-100 p-0.5 rounded">npx -y @memwyre/mcp-server</code></li>
                </ul>
              </li>
              <li>Add environment variable: <code>MEMWYRE_API_KEY</code> with your key.</li>
            </ol>

            <div class="pt-4 border-t border-gray-200 font-mono text-[11px] text-gray-500 leading-relaxed">
              * Support includes: Cursor Composer (Agent mode), Cursor Chat, and Cmd+K prompts.
            </div>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="p-8 bg-[#050614] text-white rounded text-center my-12 relative overflow-hidden">
        <h3 class="hero-serif text-2xl sm:text-3xl mb-3">Sync Context to Cursor</h3>
        <p class="text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Start building your personal long-term AI memory graph. Save context in the browser and use it in your IDE.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/signup" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#e68a6c] text-white text-sm font-semibold rounded transition-colors shadow-sm">
            Start Free
          </router-link>
          <router-link to="/blog/cursor-vs-claude-code-context" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
            Read Cursor vs Claude Code
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
