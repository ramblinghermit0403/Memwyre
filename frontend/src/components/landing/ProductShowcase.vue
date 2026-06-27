<template>
  <div class="mb-10">
    <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-3">Product</h2>
    <p class="text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-tight text-balance">AI that works at your
      speed.</p>
    <p class="mt-3 text-base sm:text-lg text-text-secondary max-w-2xl text-balance">
      Capture context once. Reuse it infinitely. Keep your flow state unbroken across every tool.
    </p>
  </div>

  <!-- Showcase Cards Grid -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">

    <!-- Card 1: Inbox -->
    <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
      <!-- Content: icon + title + description -->
      <div class="p-6 pb-3">
        <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
          </svg>
        </div>
        <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Triage &amp; Flow</h3>
        <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">Triage incoming AI research and captures
          without breaking your deep work flow.</p>
      </div>
      <!-- Image: component visual -->
      <div class="relative flex-1 min-h-[380px] overflow-hidden">
        <div class="absolute pl-6 pr-6 inset-x-0 top-0 bottom-[-80px]">
          <div
            class="flex flex-col bg-white rounded-t-2xl shadow-xl border border-black/5 border-b-0 overflow-hidden h-full">
            <div class="p-5 border-b border-gray-100 flex justify-between items-center bg-[#F7F6F3]/80">
              <h3 class="text-base font-semibold text-gray-900">Incoming Items</h3>
              <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-green-400 animate-pulse"></span>
                <span class="text-xs text-gray-400 font-medium">Live</span>
              </div>
            </div>
            <div class="flex-1 p-4 space-y-3">
              <div class="p-4 rounded-xl border border-gray-200 bg-[#F7F6F3]/50">
                <h4 class="font-semibold text-gray-900 mb-2 text-sm leading-snug">ICSSR Priority Areas 2025-26
                  Overview</h4>
                <div class="flex justify-between items-end">
                  <div class="flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                      <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-5 h-5" />
                      <span class="text-xs text-gray-500 font-medium">perplexity</span>
                    </div>
                    <span
                      class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-semibold w-fit bg-orange-100 text-orange-700">Pending</span>
                  </div>
                  <span class="text-[10px] text-gray-400">Just now</span>
                </div>
              </div>
              <div class="p-4 rounded-xl border border-gray-200 bg-white">
                <h4 class="font-semibold text-gray-900 mb-2 text-sm leading-snug">Using OpenAI with Claude Code
                </h4>
                <div class="flex justify-between items-end">
                  <div class="flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                      <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-5 h-5" />
                      <span class="text-xs text-gray-500 font-medium">gemini</span>
                    </div>
                    <span
                      class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-semibold w-fit bg-orange-100 text-orange-700">Pending</span>
                  </div>
                  <span class="text-[10px] text-gray-400">5h ago</span>
                </div>
              </div>
              <div class="p-4 rounded-xl border border-gray-200 bg-white">
                <h4 class="font-semibold text-gray-900 mb-2 text-sm leading-snug">Memwyre Launches Universal AI
                  Memory</h4>
                <div class="flex justify-between items-end">
                  <div class="flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                      <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-5 h-5" />
                      <span class="text-xs text-gray-500 font-medium">openclaw</span>
                    </div>
                    <span
                      class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-semibold w-fit bg-green-100 text-green-700">Approved</span>
                  </div>
                  <span class="text-[10px] text-gray-400">8d ago</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none">
        </div>
      </div>
    </div>

    <!-- Card 2: Cross-Post to AI -->
    <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
      <!-- Content: icon + title + description -->
      <div class="p-6 pb-3">
        <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
          </svg>
        </div>
        <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Instant AI Handoff</h3>
        <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">Continue any conversation in another AI
          tool with full context. One click to hand off.</p>
      </div>
      <!-- Component visual: literal dropdown -->
      <div class="relative flex-1 min-h-[380px] overflow-hidden">
        <div class="absolute pl-6 pr-6 inset-x-0 top-0 bottom-[-80px]">
          <div class="flex flex-col rounded-t-2xl  overflow-hidden h-full items-center justify-start">
            <div class="relative w-full max-w-md rounded-xl border border-gray-200 bg-white shadow-lg z-20 p-3">
              <button
                class="w-full text-left text-base font-medium px-4 py-2 bg-gray-100 rounded-lg flex items-center gap-4">
                <img src="@/assets/openai.svg" alt="ChatGPT" class="w-8 h-8" />
                Continue in ChatGPT
              </button>
              <button
                class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                <img src="@/assets/claude-color.svg" alt="Claude" class="w-8 h-8" />
                Continue in Claude
              </button>
              <button
                class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-8 h-8" />
                Continue in Gemini
              </button>
              <button
                class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-8 h-8" />
                Continue in Perplexity
              </button>
              <button
                class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M8 16H7a2 2 0 01-2-2V5a2 2 0 012-2h9a2 2 0 012 2v1"></path>
                  <rect x="9" y="9" width="10" height="12" rx="2" ry="2" stroke-width="2"></rect>
                </svg>
                Copy Context
              </button>
            </div>
          </div>
        </div>
        <div
          class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none">
        </div>
      </div>
    </div>

    <!-- Card 3: Recent AI Work Timeline -->
    <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
      <!-- Content: icon + title + description -->
      <div class="p-6 pb-3">
        <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Compounding Knowledge</h3>
        <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">Never repeat yourself. Every prompt and
          insight becomes searchable, reusable leverage.</p>
      </div>
      <!-- Image: component visual -->
      <div class="relative flex-1 min-h-[380px] overflow-hidden">
        <div class="absolute pl-10 inset-x-0 top-0 bottom-[-80px]">
          <div
            class="flex flex-col bg-white rounded-t-2xl shadow-xl border border-black/5 border-b-0 overflow-hidden h-full">
            <div class="p-5 border-b border-gray-100 flex items-center justify-between bg-[#F7F6F3]/80">
              <div>
                <h3 class="text-base font-semibold text-gray-900">Recent Memories</h3>
                <p class="text-[11px] text-gray-400 mt-0.5">Your interaction timeline across memories.</p>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-xs border border-gray-200 rounded-md px-2.5 py-1 bg-white text-gray-600">All
                  Sources</span>
              </div>
            </div>
            <div class="relative p-5 space-y-5">
              <div class="space-y-3">
                <h4 class="text-[11px] uppercase tracking-wider text-gray-400 font-bold">Today</h4>
                <div class="border-t border-gray-100">
                  <div class="py-3.5 flex items-start gap-3">
                    <img src="@/assets/openai.svg" alt="ChatGPT" class="w-6 h-6 shrink-0 mt-0.5" />
                    <div class="min-w-0 flex-1">
                      <p class="text-sm font-semibold text-gray-900 truncate">Refining Memwyre Pitch Strategy</p>
                      <p class="text-[11px] text-gray-400 mt-0.5">ChatGPT · conversation · 11:25 AM</p>
                      <p class="text-xs text-gray-500 mt-1.5 line-clamp-2">Rating: 6.5/10 — Good instinct, clear
                        pain — but it's too explicit, a bit salesy...</p>
                      <span
                        class="inline-flex items-center mt-2 px-2 py-0.5 rounded text-[10px] font-medium bg-blue-50 text-blue-600 border border-blue-100">memwyre</span>
                    </div>
                    <div class="flex items-center gap-1.5 shrink-0">
                      <span
                        class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Open</span>
                      <span
                        class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Use
                        in AI ✨</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="space-y-3">
                <h4 class="text-[11px] uppercase tracking-wider text-gray-400 font-bold">Yesterday</h4>
                <div class="border-t border-gray-100 divide-y divide-gray-100">
                  <div class="py-3.5 flex items-start gap-3">
                    <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-6 h-6 shrink-0 mt-0.5" />
                    <div class="min-w-0 flex-1">
                      <p class="text-sm font-semibold text-gray-900 truncate">Open-source remote MCP clients
                        overview</p>
                      <p class="text-[11px] text-gray-400 mt-0.5">Perplexity · conversation · 01:24 PM</p>
                      <p class="text-xs text-gray-500 mt-1.5 line-clamp-2">Open-source remote MCP clients are
                        available on GitHub, enabling connections to remote MCP servers...</p>
                      <span
                        class="inline-flex items-center mt-2 px-2 py-0.5 rounded text-[10px] font-medium bg-blue-50 text-blue-600 border border-blue-100">memwyre</span>
                    </div>
                    <div class="flex items-center gap-1.5 shrink-0">
                      <span
                        class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Open</span>
                      <span
                        class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Use
                        in AI ✨</span>
                    </div>
                  </div>
                  <div class="py-3.5 flex items-start gap-3">
                    <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-6 h-6 shrink-0 mt-0.5" />
                    <div class="min-w-0 flex-1">
                      <p class="text-sm font-semibold text-gray-900 truncate">Piusi K600/3 Upgrade Guide</p>
                      <p class="text-[11px] text-gray-400 mt-0.5">Gemini · conversation · 09:57 PM</p>
                      <p class="text-xs text-gray-500 mt-1.5 line-clamp-2">The Piusi K600/3 is a significant
                        upgrade over the K24 because it uses Oval Gears instead of a turbine...</p>
                    </div>
                    <div class="flex items-center gap-1.5 shrink-0">
                      <span
                        class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Open</span>
                      <span
                        class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Use
                        in AI ✨</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none">
        </div>
      </div>
    </div>

    <!-- Card 4: Custom Permissions -->
    <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
      <!-- Content: icon + title + description -->
      <div class="p-6 pb-3">
        <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
        </div>
        <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Custom Permissions</h3>
        <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">You're in control of what each
          integration can see and do with your vault.</p>
      </div>
      <!-- Component visual: permissions list -->
      <div class="relative flex-1 min-h-[380px] overflow-hidden">
        <div class="absolute pl-6 pr-6 inset-x-0 top-0 bottom-[-80px]">
          <div class="flex flex-col overflow-hidden h-full">
            <div class="flex-1 space-y-1">
              <!-- Row 1: ChatGPT -->
              <div class="flex items-center justify-between py-2 px-1 rounded-xl">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                    <img src="@/assets/openai.svg" alt="ChatGPT" class="w-8 h-8" />
                  </div>
                  <span class="text-2xl font-bold text-gray-900">ChatGPT</span>
                </div>
                <span class="text-base text-gray-400 flex items-center gap-1">Can read &amp; write <svg
                    class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg></span>
              </div>
              <!-- Row 2: MCP (highlighted) -->
              <div class="flex items-center justify-between py-2 px-1 rounded-xl bg-[#F7F6F3]/60">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                    <svg class="w-8 h-8 text-primary" viewBox="0 0 180 180" fill="none"
                      xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M18 84.8528L85.8822 16.9706C95.2548 7.59798 110.451 7.59798 119.823 16.9706V16.9706C129.196 26.3431 129.196 41.5391 119.823 50.9117L68.5581 102.177"
                        stroke="currentColor" stroke-width="12" stroke-linecap="round" />
                      <path
                        d="M69.2652 101.47L119.823 50.9117C129.196 41.5391 144.392 41.5391 153.765 50.9117L154.118 51.2652C163.491 60.6378 163.491 75.8338 154.118 85.2063L92.7248 146.6C89.6006 149.724 89.6006 154.789 92.7248 157.913L105.331 170.52"
                        stroke="currentColor" stroke-width="12" stroke-linecap="round" />
                      <path
                        d="M102.853 33.9411L52.6482 84.1457C43.2756 93.5183 43.2756 108.714 52.6482 118.087V118.087C62.0208 127.459 77.2167 127.459 86.5893 118.087L136.794 67.8822"
                        stroke="currentColor" stroke-width="12" stroke-linecap="round" />
                    </svg>
                  </div>
                  <span class="text-2xl font-bold text-gray-900">MCP Server</span>
                </div>
                <span
                  class="text-lg text-gray-600 flex items-center gap-1 bg-white px-3 py-1.5 rounded-lg border border-gray-200 shadow-sm">Full
                  access <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg></span>
              </div>
              <!-- Row 3: Chrome -->
              <div class="flex items-center justify-between py-2 px-1 rounded-xl">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                    <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-8 h-8" />
                  </div>
                  <span class="text-2xl font-bold text-gray-900">Chrome</span>
                </div>
                <span class="text-base text-gray-400 flex items-center gap-1">Can write <svg class="w-4 h-4"
                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg></span>
              </div>
              <!-- Row 5: Notion -->
              <div class="flex items-center justify-between py-2 px-1 rounded-xl">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                    <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-8 h-8" />
                  </div>
                  <span class="text-2xl font-bold text-gray-900">Notion</span>
                </div>
                <span class="text-base text-gray-400 flex items-center gap-1">Can view <svg class="w-4 h-4"
                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg></span>
              </div>
            </div>
          </div>
        </div>
        <div
          class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none">
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
// No reactive state needed for this pure template component
</script>
