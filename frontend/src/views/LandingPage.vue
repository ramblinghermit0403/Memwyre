<template>
    <div class="force-light relative min-h-screen bg-white text-text-primary transition-colors duration-300 font-sans overflow-x-hidden selection:bg-primary selection:text-white *:selection:bg-primary *:selection:text-white">

    <!-- Hero Video Background (hidden on mobile) -->
    <div class="hidden sm:block absolute -top-10 sm:-top-16 left-1/2 -translate-x-[38%] w-[120%] max-w-[1500px] lg:max-w-[1700px] h-[820px] z-0 pointer-events-none overflow-hidden opacity-40">
        <video 
            src="/hero.mp4" 
            autoplay 
            muted 
            playsinline
            class="w-full h-full object-cover video-blend"
        ></video>
    </div>

    <!-- Hero Section -->
    <div class="relative z-10 pt-28 sm:pt-32 lg:pt-40 pb-14 sm:pb-16">
      <div class="max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
        <div class="max-w-3xl">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-black/10 bg-white/70 backdrop-blur text-xs font-semibold text-text-secondary">
            <span class="inline-block w-1.5 h-1.5 rounded-full bg-primary"></span>
            Built for AI-heavy workflows
          </div>

          <h1 class="text-balance text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight leading-[1.04] text-text-primary mt-5">
            The universal inbox for all your AI work.
          </h1>
          <p class="text-balance text-base sm:text-lg md:text-xl text-text-secondary leading-relaxed mt-4">
            Capture prompts, conversations, and web context across tools—then reuse it anywhere. Your work compounds instead of disappearing.
          </p>

          <div class="mt-8 flex flex-col sm:flex-row gap-3">
            <router-link
              to="/signup"
              class="px-6 py-3 bg-primary text-white text-base font-semibold rounded-xl hover:bg-primary-600 transition-colors inline-flex items-center justify-center gap-2"
            >
              Get started
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
            </router-link>
            <a
              href="#features"
              class="px-6 py-3 border border-black/10 bg-white/60 text-text-primary text-base font-semibold rounded-xl hover:bg-black/[0.04] transition-colors inline-flex items-center justify-center"
            >
              See how it works
            </a>
          </div>

          <p class="mt-4 max-w-2xl text-sm text-text-secondary leading-relaxed">
            Explore
            <router-link to="/use-cases" class="text-primary hover:text-primary-600 font-semibold">real-world use cases</router-link>,
            review our
            <router-link to="/privacy-policy" class="text-primary hover:text-primary-600 font-semibold">privacy policy</router-link>
            and
            <router-link to="/terms" class="text-primary hover:text-primary-600 font-semibold">terms of service</router-link>.
            MemWyre is built around standards like
            <a href="https://modelcontextprotocol.io/introduction" target="_blank" rel="noopener noreferrer" class="text-primary hover:text-primary-600 font-semibold">Model Context Protocol</a>
            and official
            <a href="https://developer.chrome.com/docs/extensions" target="_blank" rel="noopener noreferrer" class="text-primary hover:text-primary-600 font-semibold">Chrome extension APIs</a>.
          </p>

          <div class="mt-10 pt-6 border-t border-black/5">
            <div class="text-xs font-semibold uppercase tracking-widest text-text-muted">Supported AI tools</div>
            <div class="mt-4 flex flex-wrap items-center gap-x-8 gap-y-4 text-sm text-text-muted">
              <span class="inline-flex items-center gap-3">
                <span class="inline-flex items-center justify-center w-14 h-14 rounded-lg bg-white/70 border border-black/10">
                  <img src="@/assets/openai.svg" alt="ChatGPT" class="w-10 h-10" />
                </span>
                ChatGPT
              </span>
              <span class="inline-flex items-center gap-3">
                <span class="inline-flex items-center justify-center w-14 h-14 rounded-lg bg-white/70 border border-black/10">
                  <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-10 h-10" />
                </span>
                Perplexity
              </span>
              <span class="inline-flex items-center gap-3">
                <span class="inline-flex items-center justify-center w-14 h-14 rounded-lg bg-white/70 border border-black/10">
                  <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-10 h-10" />
                </span>
                Chrome
              </span>
              <span class="inline-flex items-center gap-3">
                <span class="inline-flex items-center justify-center w-14 h-14 rounded-lg bg-white/70 border border-black/10">
                  <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-10 h-10" />
                </span>
                Notion
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Inbox Showcase -->
    <div id="features" class="py-16 sm:py-20">
      <div class="max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
        <div class="mb-10">
          <h2 class="text-xs font-semibold uppercase tracking-widest text-text-muted mb-3">Product</h2>
          <p class="text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-tight text-balance">AI that works at your speed.</p>
          <p class="mt-3 text-base sm:text-lg text-text-secondary max-w-2xl text-balance">
            Capture context once. Reuse it infinitely. Keep your flow state unbroken across every tool.
          </p>
        </div>

        <div class="mb-8 flex flex-wrap gap-2">
          <a href="#features" class="px-3 py-1.5 rounded-full text-sm font-semibold border border-black/10 bg-white/70 hover:bg-black/[0.04] transition-colors">Overview</a>
          <a href="#workflow" class="px-3 py-1.5 rounded-full text-sm font-semibold border border-black/10 bg-white/70 hover:bg-black/[0.04] transition-colors">Workflow</a>
          <a href="#ecosystem" class="px-3 py-1.5 rounded-full text-sm font-semibold border border-black/10 bg-white/70 hover:bg-black/[0.04] transition-colors">Ecosystem</a>
          <a href="#use-cases" class="px-3 py-1.5 rounded-full text-sm font-semibold border border-black/10 bg-white/70 hover:bg-black/[0.04] transition-colors">Use cases</a>
          <a href="#pricing" class="px-3 py-1.5 rounded-full text-sm font-semibold border border-black/10 bg-white/70 hover:bg-black/[0.04] transition-colors">Pricing</a>
          <a href="#faq" class="px-3 py-1.5 rounded-full text-sm font-semibold border border-black/10 bg-white/70 hover:bg-black/[0.04] transition-colors">FAQ</a>
        </div>

        <!-- Showcase Cards Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">

          <!-- Card 1: Inbox -->
          <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
            <!-- Content: icon + title + description -->
            <div class="p-6 pb-3">
              <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" /></svg>
              </div>
              <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Triage &amp; Flow</h3>
              <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">Triage incoming AI research and captures without breaking your deep work flow.</p>
            </div>
            <!-- Image: component visual -->
            <div class="relative flex-1 min-h-[380px] overflow-hidden">
              <div class="absolute pl-6 pr-6 inset-x-0 top-0 bottom-[-80px]">
                <div class="flex flex-col bg-white rounded-t-2xl shadow-xl border border-black/5 border-b-0 overflow-hidden h-full">
                  <div class="p-5 border-b border-gray-100 flex justify-between items-center bg-[#F7F6F3]/80">
                    <h3 class="text-base font-semibold text-gray-900">Incoming Items</h3>
                    <div class="flex items-center gap-1.5">
                      <span class="w-2.5 h-2.5 rounded-full bg-green-400 animate-pulse"></span>
                      <span class="text-xs text-gray-400 font-medium">Live</span>
                    </div>
                  </div>
                  <div class="flex-1 p-4 space-y-3">
                    <div class="p-4 rounded-xl border border-gray-200 bg-[#F7F6F3]/50">
                      <h4 class="font-semibold text-gray-900 mb-2 text-sm leading-snug">ICSSR Priority Areas 2025-26 Overview</h4>
                      <div class="flex justify-between items-end">
                        <div class="flex flex-col gap-2">
                          <div class="flex items-center gap-2">
                            <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-5 h-5" />
                            <span class="text-xs text-gray-500 font-medium">perplexity</span>
                          </div>
                          <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-semibold w-fit bg-orange-100 text-orange-700">Pending</span>
                        </div>
                        <span class="text-[10px] text-gray-400">Just now</span>
                      </div>
                    </div>
                    <div class="p-4 rounded-xl border border-gray-200 bg-white">
                      <h4 class="font-semibold text-gray-900 mb-2 text-sm leading-snug">Using OpenAI with Claude Code</h4>
                      <div class="flex justify-between items-end">
                        <div class="flex flex-col gap-2">
                          <div class="flex items-center gap-2">
                            <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-5 h-5" />
                            <span class="text-xs text-gray-500 font-medium">gemini</span>
                          </div>
                          <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-semibold w-fit bg-orange-100 text-orange-700">Pending</span>
                        </div>
                        <span class="text-[10px] text-gray-400">5h ago</span>
                      </div>
                    </div>
                    <div class="p-4 rounded-xl border border-gray-200 bg-white">
                      <h4 class="font-semibold text-gray-900 mb-2 text-sm leading-snug">MemWyre Launches Universal AI Memory</h4>
                      <div class="flex justify-between items-end">
                        <div class="flex flex-col gap-2">
                          <div class="flex items-center gap-2">
                            <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-5 h-5" />
                            <span class="text-xs text-gray-500 font-medium">openclaw</span>
                          </div>
                          <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-semibold w-fit bg-green-100 text-green-700">Approved</span>
                        </div>
                        <span class="text-[10px] text-gray-400">8d ago</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none"></div>
            </div>
          </div>

          <!-- Card 2: Cross-Post to AI -->
          <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
            <!-- Content: icon + title + description -->
            <div class="p-6 pb-3">
              <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" /></svg>
              </div>
              <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Instant AI Handoff</h3>
              <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">Continue any conversation in another AI tool with full context. One click to hand off.</p>
            </div>
            <!-- Component visual: literal dropdown -->
            <div class="relative flex-1 min-h-[380px] overflow-hidden">
              <div class="absolute pl-6 pr-6 inset-x-0 top-0 bottom-[-80px]">
                <div class="flex flex-col rounded-t-2xl  overflow-hidden h-full items-center justify-start">
                  <div class="relative w-full max-w-md rounded-xl border border-gray-200 bg-white shadow-lg z-20 p-3">
                    <button class="w-full text-left text-base font-medium px-4 py-2 bg-gray-100 rounded-lg flex items-center gap-4">
                      <img src="@/assets/openai.svg" alt="ChatGPT" class="w-8 h-8" />
                      Continue in ChatGPT
                    </button>
                    <button class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                      <img src="@/assets/claude-color.svg" alt="Claude" class="w-8 h-8" />
                      Continue in Claude
                    </button>
                    <button class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                      <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-8 h-8" />
                      Continue in Gemini
                    </button>
                    <button class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                      <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-8 h-8" />
                      Continue in Perplexity
                    </button>
                    <button class="w-full text-left text-base font-medium px-4 py-2 hover:bg-gray-100 rounded-lg flex items-center gap-4">
                      <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H7a2 2 0 01-2-2V5a2 2 0 012-2h9a2 2 0 012 2v1"></path><rect x="9" y="9" width="10" height="12" rx="2" ry="2" stroke-width="2"></rect></svg>
                      Copy Context
                    </button>
                  </div>
                </div>
              </div>
              <div class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none"></div>
            </div>
          </div>

          <!-- Card 3: Recent AI Work Timeline -->
          <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
            <!-- Content: icon + title + description -->
            <div class="p-6 pb-3">
              <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              </div>
              <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Compounding Knowledge</h3>
              <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">Never repeat yourself. Every prompt and insight becomes searchable, reusable leverage.</p>
            </div>
            <!-- Image: component visual -->
            <div class="relative flex-1 min-h-[380px] overflow-hidden">
              <div class="absolute pl-10 inset-x-0 top-0 bottom-[-80px]">
                <div class="flex flex-col bg-white rounded-t-2xl shadow-xl border border-black/5 border-b-0 overflow-hidden h-full">
                  <div class="p-5 border-b border-gray-100 flex items-center justify-between bg-[#F7F6F3]/80">
                    <div>
                      <h3 class="text-base font-semibold text-gray-900">Recent AI Work</h3>
                      <p class="text-[11px] text-gray-400 mt-0.5">Your interaction timeline across AI tools.</p>
                    </div>
                    <div class="flex items-center gap-2">
                      <span class="text-xs border border-gray-200 rounded-md px-2.5 py-1 bg-white text-gray-600">All Sources</span>
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
                            <p class="text-xs text-gray-500 mt-1.5 line-clamp-2">Rating: 6.5/10 — Good instinct, clear pain — but it's too explicit, a bit salesy...</p>
                            <span class="inline-flex items-center mt-2 px-2 py-0.5 rounded text-[10px] font-medium bg-blue-50 text-blue-600 border border-blue-100">memwyre</span>
                          </div>
                          <div class="flex items-center gap-1.5 shrink-0">
                            <span class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Open</span>
                            <span class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Use in AI ✨</span>
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
                            <p class="text-sm font-semibold text-gray-900 truncate">Open-source remote MCP clients overview</p>
                            <p class="text-[11px] text-gray-400 mt-0.5">Perplexity · conversation · 01:24 PM</p>
                            <p class="text-xs text-gray-500 mt-1.5 line-clamp-2">Open-source remote MCP clients are available on GitHub, enabling connections to remote MCP servers...</p>
                            <span class="inline-flex items-center mt-2 px-2 py-0.5 rounded text-[10px] font-medium bg-blue-50 text-blue-600 border border-blue-100">memwyre</span>
                          </div>
                          <div class="flex items-center gap-1.5 shrink-0">
                            <span class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Open</span>
                            <span class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Use in AI ✨</span>
                          </div>
                        </div>
                        <div class="py-3.5 flex items-start gap-3">
                          <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-6 h-6 shrink-0 mt-0.5" />
                          <div class="min-w-0 flex-1">
                            <p class="text-sm font-semibold text-gray-900 truncate">Piusi K600/3 Upgrade Guide</p>
                            <p class="text-[11px] text-gray-400 mt-0.5">Gemini · conversation · 09:57 PM</p>
                            <p class="text-xs text-gray-500 mt-1.5 line-clamp-2">The Piusi K600/3 is a significant upgrade over the K24 because it uses Oval Gears instead of a turbine...</p>
                          </div>
                          <div class="flex items-center gap-1.5 shrink-0">
                            <span class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Open</span>
                            <span class="text-[11px] px-2 py-1 rounded-md border border-gray-200 text-gray-500 bg-white">Use in AI ✨</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none"></div>
            </div>
          </div>

          <!-- Card 4: Custom Permissions -->
          <div class="bg-[#F7F6F3] rounded-2xl overflow-hidden flex flex-col border border-black/5 shadow-sm">
            <!-- Content: icon + title + description -->
            <div class="p-6 pb-3">
              <div class="w-10 h-10 flex items-center justify-left text-primary mb-1">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
              </div>
              <h3 class="text-lg sm:text-xl font-bold text-[#191919] tracking-tight mb-2">Custom Permissions</h3>
              <p class="text-sm sm:text-base text-[#191919]/60 leading-relaxed">You're in control of what each integration can see and do with your vault.</p>
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
                      <span class="text-base text-gray-400 flex items-center gap-1">Can read &amp; write <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg></span>
                    </div>
                    <!-- Row 2: MCP (highlighted) -->
                    <div class="flex items-center justify-between py-2 px-1 rounded-xl bg-[#F7F6F3]/60">
                      <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                          <svg class="w-8 h-8 text-primary" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M18 84.8528L85.8822 16.9706C95.2548 7.59798 110.451 7.59798 119.823 16.9706V16.9706C129.196 26.3431 129.196 41.5391 119.823 50.9117L68.5581 102.177" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                            <path d="M69.2652 101.47L119.823 50.9117C129.196 41.5391 144.392 41.5391 153.765 50.9117L154.118 51.2652C163.491 60.6378 163.491 75.8338 154.118 85.2063L92.7248 146.6C89.6006 149.724 89.6006 154.789 92.7248 157.913L105.331 170.52" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                            <path d="M102.853 33.9411L52.6482 84.1457C43.2756 93.5183 43.2756 108.714 52.6482 118.087V118.087C62.0208 127.459 77.2167 127.459 86.5893 118.087L136.794 67.8822" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                          </svg>
                        </div>
                        <span class="text-2xl font-bold text-gray-900">MCP Server</span>
                      </div>
                      <span class="text-lg text-gray-600 flex items-center gap-1 bg-white px-3 py-1.5 rounded-lg border border-gray-200 shadow-sm">Full access <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg></span>
                    </div>
                    <!-- Row 3: Chrome -->
                    <div class="flex items-center justify-between py-2 px-1 rounded-xl">
                      <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                          <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-8 h-8" />
                        </div>
                        <span class="text-2xl font-bold text-gray-900">Chrome</span>
                      </div>
                      <span class="text-base text-gray-400 flex items-center gap-1">Can write <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg></span>
                    </div>
                    <!-- Row 5: Notion -->
                    <div class="flex items-center justify-between py-2 px-1 rounded-xl">
                      <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-lg bg-white flex items-center justify-center">
                          <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-8 h-8" />
                        </div>
                        <span class="text-2xl font-bold text-gray-900">Notion</span>
                      </div>
                      <span class="text-base text-gray-400 flex items-center gap-1">Can view <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg></span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[var(--bg-surface-2)] to-transparent z-10 pointer-events-none"></div>
            </div>
          </div>

        </div>

        <!-- Video Demos -->
        <div class="space-y-32 mt-32">

          <!-- Video 1 -->
          <div>
            <div class="mb-6">
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">Cross-Post Context Instantly</h3>
              <p class="text-base text-gray-500 mt-2 max-w-xl">Find the exact reference you need and launch it directly into your preferred AI model.</p>
            </div>
            <div class="rounded-2xl overflow-hidden" style="background-color: #fef3e2;">
              <div class="p-4 sm:p-6 md:p-10">
                <div class="rounded-2xl overflow-hidden shadow-xl">
                  <video
                    ref="demoVideo1"
                    src="/demo_1_memwyre.mp4"
                    muted
                    loop
                    playsinline
                    class="w-full object-cover scale-[1.12]"
                    style="aspect-ratio: 16/9;"
                  ></video>
                </div>
              </div>
            </div>
          </div>

          <!-- Video 2 -->
          <div>
            <div class="mb-6">
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">Granular Memory Control</h3>
              <p class="text-base text-gray-500 mt-2 max-w-xl">Review, edit, and curate your memories before they are saved to your vault.</p>
            </div>
            <div class="rounded-2xl overflow-hidden" style="background-color: #dbeafe;">
              <div class="p-4 sm:p-6 md:p-10">
                <div class="rounded-2xl overflow-hidden shadow-xl">
                  <video
                    ref="demoVideo2"
                    src="/demo_2_memwyre.mp4"
                    muted
                    loop
                    playsinline
                    class="w-full object-cover scale-[1.12]"
                    style="aspect-ratio: 16/9;"
                  ></video>
                </div>
              </div>
            </div>
          </div>

          <!-- Chat Demo -->
          <div>
            <div class="mb-6">
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">Contextual Chat Interface</h3>
              <p class="text-base text-gray-500 mt-2 max-w-xl">Ask questions grounded in your personal knowledge base — with sources cited inline.</p>
            </div>
            <div class="rounded-2xl overflow-hidden" style="background-color: #f0fdf4;">
              <div class="p-4 sm:p-6 md:p-10">
                <ChatDemo />
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- Workflow Section -->
     <div id="workflow" class="py-16 sm:py-20">
      <div class="max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
        <div class="mb-16">
          <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Workflow</h2>
          <p class="font-display text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight text-balance">Structured for flow.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-12">
                <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200">01</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Ingestion via Browser/MCP</h3>
                        <p class="text-text-secondary">Capture the web as you browse or connect directly from your IDE using our Model Context Protocol.</p>
                    </div>
                </div>
                 <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200">02</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Context Organization</h3>
                        <p class="text-text-secondary">AI automatically parses, tags, and stores your documents, notes, and links, building your central brain.</p>
                    </div>
                </div>
                 <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200">03</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Seamless AI Chat</h3>
                        <p class="text-text-secondary">Retrieve context naturally through our UI or via your own local LLMs configured with your MemWyre MCP.</p>
                    </div>
                </div>
            </div>
            
            <div class="relative group">
                <div class="absolute -inset-1 bg-gradient-to-r from-primary/30 to-primary/10 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
                <div class="relative bg-surface border border-primary/10 rounded-2xl p-8 shadow-2xl">
                    <div class="font-mono text-sm space-y-4">
                        <div class="flex items-center gap-2 border-b border-primary/10 pb-4 mb-4">
                            <span class="w-3 h-3 rounded-full bg-primary"></span>
                            <span class="text-text-muted">Ask MemWyre</span>
                        </div>
                        <p class="text-gray-800 min-h-[50px]">
                            {{ typedText }}<span class="cursor">&nbsp;</span>
                        </p>
                        <transition name="fade">
                            <div v-if="typedText.length >= 20" class="transition-opacity duration-1000 ease-in-out">
                                <br>
                                <span class="text-text-muted">Searching 3 documents...</span><br>
                                <span class="text-primary">Found matches in "Auth Specs v2" and "API Docs".</span><br><br>
                                Based on "Auth Specs v2", you should use the OAuth2 provider pattern. Here is the implementation snippet...
                            </div>
                        </transition>
                    </div>
                </div>
            </div>
        </div>
      </div>
     </div>

    <!-- Ecosystem -->
    <div id="ecosystem" class="py-16 sm:py-20 max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
        <div class="max-w-3xl mb-16">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Ecosystem</h2>
             <p class="font-display text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-6 text-balance">Built to extend.</p>
             <p class="text-lg md:text-xl text-text-secondary">MemWyre isn't a silo. It powers your entire workflow through standard protocols.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
             <div class="p-10 bg-[#F7F6F3] rounded-2xl hover:shadow-lg transition-all duration-300">
                 <div class="w-12 h-12 bg-primary text-white rounded-lg flex items-center justify-center mb-6">
                     <svg class="w-8 h-8" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 84.8528L85.8822 16.9706C95.2548 7.59798 110.451 7.59798 119.823 16.9706V16.9706C129.196 26.3431 129.196 41.5391 119.823 50.9117L68.5581 102.177" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                        <path d="M69.2652 101.47L119.823 50.9117C129.196 41.5391 144.392 41.5391 153.765 50.9117L154.118 51.2652C163.491 60.6378 163.491 75.8338 154.118 85.2063L92.7248 146.6C89.6006 149.724 89.6006 154.789 92.7248 157.913L105.331 170.52" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                        <path d="M102.853 33.9411L52.6482 84.1457C43.2756 93.5183 43.2756 108.714 52.6482 118.087V118.087C62.0208 127.459 77.2167 127.459 86.5893 118.087L136.794 67.8822" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                     </svg>
                 </div>
                 <h3 class="text-2xl font-bold mb-4">MCP Server</h3>
                 <p class="text-text-secondary mb-8">
                     Connect MemWyre directly to Claude Desktop or any MCP-compliant client. Give your AI assistant direct access to your knowledge base.
                 </p>
                 <div class="bg-surface-2 rounded-lg p-4 font-mono text-xs text-text-secondary">
                     $ npx -y @memwyre/mcp-server
                 </div>
             </div>

             <div class="p-10 bg-[#F7F6F3] rounded-2xl hover:shadow-lg transition-all duration-300">
                 <div class="w-12 h-12 bg-primary text-white rounded-lg flex items-center justify-center mb-6 font-bold text-xl">
                      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>
                 </div>
                 <h3 class="text-2xl font-bold mb-4">Browser Extension</h3>
                 <p class="text-text-secondary mb-8">
                     Capture the web as you browse. Save articles, documentation, or code snippets instantly without breaking your flow.
                 </p>
                 <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-primary/10 text-primary text-sm font-bold">
                     <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-4 h-4" />
                     <img src="@/assets/microsoft-edge-logo.svg" alt="Edge" class="w-4 h-4" />
                     <span>Chrome &amp; Edge</span>
                 </div>
             </div>

             <div class="p-10 bg-[#F7F6F3] rounded-2xl hover:shadow-lg transition-all duration-300">
                 <div class="w-12 h-12 bg-primary text-white rounded-lg flex items-center justify-center mb-6">
                     <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-8 h-8 invert brightness-0 contrast-200" />
                 </div>
                 <h3 class="text-2xl font-bold mb-4">OpenClaw Plugin</h3>
                 <p class="text-text-secondary mb-8">
                     Give autonomous agents persistent memory. The OpenClaw plugin lets AI agents save and recall context from your vault automatically.
                 </p>
                 <div class="bg-surface-2 rounded-lg p-4 font-mono text-xs text-text-secondary">
                     $ openclaw plugins install @memwyre/openclaw
                 </div>
             </div>
        </div>
    </div>

    <!-- Pricing Section -->
    <div id="pricing" class="py-16 sm:py-20">
        <div class="max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
            <div class="text-center mb-16">
                 <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Pricing</h2>
                 <p class="font-display text-4xl font-extrabold tracking-tight text-balance">AI that works where your team works.</p>
            </div>

            <div class="max-w-md mx-auto">
                <!-- Pro (Recommended) -->
                <div class="rounded-2xl bg-[#F7F6F3] border border-black/5 p-8 sm:p-10 relative">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="text-lg font-semibold">Pro</div>
                        <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-blue-100 text-blue-700">
                            Recommended
                        </span>
                    </div>
                    <div class="flex items-end gap-2 mb-3">
                        <div class="text-4xl font-extrabold tracking-tight">$12</div>
                        <div class="text-sm text-text-muted mb-1">per member/month</div>
                    </div>
                    <p class="text-text-secondary mb-6">For growing teams to streamline teamwork with persistent AI context.</p>

                    <router-link to="/signup" class="inline-flex w-full items-center justify-center rounded-xl bg-primary text-white px-4 py-3 text-sm font-semibold hover:bg-primary-600 transition-colors">
                        Get started
                    </router-link>

                    <div class="mt-6 flex flex-wrap items-center gap-2">
                        <span class="text-xs font-semibold uppercase tracking-widest text-text-muted mr-2">Integrations</span>
                        <img src="@/assets/openai.svg" alt="ChatGPT" class="w-5 h-5" />
                        <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-5 h-5" />
                        <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-5 h-5" />
                        <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-5 h-5" />
                        <img src="/image.svg" alt="MemWyre" class="w-5 h-5 rounded" />
                    </div>

                    <!-- <div class="mt-8 text-sm font-semibold">Everything in Free, plus:</div> -->
                    <ul class="mt-4 space-y-3 text-sm text-text-secondary">
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            1M+ token storage
                        </li>
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            100K daily AI token budget
                        </li>
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            PDF &amp; web page ingestion <span class="text-xs text-text-muted">(YouTube coming soon)</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            <div class="flex flex-wrap items-center gap-2">
                              <span>MCP Server for IDE integration</span>
                              <span class="inline-flex items-center gap-1.5 ml-1">
                                <span class="inline-flex items-center justify-center w-6 h-6 rounded-md bg-white/70 border border-black/10" title="VS Code">
                                  <svg class="w-4 h-4" viewBox="0 0 256 254" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                    <path fill="#007ACC" d="M246.201 33.592 196.63 9.915a19.547 19.547 0 0 0-21.58 3.41L78.94 101.334 40.746 72.36a13.02 13.02 0 0 0-16.69 1.025L4.022 91.46a13.02 13.02 0 0 0-.17 19.365l30.96 30.01-30.96 30.01a13.02 13.02 0 0 0 .17 19.365l20.034 18.074a13.02 13.02 0 0 0 16.69 1.025l38.194-28.974 96.11 88.009a19.547 19.547 0 0 0 21.58 3.41l49.571-23.677A19.547 19.547 0 0 0 256 225.513V55.671a19.547 19.547 0 0 0-9.799-22.079zM196.923 188.82l-73.09-60.33 73.09-60.33z"/>
                                  </svg>
                                </span>
                                <span class="inline-flex items-center justify-center px-2 h-6 rounded-md bg-white/70 border border-black/10 text-xs font-semibold text-text-muted" title="Cursor">
                                  Cursor
                                </span>
                              </span>
                            </div>
                        </li>
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            Browser Extension (Chrome &amp; Edge)
                        </li>
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            OpenClaw agent plugin access
                        </li>
                        <li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-text-muted shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            Priority support
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>


    <!-- Use Cases Hero Section -->
    <div class="py-16 sm:py-20 max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-8">
                <h2 class="text-base font-bold uppercase tracking-widest text-text-muted mb-4">Why MemWyre</h2>
                <p class="font-display text-balance text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black tracking-tighter leading-[1.08]">
                    Your AI work scatters.<br>
                    <span class="text-primary">MemWyre compounds it.</span>
                </p>
                <p class="text-xl sm:text-2xl text-text-secondary leading-relaxed max-w-xl text-balance">
                    MemWyre helps you capture everything you do with AI—research, code, decisions—and turns it into persistent, accessible knowledge tailored to your workflow.
                </p>
            </div>
            
            <!-- Visual Diagram -->
            <div class="relative min-h-[400px] md:min-h-[500px] w-full max-w-xl mx-auto flex items-center justify-center p-4 md:p-10 overflow-visible group">
                <!-- Ambient Glow -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 md:w-80 h-64 md:h-80 bg-primary/15 rounded-full blur-[100px] opacity-60 group-hover:opacity-100 transition-opacity duration-1000"></div>

                <!-- SVG Connection Lines + Traveling Dots -->
                <svg class="absolute inset-0 w-full h-full z-0 pointer-events-none" viewBox="0 0 500 500" fill="none">
                    <line x1="250" y1="45" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="340" y1="170" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="460" y1="250" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="340" y1="330" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="250" y1="450" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="160" y1="330" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="40" y1="250" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="160" y1="170" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />

                    <!-- Trailing dots -->
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="0s" path="M250,45 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="0.4s" path="M340,170 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0.4s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="0.8s" path="M460,250 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0.8s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="1.2s" path="M340,330 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="1.2s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="1.6s" path="M250,450 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="1.6s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="2.0s" path="M160,330 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.0s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="2.4s" path="M40,250 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.4s" />
                    </circle>
                     <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="2.8s" path="M160,170 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.8s" />
                    </circle>
                </svg>
                
                <!-- Central Node: Memwyre -->
                <div class="relative z-10 flex flex-col items-center justify-center transform group-hover:scale-105 transition-all duration-500">
                    <img src="/image.svg" alt="MemWyre" class="w-16 h-16 md:w-20 md:h-20 mb-3" />
                    <span class="text-base md:text-lg font-bold tracking-tight text-text-primary">MemWyre</span>
                </div>

                <!-- Icons: 8 total distributed radially, alternating FAR/CLOSE -->
                
                <!-- 1. Top FAR -->
                <div class="absolute top-[3%] left-1/2 -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1">
                    <img src="@/assets/claude-color.svg" alt="Claude" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">Claude</div>
                </div>
                <!-- 2. Top Right CLOSE -->
                <div class="absolute top-[28%] left-[68%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-2" style="animation-delay: 0.3s;">
                    <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">Gemini</div>
                </div>
                <!-- 3. Right FAR -->
                <div class="absolute top-[44%] left-[92%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-3" style="animation-delay: 0.6s;">
                    <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">Chrome</div>
                </div>
                <!-- 4. Bottom Right CLOSE -->
                <div class="absolute top-[60%] left-[68%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1" style="animation-delay: 0.9s;">
                    <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">Perplexity</div>
                </div>
                <!-- 5. Bottom FAR -->
                <div class="absolute top-[84%] left-1/2 -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-2" style="animation-delay: 1.2s;">
                    <img src="@/assets/openai.svg" alt="ChatGPT" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">ChatGPT</div>
                </div>
                <!-- 6. Bottom Left CLOSE -->
                <div class="absolute top-[60%] left-[32%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-3" style="animation-delay: 1.5s;">
                    <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">Notion</div>
                </div>
                <!-- 7. Left FAR -->
                <div class="absolute top-[44%] left-[8%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1" style="animation-delay: 1.8s;">
                    <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">OpenClaw</div>
                </div>
                <!-- 8. Top Left CLOSE -->
                <div class="absolute top-[28%] left-[32%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-2" style="animation-delay: 2.1s;">
                    <img src="@/assets/Google-Antigravity-Icon-Full-Color.png" alt="Antigravity" class="w-10 h-10 md:w-14 md:h-14" />
                    <div class="text-xs md:text-sm font-bold">Antigravity</div>
                </div>
            </div>
        </div>
    </div>

    <!-- The Disconnect -->
    <div class="py-16 sm:py-20">
        <div class="max-w-4xl mx-auto px-10 sm:px-16 lg:px-28 text-center">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-8">The Disconnect</h2>
             <blockquote class="text-3xl sm:text-4xl md:text-5xl font-bold leading-tight mb-16">
                “AI is everywhere in our workflow — <span class="bg-primary text-white px-2">but none of it sticks.</span>”
            </blockquote>
             
             <!-- <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left">
                 <div class="p-6 bg-[#F7F6F3] rounded-2xl hover:shadow-md transition-all duration-300">
                     <div class="flex items-start gap-4">
                         <div class="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                             <svg class="w-5 h-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                         </div>
                         <div>
                             <div class="font-bold text-lg mb-1 text-text-primary">Ephemeral Interactions</div>
                             <p class="text-text-secondary leading-relaxed text-sm">You use AI across dozens of tools, but those valuable sessions vanish the moment tabs close.</p>
                         </div>
                     </div>
                 </div>
                 <div class="p-6 bg-[#F7F6F3] rounded-2xl hover:shadow-md transition-all duration-300">
                     <div class="flex items-start gap-4">
                         <div class="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                             <svg class="w-5 h-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                         </div>
                         <div>
                             <div class="font-bold text-lg mb-1 text-text-primary">Locked Insights</div>
                             <p class="text-text-secondary leading-relaxed text-sm">Crucial context, code snippets, and structured parameters live trapped inside isolated chat logs.</p>
                         </div>
                     </div>
                 </div>
                 <div class="p-6 bg-[#F7F6F3] rounded-2xl hover:shadow-md transition-all duration-300">
                     <div class="flex items-start gap-4">
                         <div class="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                             <svg class="w-5 h-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
                         </div>
                         <div>
                             <div class="font-bold text-lg mb-1 text-text-primary">Context Reset</div>
                             <p class="text-text-secondary leading-relaxed text-sm">After a weekend away, the reasoning behind prior complex AI outputs is gone. You start from zero.</p>
                         </div>
                     </div>
                 </div>
                 <div class="p-6 bg-[#F7F6F3] rounded-2xl hover:shadow-md transition-all duration-300">
                     <div class="flex items-start gap-4">
                         <div class="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                             <svg class="w-5 h-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" /></svg>
                         </div>
                         <div>
                             <div class="font-bold text-lg mb-1 text-text-primary">Redundant Work</div>
                             <p class="text-text-secondary leading-relaxed text-sm">You repeat the same research and re-prompt the same patterns again and again, wasting time.</p>
                         </div>
                     </div>
                 </div>
             </div> -->
        </div>
    </div>

    <!-- Use Cases Section -->
    <div id="use-cases" class="py-16 sm:py-20 max-w-7xl mx-auto px-10 sm:px-16 lg:px-28">
        <div class="text-center mb-16">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Use Cases</h2>
             <p class="font-display text-4xl lg:text-5xl font-extrabold tracking-tight mb-6 text-balance">Designed for how you work</p>
             <p class="text-xl text-text-secondary max-w-2xl mx-auto text-balance">
                 Memwyre isn't just a note app. It's a cognitive bridging tool built for the specific ways different professionals leverage AI.
             </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            
            <!-- Use Case 1: Software Engineers -->
            <div class="p-10 bg-[#F7F6F3] rounded-2xl flex flex-col hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center text-primary border border-primary/15 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Software Engineers</h3>
                </div>
                <div class="space-y-6 flex-grow">
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary mb-2">The Problem</h4>
                        <p class="text-text-secondary">Losing the context of deep debugging sessions, complex architectural choices made with AI, and scattered, hard-won code snippets.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary/70 mb-2">Memwyre Solution</h4>
                        <p class="text-text-primary font-medium">Connect your IDE directly via MCP.</p>
                        <p class="text-text-secondary mt-1">Past bug fixes, API specs, and AI chats become instantly searchable context for your next coding session, right inside Cursor or VS Code.</p>
                    </div>
                </div>
            </div>

            <!-- Use Case 2: Researchers & Analysts -->
            <div class="p-10 bg-[#F7F6F3] rounded-2xl flex flex-col hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center text-primary border border-primary/15 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Researchers & Analysts</h3>
                </div>
                <div class="space-y-6 flex-grow">
                     <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary mb-2">The Problem</h4>
                        <p class="text-text-secondary">Drowning in open tabs, PDFs, and disjointed articles. Key insights and thematic connections are easily lost or siloed across tools.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary/70 mb-2">Memwyre Solution</h4>
                        <p class="text-text-primary font-medium">Instantly capture and synthesize.</p>
                        <p class="text-text-secondary mt-1">The Browser Extension grabs highlights while Unified Ingestion parses PDFs. Use conversational chat to synthesize findings across a massive, private body of research.</p>
                    </div>
                </div>
            </div>

             <!-- Use Case 3: Product Managers -->
            <div class="p-10 bg-[#F7F6F3] rounded-2xl flex flex-col hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center text-primary border border-primary/15 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Product Managers</h3>
                </div>
                <div class="space-y-6 flex-grow">
                     <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary mb-2">The Problem</h4>
                        <p class="text-text-secondary">Competitor research, user feedback analysis, and feature brainstorming are scattered across various docs and ephemeral AI chat histories.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary/70 mb-2">Memwyre Solution</h4>
                        <p class="text-text-primary font-medium">A unified signal inbox.</p>
                        <p class="text-text-secondary mt-1">Gather market signals and parse user feedback documents centrally. Query your knowledge base to rapidly draft PRDs and business cases grounded in existing, tracked research.</p>
                    </div>
                </div>
            </div>

             <!-- Use Case 4: Students & Learners -->
            <div class="p-10 bg-[#F7F6F3] rounded-2xl flex flex-col hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center text-primary border border-primary/15 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Students & Learners</h3>
                </div>
                <div class="space-y-6 flex-grow">
                     <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary mb-2">The Problem</h4>
                        <p class="text-text-secondary">Forgetting the precise details of long tutorials, complex research papers, and online courses shortly after consuming them.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary/70 mb-2">Memwyre Solution</h4>
                        <p class="text-text-primary font-medium">Active recall on demand.</p>
                        <p class="text-text-secondary mt-1">Ingest course materials and research papers. Use conversational chat to actively test your knowledge or ask highly specific follow-up questions months later. YouTube transcript ingestion coming soon.</p>
                    </div>
                </div>
            </div>

            <!-- Use Case 5: DevOps & Automation Engineers (OpenClaw) -->
            <div class="p-10 bg-[#F7F6F3] rounded-2xl flex flex-col hover:shadow-lg transition-all duration-300 lg:col-span-2">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center border border-primary/15 shadow-sm">
                        <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-8 h-8" />
                    </div>
                    <h3 class="text-2xl font-bold">DevOps & Automation Engineers</h3>
                </div>
                <div class="space-y-6 flex-grow">
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary mb-2">The Problem</h4>
                        <p class="text-text-secondary">Autonomous agents run complex multi-step tasks but have no persistent memory between runs. Each invocation starts cold — previous decisions, debug logs, and deployment context are lost.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary/70 mb-2">Memwyre + OpenClaw Solution</h4>
                        <p class="text-text-primary font-medium">Persistent memory for autonomous agents.</p>
                        <p class="text-text-secondary mt-1">The <strong>@memwyre/openclaw-plugin</strong> gives OpenClaw agents first-class tools to save notes and retrieve context from your vault. Agents remember past runs, build on previous debugging sessions, and accumulate operational knowledge over time.</p>
                    </div>
                </div>
            </div>

        </div>
    </div>



    <!-- Bottom Line -->
    <div class="py-16 sm:py-20">
         <div class="max-w-5xl mx-auto px-10 sm:px-16 lg:px-28 text-center">
            <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Results</h2>
            <p class="font-display text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-12 text-balance">The bottom line</p>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-16">
                <div>
                     <div class="text-2xl font-bold mb-2">Faster</div>
                     <div class="text-sm text-text-muted">Context Switching</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Fewer</div>
                     <div class="text-sm text-text-muted">Repeated Prompts</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Stronger</div>
                     <div class="text-sm text-text-muted">Knowledge Retrieval</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Lasting</div>
                     <div class="text-sm text-text-muted">Personal Memory</div>
                </div>
            </div>
            <div class="inline-block p-6 border border-primary/20 rounded-2xl bg-surface shadow-sm text-lg font-medium text-text-secondary max-w-2xl">
                Memwyre turns your disjointed AI tool usage into an organized, compounding knowledge asset.
            </div>
         </div>
    </div>

    <!-- FAQ Section -->
    <div id="faq" class="py-16 sm:py-24 max-w-3xl mx-auto px-6 sm:px-10 lg:px-0">
        <div class="mb-6 text-left">
             <h2 class="font-display text-3xl sm:text-4xl font-bold tracking-tight text-gray-900">Questions & answers</h2>
        </div>

        <div class="border-t border-black/5">
            <div v-for="(faq, index) in faqs" :key="index" class="border-b border-black/5">
                <button @click="toggleFaq(index)" class="flex justify-between items-center w-full text-left py-5 group">
                    <span class="text-[15px] font-semibold text-gray-900 group-hover:text-gray-600 transition-colors">{{ faq.question }}</span>
                    <span class="ml-4 flex-shrink-0 text-gray-400 font-light text-2xl leading-none">
                        <span v-if="faq.isOpen">&minus;</span>
                        <span v-else>+</span>
                    </span>
                </button>
                <div v-show="faq.isOpen" class="text-text-secondary pb-6 leading-relaxed text-[15px] pr-8">
                    {{ faq.answer }}
                </div>
            </div>
        </div>
    </div>


  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import ChatDemo from '@/components/landing/ChatDemo.vue';


// --- Video scroll-triggered playback ---
const demoVideo1 = ref(null);
const demoVideo2 = ref(null);
let videoObserver = null;
let shouldRestoreDarkClass = false;

const setupVideoObserver = () => {
  videoObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const video = entry.target;
        if (entry.isIntersecting) {
          video.play().catch(() => {});
        } else {
          video.pause();
        }
      });
    },
    { threshold: 0.3 }
  );

  if (demoVideo1.value) videoObserver.observe(demoVideo1.value);
  if (demoVideo2.value) videoObserver.observe(demoVideo2.value);
};

onUnmounted(() => {
  if (videoObserver) videoObserver.disconnect();
  document.documentElement.style.colorScheme = '';
  if (shouldRestoreDarkClass) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
});

const faqs = ref([
    {
        question: "What exactly is MemWyre?",
        answer: "MemWyre is a unified AI memory vault that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It then makes this knowledge instantly searchable and reusable.",
        isOpen: false
    },
    {
        question: "How do I connect MemWyre to Cursor or VS Code?",
        answer: "You can connect MemWyre to Cursor, VS Code, or Claude Desktop using our official Model Context Protocol (MCP) server. This gives your AI assistant direct, real-time access to your entire personal knowledge base.",
        isOpen: false
    },
    {
        question: "Do you offer a browser extension?",
        answer: "Yes! The MemWyre browser extension (coming soon for Chrome and Edge) lets you instantly clip text, articles, and code snippets directly into your vault without breaking your flow.",
        isOpen: false
    },
     {
        question: "Is my data private and secure?",
        answer: "Absolutely. Your memory vault is fully private and encrypted. Your data is only accessible to you via authenticated sessions and your personal API keys.",
        isOpen: false
    },
    {
        question: "What is the OpenClaw plugin?",
        answer: "The OpenClaw plugin allows autonomous AI agents to read from and write to your MemWyre vault. This gives agents persistent memory across runs, letting them build on past debugging sessions and research.",
        isOpen: false
    }
]);

const toggleFaq = (index) => {
    faqs.value[index].isOpen = !faqs.value[index].isOpen;
};

// --- Animations ---
onMounted(() => {
    shouldRestoreDarkClass = document.documentElement.classList.contains('dark');
    document.documentElement.classList.remove('dark');
    document.documentElement.style.colorScheme = 'light';
    typeWriter();
    setupVideoObserver();
});


// 2. Typing Effect
const typedText = ref('');
const fullText = "> How do I implement the new auth flow?";
const typingSpeed = 50;

const typeWriter = () => {
    let i = 0;
    typedText.value = ''; // Reset
    
    const type = () => {
        if (i < fullText.length) {
            typedText.value += fullText.charAt(i);
            i++;
            setTimeout(type, typingSpeed);
        } else {
             // Optional: Loop animation after a delay
             setTimeout(() => {
                 typedText.value = '> ';
                 i = 2; 
                 type();
             }, 5000);
        }
    };
    
    // Initial delay before starting
    setTimeout(type, 1000); 
};

</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

/* Force light mode — override dark theme CSS variables */
.force-light,
.force-light * {
  --bg-app: #FAF6F0;
  --bg-surface: #FFFFFF;
  --bg-surface-2: #F7F6F3;
  --bg-elevated: #FFFFFF;
  --primary: #D97757;
  --primary-600: #C4654A;
  --accent: #D97757;
  --accent-600: #C4654A;
  --success: #059669;
  --warning: #D97706;
  --danger: #DC2626;
  --info: #D97757;
  --text-primary: #191919;
  --text-secondary: #37352F99;
  --text-muted: #37352F66;
  --border: rgba(25, 25, 25, 0.06);
  --divider-strong: rgba(25, 25, 25, 0.09);
  --backdrop: rgba(0, 0, 0, 0.4);
  --input-bg: #FFFFFF;
  --input-border: rgba(25, 25, 25, 0.08);
  --placeholder: #37352F66;
  color-scheme: light;
}

/* Typing Cursor */
.cursor {
    display: inline-block;
    width: 8px;
    background-color: currentColor;
    animation: blink 1s step-end infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

/* Video edge feathering via CSS mask — no overlays needed */
.video-blend {
    -webkit-mask-image:
        linear-gradient(to right, transparent 0%, black 40%),
        linear-gradient(to top, transparent 0%, black 40%),
        linear-gradient(to bottom, transparent 0%, black 15%);
    -webkit-mask-composite: destination-in;
    mask-image:
        linear-gradient(to right, transparent 0%, black 40%),
        linear-gradient(to top, transparent 0%, black 40%),
        linear-gradient(to bottom, transparent 0%, black 15%);
    mask-composite: intersect;
}

/* Floating icon animations */
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.animate-float-1 { animation: float 4s ease-in-out infinite; }
.animate-float-2 { animation: float 5s ease-in-out infinite reverse; }
.animate-float-3 { animation: float 6s ease-in-out infinite; }
</style>

