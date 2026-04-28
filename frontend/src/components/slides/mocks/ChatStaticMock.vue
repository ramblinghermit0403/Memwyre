<template>
  <div class="dark relative w-full h-full flex flex-col items-center justify-center bg-transparent font-sans text-left">
    
    <div class="w-[702px] bg-[#111111] rounded-[2rem] shadow-[0_40px_100px_-20px_rgba(0,0,0,0.9)] border border-white/10 overflow-hidden transform scale-110 translate-x-[-5%]">
      <!-- Header -->
      <div class="px-8 py-5 border-b border-white/5 flex items-center justify-between bg-[#1a1a1a]">
        <span class="text-sm font-bold text-gray-400 uppercase tracking-widest">Memwyre Chat</span>
        <div class="flex gap-2">
          <div class="w-3 h-3 rounded-full bg-red-500/20 border border-red-500/40"></div>
          <div class="w-3 h-3 rounded-full bg-yellow-500/20 border border-yellow-500/40"></div>
          <div class="w-3 h-3 rounded-full bg-green-500/20 border border-green-500/40"></div>
        </div>
      </div>

      <!-- Content -->
      <div class="p-8 space-y-6">
        <!-- User Message -->
        <div class="flex justify-end">
          <div class="bg-white text-black px-6 py-3 rounded-2xl rounded-tr-sm font-medium shadow-xl">
            What were the key decisions from my OAuth2 notes?
          </div>
        </div>

        <!-- AI Response -->
        <div class="flex justify-start">
          <div class="bg-[#1a1a1a] border border-white/5 px-6 py-5 rounded-2xl rounded-tl-sm text-gray-200 leading-relaxed max-w-[90%] shadow-lg">
            <p class="mb-4">Decisions finalized for the new authentication flow:</p>
            <ul class="space-y-3 list-disc pl-5 text-sm text-gray-300">
              <li><strong>Token Strategy:</strong> Short-lived access tokens (15m) with rotation.</li>
              <li><strong>Granular Scopes:</strong> Defined per-resource (e.g., <code>read:inbox</code>).</li>
            </ul>
            
            <div class="mt-6 pt-5 border-t border-white/5">
              <p class="text-[10px] uppercase font-black text-gray-500 mb-3 tracking-widest">Sources Cited</p>
              <div class="flex gap-3">
                <div class="bg-white/5 border border-white/10 px-3 py-1.5 rounded-lg text-xs flex items-center gap-2">
                   <span>📄</span> OAuth2 Notes
                </div>
                <div class="bg-white/5 border border-white/10 px-3 py-1.5 rounded-lg text-xs flex items-center gap-2">
                   <span>📄</span> API Security Memo
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
// Purely static component for cinematic slides
</script>
