<template>
  <div ref="root"
    class="dark relative w-full max-w-4xl mx-auto overflow-hidden bg-white dark:bg-[#111111] border border-gray-200/60 dark:border-gray-700/60 border-b-0 shadow-[0_20px_50px_rgba(0,0,0,0.3)] flex flex-col rounded-t-xl min-h-[400px] sm:min-h-[auto]"
    style="aspect-ratio: 16/10; text-align: left;">

    <!-- Master Camera Viewport Rig (Handles smooth zooms and pans internally) -->
    <div class="absolute inset-0 z-10 origin-center ease-[cubic-bezier(0.25,1,0.35,1)]"
      :style="{ transform: `translate(${camX}px, ${camY}px) scale(${camScale})`, transition: `all ${camDuration}ms cubic-bezier(0.25,1,0.35,1)` }">

      <!-- Layout Rig (Provides the inverse expansion needed to simulate wide FOV without border gaps) -->
      <div
        class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col ease-[cubic-bezier(0.25,1,0.35,1)]"
        :style="{ width: `${camScale < 1 ? (1 / camScale) * 100 : 100}%`, height: `${camScale < 1 ? (1 / camScale) * 100 : 100}%`, transition: `all ${camDuration}ms cubic-bezier(0.25,1,0.35,1)` }">

        <transition name="fade">
          <div v-show="phase !== 'reset'" class="absolute inset-0 flex flex-col z-10 w-full h-full">
            <!-- PHASE 1: Welcome — centered greeting + input -->
            <div v-if="!hasSent"
              class="flex-1 flex flex-col items-center justify-center z-10 px-6 transition-all duration-500">
              <h2 class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white mb-4 sm:mb-6 animate-fadeIn">Welcome, Alex</h2>
              <div class="w-full max-w-xl animate-fadeIn" style="animation-delay: 0.1s">
                <div
                  class="bg-white dark:bg-[#212121] rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-2">
                  <div class="px-5 py-3 text-base text-gray-900 dark:text-white min-h-[44px]">
                    <span class="text-sm sm:text-base">{{ typedInput }}</span>
                    <span v-if="showCursor"
                      class="inline-block w-[2px] h-[16px] sm:h-[18px] bg-gray-800 dark:bg-white ml-px align-middle animate-blink"></span>
                    <span v-if="!typedInput && !showCursor" class="text-gray-400">Ask your MemWyre...</span>
                  </div>
                  <div class="px-3 pb-1 flex justify-between items-center text-xs mt-1">
                    <span class="text-gray-400 font-medium">MemWyre Pro</span>
                    <button
                      class="p-1.5 bg-gray-900 dark:bg-white text-white dark:text-black rounded-full w-8 h-8 flex items-center justify-center shadow-sm"
                      :class="{ 'opacity-40': !typedInput }">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M5 10l7-7m0 0l7 7m-7-7v18" />
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- PHASE 2: Chat — messages + bottom input -->
            <template v-if="hasSent">
              <div class="flex-1 overflow-y-scroll p-5 z-10 pointer-events-none no-scrollbar" ref="chatArea">
                <div class="space-y-4 max-w-xl mx-auto">
                  <div v-if="userMsg" class="flex justify-end animate-fadeIn">
                    <div class="max-w-[80%]">
                      <div
                        class="bg-gray-900 dark:bg-white text-white dark:text-black px-4 py-2.5 sm:px-5 sm:py-3 rounded-2xl rounded-tr-sm shadow-sm text-xs sm:text-sm leading-relaxed font-medium">
                        {{ userMsg }}</div>
                    </div>
                  </div>

                  <!-- Skeleton shimmer loading -->
                  <div v-if="phase === 'thinking'" class="flex justify-start animate-fadeIn">
                    <div
                      class="flex-1 max-w-[90%] sm:max-w-[85%] bg-gray-50 dark:bg-[#212121] px-4 py-3 sm:px-5 sm:py-4 rounded-2xl rounded-tl-sm border border-gray-100 dark:border-gray-700 space-y-3">
                      <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer" style="width: 90%">
                      </div>
                      <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer"
                        style="width: 75%; animation-delay: 0.15s"></div>
                      <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer"
                        style="width: 60%; animation-delay: 0.3s"></div>
                      <div class="h-3 rounded-full bg-gray-200 dark:bg-gray-700 skeleton-shimmer"
                        style="width: 80%; animation-delay: 0.45s"></div>
                    </div>
                  </div>

                  <!-- AI response -->
                  <div v-if="aiText" class="flex justify-start animate-fadeIn">
                    <div class="max-w-[90%] sm:max-w-[85%]">
                      <div
                        class="bg-gray-50 dark:bg-[#212121] px-4 py-3 sm:px-5 sm:py-3 rounded-2xl rounded-tl-sm border border-gray-100 dark:border-gray-700 text-xs sm:text-sm leading-relaxed text-gray-800 dark:text-gray-200">
                        <div class="space-y-2 sm:space-y-3" v-html="aiText"></div>

                        <section v-if="showSources" class="mt-4 animate-fadeIn">
                          <p
                            class="text-[11px] uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2 font-semibold">
                            Sources</p>
                          <div class="space-y-1.5">
                            <button
                              class="w-full text-left text-xs px-1 py-1 border-b border-gray-200 dark:border-gray-700 hover:text-black dark:hover:text-white transition-colors">📄
                              OAuth2 Notes</button>
                            <button
                              class="w-full text-left text-xs px-1 py-1 border-b border-gray-200 dark:border-gray-700 hover:text-black dark:hover:text-white transition-colors">📄
                              API Security Memo</button>
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
                  <div
                    class="bg-gray-100 dark:bg-[#212121] rounded-2xl p-2 border border-gray-200/60 dark:border-gray-700/60">
                    <div class="px-3 py-2 sm:px-4 text-xs sm:text-sm text-gray-400 min-h-[32px]">Type your message
                      here...
                    </div>
                    <div class="px-2 pb-1 flex justify-between items-center text-xs mt-1">
                      <span class="text-gray-400 font-medium">MemWyre Pro</span>
                      <button
                        class="p-1.5 bg-gray-900 dark:bg-white text-white dark:text-black rounded-full w-7 h-7 flex items-center justify-center shadow-sm opacity-40">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 10l7-7m0 0l7 7m-7-7v18" />
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </template>
          </div>
        </transition>
      </div> <!-- Close Layout Rig -->

      <!-- Virtual Cursor (same style as OmnipresentDemo) -->
      <div class="absolute left-1/2 top-1/2 pointer-events-none z-30"
        :style="{ transform: `translate(${cursorX}px, ${cursorY}px)`, opacity: cursorOp, transitionDuration: cursorMoveDuration + 'ms', transition: `transform ${cursorMoveDuration}ms cubic-bezier(0.34,1.56,0.64,1), opacity 200ms` }">
        <svg class="drop-shadow-[0_4px_10px_rgba(0,0,0,0.9)]" :class="{ 'scale-75': cursorClick }"
          style="width:32px;height:32px;color:white;transition:transform 0.1s ease;" viewBox="0 0 24 24"
          fill="currentColor" stroke="black" stroke-width="1.2">
          <path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 0 1 .35-.15h6.87a.5.5 0 0 0 .35-.85L5.5 3.21z" />
        </svg>
      </div>

    </div> <!-- End Camera Viewport Rig -->
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue';

const PROMPT = 'What were the key decisions from my OAuth2 notes?';
const RESPONSE = `<p class="mb-3">Based on your API Security Memo and OAuth2 Notes from last week, here are the key architectural decisions you finalized for the new authentication flow:</p>
<ul class="space-y-2 mb-3 list-disc pl-5">
  <li><strong>Token Strategy:</strong> You selected <strong>short-lived access tokens</strong> (15 minute expiration) paired with refresh token rotation to minimize the window of vulnerability.</li>
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

const camX = ref(0);
const camY = ref(0);
const camScale = ref(1);
const camDuration = ref(1000);

// Virtual cursor
const cursorX = ref(0);
const cursorY = ref(80);
const cursorOp = ref(0);
const cursorClick = ref(false);
const cursorMoveDuration = ref(400);

let timers = [];
let alive = false;
let observer = null;

const focusCamera = (x, y, scale = 1, duration = 1000) => {
  camX.value = -x;
  camY.value = -y;
  camScale.value = scale;
  camDuration.value = duration;
};

const wait = (ms) => new Promise(r => { const t = setTimeout(r, ms); timers.push(t); });
function scrollDown() { nextTick(() => { if (chatArea.value) chatArea.value.scrollTo({ top: chatArea.value.scrollHeight, behavior: 'auto' }); }); }

async function loop() {
  while (alive) {
    // Reset to welcome
    phase.value = 'welcome';
    typedInput.value = PROMPT;
    showCursor.value = false;
    hasSent.value = false;
    userMsg.value = '';
    aiText.value = '';
    showSources.value = false;

    await wait(600);
    if (!alive) return;

    // Show cursor briefly to indicate "active" state before click
    showCursor.value = true;
    await wait(400);
    showCursor.value = false;

    // Pre-position cursor off-screen bottom-right before revealing
    cursorX.value = 380;
    cursorY.value = 180;
    cursorOp.value = 0;
    cursorMoveDuration.value = 0; // instant invisible reposition
    await wait(20);

    // Zoom-in AND click fire simultaneously
    focusCamera(252, 78, 1.9, 600); // slower zoom-in (600ms)

    // Reveal and glide directly to the send button from bottom-right
    cursorOp.value = 1;
    cursorX.value = 252;
    cursorY.value = 78;
    cursorMoveDuration.value = 700;
    await wait(750); // wait for cursor to fully land on button


    cursorClick.value = true;
    await wait(300);
    cursorClick.value = false;
    await wait(200);

    // Zoom out internal components to 65% scale by inversely expanding the container
    focusCamera(0, 0, 0.67, 1000);
    cursorOp.value = 0;

    // Send — transitions layout
    userMsg.value = PROMPT;
    typedInput.value = '';
    hasSent.value = true;
    phase.value = 'thinking';

    await wait(200);
    scrollDown();
    await wait(1200); // reduced by 300ms
    if (!alive) return;

    // Pre-typed response
    phase.value = 'responding';
    aiText.value = RESPONSE;
    scrollDown();
    await wait(500);
    aiText.value = RESPONSE;
    await wait(300);

    showSources.value = true;
    scrollDown();

    phase.value = 'done';

    await wait(2500); // reduced from 4500 to match timeline velocity
    if (!alive) return;

    // Internal Reset
    phase.value = 'reset';
    focusCamera(0, 0, 1.0, 600); // 1x reset camera smoothly
    cursorOp.value = 0;

    await wait(500); // Wait for transition fade to finish cleanly
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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s cubic-bezier(0.25, 1, 0.35, 1);
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@keyframes bouncePop {
  0% {
    opacity: 0;
    transform: translateY(20px) scale(0.8);
  }

  60% {
    opacity: 1;
    transform: translateY(-5px) scale(1.05);
  }

  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.animate-fadeIn {
  animation: bouncePop .5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

@keyframes blink {

  0%,
  50% {
    opacity: 1
  }

  51%,
  100% {
    opacity: 0
  }
}

.animate-blink {
  animation: blink .8s infinite;
}

.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }

  100% {
    background-position: 200% 0;
  }
}

.skeleton-shimmer {
  background: linear-gradient(90deg,
      rgba(156, 163, 175, 0.15) 25%,
      rgba(156, 163, 175, 0.35) 50%,
      rgba(156, 163, 175, 0.15) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}

:root.dark .skeleton-shimmer,
.dark .skeleton-shimmer {
  background: linear-gradient(90deg,
      rgba(255, 255, 255, 0.06) 25%,
      rgba(255, 255, 255, 0.15) 50%,
      rgba(255, 255, 255, 0.06) 75%);
  background-size: 200% 100%;
}
</style>
