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
          <div>/ PRODUCTS / PERSONAL APP</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              One Memory for<br class="hidden sm:block" />
              <span class="inline-block italic font-medium">Every <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">AI you use.</span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              One memory across every AI you use. Save it once and it shows up in Cursor, Claude, ChatGPT, wherever you work. Stop re-introducing yourself to a blank slate.
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
                  Get Personal App →
                </router-link>
                <router-link to="/dashboard"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  Launch Web App
                </router-link>
              </div>
            </div>
          </div>

          <!-- Interactive Chat Mockup with Memwyre -->
          <div class="border border-gray-200 bg-white p-6 rounded-lg relative flex flex-col justify-between min-h-[300px] shadow-lg">
            <div class="flex items-center justify-between border-b border-gray-100 pb-3 mb-4">
              <div class="flex items-center gap-2">
                <div class="w-6 h-6 rounded-full bg-[#D97757] text-white flex items-center justify-center text-xs">✨</div>
                <span class="font-bold text-sm text-gray-900">Memwyre Memory Assistant</span>
              </div>
              <span class="text-[10px] font-mono text-gray-400 font-bold uppercase tracking-wider">online</span>
            </div>
            
            <div class="space-y-4 flex-1 font-sans text-xs sm:text-sm">
              <div class="bg-gray-50 p-3 rounded text-gray-600 text-right max-w-[80%] ml-auto">
                What was that framework I used for the landing page last week?
              </div>
              <div class="bg-orange-50/50 border border-orange-100 p-3 rounded text-gray-700 max-w-[80%]">
                You used <span class="font-bold text-[#D97757]">Vite + Vue 3</span> with Tailwind CSS. I have indexed the configuration file in your vault.
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
            Every AI meets you as a stranger.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'Blank Slates', body: 'AI chat sessions have no cross-session recall. You must continuously re-upload directories and state details on refresh.' },
            { title: 'No Continuity', body: 'Insights or coding solutions achieved in ChatGPT are completely invisible when you work inside Cursor or Claude.' },
            { title: 'Forgotten Knowledge', body: 'Useful references, shell scripts, and architectural decisions are lost once chat histories roll off active listings.' }
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
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Workflow</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Set up once &amp; you're done.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-6 space-y-8">
            <div v-for="(step, idx) in [
              { title: 'Unified Ingestion Inbox', body: 'Route all incoming notes, webpage clips, and CLI runs directly to your pending Inbox queue for approval.' },
              { title: 'WebSocket Live Streams', body: 'Receive instant pushes when new memory clusters or facts are processed by your background workers.' },
              { title: 'Granular Key Permissions', body: 'Provision scoped API keys (e.g. read:inbox, write:memories) rather than granting blanket server access.' }
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

          <div class="lg:col-span-6 border border-gray-200 rounded-lg overflow-hidden bg-white p-6 flex flex-col justify-center min-h-[200px]">
            <div class="text-center space-y-4">
              <div class="font-bold text-gray-900 text-base">Integrated Everywhere</div>
              <p class="text-xs text-gray-500 leading-relaxed max-w-xs mx-auto">
                Syncs across every major client, editor, and browser. Portable context, zero lock-in.
              </p>
              <div class="flex flex-wrap justify-center gap-4 pt-2">
                <div v-for="logo in logoList" :key="logo.name" class="w-10 h-10 bg-white border border-gray-200 rounded-md flex items-center justify-center p-2 shadow-sm hover:border-[#D97757]/30 transition-all duration-300" :title="logo.name">
                  <img :src="logo.src" class="w-full h-full object-contain" :alt="logo.name" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. MEMWYRE COMPANION -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Memwyre Assistant</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Want to ask your memory directly? Use Memwyre.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="space-y-4">
            <h3 class="text-xl font-bold text-gray-900">Your custom knowledge assistant</h3>
            <p class="text-sm text-gray-500 leading-relaxed">
              Memwyre is your direct interface to your second brain. Chat, query, or search for references. Memwyre uses advanced RAG and memory graphs to answer questions about your specific projects and preferences.
            </p>
            <ul class="space-y-2 text-sm text-gray-600">
              <li>• Access all connections in a single search box</li>
              <li>• Completely private and secure</li>
              <li>• Delete or edit memories at any time</li>
            </ul>
          </div>
          <div class="border border-gray-200 rounded p-6 bg-white flex flex-col justify-center">
            <div class="text-xs font-mono text-gray-400 mb-2">// SAMPLE MEMWYRE SEARCH</div>
            <div class="font-mono text-sm text-gray-800">
              <span class="text-[#D97757]">&gt;</span> find: "auth routing setup"<br>
              <span class="text-green-600">Found 3 references across Gmail &amp; Github.</span><br>
              <span class="text-gray-500">Summary: Himanshu updated the routing config in pull request #12.</span>
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
          The last time you start from scratch.
        </h3>
        <p class="text-sm text-gray-500 max-w-md mx-auto mb-6">
          Initialize your personal memory layer today. Free for personal use.
        </p>
        <router-link to="/signup" class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Initialize Personal Memory
        </router-link>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import cursorLogo from '@/assets/cursor_CUBE_2D_LIGHT.svg';
import claudeLogo from '@/assets/claude-color.svg';
import openaiLogo from '@/assets/openai.svg';
import vscodeLogo from '@/assets/vscode.svg';
import chromeLogo from '@/assets/chrome-logo-svgrepo-com.svg';
import edgeLogo from '@/assets/microsoft-edge-logo.svg';
import windsurfLogo from '@/assets/windsurf.ico';
import SiteFooter from '@/components/SiteFooter.vue';

const logoList = [
  { name: 'Cursor', src: cursorLogo },
  { name: 'Claude', src: claudeLogo },
  { name: 'OpenAI / ChatGPT', src: openaiLogo },
  { name: 'VS Code', src: vscodeLogo },
  { name: 'Chrome', src: chromeLogo },
  { name: 'Edge', src: edgeLogo },
  { name: 'Windsurf', src: windsurfLogo }
];
</script>
