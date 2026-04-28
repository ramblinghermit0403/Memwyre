<template>
  <div class="w-full flex items-center justify-center p-4">
    <div class="relative w-full max-w-[280px] bg-gray-900 rounded-xl shadow-[0_20px_50px_rgba(0,0,0,0.3)] overflow-hidden border border-gray-700/50 font-mono scale-[1.05]">
      <!-- Terminal Header -->
      <div class="flex items-center gap-2 px-3 py-2 bg-gray-800/80 border-b border-gray-700/50">
        <div class="flex gap-1.5">
          <div class="w-2.5 h-2.5 rounded-full bg-red-500"></div>
          <div class="w-2.5 h-2.5 rounded-full bg-yellow-500"></div>
          <div class="w-2.5 h-2.5 rounded-full bg-green-500"></div>
        </div>
        <div class="text-[10px] text-gray-400 mx-auto opacity-70">terminal</div>
      </div>
      
      <!-- Terminal Body -->
      <div class="p-4 text-xs h-[170px] flex flex-col justify-start relative pt-6">
         <div class="text-green-400 mb-3">> <span class="text-white">{{ commandText }}</span><span v-if="showCursor" class="animate-pulse">_</span></div>
         
         <transition name="fade">
           <div v-if="step >= 1" class="text-gray-400 mb-1.5 truncate">Resolving dependencies...</div>
         </transition>
         
         <transition name="fade">
           <div v-if="step >= 2" class="text-gray-400 mb-4 truncate">Connecting to Memwyre API...</div>
         </transition>
         
         <transition name="pop">
           <div v-if="step >= 3" class="mt-2 flex items-center gap-2 bg-green-500/10 text-green-400 p-2.5 rounded-lg border border-green-500/20 w-max shadow-[0_0_15px_rgba(34,197,94,0.1)]">
             <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
               <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
             </svg>
             <span class="font-bold tracking-wide text-sm">Setup Complete (0.8s)</span>
           </div>
         </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const commandText = ref('')
const fullCommand = 'mcp install memwyre'
const showCursor = ref(true)
const step = ref(0)
let isRunning = true

const sleep = (ms) => new Promise(r => { if(isRunning) setTimeout(r, ms) })

const playAnimation = async () => {
  if(!isRunning) return
  step.value = 0
  commandText.value = ''
  showCursor.value = true
  
  await sleep(600)
  
  for(let char of fullCommand) {
    if(!isRunning) return
    commandText.value += char
    await sleep(40) // Fast typing
  }
  
  showCursor.value = false
  await sleep(150)
  if(!isRunning) return
  step.value = 1
  
  await sleep(300)
  if(!isRunning) return
  step.value = 2
  
  await sleep(300)
  if(!isRunning) return
  step.value = 3
  
  await sleep(2500)
  if(!isRunning) return
  playAnimation()
}

onMounted(() => {
  isRunning = true
  playAnimation()
})

onUnmounted(() => {
  isRunning = false
})
</script>

<style scoped>
.fade-enter-active { transition: opacity 0.2s; }
.fade-enter-from { opacity: 0; }
.pop-enter-active { transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); }
.pop-enter-from { opacity: 0; transform: scale(0.8) translateY(10px); }
</style>
