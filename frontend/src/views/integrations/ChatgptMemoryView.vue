<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ INTEGRATIONS / CHATGPT</div>
          <div>V2.0 STABLE</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          ChatGPT Memory <br />
          <span class="italic font-medium text-gray-900">Persistent Context for <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">OpenAI Chat.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          Give ChatGPT a persistent memory layer. Connect your browser sessions directly to your personal Memwyre memory vault using our browser extension or custom GPT configurations.
        </p>
      </div>

      <!-- Main Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 py-12 text-left">
        
        <!-- Details Column -->
        <div class="lg:col-span-7 space-y-8">
          <div class="space-y-4">
            <h3 class="hero-serif text-2xl text-gray-900">Stop Starting From Scratch with ChatGPT</h3>
            <p class="text-gray-600 leading-relaxed text-sm">
              ChatGPT has built-in memory, but it's isolated to the web interface and doesn't sync across your developer IDEs, terminals, or other AI tools. Memwyre acts as a unified context manager. It clips and extracts memories from your ChatGPT interactions and saves them directly into your Memory Graph.
            </p>
            <p class="text-gray-600 leading-relaxed text-sm">
              Whether you are teaching ChatGPT a complex styling convention or telling it details about your database structures, the fact is extracted and structured. You can immediately reference that same fact inside Cursor, Claude, or your local terminal session.
            </p>
          </div>

          <div class="space-y-4">
            <h4 class="font-mono text-xs uppercase font-bold text-gray-400">Core Features</h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">One-Click Clips</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Save entire chats, code blocks, or custom instructions directly to your vault from the ChatGPT UI.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Cross-Tool Sync</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Any memory saved in ChatGPT is immediately queryable inside Cursor, Claude Code, and terminal tools.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Custom GPT Integration</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Connect Memwyre as an Action schema inside custom ChatGPT GPTs for automated background updates.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <div class="font-bold text-sm text-gray-900">Smart Pruning</div>
                <p class="text-xs text-gray-500 mt-1 leading-relaxed">Outdated coding rules and intermediate errors are pruned from the context automatically.</p>
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

            <h4 class="text-xs uppercase font-mono font-bold text-gray-400">How to Setup</h4>
            <ol class="list-decimal pl-4 space-y-4 text-sm text-gray-600">
              <li>
                <strong>Install the Extension</strong>:
                Get our official <router-link to="/extension" class="text-[#D97757] underline">Chrome Extension</router-link> to add Memwyre controls straight to ChatGPT.
              </li>
              <li>
                <strong>Bind API Key</strong>:
                Log into your Memwyre dashboard, copy your API key, and configure the extension.
              </li>
              <li>
                <strong>Connect Custom GPTs (Optional)</strong>:
                Paste the Memwyre OpenAPI Action schema inside your custom GPT settings to give it background access.
              </li>
            </ol>

            <div class="pt-4 border-t border-gray-200 font-mono text-[11px] text-gray-500 leading-relaxed">
              * Support includes: ChatGPT Free, Plus, Team, and Enterprise workspaces.
            </div>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="p-8 bg-[#050614] text-white rounded text-center my-12 relative overflow-hidden">
        <h3 class="hero-serif text-2xl sm:text-3xl mb-3">Sync Your ChatGPT Conversations</h3>
        <p class="text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Start building your personal long-term AI memory graph. Save context in the browser and use it in your IDE.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/signup" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#e68a6c] text-white text-sm font-semibold rounded transition-colors shadow-sm">
            Start Free
          </router-link>
          <router-link to="/extension" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
            Install Chrome Extension
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
