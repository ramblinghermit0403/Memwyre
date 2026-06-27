<template>
  <div class="relative w-full h-full flex items-center justify-center bg-transparent font-sans text-left">
    
    <!-- Outer Card without background shadow, adapts to light/dark mode like the real timeline container -->
    <div class="w-full max-w-2xl bg-white dark:bg-[#111111] rounded-[2rem] border border-gray-200 dark:border-white/5 overflow-hidden transform scale-125 rotate-[-2deg] translate-x-[-10%] min-h-[700px] flex flex-col">
      <div class="flex-1 overflow-y-auto custom-scrollbar p-8 space-y-8">
        
        <!-- Date Header 1 -->
        <div class="space-y-4">
          <h4 class="text-xs uppercase tracking-wider text-gray-400 dark:text-gray-500 font-bold">4/10/2026</h4>
          <ul class="divide-y divide-gray-200 dark:divide-white/5 border-t border-b border-gray-200 dark:border-white/5">
            <li class="py-6">
              <div class="flex items-start justify-between gap-4">
                <div class="min-w-0 flex-1">
                  <div class="flex items-start gap-4">
                    <!-- Source Icon Container -->
                    <div class="w-8 h-8 flex items-center justify-center shrink-0 bg-gray-100 dark:bg-white/5 rounded overflow-hidden mt-0.5">
                      <!-- Adaptive OpenAI SVG Icon -->
                      <svg class="w-4 h-4 text-gray-800 dark:text-white" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9.205 8.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357 1.356-.523 2.117-.523 2.854 0 4.662 2.212 4.662 4.566 0 .167 0 .357-.024.547l-4.71-2.759a.797.797 0 00-.856 0l-5.97 3.473zm10.609 8.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473 1.95-1.118a.433.433 0 01.476 0l4.543 2.617c1.309.76 2.189 2.378 2.189 3.948 0 1.808-1.07 3.473-2.76 4.163zM7.802 12.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545 1.95-4.472 4.591-4.472 1 0 1.927.333 2.712.928L8.23 5.067c-.285.166-.428.404-.428.737v6.898zM12 15.128l-2.795-1.57v-3.33L12 8.658l2.795 1.57v3.33L12 15.128zm1.796 7.23c-1 0-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974 1.142c.167.095.238.238.238.428v5.233c0 2.545-1.974 4.472-4.614 4.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482 4.482 0 014.21 6.327v5.423c0 2.333.143.571.428.738l5.947 3.449-1.95 1.118a.432.432 0 01-.476 0zm-.262 3.9c-2.688 0-4.662-2.021-4.662-4.519 0-.19.024-.38.047-.57l4.686 2.71c.286.167.571.167.856 0l5.97-3.448v2.26c0 .19-.07.333-.237.428l-4.543 2.616c-.619.357-1.356.523-2.117.523zm5.899 2.83a5.947 5.947 0 005.827-4.756C22.287 18.339 24 15.84 24 13.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498 0-3.401-2.759-5.947-5.946-5.947-.642 0-1.26-.095-1.88-.31A5.962 5.962 0 0010.205 0a5.947 5.947 0 00-5.827 4.757C1.713 5.447 0 7.945 0 10.49c0 1.666.713 3.283 1.998 4.448-.119.5-.19 1-.19 1.499 0 3.401 2.759 5.946 5.946 5.946.642 0 1.26-.095 1.88-.309a5.96 5.96 0 004.162 1.713z" />
                      </svg>
                    </div>
                    <div class="min-w-0">
                      <p class="text-base font-semibold text-gray-900 dark:text-white truncate">Enhancing AI Idea Retention</p>
                      <p class="text-[10px] text-gray-400 dark:text-gray-500 mt-1 uppercase tracking-widest font-bold">ChatGPT | Conversation | 07:54 PM</p>
                      <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 line-clamp-2 leading-relaxed italic opacity-85">"👉 Treat AI conversations like assets, not chats. Capture only what matters..."</p>
                      
                      <!-- Status Tag -->
                      <div class="mt-3 flex items-center gap-3">
                         <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200/60 dark:bg-emerald-950/30 dark:text-emerald-300/90 dark:border-emerald-900/40 uppercase tracking-widest">Approved</span>
                         <div class="relative">
                           <button class="inline-flex items-center gap-1.5 text-[10px] px-2 py-1 rounded-md border border-gray-200 dark:border-white/10 bg-gray-50 dark:bg-white/5 text-gray-500 dark:text-gray-400">
                             <span>MEMWYRE</span>
                           </button>
                         </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="flex items-center gap-2 shrink-0">
                  <button class="inline-flex items-center gap-1.5 text-[10px] px-3 py-1.5 rounded-md border border-gray-200 dark:border-white/10 text-gray-700 dark:text-gray-300 bg-white dark:bg-transparent hover:bg-gray-50 dark:hover:bg-white/5 shadow-sm">Open</button>
                  <button class="inline-flex items-center gap-1.5 text-[10px] px-3 py-1.5 rounded-md border border-[#D97757]/20 dark:border-[#D97757]/30 bg-[#D97757]/10 text-[#D97757] font-bold">Use in AI</button>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <!-- Date Header 2 -->
        <div class="space-y-4">
          <h4 class="text-xs uppercase tracking-wider text-gray-400 dark:text-gray-500 font-bold">4/3/2026</h4>
          <ul class="divide-y divide-gray-200 dark:divide-white/5 border-t border-b border-gray-200 dark:border-white/5">
            <li class="py-6">
              <div class="flex items-start justify-between gap-4">
                <div class="min-w-0 flex-1">
                  <div class="flex items-start gap-4">
                    <div class="w-8 h-8 flex items-center justify-center shrink-0 bg-gray-100 dark:bg-white/5 rounded overflow-hidden mt-0.5">
                      <img src="https://www.google.com/s2/favicons?domain=dodopayments.com&sz=64" alt="Source Icon" class="w-full h-full object-cover">
                    </div>
                    <div class="min-w-0">
                      <p class="text-base font-semibold text-gray-900 dark:text-white truncate">Dodo Payments Documentation</p>
                      <p class="text-[10px] text-gray-400 dark:text-gray-500 mt-1 uppercase tracking-widest font-bold">https://dodopayments.com/ | Webpage | 09:35 AM</p>
                      <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 line-clamp-2 leading-relaxed">"The complete monetization stack for AI-first companies. Credit-based billing, usage metering..."</p>
                      
                      <!-- Status Tag -->
                      <div class="mt-3 flex items-center gap-3">
                         <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200/60 dark:bg-emerald-950/30 dark:text-emerald-300/90 dark:border-emerald-900/40 uppercase tracking-widest">Approved</span>
                         <div class="relative">
                           <button class="inline-flex items-center gap-1.5 text-[10px] px-2 py-1 rounded-md border border-gray-200 dark:border-white/10 bg-gray-50 dark:bg-white/5 text-gray-500 dark:text-gray-400">
                             <span>Unassigned</span>
                           </button>
                         </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
// High-fidelity production mock for cinematic slides
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
}
</style>
