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
          <div>/ PRODUCTS / CHROME EXTENSION</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              Your browser, with<br class="hidden sm:block" />
              <span class="inline-block">a <span class="italic font-medium">photographic <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">memory.</span></span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              Save AI chats, reusable prompts, code snippets, and webpage content directly from ChatGPT, Claude, and any site with a single click. Keep your research context fresh without breaking your flow.
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
                <a href="https://chromewebstore.google.com/detail/memwyre/biplnkodgfdgejgblohhjeckiclfpekn" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-[#050614] text-white font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md text-xs sm:text-sm inline-flex items-center justify-center gap-2">
                  Install Chrome Extension →
                </a>
                <a href="https://microsoftedge.microsoft.com/addons/detail/memwyre/ihibkjgaiafhhbjmchmkphlkomodkmpd" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  View Edge Add-on
                </a>
              </div>
            </div>
          </div>

          <!-- Chrome Extension GUI Mockup Window -->
          <div class="border border-gray-200 bg-white rounded-lg relative flex flex-col justify-between min-h-[360px] shadow-xl overflow-hidden">
            <!-- Simulated Browser Header -->
            <div class="bg-gray-50 border-b border-gray-200 px-4 py-3 flex items-center justify-between">
              <div class="flex items-center gap-1.5">
                <div class="w-3.5 h-3.5 rounded-full bg-red-400"></div>
                <div class="w-3.5 h-3.5 rounded-full bg-yellow-400"></div>
                <div class="w-3.5 h-3.5 rounded-full bg-green-400"></div>
              </div>
              <div class="bg-white border border-gray-200 rounded px-3 py-1 text-[11px] font-mono text-gray-500 w-2/3 truncate text-center">
                https://chat.openai.com/c/active-thread
              </div>
              <div class="w-6 h-6 rounded-full bg-gray-200 flex items-center justify-center text-[10px] font-bold text-gray-600 font-mono">MW</div>
            </div>
            
            <!-- Active Webpage Content (Simulated ChatGPT UI) -->
            <div class="p-6 flex-1 bg-gray-50/50 flex flex-col justify-between relative">
              <div class="space-y-4">
                <div class="flex gap-2">
                  <div class="w-6 h-6 rounded-full bg-gray-300 flex items-center justify-center text-[10px] font-bold text-gray-700 shrink-0">AI</div>
                  <div class="bg-white border border-gray-200/80 p-3 rounded shadow-sm text-xs leading-relaxed max-w-[85%]">
                    Here is the correct Tailwind configuration. Let's make sure the custom font and borders are set up...
                  </div>
                </div>
              </div>

              <!-- Floating Memwyre Extension Popup -->
              <div class="absolute top-4 right-4 w-72 bg-white border border-gray-900/10 shadow-2xl rounded-lg p-4 font-sans text-xs z-20 hover:border-gray-900/20 transition-all duration-300">
                <div class="flex items-center justify-between border-b border-gray-100 pb-2.5 mb-3">
                  <div class="flex items-center gap-1.5">
                    <img src="/logo.png" alt="Memwyre" class="h-4 w-auto" />
                    <span class="font-bold text-[11px] text-gray-900">Browser Ingest</span>
                  </div>
                  <div class="flex items-center gap-1 text-[10px] text-green-600 font-medium">
                    <span class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span>
                    Vault Sync Active
                  </div>
                </div>

                <div class="space-y-3">
                  <div class="bg-gray-50 border border-gray-150 p-2.5 rounded font-mono text-[10px] text-gray-500 space-y-1">
                    <div class="font-bold text-gray-700">DETECTED: AI Chat Exchange</div>
                    <div>Source: chat.openai.com</div>
                    <div>Tokens: ~1,240 words</div>
                  </div>

                  <div>
                    <label class="block font-medium text-gray-700 mb-1">Add Tags / Context</label>
                    <input type="text" value="#tailwind #config #landing-page" class="w-full bg-white border border-gray-300 rounded px-2.5 py-1.5 text-xs focus:outline-none focus:border-[#D97757]" />
                  </div>

                  <button @click="triggerCapture" class="w-full py-2 bg-[#D97757] text-white font-bold rounded shadow-sm hover:bg-[#e68a6c] transition-colors duration-200 flex items-center justify-center gap-1.5">
                    <span v-if="!isSaving">Save Conversation Context</span>
                    <span v-else class="flex items-center gap-1">
                      <svg class="animate-spin h-3.5 w-3.5 text-white" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Syncing to Vault...
                    </span>
                  </button>
                  <p class="text-[10px] text-green-600 text-center font-bold mt-2" v-if="hasSaved">✓ Captured successfully! Added to Inbox.</p>
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
            AI research context decays in minutes.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'Chat Expiry & Loss', body: 'Valuable debugging logs, prompts, and config details roll off ChatGPT and Claude listings or get lost in hundreds of threads.' },
            { title: 'Copy-Paste Fatigue', body: 'Constantly copy-pasting code blocks and stack trace logs from your browser into local text files is slow and disrupts flow.' },
            { title: 'Resource-Heavy Tabs', body: 'Keeping 60 browser tabs open for context consumes system memory and offers no searchable indexing.' }
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
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Ingestion Workflow</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            One click to freeze browser context.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-6 space-y-8">
            <div v-for="(step, idx) in [
              { title: '1. Secure Auth Token Linkage', body: 'Link your browser to your private vault in one step using a secure, short-lived Access Token generated inside your settings.' },
              { title: '2. Native In-Chat Save Buttons', body: 'Adds tiny, integrated Memwyre buttons directly into the ChatGPT, Claude, and Gemini interfaces to clip the active exchange.' },
              { title: '3. Full Page Webpage Clipper', body: 'Click the browser extension button to convert any blog post, documentation page, or GitHub issue into clean markdown context.' }
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
              <div class="font-bold text-gray-900 text-base">Integrated Browser Ecosystem</div>
              <p class="text-xs text-gray-500 leading-relaxed max-w-xs mx-auto">
                Works across Chrome-based browsers and Edge. Secure storage separates access keys from active tabs.
              </p>
              <div class="flex justify-center gap-6 pt-2">
                <div class="w-14 h-14 bg-white border border-gray-200 rounded-lg flex items-center justify-center p-3.5 shadow-sm hover:border-[#D97757]/30 transition-all duration-300" title="Google Chrome">
                  <img :src="chromeLogo" class="w-full h-full object-contain" alt="Google Chrome" />
                </div>
                <div class="w-14 h-14 bg-white border border-gray-200 rounded-lg flex items-center justify-center p-3.5 shadow-sm hover:border-[#D97757]/30 transition-all duration-300" title="Microsoft Edge">
                  <img :src="edgeLogo" class="w-full h-full object-contain" alt="Microsoft Edge" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. CAPTURED MEMORY PREVIEW -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Vault Capture</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Secure browser isolation by design.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="space-y-4">
            <h3 class="text-xl font-bold text-gray-900">Only save what you choose</h3>
            <p class="text-sm text-gray-500 leading-relaxed">
              We value privacy above all else. The extension runs in strict isolation and only extracts text from target pages (like ChatGPT, Claude, and active research documents) when you explicitly trigger the save function.
            </p>
            <ul class="space-y-2 text-sm text-gray-600">
              <li>• Short-lived tokens securely isolated in extension storage</li>
              <li>• 100% client-side script execution</li>
              <li>• Zero tracking of outside tabs or web history</li>
            </ul>
          </div>
          <div class="border border-gray-200 rounded p-6 bg-white flex flex-col justify-center">
            <div class="text-xs font-mono text-gray-400 mb-2">// SECURITY & PERMISSIONS</div>
            <div class="font-mono text-sm text-gray-800 space-y-2">
              <div><span class="text-green-600">activeTab</span>: Only read current page text upon clip request.</div>
              <div><span class="text-green-600">scripting</span>: Convert DOM to clean markdown formatting.</div>
              <div class="text-gray-500">Result: Encrypted sync directly to your personal brain vault.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 5. FINAL CALL TO ACTION BANNER -->
      <div class="border border-dashed border-gray-300 rounded-none p-12 text-center bg-white relative my-12 sm:my-16 overflow-hidden">
        <!-- corner brackets -->
        <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-gray-400"></div>
        <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-gray-400"></div>
        <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-gray-400"></div>
        <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-gray-400"></div>

        <h3 class="hero-serif text-2xl sm:text-3xl lg:text-4xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-4">
          Capture context, anywhere on the web.
        </h3>
        <p class="text-sm text-gray-500 max-w-md mx-auto mb-6">
          Install the browser extension today and never repeat yourself to a blank AI slate.
        </p>
        <a href="https://chromewebstore.google.com/detail/memwyre/biplnkodgfdgejgblohhjeckiclfpekn" target="_blank"
          class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Install Chrome Extension
        </a>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import chromeLogo from '@/assets/chrome-logo-svgrepo-com.svg';
import edgeLogo from '@/assets/microsoft-edge-logo.svg';
import SiteFooter from '@/components/SiteFooter.vue';

const isSaving = ref(false);
const hasSaved = ref(false);

const triggerCapture = () => {
  if (isSaving.value || hasSaved.value) return;
  isSaving.value = true;
  setTimeout(() => {
    isSaving.value = false;
    hasSaved.value = true;
  }, 1200);
};
</script>
