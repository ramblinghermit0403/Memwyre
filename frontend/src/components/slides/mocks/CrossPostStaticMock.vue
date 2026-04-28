<template>
  <div class="relative w-full h-full flex flex-col items-center justify-center bg-transparent font-sans text-left">
    
    <!-- Cross-Post Dropdown Mock -->
    <div class="w-[600px] bg-[#111111] rounded-[2rem] shadow-[0_40px_100px_-20px_rgba(0,0,0,0.9)] border border-white/10 overflow-hidden transform scale-110">
      <!-- Header -->
      <div class="px-8 py-6 border-b border-white/5 flex items-center justify-between bg-[#1a1a1a]">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-[#D97757]/20 border border-[#D97757]/40 flex items-center justify-center">
            <svg class="w-5 h-5 text-[#D97757]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
            </svg>
          </div>
          <span class="text-lg font-bold text-white tracking-wide">Continue in another AI</span>
        </div>
      </div>

      <!-- List of models -->
      <div class="p-6 space-y-3">
        <!-- ChatGPT -->
        <div class="w-full flex items-center gap-6 px-6 py-4 bg-white/5 border border-white/10 rounded-2xl">
          <img src="@/assets/openai.svg" class="w-10 h-10 object-contain invert brightness-0" alt="ChatGPT" />
          <span class="text-xl font-medium text-gray-200">Continue in ChatGPT</span>
        </div>

        <!-- Claude -->
        <div class="w-full flex items-center gap-6 px-6 py-4 bg-white/5 border border-white/10 rounded-2xl">
          <img src="@/assets/claude-color.svg" alt="Claude" class="w-10 h-10 object-contain" />
          <span class="text-xl font-medium text-gray-200">Continue in Claude</span>
        </div>

        <!-- Gemini -->
        <div class="w-full flex items-center gap-6 px-6 py-4 bg-white/5 border border-white/10 rounded-2xl">
          <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-10 h-10 object-contain" />
          <span class="text-xl font-medium text-gray-200">Continue in Gemini</span>
        </div>

        <!-- Copy Context (Special Action) -->
        <div class="w-full flex items-center gap-6 px-6 py-4 bg-white/10 border border-[#D97757]/30 rounded-2xl mt-4">
          <svg class="w-10 h-10 text-[#D97757]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
          </svg>
          <div>
            <span class="text-xl font-bold text-white block">Copy Context</span>
            <span class="text-xs text-[#D97757] font-bold uppercase tracking-widest">Hand off manually</span>
          </div>
        </div>
      </div>

      <!-- Footer Toast -->
      <div class="mt-4 px-8 py-4 bg-[#D97757]/10 border-t border-white/5 flex items-center justify-between">
         <span class="text-sm text-gray-400">Current model: <span class="text-white font-bold">GPT-4o</span></span>
         <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-green-500 shadow-[0_0_10px_rgba(34,197,94,0.5)]"></span>
            <span class="text-xs font-bold text-green-500 uppercase">Context Ready</span>
         </div>
      </div>
    </div>

  </div>
</template>

<script setup>
// Purely static component for cinematic slides
</script>
