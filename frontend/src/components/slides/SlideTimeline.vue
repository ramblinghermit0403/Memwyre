<template>
  <div class="w-[1920px] h-[1080px] bg-[#1f1f23] overflow-hidden flex relative p-24 font-sans text-white">
    
    <!-- Top Left Brand -->
    <div class="absolute top-20 left-24 text-4xl font-medium text-gray-400 tracking-wide">
      memwyre.tech
    </div>

    <!-- Left Column: Marketing Copy -->
    <div class="w-[45%] h-full flex flex-col justify-start pt-32 pr-12 z-10 relative">
       <h1 class="text-[5rem] font-bold leading-[1.15] tracking-tight text-gray-100">
        Your memories,<br/>
        across LLMs<br/>
        <span class="text-[#D97757]">and web.</span>
       </h1>
    </div>

    <!-- Right Column: Product Showcase -->
    <div class="w-[55%] h-full relative">
       <div class="absolute inset-y-0 right-12 flex items-center justify-end transform translate-x-[-300px]">
           <TimelineStaticMock class="transform scale-[0.85] rotate-[-2deg] origin-right" />
       </div>
    </div>
  </div>
</template>

<script setup>
import TimelineStaticMock from './mocks/TimelineStaticMock.vue'
</script>
