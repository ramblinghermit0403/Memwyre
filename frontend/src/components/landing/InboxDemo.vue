<template>
  <div ref="root"
    class="dark w-full relative mx-auto overflow-hidden bg-[#111111] border border-gray-700/60 flex items-center justify-center rounded-xl min-h-[400px] font-sans">

    <!-- Single Camera Rig -->
    <div class="absolute w-full h-full z-10 flex items-center justify-center origin-center"
      :style="{ transform: `translate(${camX}px, ${camY}px) scale(${camScale})`, transition: `all ${camDuration}ms cubic-bezier(0.25,1,0.35,1)` }">

      <!-- ======= SHOT 0: Inbox Icon + Badge Counter ======= -->
      <transition name="velocity">
        <div v-if="shot === 0" key="shot0" class="absolute flex items-center justify-center w-full h-full">
          <div class="relative">
            <svg class="w-20 h-20 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"
              stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
            </svg>
            <div v-if="badgeCount > 0"
              class="absolute -top-2 -right-2 w-7 h-7 bg-red-500 rounded-full flex items-center justify-center text-white text-xs font-bold shadow-lg shadow-red-500/40">
              {{ badgeCount }}
            </div>
          </div>
        </div>
      </transition>

      <!-- ======= SHOT 1: Inbox List with cursor click ======= -->
      <transition name="velocity">
        <div v-if="shot === 1" key="shot1" class="absolute flex items-center justify-center w-full h-full px-4">
          <div
            class="w-[380px] flex flex-col bg-[#212121] rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.6)] border border-white/10 overflow-hidden"
            style="max-height: 90%;">
            <div class="p-4 border-b border-white/5 flex justify-between items-center bg-[#1a1a1a]">
              <h2 class="text-base font-bold tracking-tight text-gray-100 italic transition-all duration-300">Incoming
                Items</h2>
            </div>
            <div ref="listArea" class="flex-1 overflow-y-auto p-3 space-y-3 custom-scrollbar">
              <!-- Item 1 -->
              <div class="p-4 rounded-xl border cursor-pointer transition-all duration-300"
                :class="selectedItem === 0 ? 'bg-[#333] border-[#D97757] shadow-[0_0_30px_rgba(217,119,87,0.2)]' : 'bg-[#2a2a2a] border-white/5 hover:border-white/10'">
                <h3 class="font-bold tracking-tight text-gray-100 mb-1 line-clamp-2">Enhancing AI Idea Retention</h3>
                <div class="flex justify-between items-end mt-3">
                  <div class="flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                      <div class="w-5 h-5 flex items-center justify-center shrink-0 rounded overflow-hidden">
                        <img :src="openaiSvg" alt="Source"
                          class="w-full h-full object-cover rounded-sm invert opacity-90">
                      </div>
                      <span
                        class="text-[11px] font-mono text-gray-400 truncate max-w-[140px] tracking-tight">chatgpt</span>
                    </div>
                    <span
                      class="inline-flex items-center px-2 py-0.5 rounded-md text-[10px] font-black w-fit bg-[#D97757]/20 text-[#D97757] border border-[#D97757]/30 uppercase tracking-widest">Pending</span>
                  </div>
                  <span class="text-[10px] uppercase font-bold tracking-tighter text-gray-500">1d ago</span>
                </div>
              </div>
              <!-- Item 2 -->
              <div class="p-4 rounded-xl border border-white/5 cursor-pointer transition-all bg-[#2a2a2a] opacity-60">
                <h3 class="font-bold tracking-tight text-gray-100 mb-1 line-clamp-2">Geriforte: Herbal Wellness</h3>
                <div class="flex justify-between items-end mt-3">
                  <div class="flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                      <div class="w-5 h-5 flex items-center justify-center shrink-0 rounded overflow-hidden">
                        <img :src="openaiSvg" alt="Source"
                          class="w-full h-full object-cover rounded-sm invert opacity-90">
                      </div>
                      <span class="text-[11px] font-mono text-gray-400 tracking-tight">chatgpt</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- ======= SHOT 2: Action Bar (standalone) ======= -->
      <transition name="velocity">
        <div v-if="shot === 2" key="shot2" class="absolute flex items-center justify-center w-full h-full px-4">
          <div
            class="p-4 bg-[#1a1a1a] rounded-2xl border border-white/10 flex items-center gap-3 shadow-[0_20px_60px_rgba(0,0,0,0.8)]">
            <button
              class="px-5 py-2.5 bg-white/5 text-gray-300 text-sm font-bold rounded-xl border border-white/5 hover:bg-white/10 transition-all flex items-center gap-2 tracking-wide uppercase text-[12px]">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z">
                </path>
              </svg>
              Edit
            </button>
            <button
              class="px-5 py-2.5 bg-white/5 text-red-400 text-sm font-bold rounded-xl border border-white/5 hover:bg-red-500/10 transition-all flex items-center gap-2 tracking-wide uppercase text-[12px]">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
              Dismiss
            </button>
            <button
              class="px-8 py-2.5 text-white text-base font-bold rounded-xl shadow-lg transition-all transform flex items-center gap-2 min-w-[130px] justify-center"
              :class="approved ? 'bg-[#1B8054] shadow-[0_0_30px_rgba(27,128,84,0.4)]' : 'bg-[#D97757] hover:bg-[#C4654A] shadow-[0_0_30px_rgba(217,119,87,0.3)]'">
              <svg v-if="approved" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
              </svg>
              {{ approved ? 'Saved!' : 'Approve' }}
            </button>
          </div>
        </div>
      </transition>

    </div> <!-- End Camera Rig -->

    <!-- Virtual Cursor -->
    <div class="absolute left-1/2 top-1/2 pointer-events-none z-30"
      :style="{ transform: `translate(${cursorX}px, ${cursorY}px)`, opacity: cursorOp, transition: `transform ${cursorMoveDuration}ms cubic-bezier(0.34,1.56,0.64,1), opacity 200ms` }">
      <svg class="drop-shadow-[0_4px_12px_rgba(0,0,0,0.9)]"
        :class="{ 'scale-75 transition-transform duration-75': cursorClick }"
        style="width:34px;height:34px;color:white;" viewBox="0 0 24 24" fill="currentColor" stroke="black"
        stroke-width="1.2">
        <path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 0 1 .35-.15h6.87a.5.5 0 0 0 .35-.85L5.5 3.21z" />
      </svg>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const openaiSvg = "data:image/svg+xml,%3csvg%20fill-rule='evenodd'%20height='1em'%20style='flex:none;line-height:1'%20viewBox='0%200%2024%2024'%20width='1em'%20xmlns='http://www.w3.org/2000/svg'%3e%3cstyle%3epath%20{%20fill:%20%23111111;%20}%3c/style%3e%3ctitle%3eOpenAI%3c/title%3e%3cpath%20d='M9.205%208.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357%201.356-.523%202.117-.523%202.854%200%204.662%202.212%204.662%204.566%200%20.167%200%20.357-.024.547l-4.71-2.759a.797.797%200%2000-.856%200l-5.97%203.473zm10.609%208.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473%201.95-1.118a.433.433%200%2001.476%200l4.543%202.617c1.309.76%202.189%202.378%202.189%203.948%200%201.808-1.07%203.473-2.76%204.163zM7.802%2012.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545%201.95-4.472%204.591-4.472%201%200%201.927.333%202.712.928L8.23%205.067c-.285.166-.428.404-.428.737v6.898zM12%2015.128l-2.795-1.57v-3.33L12%208.658l2.795%201.57v3.33L12%2015.128zm1.796%207.23c-1%200-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974%201.142c.167.095.238.238.238.428v5.233c0%202.545-1.974%204.472-4.614%204.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482%204.482%200%20014.21%206.327v5.423c0%20.333.143.571.428.738l5.947%203.449-1.95%201.118a.432.432%200%2001-.476%200zm-.262%203.9c-2.688%200-4.662-2.021-4.662-4.519%200-.19.024-.38.047-.57l4.686%202.71c.286.167.571.167.856%200l5.97-3.448v2.26c0%20.19-.07.333-.237.428l-4.543%202.616c-.619.357-1.356.523-2.117.523zm5.899%202.83a5.947%205.947%200%20005.827-4.756C22.287%2018.339%2024%2015.84%2024%2013.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498%200-3.401-2.759-5.947-5.946-5.947-.642%200-1.26-.095-1.88-.31A5.962%205.962%200%200010.205%200a5.947%205.947%200%2000-5.827%204.757C1.713%205.447%200%207.945%200%2010.49c0%201.666.713%203.283%201.998%204.448-.119.5-.19%201-.19%201.499%200%203.401%202.759%205.946%205.946%205.946.642%200%201.26-.095%201.88-.309a5.96%205.96%200%20004.162%201.713z'%3e%3c/path%3e%3c/svg%3e";

const claudeSvg = "data:image/svg+xml,%3csvg%20height='1em'%20style='flex:none;line-height:1'%20viewBox='0%200%2024%2024'%20width='1em'%20xmlns='http://www.w3.org/2000/svg'%3e%3ctitle%3eClaude%3c/title%3e%3cpath%20d='M4.709%2015.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0%2011.784l.055-.352.48-.321.686.06%201.52.103%202.278.158%201.652.097%202.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686%201.908%201.476%202.491%201.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97%202.97%200%2001-.104-.729L6.283.134%206.696%200l.996.134.42.364.62%201.414%201.002%202.229%201.555%203.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286%201.851-.559%202.903-.364%201.942h.212l.243-.242.985-1.306%201.652-2.064.73-.82.85-.904.547-.431h1.033l.76%201.129-.34%201.166-1.064%201.347-.881%201.142-1.264%201.7-.79%201.36.073.11.188-.02%202.856-.606%201.543-.28%201.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061%201.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093%201.068%202.006%201.81%202.509%202.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649%202.345%203.521.122%201.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674%207.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434%201.967-2.18%202.945-1.726%201.845-.414.164-.717-.37.067-.662.401-.589%202.388-3.036%201.44-1.882.93-1.086-.006-.158h-.055L4.132%2018.56l-1.13.146-.487-.456.061-.746.231-.243%201.908-1.312-.006.006z'%20fill='%23D97757'%20fill-rule='nonzero'%3e%3c/path%3e%3c/svg%3e";

const FADE_TIME = 600;

const root = ref(null);
const listArea = ref(null);
const shot = ref(-1);
const badgeCount = ref(0);
const selectedItem = ref(-1);
const approved = ref(false);

const camX = ref(0);
const camY = ref(0);
const camScale = ref(0.8); // Match the loop's starting scale to prevent snapping
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

async function loop() {
  while (alive) {
    // === RESET ALL STATE ===
    shot.value = -1;
    badgeCount.value = 0;
    selectedItem.value = -1;
    approved.value = false;
    cursorOp.value = 0;
    focusCamera(0, 0, 0.8, 0); 

    // Let the component "settle" on screen before starting the first zoom
    await wait(600);
    if (!alive) return;

    // ==========================================
    // SHOT 0: Inbox icon with counting badge
    // ==========================================
    focusCamera(0, 0, 3.5, 800);
    shot.value = 0;
    await wait(600);

    for (let i = 1; i <= 10; i++) {
      if (!alive) return;
      badgeCount.value = i;
      await wait(60);
    }


    if (!alive) return;

    // Cursor flies in AND camera zooms in tighter simultaneously
    cursorX.value = 250;
    cursorY.value = 250;
    cursorMoveDuration.value = 0;
    await wait(20);

    cursorOp.value = 1;
    cursorX.value = 0;
    cursorY.value = 0;
    cursorMoveDuration.value = 450;
    focusCamera(0, 0, 3.8, 450); // Faster zoom
    await wait(200);
    if (!alive) return;

    // Click on inbox icon
    cursorClick.value = true;
    await wait(150);
    cursorClick.value = false;
    await wait(200);
    if (!alive) return;

    // Zoom out smoothly while fading
    focusCamera(0, 0, 1.0, 450);
    cursorOp.value = 0;
    shot.value = -1;
    await wait(250); // Wait for full 400ms CSS leave transition + buffer
    if (!alive) return;

    // ==========================================
    // SHOT 1: Inbox list, cursor clicks item
    // ==========================================
    focusCamera(0, 0, 1.1, 0);
    shot.value = 1;
    await wait(200);
    if (!alive) return;

    // Cursor flies in AND camera focuses on the item
    cursorX.value = 300;
    cursorY.value = 300;
    cursorMoveDuration.value = 0;
    await wait(20);

    cursorOp.value = 1;
    cursorX.value = 100;
    cursorY.value = 20;
    cursorMoveDuration.value = 450;
    focusCamera(20, -85, 1.3, 450);
    await wait(500);
    if (!alive) return;

    // Click first item
    cursorClick.value = true;
    await wait(150);
    cursorClick.value = false;
    selectedItem.value = 0;
    await wait(300);
    if (!alive) return;

    // Keep focus and fade out
    cursorOp.value = 0;
    await wait(50);
    shot.value = -1;
    await wait(350); // Wait for full 400ms CSS leave transition + buffer
    if (!alive) return;

    // ==========================================
    // SHOT 2: Action bar (standalone) + approve
    // ==========================================
    focusCamera(0, 0, 1.0, 0);
    shot.value = 2;

    focusCamera(0, 0, 1.4, 600);
    await wait(300);
    if (!alive) return;

    // Cursor flies in AND camera snaps to button
    cursorX.value = 350;
    cursorY.value = 350;
    cursorMoveDuration.value = 0;
    await wait(20);

    cursorOp.value = 1;
    cursorX.value = 118; // More to the right for Approve button
    cursorY.value = 0;   // Centered vertically on bar
    cursorMoveDuration.value = 450;
    focusCamera(118, 0, 1.8, 450);
    await wait(500);
    if (!alive) return;

    // Click Approve
    cursorClick.value = true;
    await wait(150);
    cursorClick.value = false;
    approved.value = true;

    // Zoom out to reveal the full result
    focusCamera(0, 0, 1.5, 800);
    await wait(1500);
    if (!alive) return;

    // Fade out shot 2 → loop restart
    cursorOp.value = 0;
    shot.value = -1;
    await wait(450);
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s cubic-bezier(0.25, 1, 0.35, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@keyframes badgePop {
  0% {
    transform: scale(0.3);
    opacity: 0;
  }

  50% {
    transform: scale(1.4);
  }

  75% {
    transform: scale(0.9);
  }

  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.badge-pop {
  animation: badgePop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 20px;
}
</style>
