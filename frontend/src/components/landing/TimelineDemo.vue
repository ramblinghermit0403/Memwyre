<template>
  <div class="relative overflow-hidden w-full h-full bg-black dark flex items-center justify-center">
    <!-- Master Camera Rig (handles Zoom/Pan for the entire scene including cursor and popups) -->
    <div class="absolute inset-0 z-10 flex items-center justify-center origin-center ease-[cubic-bezier(0.25,1,0.35,1)]"
      :style="{ transform: `translate(${camX}px, ${camY}px) scale(${camScale})`, transitionDuration: camDuration + 'ms', transition: `transform ${camDuration}ms cubic-bezier(0.25,1,0.35,1)` }">

      <!-- Timeline Sub-Rig (handles only the Y scroll feed) -->
      <div class="absolute inset-0 w-full ease-[cubic-bezier(0.25,1,0.35,1)] camera-rig"
        :style="{ transform: `translateY(${timelineY}px)`, transitionDuration: timelineDuration + 'ms', opacity: timelineFaded ? 0 : 1, transition: `transform ${timelineDuration}ms cubic-bezier(0.25,1,0.35,1), opacity 0.5s ease` }">

        <!-- Exact Original UI Preserved -->
        <div class="w-full bg-[#111111] min-h-screen pt-[30%] pb-[100%]">

          <!-- Timeline Feed -->
          <div class="max-w-2xl mx-auto px-8 sm:px-16 md:px-24">
            <ul
              class="divide-y divide-gray-200 dark:divide-gray-800 border-t border-b border-gray-200 dark:border-gray-800">
              <li v-for="(memory, index) in memories" :key="index"
                class="py-5 transition-all duration-300 ease-out origin-center"
                :class="{ 'scale-[1.08] bg-[#1a1a1a] rounded-xl shadow-2xl z-30 relative px-4 -mx-4 -my-2 ring-1 ring-white/10': activeIndex === index }">
                <div class="flex items-start justify-between gap-3 px-1">
                  <div class="min-w-0 flex-1">
                    <div class="flex items-start gap-3">
                      <div
                        class="w-6 h-6 flex items-center justify-center shrink-0 text-gray-400 dark:text-gray-500 rounded overflow-hidden mt-0.5">
                        <svg v-if="memory.source === 'chatgpt'" fill-rule="evenodd" viewBox="0 0 24 24"
                          xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
                          <path fill="#ffffff"
                            d="M9.205 8.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357 1.356-.523 2.117-.523 2.854 0 4.662 2.212 4.662 4.566 0 .167 0 .357-.024.547l-4.71-2.759a.797.797 0 00-.856 0l-5.97 3.473zm10.609 8.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473 1.95-1.118a.433.433 0 01.476 0l4.543 2.617c1.309.76 2.189 2.378 2.189 3.948 0 1.808-1.07 3.473-2.76 4.163zM7.802 12.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545 1.95-4.472 4.591-4.472 1 0 1.927.333 2.712.928L8.23 5.067c-.285.166-.428.404-.428.737v6.898zM12 15.128l-2.795-1.57v-3.33L12 8.658l2.795 1.57v3.33L12 15.128zm1.796 7.23c-1 0-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974 1.142c.167.095.238.238.238.428v5.233c0 2.545-1.974 4.472-4.614 4.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482 4.482 0 014.21 6.327v5.423c0 .333.143.571.428.738l5.947 3.449-1.95 1.118a.432.432 0 01-.476 0zm-.262 3.9c-2.688 0-4.662-2.021-4.662-4.519 0-.19.024-.38.047-.57l4.686 2.71c.286.167.571.167.856 0l5.97-3.448v2.26c0 .19-.07.333-.237.428l-4.543 2.616c-.619.357-1.356.523-2.117.523zm5.899 2.83a5.947 5.947 0 005.827-4.756C22.287 18.339 24 15.84 24 13.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498 0-3.401-2.759-5.947-5.946-5.947-.642 0-1.26-.095-1.88-.31A5.962 5.962 0 0010.205 0a5.947 5.947 0 00-5.827 4.757C1.713 5.447 0 7.945 0 10.49c0 1.666.713 3.283 1.998 4.448-.119.5-.19 1-.19 1.499 0 3.401 2.759 5.946 5.946 5.946.642 0 1.26-.095 1.88-.309a5.96 5.96 0 004.162 1.713z" />
                        </svg>
                        <img v-if="memory.source === 'claude'" src="@/assets/claude-color.svg"
                          class="w-full h-full object-cover">
                        <img v-if="memory.source === 'gemini'" src="@/assets/gemini-color.svg"
                          class="w-full h-full object-cover">
                        <img v-if="memory.source === 'antigravity'"
                          src="@/assets/Google-Antigravity-Icon-Full-Color.png"
                          class="w-full h-full object-cover bg-white p-[2px] rounded-sm">
                        <svg v-if="memory.source === 'extension'" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                          class="w-full h-full text-blue-500">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z">
                          </path>
                        </svg>
                        <svg v-if="memory.source === 'web'" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                          class="w-full h-full text-green-500">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9">
                          </path>
                        </svg>
                      </div>
                      <div class="min-w-0">
                        <p class="text-sm font-semibold text-gray-900 dark:text-white truncate">{{ memory.title }}</p>
                        <p class="text-xs text-gray-500 mt-1 capitalize">{{ memory.source }} | {{ memory.type }} | {{
                          memory.time }}</p>
                        <p class="text-sm text-gray-600 dark:text-gray-300 mt-2 line-clamp-2">{{ memory.content }}</p>
                        <div class="mt-2 flex items-center gap-2">
                          <div class="relative project-selector">
                            <button
                              class="inline-flex items-center justify-between gap-1.5 min-w-[120px] text-[10px] px-2 py-1 rounded-md border border-gray-200 dark:border-gray-800 bg-white dark:bg-[#1a1a1a] hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-400">
                              <span>{{ memory.tag }}</span>
                              <svg class="w-2.5 h-2.5 text-gray-500" fill="none" stroke="currentColor"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                  d="M19 9l-7 7-7-7">
                                </path>
                              </svg>
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="flex items-center gap-2 shrink-0">
                    <button
                      class="inline-flex items-center gap-1.5 text-xs px-2.5 py-1.5 rounded-md border border-gray-200 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-400">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M14 3h7m0 0v7m0-7L10 14">
                        </path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 7v12h12"></path>
                      </svg>
                      <span class="sr-only">Open</span>
                    </button>
                    <button
                      class="inline-flex items-center justify-center gap-1.5 text-xs px-3 py-1.5 rounded-md border border-gray-200 dark:border-gray-800 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800"
                      :class="{ 'bg-white/10 ring-1 ring-white/20': useInAiActive }">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M12 3l1.6 3.4L17 8l-3.4 1.6L12 13l-1.6-3.4L7 8l3.4-1.6L12 3z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M5 16l.9 1.9L8 19l-2.1 1L5 22l-.9-2L2 19l2.1-1.1L5 16z"></path>
                      </svg>
                      <span>Use in AI</span>
                      <svg class="w-3 h-3 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                      </svg>
                    </button>
                  </div>
                </div>
              </li>


            </ul>
          </div>

        </div>
      </div>

      <!-- Animated Cursor (fixed in viewport space, outside camera rig) -->
      <div class="absolute left-1/2 top-1/2 pointer-events-none z-[60]"
        :style="{ transform: `translate(${cursorX}px, ${cursorY}px)`, opacity: cursorOp, transition: `transform ${cursorDuration}ms cubic-bezier(0.34,1.56,0.64,1), opacity 200ms ease` }">
        <svg class="drop-shadow-[0_4px_10px_rgba(0,0,0,0.9)]" :class="{ 'scale-75': cursorClick }"
          style="width:28px;height:28px;color:white;transition:transform 0.1s ease;" viewBox="0 0 24 24"
          fill="currentColor" stroke="black" stroke-width="1.2">
          <path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 0 1 .35-.15h6.87a.5.5 0 0 0 .35-.85L5.5 3.21z" />
        </svg>
      </div>

      <!-- AI Handoff Dropdown Overlay (pops in centered, fixed in viewport) -->
      <transition name="pop-up">
        <div v-if="showDropdown"
          class="absolute z-50 left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none">
          <div class="w-64 rounded-xl border border-white/10 bg-black shadow-2xl p-2">
            <button
              class="w-full text-left text-sm font-medium px-3 py-2.5 rounded-lg flex items-center gap-3 text-white transition-colors duration-150"
              :class="chatGptClicked ? 'bg-white/20' : 'bg-white/10'">
              <svg fill-rule="evenodd" viewBox="0 0 24 24" class="w-5 h-5 shrink-0">
                <path fill="#ffffff"
                  d="M9.205 8.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357 1.356-.523 2.117-.523 2.854 0 4.662 2.212 4.662 4.566 0 .167 0 .357-.024.547l-4.71-2.759a.797.797 0 00-.856 0l-5.97 3.473zm10.609 8.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473 1.95-1.118a.433.433 0 01.476 0l4.543 2.617c1.309.76 2.189 2.378 2.189 3.948 0 1.808-1.07 3.473-2.76 4.163zM7.802 12.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545 1.95-4.472 4.591-4.472 1 0 1.927.333 2.712.928L8.23 5.067c-.285.166-.428.404-.428.737v6.898zM12 15.128l-2.795-1.57v-3.33L12 8.658l2.795 1.57v3.33L12 15.128zm1.796 7.23c-1 0-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974 1.142c.167.095.238.238.238.428v5.233c0 2.545-1.974 4.472-4.614 4.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482 4.482 0 014.21 6.327v5.423c0 .333.143.571.428.738l5.947 3.449-1.95 1.118a.432.432 0 01-.476 0zm-.262 3.9c-2.688 0-4.662-2.021-4.662-4.519 0-.19.024-.38.047-.57l4.686 2.71c.286.167.571.167.856 0l5.97-3.448v2.26c0 .19-.07.333-.237.428l-4.543 2.616c-.619.357-1.356.523-2.117.523zm5.899 2.83a5.947 5.947 0 005.827-4.756C22.287 18.339 24 15.84 24 13.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498 0-3.401-2.759-5.947-5.946-5.947-.642 0-1.26-.095-1.88-.31A5.962 5.962 0 0010.205 0a5.947 5.947 0 00-5.827 4.757C1.713 5.447 0 7.945 0 10.49c0 1.666.713 3.283 1.998 4.448-.119.5-.19 1-.19 1.499 0 3.401 2.759 5.946 5.946 5.946.642 0 1.26-.095 1.88-.309a5.96 5.96 0 004.162 1.713z" />
              </svg>
              Continue in ChatGPT
            </button>
            <button
              class="w-full text-left text-sm font-medium px-3 py-2.5 hover:bg-white/5 rounded-lg flex items-center gap-3 text-white/80">
              <img src="@/assets/claude-color.svg" class="w-5 h-5 shrink-0" />
              Continue in Claude
            </button>
            <button
              class="w-full text-left text-sm font-medium px-3 py-2.5 hover:bg-white/5 rounded-lg flex items-center gap-3 text-white/80">
              <img src="@/assets/gemini-color.svg" class="w-5 h-5 shrink-0" />
              Continue in Gemini
            </button>
            <button
              class="w-full text-left text-sm font-medium px-3 py-2.5 hover:bg-white/5 rounded-lg flex items-center gap-3 text-white/80">
              <img src="@/assets/perplexity-color.svg" class="w-5 h-5 shrink-0" />
              Continue in Perplexity
            </button>
            <button
              class="w-full text-left text-sm font-medium px-3 py-2.5 hover:bg-white/5 rounded-lg flex items-center gap-3 text-white/40">
              <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M8 16H7a2 2 0 01-2-2V5a2 2 0 012-2h9a2 2 0 012 2v1"></path>
                <rect x="9" y="9" width="10" height="12" rx="2" ry="2" stroke-width="2"></rect>
              </svg>
              Copy Context
            </button>
          </div>
        </div>
      </transition>

      <!-- Phase 4: ChatGPT Input Box Mock -->
      <transition name="pop-up">
        <div v-if="showInputBar"
          class="absolute z-50 left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none flex flex-col items-center">

          <!-- Greeting Message -->
          <h2 class="mb-5 text-2xl font-medium text-white tracking-tight whitespace-nowrap drop-shadow-md">Where should
            we begin?</h2>

          <div
            class="relative flex items-center bg-[#2f2f32] rounded-full p-2 pl-4 shadow-[0_15px_50px_rgba(0,0,0,0.8)] border border-white/5 transition-all duration-[400ms] w-full min-w-[320px] max-w-[420px] min-h-[50px]">

            <!-- Left Actions -->
            <div class="relative flex-none flex items-center gap-3 pr-3 text-[#b5b5b5]">
              <!-- Plus icon -->
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"></path>
              </svg>
            </div>

            <!-- Input Text -->
            <div
              class="flex-1 text-[#b5b5b5] font-medium text-[15px] transition-all duration-300 flex items-center overflow-hidden text-left">
              <!-- Sync Badge -->
              <span
                class="inline-flex items-center bg-[#3a3b40] text-gray-200 text-xs px-2 py-0.5 rounded-md mr-2 border border-white/20 whitespace-nowrap animate-badgePop shadow-md">
                <svg class="w-3 h-3 mr-1 text-[#10b981]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1">
                  </path>
                </svg>
                Idea Retention
              </span>

              <!-- Typing text -->
              <span class="whitespace-nowrap border-white/60 select-none pb-[2px] text-[#b5b5b5]">Ask anything</span>
            </div>

            <!-- Right Actions -->
            <div class="relative flex-none flex items-center gap-4 pl-3">
              <!-- Injected MemWyre Button -->
              <div class="w-8 h-8 flex items-center justify-center">
                <img src="/image.svg" class="w-5 h-5" />
              </div>

              <!-- Mic button -->
              <div class="text-[#b5b5b5] w-6 h-6 flex items-center justify-center">
                <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path>
                  <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                  <line x1="12" y1="19" x2="12" y2="22"></line>
                  <line x1="8" y1="22" x2="16" y2="22"></line>
                </svg>
              </div>

              <!-- Send/Waveform button -->
              <div
                class="w-8 h-8 flex items-center justify-center rounded-full text-black ml-1 transition-colors duration-150"
                :class="inputBarClicked ? 'bg-gray-300 scale-95' : 'bg-white'">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2v20M8 8v8M16 8v8M4 11v2M20 11v2" />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </transition>

    </div> <!-- End Master Camera Rig -->

    <!-- Bottom fade -->
    <div
      class="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-[#111111] to-transparent z-30 pointer-events-none">
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const memories = [
  {
    title: "Publishing Info for Chrome",
    source: "claude",
    type: "Response",
    time: "Mar 18",
    content: "Here's a step-by-step guide to publishing a Chrome extension: Ensure your extension has a valid manifest.json",
    tag: "dev"
  },
  {
    title: "Gemini Prompt: Dark Fantasy Scene",
    source: "gemini",
    type: "Prompt",
    time: "11:15 PM",
    content: "Here is a random dream of mine. Set: old Harry Potter style mansion dark theme. Scene: It starts with a dark ritual where people a standing in lines wearing Balck robes hiding their face and some people holding long house banners...",
    tag: "ideas"
  },
  {
    title: "Minimal MCP Server Generator",
    source: "chatgpt",
    type: "Conversation",
    time: "Mar 31",
    content: "Here’s your final, fully corrected and polished proposal with the GSoC 2026 timeline fixed and aligned. This is ready to submit",
    tag: "projects"
  },
  {
    title: "Antigravity Agent Progress",
    source: "antigravity",
    type: "Task",
    time: "Just now",
    content: "I have removed the hardcoded placeholder HTML elements and set up the v-for loop to dynamically render the memories list in TimelineDemo.vue.",
    tag: "dev"
  },
  {
    title: "Enhancing AI Idea Retention",
    source: "chatgpt",
    type: "Conversation",
    time: "2:24 PM",
    content: "Good catch. Without a solution, it feels like a rant. But here’s the nuance: you don’t want to jump straight to “use my tool.” Let’s upgrade your post",
    tag: "marketing"
  }
];

const timelineY = ref(0);
const timelineDuration = ref(1000);

const camX = ref(0);
const camY = ref(0);
const camScale = ref(1);
const camDuration = ref(1000);

const activeIndex = ref(0);

// Cursor state
const cursorX = ref(200);
const cursorY = ref(150);
const cursorOp = ref(0);
const cursorClick = ref(false);
const cursorDuration = ref(600); // ms for glide, set to 0 for instant teleport

// "Use in AI" button highlight state
const useInAiActive = ref(false);

// Dropdown visibility
const showDropdown = ref(false);
const showInputBar = ref(false);

// ChatGPT row click highlight
const chatGptClicked = ref(false);
const inputBarClicked = ref(false);

// Fade out timeline when dropdown is shown
const timelineFaded = ref(false);

const sleep = ms => new Promise(r => setTimeout(r, ms));

const scrollTimeline = (y, duration = 1000) => {
  timelineY.value = -y;
  timelineDuration.value = duration;
};

const focusCamera = (x, y, scale = 1, duration = 1000) => {
  camX.value = -x;
  camY.value = -y;
  camScale.value = scale;
  camDuration.value = duration;
};

let alive = true;

function trackScroll() {
  if (!alive) return;
  const rig = document.querySelector('.camera-rig');
  if (rig) {
    const transform = window.getComputedStyle(rig).transform;
    if (transform && transform !== 'none') {
      const match = transform.match(/matrix.*\((.+)\)/);
      if (match) {
        const parts = match[1].split(', ');
        const ty = parseFloat(parts[5]); // matrix(a,b,c,d,tx,ty) 
        if (!isNaN(ty)) {
          const focalY = -ty;
          // Approx card height including py-5 padding + content (~144px)
          activeIndex.value = Math.max(0, Math.min(memories.length - 1, Math.round(focalY / 144)));
        }
      }
    }
  }
  requestAnimationFrame(trackScroll);
}

async function loop() {
  await sleep(700);

  while (alive) {
    // --- Phase 1: Scroll from top to 5th card ---
    scrollTimeline(0, 530);
    await sleep(1000);

    // Slow scroll to center the 5th card in frame
    scrollTimeline(700, 2000);

    // Wait until scroll settles
    await sleep(1300);

    // --- Phase 2: Cursor enters from bottom-right, clicks "Use in AI" ---
    cursorDuration.value = 0;
    cursorX.value = 200;
    cursorY.value = 150;
    cursorOp.value = 0;
    await sleep(30);

    // Glide to "Use in AI" button on the active (5th) card + ZOOM
    cursorDuration.value = 500;
    cursorOp.value = 1;
    cursorX.value = 240;
    cursorY.value = 0;
    focusCamera(120, -20, 1.3, 500); // zoom in on right side button
    await sleep(570);

    // Click!
    cursorClick.value = true;
    useInAiActive.value = true;
    await sleep(120);
    cursorClick.value = false;


    // --- Phase 3: Fade timeline out, dropdown appears ---
    timelineFaded.value = true;
    focusCamera(0, 0, 1.2, 400); // pull back to center
    showDropdown.value = true;
    await sleep(400);

    // Re-enter cursor from bottom-right for shot 2
    cursorDuration.value = 0;
    cursorX.value = 200;
    cursorY.value = 150;
    cursorOp.value = 0;
    await sleep(30);

    // Glide to ChatGPT row in Dropdown
    cursorDuration.value = 500;
    cursorOp.value = 1;
    cursorX.value = -60;
    cursorY.value = -88;
    await sleep(570);

    // Click ChatGPT row
    cursorClick.value = true;
    chatGptClicked.value = true;
    await sleep(120);
    cursorClick.value = false;
    cursorOp.value = 0;
    await sleep(200);


    // Dropdown fades out, Input Bar appears
    showDropdown.value = false;
    await sleep(250);
    showInputBar.value = true;
    focusCamera(0, 0, 1.2, 500); // 1.2x Zoom for the final shot
    await sleep(2400);
    cursorClick.value = false;
    inputBarClicked.value = false;
    chatGptClicked.value = false;

    // --- Phase 4: Clean up and rewind ---
    showInputBar.value = false;
    showDropdown.value = false;
    focusCamera(0, 0, 1, 600); // Reset Master Rig camera
    await sleep(200);
    timelineFaded.value = false;
    useInAiActive.value = false;
    cursorOp.value = 0;
    await sleep(400);

    // Fast rewind to top
    scrollTimeline(0, 530);
    await sleep(670);
  }
}

onMounted(() => {
  alive = true;
  scrollTimeline(0, 0);
  requestAnimationFrame(trackScroll);
  loop();
});

onUnmounted(() => {
  alive = false;
});
</script>

<style scoped>
@keyframes bouncePop {
  0% {
    opacity: 0;
    transform: translateY(10px) scale(0.9);
  }

  60% {
    opacity: 1;
    transform: translateY(-2px) scale(1.02);
  }

  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.animate-fadeIn {
  animation: bouncePop .4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  transform-origin: top right;
}

@keyframes badgePop {
  0% {
    transform: scale(0.5);
    opacity: 0;
  }

  60% {
    transform: scale(1.15);
    opacity: 1;
  }

  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.animate-badgePop {
  opacity: 0;
  animation: badgePop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  animation-delay: 200ms;
  transform-origin: center;
}

/* Dropdown pop-up transition */
.pop-up-enter-active {
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.pop-up-leave-active {
  transition: all 0.25s ease-in;
}

.pop-up-enter-from {
  opacity: 0;
  transform: translate(-50%, -46%) scale(0.85);
}

.pop-up-leave-to {
  opacity: 0;
  transform: translate(-50%, -54%) scale(0.9);
}
</style>
