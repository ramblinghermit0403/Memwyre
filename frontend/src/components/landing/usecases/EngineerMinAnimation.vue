<script setup>
import { 
  BriefcaseIcon, 
  PlusIcon, 
  MagnifyingGlassIcon, 
  ChevronRightIcon 
} from '@heroicons/vue/24/outline';
</script>

<template>
  <div class="w-full group py-1">
    <div class="w-full bg-[#F7F6F3] rounded-[1.5rem] shadow-[0_8px_30px_rgb(0,0,0,0.06)] border border-gray-200 overflow-hidden transform group-hover:scale-[1.02] transition-transform duration-500">
      <!-- Item 1: memwyre + Toggle -->
      <div class="flex items-center justify-between px-3 py-2.5 hover:bg-gray-50/50 transition-colors">
        <div class="flex items-center gap-2">
          <div class="w-6 h-6 rounded-md border border-gray-300 flex items-center justify-center bg-[#F7F6F3] shadow-sm">
            <span class="text-[0.65rem] font-bold text-gray-500">M</span>
          </div>
          <span class="text-sm font-medium text-gray-900 tracking-tight">memwyre</span>
        </div>
        <!-- Toggle Switch -->
        <div class="w-9 h-5 bg-blue-600 rounded-full relative p-0.5 flex items-center shadow-inner">
          <div class="w-4 h-4 bg-[#F7F6F3] rounded-full shadow-sm ml-auto"></div>
        </div>
      </div>

      <!-- Item 2: Add from memwyre -->
      <div class="flex items-center justify-between px-3 py-2.5 hover:bg-gray-50/50 transition-colors">
        <div class="flex items-center gap-2">
          <div class="w-6 h-6 rounded-md border border-gray-300 flex items-center justify-center bg-[#F7F6F3] shadow-sm">
            <span class="text-[0.65rem] font-bold text-gray-500">M</span>
          </div>
          <span class="text-sm font-medium text-gray-900 tracking-tight">Add from memwyre</span>
        </div>
        <ChevronRightIcon class="w-3.5 h-3.5 text-gray-400 stroke-2" />
      </div>

      <!-- Separator -->
      <div class="h-px bg-gray-200 mx-3"></div>

      <!-- Item 3: Manage connectors -->
      <div class="flex items-center gap-2 px-3 py-2.5 hover:bg-gray-50/50 transition-colors">
        <BriefcaseIcon class="w-4.5 h-4.5 text-gray-800 flex-shrink-0" />
        <span class="text-sm font-medium text-gray-900 tracking-tight">Manage connectors</span>
      </div>

      <!-- Item 4: Add connector -->
      <div class="flex items-center gap-2 px-3 py-2.5 hover:bg-gray-50/50 transition-colors">
        <PlusIcon class="w-4.5 h-4.5 text-gray-800 flex-shrink-0" />
        <span class="text-sm font-medium text-gray-900 tracking-tight">Add connector</span>
      </div>

      <!-- Item 5: Tool access -->
      <div class="flex items-center justify-between px-3 py-2.5 hover:bg-gray-50/50 transition-colors">
        <div class="flex items-start gap-2">
          <MagnifyingGlassIcon class="w-4.5 h-4.5 text-gray-800 mt-0.5 flex-shrink-0" />
          <div class="flex flex-col">
            <span class="text-sm font-medium text-gray-900 tracking-tight">Tool access</span>
            <span class="text-[0.75rem] text-gray-500 leading-tight">Load tools when needed</span>
          </div>
        </div>
        <ChevronRightIcon class="w-3.5 h-3.5 text-gray-400 stroke-2" />
      </div>
    </div>
  </div>
</template>

<style scoped>
/* No additional styles needed as we use Tailwind */
</style>
