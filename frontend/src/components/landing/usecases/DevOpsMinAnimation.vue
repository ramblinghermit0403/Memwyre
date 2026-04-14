<template>
  <div class="w-full group py-1">
    <div class="w-full bg-[#F7F6F3] rounded-[1.5rem] overflow-hidden shadow-xl border border-gray-200">

      <!-- Header bar -->
      <div class="flex items-center gap-2 px-4 py-3 border-b border-gray-200 bg-gray-100/50">
        <div class="flex gap-1.5">
          <span class="w-2.5 h-2.5 rounded-full bg-red-400"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-yellow-400"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-green-400"></span>
        </div>
        <span class="text-[10px] text-gray-400 font-mono ml-1">openclaw agent — run #47</span>
        <span class="ml-auto flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span>
          <span class="text-[9px] text-green-600 font-mono font-medium">running</span>
        </span>
      </div>

      <!-- Log lines -->
      <div class="p-4 font-mono text-[10px] space-y-2">

        <div class="flex items-start gap-2">
          <span class="text-gray-300 shrink-0">01</span>
          <span class="text-blue-600 font-medium">✦ agent.start</span>
          <span class="text-gray-300 ml-auto font-light">0ms</span>
        </div>

        <div class="flex items-start gap-2">
          <span class="text-gray-300 shrink-0">02</span>
          <span class="text-gray-600">memwyre.recall(</span>
          <span class="text-orange-600 truncate">"deploy config"</span>
          <span class="text-gray-600">)</span>
        </div>

        <div class="flex items-start gap-2 pl-5">
          <span class="text-green-500 font-bold">↳</span>
          <span class="text-gray-500 truncate">3 memories found</span>
          <span class="text-gray-300 ml-auto font-light">12ms</span>
        </div>

        <div class="flex items-start gap-2">
          <span class="text-gray-300 shrink-0">03</span>
          <span class="text-gray-600">memwyre.recall(</span>
          <span class="text-orange-600">"last run errors"</span>
          <span class="text-gray-600">)</span>
        </div>

        <div class="flex items-start gap-2 pl-5">
          <span class="text-green-500 font-bold">↳</span>
          <span class="text-gray-500">1 memory found</span>
          <span class="text-gray-300 ml-auto font-light">8ms</span>
        </div>

        <!-- Separator -->
        <div class="border-t border-gray-200 my-1"></div>

        <div class="flex items-start gap-2">
          <span class="text-gray-300 shrink-0">04</span>
          <span class="text-purple-600 font-medium">agent.task</span>
          <span class="text-gray-500 ml-1 truncate">→ running pipeline</span>
        </div>

        <div class="flex items-start gap-2">
          <span class="text-gray-300 shrink-0">05</span>
          <span class="text-gray-600">memwyre.save(</span>
          <span class="text-orange-600">"run #47 output"</span>
          <span class="text-gray-600">)</span>
        </div>

        <div class="flex items-start gap-2 pl-5">
          <span class="text-green-600 font-bold text-[12px]">✓</span>
          <span class="text-green-600 font-medium ml-1">memory saved</span>
          <span class="text-gray-300 ml-auto font-light">3ms</span>
        </div>

        <!-- Cursor blink -->
        <div class="flex items-center gap-2 pt-1 border-t border-gray-100 mt-1">
          <span class="text-gray-300">06</span>
          <span class="text-blue-500/80">agent.complete</span>
          <span class="inline-block w-1.5 h-3 bg-gray-400 ml-1 animate-pulse"></span>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
// No reactive state needed
</script>

<style scoped>
/* Light terminal aesthetic */
</style>
