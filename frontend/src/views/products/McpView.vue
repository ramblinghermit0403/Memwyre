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
          <div>/ PRODUCTS / MCP</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              One memory.<br class="hidden sm:block" />
              <span class="inline-block italic font-medium">Every <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">AI tool.</span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              Connect Memwyre to Claude, Cursor, VS Code, Windsurf, and any MCP-compatible client. Your context follows you everywhere.
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
                  Get MCP Keys →
                </router-link>
                <a href="/docs/integrations/mcp-server" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  Read Configuration
                </a>
              </div>
            </div>
          </div>

          <!-- Interactive CLI Terminal mockup -->
          <div class="border border-gray-300 bg-gray-950 p-6 rounded-lg relative flex flex-col justify-start min-h-[300px] shadow-lg text-gray-200">
            <div class="flex items-center gap-2 border-b border-gray-800 pb-3 mb-4">
              <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
              <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
              <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
              <span class="font-mono text-xs text-gray-500 ml-2">Terminal — memwyre-mcp</span>
            </div>
            
            <div class="font-mono text-xs sm:text-sm space-y-3">
              <div class="text-gray-400">$ npx -y mcp-remote https://server.memwyre.tech/mcp --header "Authorization:Bearer YOUR_KEY"</div>
              <div class="text-[#D97757]">Initializing Memwyre Model Context Protocol Server...</div>
              <div class="text-green-400">✔ Fetched auth credentials from environment</div>
              <div class="text-green-400">✔ Configured schemas for Cursor &amp; Claude Desktop</div>
              <div class="text-green-400">✔ Listening on stdio protocol stream</div>
              <div class="text-gray-500 mt-2">// Ready! Ask Cursor: "What did I do yesterday?"</div>
              <div class="text-blue-400 mt-1">&gt; AI: According to your memory log, you updated the auth flow config...</div>
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
            Every AI conversation starts from zero.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'Context Amnesia', body: 'AI clients do not share context. Moving from VS Code to Claude Desktop forces you to explain your stack all over again.' },
            { title: 'Repeated Explanations', body: 'Spend the first 5 prompts of every session typing out setup preferences, workspace configurations, and style guides.' },
            { title: 'Scattered Knowledge', body: 'Conversations remain locked within client histories. Your team cannot reuse the insights gained in Cursor.' }
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
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Protocol Specs</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            The universal protocol for AI context.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-5 space-y-8">
            <div v-for="(step, idx) in [
              { title: 'Expose context via Stdio', body: 'The Memwyre MCP server launches as a subprocess communicating via JSON-RPC 2.0 over standard I/O.' },
              { title: 'Declare Tools & Prompts', body: 'Exposes tools like save_memory, search_memwyre, and generate_prompt directly to your LLM sessions.' },
              { title: 'Dynamically Retrieve', body: 'When your AI agent needs context, it queries your Vault via vector and keyword search in under 300ms.' }
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
              <span>cursor.config.json</span>
              <span>JSON</span>
            </div>
            <pre class="text-xs sm:text-sm font-mono overflow-x-auto text-gray-700 leading-relaxed"><code>{
  <span class="text-[#D97757]">"mcpServers"</span>: {
    <span class="text-[#D97757]">"memwyre-vault"</span>: {
      <span class="text-[#D97757]">"command"</span>: <span class="text-[#2B7FFF]">"npx"</span>,
      <span class="text-[#D97757]">"args"</span>: [
        <span class="text-[#2B7FFF]">-y</span>,
        <span class="text-[#2B7FFF]" >mcp-remote</span>,
        <span class="text-[#2B7FFF]" >https://server.memwyre.tech/mcp</span>,
        <span class="text-[#2B7FFF]" >--header</span>,
        <span class="text-[#2B7FFF]" >Authorization:Bearer bv_sk_839f201...</span>
      ]
    }
  }
}</code></pre>
          </div>
        </div>
      </div>

      <!-- 4. COMPATIBILITY -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Ecosystem</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            One command. Infinite context.
          </h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
          <div v-for="client in [
            { name: 'Cursor', desc: 'Auto-inject context', logo: cursorLogo },
            { name: 'Claude Desktop', desc: 'Direct agent tool access', logo: claudeLogo },
            { name: 'Windsurf', desc: 'Integrated cascade memory', logo: windsurfLogo },
            { name: 'VS Code', desc: 'Extension terminal sync', logo: vscodeLogo },
            { name: 'Command Line', desc: 'Local npx command pipeline', iconClass: 'fa-solid fa-terminal' }
          ]" :key="client.name" class="p-4 border border-gray-200 rounded bg-white hover:border-[#D97757]/30 transition-colors flex items-center gap-3">
            <img v-if="client.logo" :src="client.logo" class="w-6 h-6 shrink-0 object-contain" :alt="client.name" />
            <div v-else-if="client.iconClass" class="w-6 h-6 shrink-0 flex items-center justify-center text-gray-500 text-lg">
              <i :class="client.iconClass"></i>
            </div>
            <div>
              <div class="font-bold text-gray-900 text-sm mb-0.5">{{ client.name }}</div>
              <div class="text-xs text-gray-400">{{ client.desc }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4b. DETAILED TECHNICAL SPECIFICATIONS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Protocol Specs</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Technical specifications of our MCP server.
          </h2>
        </div>

        <div class="space-y-6 text-sm text-gray-600 leading-relaxed">
          <p>
            The Model Context Protocol (MCP) server acts as a local proxy between client interfaces (such as Cursor, VS Code, and Claude Desktop) and your secure Memwyre Cloud vault. The communication is established as a stdio subprocess, exchanging JSON-RPC 2.0 messages over standard input and standard output streams. This guarantees that your connection credentials remain private and isolated to your local environment.
          </p>
          <p>
            The server exposes two primary tools to the LLM agent: <code>save_memory</code> and <code>search_memwyre</code>. When an agent runs a query, it dynamically assesses whether to call these tools. For example, if you ask Cursor "What did we configure yesterday?", the LLM generates a tool call to <code>search_memwyre</code> with semantic query parameters. The local server processes the request, performs a vector search against the Memwyre vault, and returns matching context blocks in less than 300 milliseconds.
          </p>
          <p>
            Similarly, when you compile a package or explain a new requirement, the agent calls the <code>save_memory</code> tool to persist this context. The local server routes this data back to your cloud vault, ensuring that the next time you open VS Code, Claude Desktop, or Windsurf, the agent starts with the latest context. This removes the stateless amnesia problem and guarantees consistent developer guidelines across all AI client sessions.
          </p>
          <p>
            To further optimize client query performance, the local MCP proxy maintains a lightweight cache of recently accessed semantic rule blocks. This ensures that repeated lookups of static project parameters do not require a round-trip to the cloud server, reducing latency to single-digit milliseconds. When you make changes to your cloud vault via the browser or the extension, a WebSocket invalidate signal is broadcast to clear this local cache, maintaining a fully synchronized state across your tools. This guarantees real-time updates and minimal latency.
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
          Connect your team's stack to a shared memory. Stop repeating settings and setup parameters.
        </p>
        <router-link to="/signup" class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Connect Your AI Tools
        </router-link>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import cursorLogo from '@/assets/cursor_CUBE_2D_LIGHT.svg';
import claudeLogo from '@/assets/claude-color.svg';
import vscodeLogo from '@/assets/vscode.svg';
import windsurfLogo from '@/assets/windsurf.ico';
import SiteFooter from '@/components/SiteFooter.vue';
</script>
