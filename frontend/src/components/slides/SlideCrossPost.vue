<template>
  <div class="w-[1920px] h-[1080px] bg-[#1f1f23] overflow-hidden flex relative p-24 font-sans text-white">
    
    <!-- Top Left Brand -->
    <div class="absolute top-20 left-24 text-4xl font-medium text-gray-400 tracking-wide">
      memwyre.tech
    </div>

    <!-- Left Column: Marketing Copy -->
    <div class="w-[45%] h-full flex flex-col justify-start pt-32 pr-12 z-10 relative">
       <h1 class="text-[5rem] font-bold leading-[1.15] tracking-tight text-gray-100">
        Instant AI<br/>
        <span class="text-[#D97757]">Handoff.</span>
       </h1>
       <p class="mt-12 text-3xl text-gray-400 leading-relaxed max-w-[500px]">
        Continue any conversation in another AI tool with <span class="text-white font-semibold underline decoration-[#D97757] decoration-4 underline-offset-8">full context.</span> One click to hand off.
       </p>
    </div>

    <!-- Right Column: Product Showcase -->
    <div class="w-[55%] h-full relative">
         <div class="absolute inset-0 flex items-center justify-center transform translate-x-[-150px]">
            <CrossPostStaticMock class="transform scale-[1.26] rotate-2" />
        </div>
    </div>
  </div>
</template>

<script setup>
import CrossPostStaticMock from './mocks/CrossPostStaticMock.vue'
</script>
