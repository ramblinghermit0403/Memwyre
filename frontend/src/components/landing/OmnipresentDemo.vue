<template>
  <div class="relative w-full h-[400px] overflow-hidden flex items-center justify-center bg-[#111111] font-sans">
    <div class="absolute inset-0 bg-black/40 z-0"></div>

    <!-- Camera Viewport Rig -->
    <div
      class="absolute w-full h-full z-10 flex items-center justify-center origin-center ease-[cubic-bezier(0.25,1,0.35,1)]"
      :style="{ transform: `translate(${camX}px, ${camY}px) scale(${camScale})`, transitionDuration: camDuration + 'ms' }">

      <!-- Phase 1: ChatGPT Message DOM mock -->
      <transition name="velocity">
        <div v-show="phase === 1" class="absolute z-20 flex flex-col items-center justify-center w-full h-full px-4">
          <div
            class="bg-[#212121] rounded-2xl p-5 sm:p-7 shadow-[0_10px_40px_rgba(0,0,0,0.5)] border border-white/10 w-full max-w-[500px]">
            <div class="flex items-center gap-3 mb-3">
              <div
                class="w-6 h-6 rounded-full flex items-center justify-center bg-white/10 border border-white/5 overflow-hidden">
                <img :src="openAILogo" class="w-4 h-4 object-contain opacity-90 invert brightness-0" alt="ChatGPT" />
              </div>
              <span class="text-white font-semibold text-sm">ChatGPT</span>
            </div>
            <div class="text-white/90 text-[15px] sm:text-lg mb-6 leading-relaxed font-sans mt-2">
              If you want, tell me <em>why you're planning</em> to do this, and I can give you a better answer on
              whether it's actually worth it for your specific use case.
            </div>
            <!-- Action Row -->
            <div class="relative flex items-center gap-3 sm:gap-5 text-gray-400">
              <svg class="w-4 h-4 sm:w-5 sm:h-5 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z">
                </path>
              </svg>
              <svg class="w-4 h-4 sm:w-5 sm:h-5 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5">
                </path>
              </svg>
              <svg class="w-4 h-4 sm:w-5 sm:h-5 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M10 14H5.236a2 2 0 01-1.789-2.894l3.5-7A2 2 0 018.736 3h4.018a2 2 0 01.485.06l3.76.94m-7 10v5a2 2 0 002 2h.096c.5 0 .905-.405.905-.904 0-.714.211-1.412.608-2.006L17 13V4m-7 10h2m5-10h2a2 2 0 012 2v6a2 2 0 01-2 2h-2.5">
                </path>
              </svg>
              <svg class="w-4 h-4 sm:w-5 sm:h-5 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path>
              </svg>
              <svg class="w-4 h-4 sm:w-5 sm:h-5 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15">
                </path>
              </svg>

              <!-- Tooltip Toast for Phase 1 -->
              <transition name="pop">
                <div v-if="phase === 1 && subphase === 'toast'"
                  class="absolute -top-[50px] left-1/2 transform -translate-x-1/2 bg-[#1B8054] text-[#f4fef8] px-4 py-2 rounded-lg shadow-[0_0_30px_rgba(27,128,84,0.7)] text-[15px] font-bold z-30 whitespace-nowrap tracking-wide border border-[#23a36b]">
                  Saved to Memwyre!
                </div>
              </transition>

              <!-- Injected MemWyre Logo (Hover Target) -->
              <div
                class="w-8 h-8 sm:w-10 sm:h-10 rounded-[10px] border flex items-center justify-center transition-all duration-300 relative group cursor-pointer shadow-[0_0_20px_rgba(255,255,255,0.05)]"
                :class="{ 'scale-[1.3] bg-[#444] shadow-[0_0_35px_rgba(255,255,255,0.4)] border-transparent': phase === 1 && subphase === 'click', 'bg-[#383838] scale-110 shadow-[0_0_25px_rgba(27,128,84,0.4)] border-[#1B8054]': phase === 1 && subphase === 'toast', 'bg-[#2A2B32] border-gray-600 hover:scale-110 hover:shadow-[0_0_15px_rgba(255,255,255,0.15)]': phase === 1 && subphase !== 'click' && subphase !== 'toast' }">
                <svg v-if="phase === 1 && subphase === 'toast'" class="w-4 h-4 sm:w-5 sm:h-5 text-[#8b8b8b]" fill="none"
                  viewBox="0 0 24 24" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 13l4 4L19 7" />
                </svg>
                <img v-else src="/image.svg" alt="MemWyre" class="w-5 h-5 sm:w-6 sm:h-6 transition-opacity" />
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- Phase 2: ChatGPT Input Box Mock -->
      <transition name="velocity">
        <div v-show="phase === 2" class="absolute z-20 flex flex-col items-center justify-center w-full h-full">
          <!-- Input Textarea bar -->
          <div
            class="relative flex items-center bg-[#2f2f32] rounded-full p-2 pl-4 shadow-[0_15px_50px_rgba(0,0,0,0.8)] border border-white/5 transition-all duration-[400ms] w-[90%] max-w-[400px] min-h-[50px]">

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
              <transition name="pop">
                <span v-if="contextSynced"
                  class="inline-flex items-center bg-[#3a3b40] text-gray-200 text-xs px-2 py-0.5 rounded-md mr-2 shadow-[0_0_15px_rgba(255,255,255,0.15)] border border-white/20 whitespace-nowrap">
                  <svg class="w-3 h-3 mr-1 text-[#10b981]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1">
                    </path>
                  </svg>
                  Auth System Guidelines
                </span>
              </transition>

              <!-- Typing text -->
              <span class="whitespace-nowrap border-white/60 select-none pb-[2px]"
                :class="{ 'text-white': typedText !== 'Ask anything', 'border-r-[1.5px] pr-0.5 pointer-events-none': phase === 2 && !contextSynced }">{{
                  typedText }}</span>
            </div>

            <!-- Right Actions -->
            <div class="relative flex-none flex items-center gap-4 pl-3">
              <!-- Tooltip Toast for Phase 2 -->
              <transition name="pop">
                <div v-if="phase === 2 && subphase === 'toast'"
                  class="absolute -top-16 left-0 transform -translate-x-1/2 bg-[#1B8054] text-[#f4fef8] px-4 py-2 rounded-lg shadow-[0_0_30px_rgba(27,128,84,0.7)] text-[15px] font-bold z-30 whitespace-nowrap tracking-wide border border-[#23a36b]">
                  Context synced!
                </div>
              </transition>

              <!-- Injected MemWyre Button (Right Side) -->
              <div
                class="w-8 h-8 rounded-full flex items-center justify-center transition-all duration-300 relative group cursor-pointer shadow-[0_0_20px_rgba(255,255,255,0.05)]"
                :class="{ 'bg-[#444] scale-[1.3] shadow-[0_0_35px_rgba(255,255,255,0.4)] border-transparent': phase === 2 && subphase === 'click', 'bg-[#383838] scale-110 shadow-[0_0_25px_rgba(27,128,84,0.4)] border-[#1B8054] border': phase === 2 && subphase === 'toast', 'bg-transparent hover:scale-110 hover:shadow-[0_0_15px_rgba(255,255,255,0.15)]': phase === 2 && subphase !== 'click' && subphase !== 'toast' }">
                <!-- MemWyre Logo or Checkmark -->
                <svg v-if="phase === 2 && subphase === 'toast'" class="w-4 h-4 text-[#8b8b8b]" fill="none"
                  viewBox="0 0 24 24" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 13l4 4L19 7" />
                </svg>
                <img v-else src="/image.svg" class="w-5 h-5 transition-transform group-hover:scale-110" />
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
              <div class="w-8 h-8 flex items-center justify-center rounded-full bg-white text-black ml-1">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2v20M8 8v8M16 8v8M4 11v2M20 11v2" />
                </svg>
              </div>
            </div>

          </div>
        </div>
      </transition>

      <!-- Animated Cursor Overlay -->
      <div v-show="subphase !== 'init' && subphase !== 'clear'"
        class="absolute left-1/2 top-1/2 pointer-events-none z-40 transition-all duration-[400ms] ease-[cubic-bezier(0.34,1.56,0.64,1)]"
        :style="{ transform: `translate(${cursorX}px, ${cursorY}px)`, opacity: cursorOp }">
        <svg class="w-8 h-8 text-white drop-shadow-[0_4px_10px_rgba(0,0,0,0.9)]" viewBox="0 0 24 24" fill="currentColor"
          stroke="black" stroke-width="1.2">
          <path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 0 1 .35-.15h6.87a.5.5 0 0 0 .35-.85L5.5 3.21z" />
        </svg>
      </div>

    </div> <!-- End Camera Viewport Rig -->

    <!-- Edge Gradients (Fixed outside camera rig) -->
    <div
      class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[#111111] to-transparent z-20 pointer-events-none">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import openAILogo from '@/assets/openai.svg'

const phase = ref(1)
const subphase = ref('init')
const cursorX = ref(60)
const cursorY = ref(150)
const cursorOp = ref(0)

const camX = ref(0)
const camY = ref(0)
const camScale = ref(1)
const camDuration = ref(1000)

const typedText = ref('')
const fullText = "Memwyre api v1 auth specs..."
const contextSynced = ref(false)
const toastMsg = ref('')

let isRunning = true

// Helper for delaying transitions safely
const sleep = (ms) => new Promise(r => {
  if (isRunning) setTimeout(r, ms)
})

const focusCamera = (x, y, scale = 1, duration = 1000) => {
  camX.value = -x
  camY.value = -y
  camScale.value = scale
  camDuration.value = duration
}

const triggerPhase1 = async () => {
  if (!isRunning) return
  phase.value = 1
  subphase.value = 'init'
  cursorOp.value = 0
  cursorX.value = 150
  cursorY.value = 170

  // Camera zooms in on the text content quickly
  focusCamera(0, -20, 1.1, 800)
  await sleep(400)

  if (!isRunning) return
  subphase.value = 'move'
  cursorX.value = -20
  cursorY.value = 100
  cursorOp.value = 1
  await sleep(200)

  // Move to injected Memwyre icon
  cursorX.value = -10
  cursorY.value = 75
  // Camera slowly tracks and zooms in on MemWyre button
  focusCamera(-10, 70, 1.4, 600)
  await sleep(650)

  if (!isRunning) return
  subphase.value = 'click'
  await sleep(150)

  if (!isRunning) return
  subphase.value = 'toast'
  toastMsg.value = 'Exact memory saved'
  cursorX.value = -10
  cursorY.value = 85

  await sleep(600)

  if (!isRunning) return
  cursorOp.value = 0
  phase.value = 0 // Cleanup phase
  focusCamera(0, 0, 1.0, 500)
  // await sleep(500)

  triggerPhase2()
}

const triggerPhase2 = async () => {
  if (!isRunning) return
  phase.value = 2
  subphase.value = 'init'
  typedText.value = "Ask anything"
  contextSynced.value = false
  cursorOp.value = 0
  cursorX.value = -60
  cursorY.value = 150

  // Camera zooms in hard on the absolute leftmost edge of the input bar
  focusCamera(-200, 0, 1.8, 600)

  await sleep(300)

  if (!isRunning) return
  subphase.value = 'typing'
  typedText.value = ""

  for (let i = 0; i < fullText.length; i++) {
    if (!isRunning) return
    typedText.value += fullText[i]

    // Dynamically calculate camera X to trace the typing (-200 to +60)
    let progress = (i + 1) / fullText.length
    let currentX = -200 + (progress * 260)

    // 3 millisecond snap transition for a robotic typewriter stepping effect
    focusCamera(currentX, 0, 1.8, 3)

    await sleep(25) // High speed typing
  }
  await sleep(200)

  if (!isRunning) return
  cursorOp.value = 1
  await sleep(30)
  subphase.value = 'move'

  // Move cursor to MemWyre Button (Right side)
  cursorX.value = 100
  cursorY.value = 15
  // Camera snaps forcefully to the action cluster on the far right
  focusCamera(100, 15, 1.9, 400)
  await sleep(450)

  if (!isRunning) return
  subphase.value = 'click'
  await sleep(120)

  // Context Sync Action!
  contextSynced.value = true
  await sleep(80)

  if (!isRunning) return
  subphase.value = 'toast'
  toastMsg.value = 'Context synced'
  cursorX.value = 100
  cursorY.value = 25

  // Instant zoom out to frame the interaction at 1.5x!
  focusCamera(0, 0, 1.5, 250)

  await sleep(400)

  if (!isRunning) return
  cursorOp.value = 0
  phase.value = 0 // Clean up
  focusCamera(0, 0, 1, 500)
  await sleep(500)

  // Loop back
  triggerPhase1()
}

onMounted(() => {
  isRunning = true
  triggerPhase1()
})

onUnmounted(() => {
  isRunning = false
})
</script>

<style scoped>
/* Snappy Zoom In/Out for parent blocks */
.velocity-enter-active {
  transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.velocity-leave-active {
  transition: all 0.4s cubic-bezier(0.6, -0.28, 0.735, 0.045);
}

.velocity-enter-from,
.velocity-leave-to {
  opacity: 0;
  transform: scale(0.6);
}

/* Aggressive Pop for Toasts and Badges */
.pop-enter-active {
  transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.pop-leave-active {
  transition: all 0.3s ease-in;
}

.pop-enter-from {
  opacity: 0;
  transform: translateY(15px) scale(0.5);
}

.pop-leave-to {
  opacity: 0;
  transform: scale(0.8);
}
</style>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translate(-50%, -20px) scale(0.95);
}
</style>
