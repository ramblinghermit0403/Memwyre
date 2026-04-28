<template>
  <div class="relative w-full h-full overflow-hidden flex items-center justify-center bg-transparent font-sans">
    
    <!-- Static UI Container (Removed w-full/h-full to prevent overflow-hidden clipping) -->
    <div class="flex flex-col items-center justify-center gap-12 w-full max-w-[650px]">
      
      <!-- Component 1: Captured Message (Phase 1) -->
      <div class="relative w-full">
        <div class="bg-[#111111] rounded-[2rem] p-7 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.9)] border border-white/10 w-full relative">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-6 h-6 rounded-full flex items-center justify-center bg-white/10 border border-white/5 overflow-hidden">
                <img src="@/assets/openai.svg" class="w-4 h-4 object-contain invert brightness-0" alt="ChatGPT" />
            </div>
            <span class="text-white font-semibold text-sm">ChatGPT</span>
          </div>
          <div class="text-white/90 text-[15px] sm:text-lg mb-6 leading-relaxed font-sans mt-2">
            If you want, tell me <em>why you're planning</em> to do this, and I can give you a better answer on whether it's actually worth it for your specific use case.
          </div>
          
          <!-- Action Row -->
          <div class="relative flex items-center gap-5 text-gray-500">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" stroke-width="2" /></svg>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" stroke-width="2" /></svg>
            
            <!-- Static Toast for Phase 1 -->
            <div class="absolute -top-[55px] left-1/2 transform -translate-x-[calc(50%+200px)] scale-90 bg-[#1B8054] text-[#f4fef8] px-4 py-2 rounded-lg shadow-[0_0_30px_rgba(27,128,84,0.7)] text-[15px] font-bold z-30 whitespace-nowrap tracking-wide border border-[#23a36b]">
              Saved to Memwyre!
            </div>

            <!-- Injected MemWyre Logo (Static Target) -->
            <div class="w-10 h-10 rounded-full bg-[#111111] shadow-[0_0_35px_rgba(27,128,84,0.4)] border border-[#1B8054] flex items-center justify-center scale-110">
              <img src="/image.svg" alt="Memwyre" class="w-6 h-6 object-contain" />
            </div>
          </div>
        </div>
      </div>

      <!-- Component 2: Omnipresent Input (Phase 2) -->
      <div class="relative w-full">
        <!-- Input Textarea bar -->
        <div class="relative flex items-center bg-[#111111] rounded-full p-3 pl-5 shadow-[0_30px_90px_-15px_rgba(0,0,0,1)] border border-white/10 w-full min-h-[60px]">
          <!-- Left Actions -->
          <div class="flex-none flex items-center gap-3 pr-4 text-[#b5b5b5]">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"></path>
            </svg>
          </div>

          <!-- Input Text -->
          <div class="flex-1 flex items-center overflow-hidden">
            <span class="inline-flex items-center bg-[#3a3b40] text-gray-200 text-sm px-3 py-1 rounded-md mr-3 border border-white/20 whitespace-nowrap">
              <svg class="w-4 h-4 mr-2 text-[#10b981]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path>
              </svg>
              Auth System Guidelines
            </span>
            <span class="text-white text-lg font-medium">Memwyre api v1...</span>
          </div>

          <!-- Right Actions -->
          <div class="flex-none flex items-center gap-5 pl-4">
             <div class="w-10 h-10 rounded-full flex items-center justify-center bg-[#1B8054] shadow-[0_0_30px_rgba(27,128,84,0.5)] border border-[#23a36b]">
                <svg class="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
                  <path d="M5 13l4 4L19 7" />
                </svg>
             </div>
             <div class="w-10 h-10 flex items-center justify-center rounded-full bg-white text-black">
                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                  <path d="M12 2v20M8 8v8M16 8v8M4 11v2M20 11v2" />
                </svg>
             </div>
          </div>
        </div>

        <!-- Toast Floating Above Component 2 -->
        <div class="absolute -top-16 bg-[#1B8054] text-[#f4fef8] px-6 py-3 rounded-xl shadow-[0_10px_40px_rgba(27,128,84,0.6)] text-lg font-bold z-30 border border-[#23a36b] right-[30px]">
          Context synced!
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
// Purely static component for cinematic slides
</script>
