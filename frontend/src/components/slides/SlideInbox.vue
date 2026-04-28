<template>
  <div class="w-[1920px] h-[1080px] bg-[#1f1f23] overflow-hidden flex relative p-24 font-sans text-white">
    
    <!-- Top Left Brand -->
    <div class="absolute top-20 left-24 text-4xl font-medium text-gray-400 tracking-wide">
      memwyre.tech
    </div>

    <!-- Left Column: Marketing Copy -->
    <div class="w-[35%] h-full flex flex-col justify-start pt-32 pr-12 z-10 relative">
       <h1 class="text-[5rem] font-bold leading-[1.15] tracking-tight text-gray-100">
        Control your knowledge.<br/>
        <span class="text-[#D97757]">Your vault, your rules.</span>
       </h1>
    </div>

    <div class="flex-1 h-full relative">
       <div class="absolute inset-0 flex items-center justify-center transform translate-x-[-320px] translate-y-[-20px]">
           <!-- Ghost Layers for "Shows Behind" Effect -->
           <div class="absolute w-[520px] h-[600px] bg-white/[0.03] rounded-xl transform translate-x-8 translate-y-8 border border-white/5"></div>
           <div class="absolute w-[520px] h-[600px] bg-white/[0.02] rounded-xl transform translate-x-16 translate-y-16 border border-white/5"></div>
           
           <!-- Main Component -->
           <div class="w-[520px] relative z-20">
               <InboxStaticMock />
           </div>
       </div>
    </div>
  </div>
</template>

<script setup>
import InboxStaticMock from './mocks/InboxStaticMock.vue'
</script>
