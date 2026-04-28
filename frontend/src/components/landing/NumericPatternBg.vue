<template>
  <div class="absolute inset-0 overflow-hidden pointer-events-none opacity-[0.05] select-none">
    <div class="grid grid-cols-12 gap-2 p-4 text-[10px] font-mono leading-none break-all text-[#9575CD]">
      <div v-for="i in 400" :key="i" class="h-4 flex items-center justify-center">
        {{ Math.floor(Math.random() * 10) }}
      </div>
    </div>
  </div>
</template>

<script setup>
// Static numeric pattern for backgrounds
</script>
