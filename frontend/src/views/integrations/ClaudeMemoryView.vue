<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ INTEGRATIONS / CLAUDE</div>
          <div>V2.0 STABLE</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          Claude Memory <br />
          <span class="italic font-medium text-gray-900">Persistent Graph Context for <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Claude.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          Connect your Claude Desktop app or Claude Code terminal CLI to a unified memory layer. Inject codebase instructions, remember past debugging choices, and keep context compact.
        </p>
      </div>

      <!-- Main Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 py-12 text-left">
        
        <!-- Details Column -->
        <div class="lg:col-span-7 space-y-8">
          <div class="space-y-4">
            <h3 class="hero-serif text-2xl text-gray-900">Empower Claude with Persistent Knowledge</h3>
            <p class="text-gray-600 leading-relaxed text-sm">
              Anthropic's Claude models excel at complex reasoning, coding syntax, and layout structure. However, without a memory layer, Claude sessions quickly run out of memory or repeat identical mistakes. By connecting Claude to Memwyre, you provide a structured memory vault that Claude can query and save to dynamically.
            </p>
            <p class="text-gray-600 leading-relaxed text-sm">
              Whether you are using Claude Desktop for copywriting and architecture planning or Claude Code inside your local terminal for terminal tasks, Memwyre feeds context seamlessly.
            </p>
          </div>

          <div class="space-y-4">
            <h4 class="font-mono text-xs uppercase font-bold text-gray-400">Core Capabilities</h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Claude Code Integration</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Save terminal conversations automatically on exit and inject context dynamically when starting sessions.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Claude Desktop MCP</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Read and write memories directly within your desktop assistant sidebar via local MCP server integration.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Dynamic Pruning</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Keeps Claude's context footprints low. Saves token costs by filtering out duplicate CLI or compiler logs.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Entity Relationships</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Claude maps connections between databases, files, and styles, allowing multi-hop reasoning next turn.</p>
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

            <h4 class="text-xs uppercase font-mono font-bold text-gray-400">Claude Desktop Configuration</h4>
            <p class="text-xs text-gray-500">
              Add the following to your <code>claude_desktop_config.json</code> file:
            </p>
            
            <pre class="bg-gray-900 text-gray-100 border border-gray-800 rounded p-4 font-mono text-[10px] overflow-x-auto text-left"><code>{
  "mcpServers": {
    "memwyre-memory": {
      "command": "npx",
      "args": ["-y", "@memwyre/mcp-server"],
      "env": {
        "MEMWYRE_API_KEY": "YOUR_MEMWYRE_KEY"
      }
    }
  }
}</code></pre>

            <div class="pt-4 border-t border-gray-200 font-mono text-[11px] text-gray-500 leading-relaxed">
              * Official guide: <router-link to="/blog/mcp-persistent-memory" class="text-[#D97757] underline">Claude Desktop Memory Guide</router-link> or <router-link to="/blog/claude-code-memory-ingestion" class="text-[#D97757] underline">Claude Code Guide</router-link>.
            </div>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="p-8 bg-[#050614] text-white rounded text-center my-12 relative overflow-hidden">
        <h3 class="hero-serif text-2xl sm:text-3xl mb-3">Integrate with Claude in Under 5 Minutes</h3>
        <p class="text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Start building your personal long-term AI memory graph. Save context in the browser and use it in your IDE.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/signup" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#e68a6c] text-white text-sm font-semibold rounded transition-colors shadow-sm">
            Start Free
          </router-link>
          <a href="/docs/" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
            Read Integration Docs
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
