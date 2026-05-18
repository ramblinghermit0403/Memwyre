<template>
  <div
    class="force-light relative min-h-[100svh] bg-white text-text-primary transition-colors duration-300 font-sans overflow-x-hidden selection:bg-primary selection:text-white *:selection:bg-primary *:selection:text-white">

    <!-- Hero Section -->
    <div data-theme="light"
      class="hero-wash relative z-10 pt-16 sm:pt-20 lg:pt-24 pb-[120px] sm:pb-[136px] overflow-hidden min-h-[calc(100svh-88px)] flex items-center">

      <div class="absolute inset-0 z-0 hero-grain pointer-events-none"></div>

      <!-- Background Animation Layer -->
      <div class="absolute inset-0 z-[1] pointer-events-none overflow-hidden flex items-center justify-end"
        aria-hidden="true">
        <div class="relative w-full lg:w-1/2 h-full flex items-center justify-center">
          <ProcessorAnimation />
        </div>
      </div>

      <div
        class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center relative z-10 w-full">

        <div class="lg:col-span-6 text-left -mt-28 sm:mt-0 lg:-mt-[130px] lg:ml-10 px-0 sm:px-4">

          <h1
            class="animate-fade-in-up hero-serif text-5xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
            Stop repeating <br class="hidden md:block" />
            <span class="block text-[rgb(1,1,16)] italic font-medium">to
              every AI
              tool.</span>
          </h1>

          <p
            class="animate-fade-in-up animation-delay-150 text-balance text-lg sm:text-xl lg:text-xl text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
            Memwyre turns your prompts, conversations, and research into a memory layer you can reuse anywhere you work
            with AI.
          </p>

          <div
            class="animate-fade-in-up animation-delay-300 flex flex-row items-center justify-start gap-3 sm:gap-4 mt-6 sm:mt-10">
            <router-link to="/signup"
              class="w-auto px-4 py-2 sm:px-8 sm:py-3.5 bg-[#050614] text-white font-bold rounded-full hover:bg-gray-800 transition-all duration-300 shadow-xl text-xs sm:text-base inline-flex items-center justify-center gap-2">
              <span class="grid grid-cols-2 gap-0.5 w-4 h-4" aria-hidden="true">
                <span class="bg-white"></span>
                <span class="bg-white"></span>
                <span class="bg-white"></span>
                <span class="bg-white"></span>
              </span>
              Get Started — It's Free
            </router-link>
            <router-link to="/pricing"
              class="w-auto px-4 py-2 sm:px-8 sm:py-3.5 bg-white/30 text-[#050614] font-bold rounded-full border border-[#050614] hover:bg-white/60 transition-all duration-300 text-xs sm:text-base inline-flex items-center justify-center">
              See Plans
            </router-link>
          </div>

        </div>

        <div class="hidden lg:block lg:col-span-6 relative min-h-[650px] pointer-events-none" aria-hidden="true">
        </div>

      </div>
    </div>



    <!-- Features Section (WHITE) -->
    <div id="features" data-theme="light" class="relative z-20 pt-16 sm:pt-20 pb-16 sm:pb-24 bg-white">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">

        <!-- Video Demos -->
        <div class="space-y-14 sm:space-y-20 mb-16 sm:mb-20">

          <!-- 1. Omnipresent Overlay Demo -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center">
            <div class="lg:col-span-5 mb-6 lg:mb-0">
              <div class="w-12 h-12 flex items-center justify-left text-gray-900 mb-4">
                <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">Access it from
                any app</h3>
              <p class="text-base text-gray-500 mt-4 leading-relaxed max-w-xl">Invoke Memwyre instantly on top of
                any
                app. Your context is always one keystroke away with our native desktop experience.</p>
              <ul class="mt-6 space-y-3">
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Works across every
                      app</span> — ChatGPT, Claude, Notion, email — without switching tabs.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">One-click memory
                      capture</span> — save any message or thought directly to your vault mid-conversation.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Context sync in one
                      click</span> — instantly push your personal knowledge base into any active AI session.</span>
                </li>
              </ul>
            </div>
            <div
              class="lg:col-span-7 rounded-2xl overflow-hidden shadow-xl border border-black/5 relative aspect-[16/10]">
              <!-- Animated Omnipresent Demo -->
              <OmnipresentDemo />
            </div>
          </div>


          <!-- 3. Cross-Post Context -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center">
            <div class="lg:col-span-5 mb-6 lg:mb-0">
              <div class="w-12 h-12 flex items-center justify-left text-gray-900 mb-4">
                <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight"> Send to any AI
                in one click</h3>
              <p class="text-base text-gray-500 mt-4 leading-relaxed max-w-xl">Find the exact reference you need and
                launch it directly into your preferred AI model.</p>
              <ul class="mt-6 space-y-3">
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Semantic memory
                      search</span> — find any note or past context in seconds, even if you don't remember the exact
                    words.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Launch into any
                      AI</span> — send your memory directly to ChatGPT, Claude, Gemini, or Perplexity as a
                    pre-loaded
                    prompt.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">No copy-paste</span>
                    —
                    the reference is inserted automatically, preserving full formatting and context.</span>
                </li>
              </ul>
            </div>
            <div
              class="lg:col-span-7 rounded-2xl overflow-hidden shadow-xl border border-black/5 aspect-[16/10] relative">
              <TimelineDemo />
            </div>
          </div>


          <!-- 2. Ask MemWyre (Contextual Chat) -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center">
            <div class="lg:col-span-5 mb-6 lg:mb-0">
              <div class="w-12 h-12 flex items-center justify-left text-gray-900 mb-4">
                <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">Chat with your
                notes</h3>
              <p class="text-base text-gray-500 mt-4 leading-relaxed max-w-xl">Ask questions grounded in your
                personal
                knowledge base — with sources cited inline.</p>
              <ul class="mt-6 space-y-3">
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Grounded
                      answers</span>
                    — every response is anchored to documents and notes you've personally saved, not generic web
                    data.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Inline source
                      citations</span> — see exactly which memory or document each part of the answer came
                    from.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Your AI, not a
                      generic
                      one</span> — it knows your decisions, your notes, and your context without
                    re-explaining.</span>
                </li>
              </ul>
            </div>
            <div
              class="lg:col-span-7 rounded-2xl overflow-hidden shadow-xl border border-black/5 relative aspect-[16/10]">
              <ChatDemo />
            </div>
          </div>


          <!-- 4. Granular Memory Control -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center">
            <div class="lg:col-span-5 mb-6 lg:mb-0">
              <div class="w-12 h-12 flex items-center justify-left text-gray-900 mb-4">
                <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                </svg>
              </div>
              <h3 class="font-display text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">You decide
                what's saved</h3>
              <p class="text-base text-gray-500 mt-4 leading-relaxed max-w-xl">Review, edit, and curate your
                memories
                before they are saved to your vault.</p>
              <ul class="mt-6 space-y-3">
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Review before
                      saving</span> — preview every captured memory and edit it before it becomes part of your
                    vault.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Tag and
                      organize</span>
                    — add custom labels so memories are surfaced in the right context at the right time.</span>
                </li>
                <li class="flex items-start gap-3">
                  <span
                    class="mt-1 w-4 h-4 rounded-full bg-gray-900 flex-shrink-0 flex items-center justify-center"><svg
                      class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg></span>
                  <span class="text-sm text-gray-600"><span class="font-semibold text-gray-900">Full delete
                      control</span> — remove any memory at any time. Your vault, your rules.</span>
                </li>
              </ul>
            </div>
            <div
              class="lg:col-span-7 rounded-2xl overflow-hidden shadow-xl border border-black/5 relative bg-[#111111] aspect-[16/10]">
              <InboxDemo />
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- Ecosystem Section (BLACK) -->
    <div id="ecosystem" data-theme="dark"
      class="relative py-16 sm:py-24 bg-[#111111] rounded-[2rem] sm:rounded-[3.5rem] overflow-hidden">
      <!-- Background Image Layer -->
      <div class="absolute inset-0 z-0 pointer-events-none select-none">
        <img src="@/assets/ecosystem-bg.jpg" alt="" class="w-full h-full object-cover object-center" />
      </div>

      <div class="relative z-10 max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="max-w-3xl mb-16">
          <h2 class="text-sm font-bold uppercase tracking-widest text-black/60 mb-4">Ecosystem</h2>
          <p
            class="font-display text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-6 text-balance text-black">
            Built to extend.</p>
          <p class="text-lg md:text-xl text-black/80">MemWyre isn't a silo. It powers your entire workflow
            through standard protocols.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            class="p-10 bg-white border border-black/10 rounded-2xl shadow-lg transition-all duration-300 relative overflow-hidden group">
            <!-- Tilted MCP Background Icon -->
            <div
              class="absolute z-0 -top-12 -right-12 w-52 h-52 opacity-70 group-hover:opacity-95 rotate-[20deg] pointer-events-none transition-opacity duration-500 text-black">
              <svg viewBox="0 0 172 172" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
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
            <h3 class="relative z-10 text-2xl font-bold mb-4 mt-8 text-black">MCP Server</h3>
            <p class="relative z-10 text-gray-600 mb-8">
              Connect MemWyre directly to Claude Desktop or any MCP-compliant client. Give your AI assistant
              direct access to your knowledge base.
            </p>
            <div class="relative z-10 bg-gray-50 border border-black/5 rounded-lg p-4 font-mono text-xs text-gray-700">
              $ npx -y @memwyre/mcp-server
            </div>
          </div>

          <div
            class="p-10 bg-white border border-black/10 rounded-2xl shadow-lg transition-all duration-300 relative overflow-hidden group">
            <!-- Tilted Chrome Background Icon -->
            <img src="@/assets/chrome-logo-svgrepo-com.svg" alt=""
              class="absolute z-0 -top-14 -right-14 w-56 h-56 opacity-70 group-hover:opacity-95 rotate-[25deg] pointer-events-none transition-opacity duration-500" />

            <h3 class="relative z-10 text-2xl font-bold mb-4 mt-8 text-black">Browser Extension</h3>
            <p class="relative z-10 text-gray-600 mb-8">
              Capture the web as you browse. Save articles, documentation, or code snippets instantly without
              breaking your flow.
            </p>
            <div
              class="relative z-10 inline-flex items-center gap-3 px-4 py-2 rounded-full border border-black/5 bg-gray-50 text-gray-800 text-sm font-bold">
              <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-6 h-6" />
              <img src="@/assets/microsoft-edge-logo.svg" alt="Edge" class="w-6 h-6" />
              <span>Chrome &amp; Edge</span>
            </div>
          </div>

          <div
            class="p-10 bg-white border border-black/10 rounded-2xl shadow-lg transition-all duration-300 relative overflow-hidden group">
            <!-- Tilted OpenClaw Background Icon -->
            <img src="@/assets/openclaw-color.svg" alt=""
              class="absolute z-0 -top-12 -right-12 w-52 h-52 opacity-75 group-hover:opacity-95 rotate-[20deg] pointer-events-none transition-opacity duration-500" />

            <h3 class="relative z-10 text-2xl font-bold mb-4 mt-8 text-black">OpenClaw Plugin</h3>
            <p class="relative z-10 text-gray-600 mb-8">
              Give autonomous agents persistent memory. The OpenClaw plugin lets AI agents save and recall context
              from your vault automatically.
            </p>
            <div class="relative z-10 bg-gray-50 border border-black/5 rounded-lg p-4 font-mono text-xs text-gray-700">
              $ openclaw plugins install @memwyre/openclaw
            </div>
          </div>
        </div>
      </div>
    </div>



    <!-- Use Cases Section (WHITE) -->
    <div id="use-cases" data-theme="light" class="py-24 sm:py-32 bg-white border-t border-black/5">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">


        <div class="grid grid-cols-1 md:grid-cols-12 gap-4">
          <!-- Use Case 1: Software Engineers (WIDER) -->
          <div
            class="md:col-span-7 relative min-h-[450px] bg-[#faf0cc] rounded-2xl overflow-hidden group transition-all duration-500 flex flex-col border border-black/5">
            <!-- Text Layer (TOP) -->
            <div class="relative z-20 p-8 pb-0 text-left">
              <h3 class="font-display text-2xl font-extrabold text-gray-900 mb-2 tracking-tight">Native IDE Memory</h3>
              <p class="text-gray-600 text-sm leading-relaxed max-w-md font-medium">
                Connect your IDE directly via MCP. Past bug fixes and API specs become instantly searchable context
                inside Cursor.
              </p>
            </div>

            <!-- Animation Layer (BOTTOM) -->
            <div class="relative z-10 flex-1 flex items-center justify-center p-8 overflow-hidden">
              <div class="w-full max-w-[320px] transition-transform duration-500">
                <EngineerMinAnimation />
              </div>
            </div>
          </div>

          <!-- Use Case 2: 60-Second Setup (NARROWER) -->
          <div
            class="md:col-span-5 relative min-h-[450px] bg-[#f7f6f3] rounded-2xl overflow-hidden group transition-all duration-500 flex flex-col border border-black/5">
            <!-- Text Layer (TOP) -->
            <div class="relative z-20 p-8 pb-0 text-left">
              <h3 class="font-display text-2xl font-extrabold text-gray-900 mb-2 tracking-tight">60-Second Setup</h3>
              <p class="text-gray-600 text-sm leading-relaxed font-medium">
                No complex onboarding or data migrations. Install the MCP server and connect your workspace instantly.
              </p>
            </div>

            <!-- Animation Layer (BOTTOM) -->
            <div class="relative z-10 flex-1 flex items-center justify-center p-6 overflow-hidden">
              <div class="w-full max-w-[320px] transition-transform duration-500">
                <SetupTimerAnimation />
              </div>
            </div>
          </div>

          <!-- Use Case 3: DevOps & Agents (NARROWER) -->
          <div
            class="md:col-span-5 relative min-h-[450px] bg-[#f7f6f3] rounded-2xl overflow-hidden group transition-all duration-500 flex flex-col border border-black/5">
            <!-- Text Layer (TOP) -->
            <div class="relative z-20 p-8 pb-0 text-left">
              <h3 class="font-display text-2xl font-extrabold text-gray-900 mb-2 tracking-tight">DevOps & Agents</h3>
              <p class="text-gray-600 text-sm leading-relaxed font-medium">
                Agents remember past runs and build on previous sessions, accumulating knowledge.
              </p>
            </div>

            <!-- Animation Layer (BOTTOM) -->
            <div class="relative z-10 flex-1 flex items-center justify-center p-8 overflow-hidden">
              <div class="w-full max-w-[280px] transition-transform duration-500">
                <DevOpsMinAnimation />
              </div>
            </div>
          </div>

          <!-- Use Case 4: Product Managers (WIDER) -->
          <div
            class="md:col-span-7 relative min-h-[450px] bg-[#DBF1F5] rounded-2xl overflow-hidden group transition-all duration-500 flex flex-col border border-black/5">
            <!-- Text Layer (TOP) -->
            <div class="relative z-20 p-8 pb-0 text-left">
              <h3 class="font-display text-2xl font-extrabold text-gray-900 mb-2 tracking-tight">Works With Every LLM
              </h3>
              <p class="text-gray-600 text-sm leading-relaxed max-w-md font-medium">
                One memory layer across ChatGPT, Gemini, and Claude. Your context follows you, no matter which LLM you
                use.
              </p>
            </div>

            <!-- Animation Layer (Centered) -->
            <div class="absolute inset-0 z-10 flex items-center justify-center">
              <ScatteredWorkMinAnimation />
            </div>
          </div>

        </div>
      </div>
    </div>






    <!-- Workflow Section (HOW IT WORKS) -->
    <div id="workflow" data-theme="light" class="py-20 sm:py-28 bg-white border-t border-black/5">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="mb-16">
          <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">Workflow</h2>
          <p
            class="font-display text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 text-balance">
            Structured for flow.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="space-y-12">
            <div class="flex gap-6">
              <span class="text-4xl font-light text-gray-200 leading-none shrink-0">01</span>
              <div>
                <h3 class="text-2xl font-bold text-gray-900 mb-2">Ingestion via Browser / MCP</h3>
                <p class="text-gray-500 leading-relaxed">Capture the web as you browse or connect directly from your IDE
                  using our Model Context Protocol server.</p>
              </div>
            </div>
            <div class="flex gap-6">
              <span class="text-4xl font-light text-gray-200 leading-none shrink-0">02</span>
              <div>
                <h3 class="text-2xl font-bold text-gray-900 mb-2">Context Organisation</h3>
                <p class="text-gray-500 leading-relaxed">AI automatically parses, tags, and stores your documents,
                  notes, and links — building your central brain.</p>
              </div>
            </div>
            <div class="flex gap-6">
              <span class="text-4xl font-light text-gray-200 leading-none shrink-0">03</span>
              <div>
                <h3 class="text-2xl font-bold text-gray-900 mb-2">Seamless AI Chat</h3>
                <p class="text-gray-500 leading-relaxed">Retrieve context naturally through our UI or via your own local
                  LLMs configured with your MemWyre MCP.</p>
              </div>
            </div>
          </div>

          <div class="relative group">
            <div
              class="absolute -inset-1 bg-gradient-to-r from-[#D97757]/30 to-[#FF9A7B]/10 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000">
            </div>
            <div class="relative bg-white border border-[#D97757]/10 rounded-2xl p-8 shadow-2xl">
              <div class="font-mono text-sm space-y-4">
                <div class="flex items-center gap-2 border-b border-[#D97757]/10 pb-4 mb-4">
                  <span class="w-3 h-3 rounded-full bg-[#D97757]"></span>
                  <span class="text-gray-400">Ask MemWyre</span>
                </div>
                <p class="text-gray-800 min-h-[50px]">
                  {{ typedText }}<span class="cursor">&nbsp;</span>
                </p>
                <div class="transition-opacity duration-1000 ease-in-out">
                  <br>
                  <span class="text-gray-400">Searching 3 documents...</span><br>
                  <span class="text-[#D97757]">Found matches in "Auth Specs v2" and "API Docs".</span><br><br>
                  Based on "Auth Specs v2", you should use the OAuth2 provider pattern. Here is the implementation
                  snippet...
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="faq" data-theme="light" class="py-20 sm:py-28 bg-[#f7f6f3] border-t border-black/5">
      <div class="max-w-7xl mx-auto px-6 sm:px-10 lg:px-12">
        <div class="mb-10 text-left">
          <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">FAQ</h2>
          <p class="font-display text-3xl sm:text-4xl font-bold tracking-tight text-gray-900">Questions &amp; answers
          </p>
        </div>

        <div class="border-t border-black/5">
          <div v-for="(faq, index) in faqs" :key="index" class="border-b border-black/5">
            <button @click="toggleFaq(index)" class="flex justify-between items-center w-full text-left py-5 group">
              <span class="text-[15px] font-semibold text-gray-900 group-hover:text-gray-500 transition-colors">{{
                faq.question }}</span>
              <span class="ml-4 flex-shrink-0 text-gray-400 font-light text-2xl leading-none">
                <span v-if="faq.isOpen">&minus;</span>
                <span v-else>+</span>
              </span>
            </button>
            <div v-show="faq.isOpen" class="text-gray-500 pb-6 leading-relaxed text-[15px] pr-8">
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Final CTA Section: Memory and Personality -->
    <div
      class="pt-20 pb-10 sm:pt-28 sm:pb-16 bg-white text-center px-6 relative overflow-hidden border-t border-black/5">
      <!-- Numeric background animation -->
      <NumericBgAnimation :invert="true" class="absolute inset-0 z-0 opacity-40" />

      <div class="max-w-7xl mx-auto relative z-10">
        <h2 class="font-display text-5xl sm:text-7xl lg:text-[7rem] font-medium tracking-tight mb-10 leading-[0.95]">
          <span
            class="bg-clip-text text-transparent bg-[repeating-linear-gradient(to_bottom,#111,#111_6px,white_6px,white_9px)]">
            The Second Brain
          </span><br />
          <span class="text-black">
            For Your AI.
          </span>
        </h2>
        <p class="text-gray-600 text-xl sm:text-2xl mb-14 max-w-3xl mx-auto font-medium leading-relaxed">
          A persistent knowledge vault that works everywhere you use AI.
        </p>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-5">
          <router-link to="/signup"
            class="w-full sm:w-auto px-10 py-4 bg-black text-white font-bold rounded-xl hover:bg-gray-800 transition-all duration-300 shadow-xl hover:scale-105">
            Get Started — It's Free
          </router-link>
          <router-link to="/pricing"
            class="w-full sm:w-auto px-10 py-4 bg-white text-black font-bold rounded-xl border border-black/10 hover:bg-black/5 transition-all duration-300 hover:border-black/20">
            Compare Plans
          </router-link>
        </div>
      </div>

      <div
        class="max-w-7xl mx-auto px-8 lg:px-12 mt-12 relative z-10 border-t border-black/5 pt-10 flex flex-col md:flex-row justify-between items-start gap-8 text-left">
        <div class="flex flex-col items-start gap-8">
          <!-- Socials -->
          <div class="flex items-center gap-5">
            <a v-if="false" href="https://linkedin.com/company/memwyre" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
              </svg>
            </a>
            <a href="https://twitter.com/MemWyre" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
              </svg>
            </a>
            <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
              </svg>
            </a>
          </div>

          <div class="flex items-center gap-2">
            <img src="/image.svg" alt="MemWyre" class="w-6 h-6 rounded" />
            <span class="font-medium text-2xl text-black tracking-tight"
              style="font-family: 'Inter', system-ui, sans-serif;">Memwyre</span>
          </div>
          <p class="text-sm text-gray-500 max-w-xs leading-relaxed">
            Building the unified memory layer for the next generation of AI agents and professionals.
          </p>
          <p class="text-xs text-black/30 font-medium">© 2026 Memwyre. Crafted for clarity.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-12 sm:gap-24 w-full md:w-auto">
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Product</h4>
            <router-link to="/#features"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Features</router-link>
            <router-link to="/pricing"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Pricing</router-link>
            <router-link to="/#ecosystem"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Ecosystem</router-link>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Support</h4>
            <a href="mailto:shivharehimansh@gmail.com"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Contact Us</a>
            <a href="https://x.com/MemWyre" target="_blank"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Twitter</a>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Legal</h4>
            <router-link to="/privacy-policy"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Privacy</router-link>
            <router-link to="/terms"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Terms</router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- ScrollLaunch Badge (Detectable but visually hidden) -->
    <div class="sr-only">
      <a href="https://www.scrolllaunch.com/products/memwyre?utm_source=badge&utm_medium=embed&utm_campaign=memwyre&ref=scrolllaunch"
        target="_blank" rel="noopener noreferrer">
        <img src="https://www.scrolllaunch.com/api/badge/memwyre" alt="Featured on ScrollLaunch" width="220" height="48"
          loading="lazy" />
      </a>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import frame10Png from '@/assets/motion/FRAME 10.png';
import ChatDemo from '@/components/landing/ChatDemo.vue';
import OmnipresentDemo from '@/components/landing/OmnipresentDemo.vue';
import TimelineDemo from '@/components/landing/TimelineDemo.vue';
import InboxDemo from '@/components/landing/InboxDemo.vue';
import ScatteredWorkHero from '@/components/landing/ScatteredWorkHero.vue';
import ProductShowcase from '@/components/landing/ProductShowcase.vue';
import SetupTimerAnimation from '@/components/landing/usecases/SetupTimerAnimation.vue';
import NumericBgAnimation from '@/components/landing/NumericBgAnimation.vue';
import LavaNumericPattern from '@/components/landing/LavaNumericPattern.vue';
import ProcessorAnimation from '@/components/landing/ProcessorAnimation.vue';

// Use Case Animations
import EngineerMinAnimation from '@/components/landing/usecases/EngineerMinAnimation.vue';
import DevOpsMinAnimation from '@/components/landing/usecases/DevOpsMinAnimation.vue';
import ScatteredWorkMinAnimation from '@/components/landing/usecases/ScatteredWorkMinAnimation.vue';


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
          video.play().catch(() => { });
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



// --- Animations ---
onMounted(() => {
  shouldRestoreDarkClass = document.documentElement.classList.contains('dark');
  document.documentElement.classList.remove('dark');
  document.documentElement.style.colorScheme = 'light';
  typeWriter();
  setupVideoObserver();
});


// 3. FAQ accordion
const faqs = ref([
  {
    question: "What exactly is MemWyre?",
    answer: "MemWyre is a unified AI memory vault that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It then makes this knowledge instantly searchable and reusable.",
    isOpen: false
  },
  {
    question: "Is there a free plan?",
    answer: "Yes! MemWyre has a generous free tier that includes up to 50 memories, 10 document uploads, 30 AI chat messages, and full IDE integration via MCP. No credit card required — just sign up and start building your brain.",
    isOpen: false
  },
  {
    question: "How do I connect MemWyre to Cursor or VS Code?",
    answer: "You can connect MemWyre to Cursor, VS Code, or Claude Desktop using our official Model Context Protocol (MCP) server. This gives your AI assistant direct, real-time access to your entire personal knowledge base.",
    isOpen: false
  },
  {
    question: "Do you offer a browser extension?",
    answer: "Yes! The MemWyre browser extension (available for Chrome and Edge) lets you instantly clip text, articles, and code snippets directly into your vault without breaking your flow.",
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

// 2. Typing Effect
const typedText = ref("> How do I implement the new auth flow?");

const typeWriter = () => {
  // No-op - text is now pre-typed
};

</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

/* Force light mode — override dark theme CSS variables */
.hero-wash {
  background:
    radial-gradient(circle at 23% 14%, rgba(255, 231, 92, 0.72), transparent 30%),
    radial-gradient(circle at 74% 30%, rgba(255, 235, 125, 0.76), transparent 32%),
    radial-gradient(circle at 12% 86%, rgba(149, 205, 255, 0.68), transparent 34%),
    radial-gradient(circle at 88% 91%, rgba(175, 220, 255, 0.62), transparent 32%),
    linear-gradient(115deg, #fff7ca 0%, #fffdf4 43%, #eff8ff 100%);
}

.hero-grain {
  background-image:
    linear-gradient(115deg, rgba(255, 255, 255, 0.6), transparent 52%),
    radial-gradient(circle at center, rgba(5, 6, 20, 0.05) 1px, transparent 1px);
  background-size: auto, 28px 28px;
  opacity: 0.34;
}

.hero-serif {
  font-family: 'DM Serif Text', serif;
  letter-spacing: -0.02em;
}

.hero-visual {
  transform: translate(5%, 3%) rotate(-29deg) skewX(-2deg) scale(0.92);
  transform-origin: center;
}

.hero-track {
  position: absolute;
  left: -12%;
  right: -20%;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(5, 6, 20, 0.16), transparent);
}

.hero-track-one {
  top: 48%;
}

.hero-track-two {
  top: 64%;
}

.voice-card {
  position: absolute;
  width: 182px;
  min-height: 62px;
  display: grid;
  gap: 6px;
  padding: 14px 18px;
  border: 1.5px solid rgba(5, 6, 20, 0.86);
  border-radius: 999px;
  background: rgba(247, 251, 255, 0.76);
  box-shadow: 0 18px 0 rgba(5, 6, 20, 0.08);
}

.voice-card span {
  height: 2px;
  border-radius: 999px;
  background: repeating-linear-gradient(90deg, #050614 0 9px, transparent 9px 17px);
}

.voice-card-one {
  left: 5%;
  bottom: 12%;
}

.voice-card-two {
  left: 34%;
  bottom: 21%;
}

.voice-card-three {
  left: 17%;
  bottom: -1%;
}

.hero-keyboard {
  position: absolute;
  left: 40%;
  top: 43%;
  width: 320px;
  height: 150px;
  border: 2px solid #050614;
  border-radius: 24px;
  background: linear-gradient(180deg, #fffef6 0%, #ffe477 100%);
  box-shadow: 18px 24px 0 rgba(5, 6, 20, 0.1);
}

.hero-keyboard::before {
  content: "";
  position: absolute;
  inset: 18px 20px 34px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.76);
  border: 1px solid rgba(5, 6, 20, 0.18);
}

.key {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
  height: 74px;
  border: 2px solid #050614;
  border-radius: 14px;
  background: #fbfcff;
  color: #475569;
  font-size: 13px;
  font-weight: 700;
  box-shadow: 10px 12px 0 rgba(5, 6, 20, 0.1);
}

.key-shift {
  left: 6px;
  top: -48px;
}

.key-control {
  right: 4px;
  top: -14px;
}

.key-main {
  left: 98px;
  top: 30px;
  min-width: 96px;
  height: 78px;
  background: #2c2b27;
}

.key-main img {
  width: 42px;
  height: 42px;
  filter: brightness(0) invert(1);
}

.hero-pill {
  position: absolute;
  min-width: 190px;
  padding: 13px 20px;
  border-radius: 999px;
  background: #2c2b27;
  color: #ffe26e;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 0.02em;
  box-shadow: 0 12px 0 rgba(5, 6, 20, 0.12);
}

.hero-pill::before {
  content: "";
  display: inline-block;
  width: 30px;
  height: 30px;
  margin-right: 12px;
  vertical-align: middle;
  border-radius: 999px;
  border: 2px solid #050614;
  background: radial-gradient(circle at center, #ffe26e 0 45%, transparent 47%), #ffe26e;
}

.pill-one {
  right: -2%;
  top: 8%;
}

.pill-two {
  right: 20%;
  top: 30%;
}

.pill-three {
  right: 33%;
  top: 50%;
}

.pill-four {
  right: -12%;
  top: 45%;
}

@media (max-width: 1023px) {
  .hero-visual {
    transform: rotate(-23deg) scale(0.84);
    min-height: 430px;
  }

  .hero-keyboard {
    left: 31%;
  }

  .pill-one {
    right: 2%;
  }

  .pill-four {
    right: -2%;
  }
}

@media (max-width: 640px) {
  .hero-visual {
    margin-top: -34px;
    transform: rotate(-19deg) scale(0.66);
    min-height: 330px;
  }
}

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

  0%,
  100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

@keyframes gradient-slow {

  0%,
  100% {
    background-position: 0% 0%;
  }

  50% {
    background-position: 100% 100%;
  }
}

.animate-gradient-slow {
  background-size: 200% 200%;
  animation: gradient-slow 8s ease-in-out infinite;
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

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}

.animate-float-1 {
  animation: float 4s ease-in-out infinite;
}

.animate-float-2 {
  animation: float 5s ease-in-out infinite reverse;
}

.animate-float-3 {
  animation: float 6s ease-in-out infinite;
}

@keyframes gradient-x {

  0%,
  100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

.animate-gradient-x {
  background-size: 200% 200%;
  animation: gradient-x 4s ease-in-out infinite;
}
</style>
