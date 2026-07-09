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
          <div>/ PRODUCTS / PLUGINS</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              Your AI knows<br class="hidden sm:block" />
              <span class="inline-block italic font-medium">your <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">project.</span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              Memwyre plugins for Claude Code, OpenClaw, OpenCode, and Hermes Agent. One-click memory save, automatic context injection, and project-scoped knowledge.
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
                  Get Developer Plugins →
                </router-link>
                <a href="/docs/integrations/plugins/claude" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  View Documentation
                </a>
              </div>
            </div>
          </div>

          <!-- Project file scope diagram mockup -->
          <div class="border border-dashed border-gray-300 bg-white p-8 relative flex flex-col justify-center min-h-[300px]">
            <!-- corner brackets -->
            <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-gray-400"></div>
            <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-gray-400"></div>
            <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-gray-400"></div>
            <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-gray-400"></div>

            <div class="max-w-md mx-auto w-full space-y-4 font-mono text-xs">
              <div class="border border-gray-200 bg-white p-3 rounded shadow-sm">
                <div class="text-[#D97757] font-bold mb-1">📁 workspace-root/</div>
                <div class="pl-4 text-gray-500">├── 📁 src/</div>
                <div class="pl-4 text-gray-500">├── 📁 .memwyre/</div>
                <div class="pl-8 text-green-600 font-semibold">└── 📄 project-scope.db (Indexed!)</div>
              </div>
              
              <div class="flex items-center gap-3 bg-white border border-gray-200 p-3 rounded shadow-sm">
                <span class="text-xl">🚀</span>
                <div>
                  <div class="font-bold text-gray-900">Project Scoping</div>
                  <div class="text-[10px] text-gray-400">Auto-filters memory query by directory scope</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. THE PROBLEM / USE CASE -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">The Disconnect</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Every AI tool starts from zero.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'No Project Memory', body: 'AI agents operate strictly on local context directories. They forget historical debugging runs and architecture decisions.' },
            { title: 'Repeated Explanations', body: 'Developers waste time repeatedly explaining libraries version mismatches, build requirements, and codebase conventions.' },
            { title: 'Isolated Tooling', body: 'Conversations remain locked within client histories. Your team cannot reuse the insights gained in Claude Code.' }
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
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Plugin Specs</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Install once. Remember forever.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-5 space-y-8">
            <div v-for="(step, idx) in [
              { title: 'Add config parameters', body: 'Configure the Memwyre plugin under plugins.entries.openclaw-plugin in openclaw.json with your key (starts with bv_sk_).' },
              { title: 'Semantic Loop Protection', body: 'The plugin tracks queries and intercepts duplicate searches, preventing LLM agents from entering infinite query loops.' },
              { title: 'Prompt Sanitization', body: 'Automatically strips reasoning, thought, and role tags from context streams to prevent agent message parser crashes.' }
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
              <span>openclaw.json</span>
              <span>JSON</span>
            </div>
            <pre class="text-xs sm:text-sm font-mono overflow-x-auto text-gray-700 leading-relaxed"><code>{
  <span class="text-[#D97757]">"plugins"</span>: {
    <span class="text-[#D97757]">"entries"</span>: {
      <span class="text-[#D97757]">"openclaw-plugin"</span>: {
        <span class="text-[#D97757]">"enabled"</span>: <span class="text-[#2B7FFF]">true</span>,
        <span class="text-[#D97757]">"config"</span>: {
          <span class="text-[#D97757]">"apiKey"</span>: <span class="text-[#2B7FFF]">"bv_sk_your_api_key_here"</span>,
          <span class="text-[#D97757]">"hostUrl"</span>: <span class="text-[#2B7FFF]">"https://server.memwyre.tech"</span>
        }
      }
    }
  }
}</code></pre>
          </div>
        </div>
      </div>

      <!-- 4. SUPPORTED DEVELOPER PLUGINS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Ecosystem</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Built for the tools you love.
          </h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="agent in [
            { name: 'Claude Code', desc: 'Auto-inject command line prompts & error summaries', logo: claudeLogo },
            { name: 'OpenClaw', desc: 'Autonomous memory hooks for multi-agent workflows', logo: openclawLogo },
            { name: 'OpenCode', desc: 'Shared coding patterns & architecture conventions', iconClass: 'fa-solid fa-code' },
            { name: 'Hermes Agent', desc: 'Secure local-first knowledge extraction & scoping', iconClass: 'fa-solid fa-robot' }
          ]" :key="agent.name" class="p-6 border border-gray-200 rounded bg-white hover:border-[#D97757]/30 transition-all duration-300 flex flex-col justify-between min-h-[200px]">
            <div>
              <div class="flex items-center gap-3 mb-2">
                <img v-if="agent.logo" :src="agent.logo" class="w-8 h-8 shrink-0 object-contain" :alt="agent.name" />
                <div v-else-if="agent.iconClass" class="w-8 h-8 shrink-0 flex items-center justify-center text-gray-500 text-2xl">
                  <i :class="agent.iconClass"></i>
                </div>
                <div class="font-bold text-gray-900 text-base leading-tight">{{ agent.name }}</div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">{{ agent.desc }}</p>
            </div>
            <div class="text-[10px] font-mono text-green-600 font-bold uppercase tracking-wider mt-4">✔ plugin active</div>
          </div>
        </div>
      </div>

      <!-- 4b. DETAILED TECHNICAL SPECIFICATIONS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Integration Details</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Technical specifications of our developer plugins.
          </h2>
        </div>

        <div class="space-y-6 text-sm text-gray-600 leading-relaxed">
          <p>
            Memwyre developer plugins extend your command-line and agent environments by hooking directly into their execution cycles. For CLI tools like Claude Code, the integration exposes shell hooks that run before a command executes (pre-command hook) and after it exits (post-command hook). This allows the plugin to automatically capture error outputs, build files, and command history, streaming them into your memory vault as structured entries without requiring manual copy-pasting.
          </p>
          <p>
            For autonomous frameworks such as OpenClaw, the plugin implements a persistent memory provider. As the agent plans and executes tasks, it queries the memory graph via vector semantic matching to retrieve relevant historical insights, while writing new learnings back to the graph. This creates a stateful workspace where agents can build upon work done in previous runs.
          </p>
          <p>
            To prevent LLM context-window exhaustion and optimize token usage, the plugin uses a client-side filter. It dynamically selects and injects only the most relevant style rules, environment variables, and codebase paths based on the current task's scope. All interactions are signed using your developer API token, securing the connection between local CLI agents and your private cloud memory.
          </p>
          <p>
            In IDE environments like VS Code and Cursor, the plugins run in the editor background, subscribing to active buffer state updates. When you open a file or start editing a line, the plugin extracts import statements and class definitions, querying your vault for related documentation pages. This allows the AI assistant to automatically suggest correct parameters or identify deprecated functions based on past debugging sessions stored in your vault. This real-time suggestion model boosts developer velocity.
          </p>
          <p>
            All remote server interactions are authenticated via standard API keys that you can generate and rotate within the settings tab. The plugin client library maintains an offline-first storage queue; if your network connection drops, tool calls and saved memories are queued locally and synchronized automatically once the connection is restored, ensuring zero interruption in developer workflows. This local persistence queue makes the system fully reliable, resilient to network drops, and highly secure.
          </p>
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
          Give your AI agents a persistent long-term memory. Setup plugins in under 5 minutes.
        </p>
        <router-link to="/signup" class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Get Developer Plugins
        </router-link>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import claudeLogo from '@/assets/claude-color.svg';
import openclawLogo from '@/assets/openclaw-color.svg';
import SiteFooter from '@/components/SiteFooter.vue';
</script>
