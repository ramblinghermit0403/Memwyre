<template>
  <div ref="root" class="relative w-full max-w-4xl mx-auto overflow-hidden bg-white dark:bg-[#1a1917] border border-gray-200/60 dark:border-gray-700/60 border-b-0 shadow-xl flex flex-col rounded-t-xl min-h-[400px] sm:min-h-[auto]" style="aspect-ratio: 16/10;">
    <!-- Dot grid bg -->
    <div class="absolute inset-0 z-0 pointer-events-none opacity-40 dark:opacity-20"
         style="background-image: radial-gradient(#9ca3af 1px, transparent 1px); background-size: 32px 32px;"></div>

    <!-- PHASE 1: Welcome — centered greeting + input -->
    <div v-if="!hasSent" class="flex-1 flex flex-col items-center justify-center z-10 px-6 transition-all duration-500">
      <h2 class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white mb-4 sm:mb-6">Welcome, Alex</h2>
      <div class="w-full max-w-xl">
        <div class="bg-white dark:bg-[#2a2826] rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-2">
          <div class="px-5 py-3 text-base text-gray-900 dark:text-white min-h-[44px]">
            <span class="text-sm sm:text-base">{{ typedInput }}</span>
            <span v-if="showCursor" class="inline-block w-[2px] h-[16px] sm:h-[18px] bg-gray-800 dark:bg-white ml-px align-middle animate-blink"></span>
            <span v-if="!typedInput && !showCursor" class="text-gray-400">Ask your MemWyre...</span>
          </div>
          <div class="px-3 pb-1 flex justify-between items-center text-xs mt-1">
            <span class="text-gray-400 font-medium">MemWyre Pro</span>
            <button class="p-1.5 bg-[#D97757] text-white rounded-full w-8 h-8 flex items-center justify-center shadow-sm" :class="{ 'opacity-40': !typedInput }">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" /></svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- PHASE 2: Chat — messages + bottom input -->
    <template v-if="hasSent">
      <div class="flex-1 overflow-y-scroll p-5 z-10 pointer-events-none no-scrollbar" ref="chatArea" style="scroll-behavior: smooth;">
        <div class="space-y-4 max-w-xl mx-auto">
          <!-- User bubble -->
          <div v-if="userMsg" class="flex justify-end animate-fadeIn">
            <div class="max-w-[80%]">
              <div class="bg-[#D97757] text-white px-4 py-2.5 sm:px-5 sm:py-3 rounded-2xl rounded-tr-sm shadow-sm text-xs sm:text-sm leading-relaxed">{{ userMsg }}</div>
            </div>
          </div>

          <!-- Skeleton shimmer loading -->
          <div v-if="phase === 'thinking'" class="flex justify-start gap-3 animate-fadeIn">
            <div class="w-7 h-7 rounded-full bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-700 flex items-center justify-center shrink-0">
              <svg class="w-4 h-4 text-gray-600 dark:text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" /></svg>
            </div>
            <div class="flex-1 max-w-[90%] sm:max-w-[85%] bg-gray-50 dark:bg-[#2a2826] px-4 py-3 sm:px-5 sm:py-4 rounded-2xl rounded-tl-sm border border-gray-100 dark:border-gray-700 space-y-3">
              <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer" style="width: 90%"></div>
              <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer" style="width: 75%; animation-delay: 0.15s"></div>
              <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer" style="width: 60%; animation-delay: 0.3s"></div>
              <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer" style="width: 80%; animation-delay: 0.45s"></div>
            </div>
          </div>

          <!-- AI response -->
          <div v-if="aiText" class="flex justify-start gap-3 animate-fadeIn">
            <div class="w-7 h-7 rounded-full bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-700 flex items-center justify-center shrink-0 mt-1">
              <svg class="w-4 h-4 text-gray-600 dark:text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" /></svg>
            </div>
            <div class="max-w-[90%] sm:max-w-[85%]">
              <div class="bg-gray-50 dark:bg-[#2a2826] px-4 py-3 sm:px-5 sm:py-3 rounded-2xl rounded-tl-sm border border-gray-100 dark:border-gray-700 text-xs sm:text-sm leading-relaxed text-gray-800 dark:text-gray-200">
                <div class="space-y-2 sm:space-y-3" v-html="aiText"></div>
                
                <section v-if="showSources" class="mt-4 animate-fadeIn">
                  <p class="text-[11px] uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2 font-semibold">Sources</p>
                  <div class="space-y-1.5">
                    <button class="w-full text-left text-xs px-1 py-1 border-b border-gray-200 dark:border-gray-700 hover:text-[#D97757] transition-colors">📄 OAuth2 Notes</button>
                    <button class="w-full text-left text-xs px-1 py-1 border-b border-gray-200 dark:border-gray-700 hover:text-[#D97757] transition-colors">📄 API Security Memo</button>
                  </div>
                </section>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom input bar -->
      <div class="px-4 pb-3 pt-1 z-10">
        <div class="max-w-xl mx-auto">
          <div class="bg-gray-100 dark:bg-[#2a2826] rounded-2xl p-2 border border-gray-200/60 dark:border-gray-700/60">
            <div class="px-3 py-2 sm:px-4 text-xs sm:text-sm text-gray-400 min-h-[32px]">Type your message here...</div>
            <div class="px-2 pb-1 flex justify-between items-center text-xs mt-1">
              <span class="text-gray-400 font-medium">MemWyre Pro</span>
              <button class="p-1.5 bg-[#D97757] text-white rounded-full w-7 h-7 flex items-center justify-center shadow-sm opacity-40">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" /></svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue';

const PROMPT = 'What were the key decisions from my OAuth2 notes?';
const RESPONSE = `<p class="mb-3">Based on your API Security Memo and OAuth2 Notes from last week, here are the key architectural decisions you finalized for the new authentication flow:</p>
<ul class="space-y-2 mb-3 list-disc pl-5">
  <li><strong>Token Strategy:</strong> You selected <strong>short-lived access tokens</strong> (15 minute expiration) paired with refresh token rotation to minimize the window of vulnerability.</li>
  <li><strong>Authorization Flow:</strong> The SPA will use the <strong>Authorization Code flow with PKCE</strong>. You explicitly decided against Implicit Flow due to token leakage risks in the browser history.</li>
  <li><strong>Session Storage:</strong> All tokens will be stored in strict <strong>httpOnly, Secure cookies</strong>. LocalStorage was ruled out to prevent XSS attacks from reading the tokens.</li>
  <li><strong>Granular Scopes:</strong> Access scopes are defined per-resource (e.g., <code>read:inbox</code>, <code>write:memories</code>) rather than granting blanket API access.</li>
</ul>
<p>Would you like me to pull up the exact code snippet you saved for the PKCE code challenge generator?</p>`;

const phase = ref('welcome');
const typedInput = ref('');
const showCursor = ref(false);
const hasSent = ref(false);
const userMsg = ref('');
const aiText = ref('');
const showSources = ref(false);
const chatArea = ref(null);
const root = ref(null);

let timers = [];
let alive = false;
let observer = null;

const wait = (ms) => new Promise(r => { const t = setTimeout(r, ms); timers.push(t); });
function scrollDown() { nextTick(() => { if (chatArea.value) chatArea.value.scrollTo({ top: chatArea.value.scrollHeight, behavior: 'smooth' }); }); }

async function loop() {
  while (alive) {
    // Reset to welcome
    phase.value = 'welcome';
    typedInput.value = '';
    showCursor.value = false;
    hasSent.value = false;
    userMsg.value = '';
    aiText.value = '';
    showSources.value = false;
    if (root.value) { root.value.style.transition = 'none'; root.value.style.opacity = '1'; }

    await wait(1200);
    if (!alive) return;

    // Typewriter in centered input
    showCursor.value = true;
    for (let i = 0; i < PROMPT.length; i++) {
      if (!alive) return;
      typedInput.value = PROMPT.slice(0, i + 1);
      await wait(50);
    }
    await wait(500);
    showCursor.value = false;

    // Send — transitions layout
    userMsg.value = PROMPT;
    typedInput.value = '';
    hasSent.value = true;
    phase.value = 'thinking';
    await wait(100);
    scrollDown();
    await wait(1500);
    if (!alive) return;

    // Stream response
    phase.value = 'responding';
    const words = RESPONSE.split(/(?<=\s)/);
    let buf = '';
    for (let i = 0; i < words.length; i++) {
      if (!alive) return;
      buf += words[i];
      aiText.value = buf;
      if (i % 3 === 0) scrollDown();
      await wait(40);
    }
    aiText.value = RESPONSE;
    await wait(300);
    showSources.value = true;
    scrollDown();
    phase.value = 'done';

    await wait(8000);
    if (!alive) return;

    // Fade out & restart
    if (root.value) {
      root.value.style.transition = 'opacity 0.6s ease';
      root.value.style.opacity = '0.3';
    }
    await wait(900);
  }
}

function stop() { alive = false; timers.forEach(t => clearTimeout(t)); timers = []; }

onMounted(() => {
  observer = new IntersectionObserver(([e]) => {
    if (e.isIntersecting && !alive) { alive = true; loop(); }
    else if (!e.isIntersecting && alive) { stop(); }
  }, { threshold: 0.25 });
  if (root.value) observer.observe(root.value);
});

onUnmounted(() => { stop(); if (observer) observer.disconnect(); });
</script>

<style scoped>
@keyframes fadeIn { from { opacity:0; transform:translateY(6px) } to { opacity:1; transform:translateY(0) } }
.animate-fadeIn { animation: fadeIn .3s ease-out; }
@keyframes blink { 0%,50%{opacity:1} 51%,100%{opacity:0} }
.animate-blink { animation: blink .8s infinite; }
.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.skeleton-shimmer {
  background: linear-gradient(90deg, 
    rgba(156,163,175,0.15) 25%, 
    rgba(156,163,175,0.35) 50%, 
    rgba(156,163,175,0.15) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}
:root.dark .skeleton-shimmer,
.dark .skeleton-shimmer {
  background: linear-gradient(90deg, 
    rgba(255,255,255,0.06) 25%, 
    rgba(255,255,255,0.15) 50%, 
    rgba(255,255,255,0.06) 75%
  );
  background-size: 200% 100%;
}
</style>
