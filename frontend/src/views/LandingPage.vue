<template>
  <div
    class="force-light relative min-h-[100svh] bg-white text-text-primary transition-colors duration-300 font-sans overflow-x-hidden selection:bg-primary selection:text-white *:selection:bg-primary *:selection:text-white">

    <!-- Global Vertical Grid Lines -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 pointer-events-none select-none z-30"></div>

    <!-- Hero Section -->
    <div data-theme="light"
      class="hero-wash relative z-10 pt-16 sm:pt-24 lg:pt-12 pb-10 sm:pb-20 overflow-hidden min-h-[calc(100svh-88px)] flex items-center">

      <div class="absolute inset-0 z-0 hero-grain pointer-events-none"></div>

      <!-- Layout Grid Lines (Pinecone Blueprint Style) -->
      <div class="absolute inset-0 z-0 pointer-events-none select-none overflow-hidden">
        
        <!-- Center column divider line -->
        <div class="absolute left-1/2 top-0 bottom-0 w-px bg-gray-200 hidden lg:block"></div>

        <!-- Horizontal grid line below hero header elements -->
        <div class="absolute top-[55%] left-0 right-0 h-px bg-gray-300/80 hidden sm:block"></div>
        <!-- Horizontal grid line above logo/footer elements inside hero -->
        <div class="absolute bottom-[90px] left-0 right-0 h-px bg-gray-300/80 hidden sm:block"></div>

        <!-- Intersecting crosshairs at boundary coordinates -->
        <div class="hidden sm:block absolute top-[88px] left-6 sm:left-8 lg:left-[calc(50%-640px)] w-4 h-4 -translate-x-1/2 -translate-y-1/2">
          <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="hidden sm:block absolute top-[88px] right-6 sm:right-8 lg:right-[calc(50%-640px)] w-4 h-4 translate-x-1/2 -translate-y-1/2">
          <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="hidden sm:block absolute top-[55%] left-6 sm:left-8 lg:left-[calc(50%-640px)] w-4 h-4 -translate-x-1/2 -translate-y-1/2">
          <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="hidden sm:block absolute top-[55%] right-6 sm:right-8 lg:right-[calc(50%-640px)] w-4 h-4 translate-x-1/2 -translate-y-1/2">
          <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="hidden sm:block absolute bottom-[90px] left-6 sm:left-8 lg:left-[calc(50%-640px)] w-4 h-4 -translate-x-1/2 -translate-y-1/2">
          <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="hidden sm:block absolute bottom-[90px] right-6 sm:right-8 lg:right-[calc(50%-640px)] w-4 h-4 translate-x-1/2 -translate-y-1/2">
          <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
        </div>
      </div>

      <!-- Background Animation Layer -->
      <div
        class="hero-animation-layer absolute inset-0 z-[1] pointer-events-none overflow-hidden flex items-center justify-end"
        :class="{ 'hero-animation-layer-ready': heroAnimationReady }"
        :style="heroAnimationStyle"
        aria-hidden="true">
        <div class="relative w-full lg:w-1/2 h-full flex items-center justify-center">
          <ProcessorAnimation v-if="heroAnimationMounted" />
        </div>
      </div>

      <div
        class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center relative z-10 w-full">

        <div class="lg:col-span-6 text-left pt-8 pb-8 sm:pt-28 lg:pt-0 lg:mt-[20px] lg:ml-10 px-0 sm:px-4 -translate-y-[120px] md:-translate-y-[100px] lg:translate-y-0">

          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold mb-6 border border-emerald-200 animate-fade-in-up">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
            Early Access Open
          </div>

          <h1
            class="animate-fade-in-up hero-serif text-4xl sm:text-5xl md:text-5xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
            Your AI <br class="hidden md:block" />should <span class="italic font-medium">remember <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">everything.</span></span>
          </h1>

          <p
            class="animate-fade-in-up animation-delay-150 text-balance text-base text-[#111827] leading-relaxed mt-4 sm:mt-5 max-w-2xl font-normal">
            Memwyre is the AI Memory Platform that gives every AI tool, agent, and conversation a persistent, shared memory.
          </p>

          <!-- Unified Buttons and Installer Container for symmetry -->
          <div class="flex flex-col gap-3 mt-4 sm:mt-6 max-w-[340px] sm:max-w-[380px] w-full animate-fade-in-up animation-delay-300 z-20">
            <!-- Buttons with technical grid brackets -->
            <div class="relative w-full p-3 border border-dashed border-gray-300 rounded-none">
              <!-- Content (Buttons) -->
              <div class="flex flex-row items-center justify-start gap-3 sm:gap-4 w-full">
                <router-link to="/signup/"
                  class="flex-1 px-4 py-2 lg:py-2.5 bg-[#050614] text-white font-bold sm:font-semibold lg:font-bold rounded-none hover:bg-gray-800 transition-all duration-300 shadow-md text-xs sm:text-sm lg:text-base inline-flex items-center justify-center text-center">
                  Get Started
                </router-link>
                <router-link to="/#pricing"
                  class="flex-1 px-4 py-2 lg:py-2.5 bg-white text-[#050614] font-bold sm:font-semibold lg:font-bold rounded-none border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm lg:text-base inline-flex items-center justify-center text-center">
                  See Plans
                </router-link>
              </div>
            </div>

            <!-- Command Installer Codeblock in Hero -->
            <div class="relative bg-gray-50 border border-dashed border-gray-300 rounded-none p-3.5 font-mono text-[11px] sm:text-xs text-gray-800 flex items-center justify-between gap-3 w-full select-none">
              <div class="flex items-center gap-1.5 overflow-x-auto whitespace-nowrap scrollbar-none select-all py-0.5">
                <span class="text-[#D97757] select-none font-bold">$</span>
                <span>npx -y install-memwyre</span>
              </div>
              <button 
                @click="copyHeroCommand" 
                class="text-[#D97757] hover:text-[#C4654A] font-semibold text-[10px] sm:text-xs tracking-wider uppercase shrink-0 transition-colors cursor-pointer select-none"
              >
                {{ heroCommandCopied ? 'Copied' : 'Copy' }}
              </button>
            </div>
          </div>

        </div>

        <div class="hidden lg:block lg:col-span-6 relative min-h-[650px] pointer-events-none" aria-hidden="true">
        </div>

      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    

    <!-- Why AI Forgets Problem Framing Section -->
    <div id="problem-framing" data-theme="light" class="relative z-20 pt-10 pb-10 md:pt-16 md:pb-16 bg-white">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ THE PROBLEM</div>
          <div>[1/9]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 md:mb-12"></div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-start">
          <div class="lg:col-span-5 text-left">
            <h2 class="hero-serif text-3xl sm:text-5xl lg:text-[56px] tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-4 md:mb-6">
              Why your <span class="italic font-medium">AI has <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">amnesia.</span></span>
            </h2>
            <p class="text-base text-gray-500 leading-relaxed font-normal mb-6 md:mb-8">
              Every time you open a new chat tab, you start from zero. Your AI forgets your style guides, database schemas, API keys, and coding conventions.
            </p>
          </div>
          <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6">
            <div class="p-5 md:p-6 bg-white border border-dashed border-gray-300 shadow-sm rounded text-left">
              <div class="text-[#D97757] font-bold text-lg mb-2">The Copy-Paste Tax</div>
              <p class="text-xs text-gray-500 leading-relaxed font-normal">
                Developers waste hours pasting markdown guidelines and code context over and over again to keep tools aligned.
              </p>
            </div>
            <div class="p-5 md:p-6 bg-white border border-dashed border-gray-300 shadow-sm rounded text-left">
              <div class="text-[#D97757] font-bold text-lg mb-2">Context Window Noise</div>
              <p class="text-xs text-gray-500 leading-relaxed font-normal">
                Feeding massive files into prompts is expensive, introduces latency, and dilutes the model's attention, causing hallucinations.
              </p>
            </div>
            <div class="p-5 md:p-6 bg-white border border-dashed border-gray-300 shadow-sm rounded text-left">
              <div class="text-[#D97757] font-bold text-lg mb-2">Stateless Silos</div>
              <p class="text-xs text-gray-500 leading-relaxed font-normal">
                Your browser chat doesn't talk to your IDE, and your terminal agent doesn't know what you discussed 10 minutes ago.
              </p>
            </div>
            <div class="p-5 md:p-6 bg-white border border-dashed border-gray-300 shadow-sm rounded text-left">
              <div class="text-[#D97757] font-bold text-lg mb-2">Memwyre's Shared Layer</div>
              <p class="text-xs text-gray-500 leading-relaxed font-normal">
                A single memory layer securely sits between you and all your AI models, retrieving only the exact facts needed.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>


    <!-- Works with every LLM & Tool Section -->
    <div id="llm-compatibility" data-theme="light" class="relative z-20 pt-10 pb-0 md:pt-16 bg-white">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ PLATFORM COMPATIBILITY</div>
          <div>[2/9]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 md:mb-12"></div>

        <div class="text-center max-w-3xl mx-auto mb-8 md:mb-16">
          <h2 class="hero-serif text-2xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-4 md:mb-6">
            One memory layer. <span class="italic font-medium">Every tool <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">connected.</span></span>
          </h2>
          <p class="text-base text-gray-500 leading-relaxed font-normal">
            Memwyre is not a standalone chatbot. It is a universal context layer that plugs directly into the models, editors, and terminal tools you already use every day.
          </p>
        </div>

        <!-- Horizontal Logo Grid -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 border-t border-b border-gray-300/80 bg-white relative z-20 mb-8 md:mb-16">
          <div class="flex overflow-x-auto no-scrollbar md:grid md:grid-cols-7 divide-x divide-gray-300/80 scrollbar-none snap-x snap-mandatory">
            
            <!-- Claude Desktop -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/claude-color.svg" alt="Claude" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">Claude Desktop</span>
            </div>

            <!-- VS Code -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/vscode.svg" alt="VS Code" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">VS Code</span>
            </div>

            <!-- Windsurf -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/windsurf.ico" alt="Windsurf" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">Windsurf</span>
            </div>

            <!-- OpenClaw -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">OpenClaw</span>
            </div>

            <!-- Claude Code -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/claudecode-color.svg" alt="Claude Code" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">Claude Code</span>
            </div>

            <!-- ChatGPT -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/openai.svg" alt="ChatGPT" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">ChatGPT</span>
            </div>

            <!-- Cursor AI -->
            <div class="flex flex-col items-center justify-center gap-2 sm:gap-3 p-3 sm:p-5 bg-white min-h-[90px] sm:min-h-[100px] transition-all duration-300 hover:bg-gray-50/50 group cursor-pointer w-[110px] md:w-auto shrink-0 md:shrink snap-center">
              <img src="@/assets/cursor_CUBE_2D_LIGHT.svg" alt="Cursor AI" class="w-6 h-6 sm:w-8 sm:h-8 object-contain transition-transform duration-300 group-hover:scale-110" />
              <span class="text-[9px] sm:text-xs font-semibold text-gray-700 group-hover:text-gray-900 transition-colors text-center truncate w-full">Cursor AI</span>
            </div>

          </div>
        </div>

        <!-- Snippets of Use Cases (IDE/Agent Integrations & Multi-Model compatibility) -->
        <div class="-mx-8 sm:-mx-8 lg:-mx-12 lg:border-t lg:border-b lg:border-gray-300/80 bg-white relative z-20">
          <div class="flex lg:grid flex-nowrap lg:grid-cols-3 items-stretch gap-6 lg:gap-0 overflow-x-auto no-scrollbar scrollbar-none snap-x snap-mandatory px-8 lg:px-0">
            
            <!-- Column 1: IDE Integration -->
            <div class="w-[290px] sm:w-[390px] lg:w-full shrink-0 snap-align-start p-5 sm:p-8 flex flex-col justify-between min-h-[380px] lg:min-h-[440px] text-left border border-gray-200 lg:border-0 lg:border-r lg:border-gray-300/80 rounded-lg lg:rounded-none">
              <div>
                <div class="text-xs font-bold text-[#D97757] tracking-widest uppercase mb-3 font-mono">01 / IDE INTEGRATION</div>
                <h3 class="font-display text-xl font-extrabold text-gray-900 mb-3 tracking-tight">Native IDE Memory</h3>
                <p class="text-gray-500 text-xs sm:text-sm leading-relaxed font-normal">
                  Connect your IDE directly via MCP. Past bug fixes, configuration choices, and API schemas become instantly searchable context inside Cursor, VS Code, or Windsurf.
                </p>
              </div>
              <div class="mt-6 -mx-6 sm:-mx-8 -mb-6 sm:-mb-8 flex justify-center h-44 md:h-56 overflow-hidden border-t border-gray-200/80 bg-gray-50 relative">
                <div class="scale-[0.6] md:scale-[0.7] origin-top pt-4 w-full flex justify-center">
                  <EngineerMinAnimation />
                </div>
              </div>
            </div>
            
            <!-- Column 2: Terminal Agents -->
            <div class="w-[290px] sm:w-[390px] lg:w-full shrink-0 snap-align-start p-5 sm:p-8 flex flex-col justify-between min-h-[380px] lg:min-h-[440px] text-left border border-gray-200 lg:border-0 lg:border-r lg:border-gray-300/80 rounded-lg lg:rounded-none">
              <div>
                <div class="text-xs font-bold text-[#D97757] tracking-widest uppercase mb-3 font-mono">02 / TERMINAL AGENTS</div>
                <h3 class="font-display text-xl font-extrabold text-gray-900 mb-3 tracking-tight">DevOps &amp; Code Agents</h3>
                <p class="text-gray-500 text-xs sm:text-sm leading-relaxed font-normal">
                  Empower terminal tools like Claude Code and OpenClaw. Agents save debug results and project conventions, building cumulative operational memory.
                </p>
              </div>
              <div class="mt-6 -mx-6 sm:-mx-8 -mb-6 sm:-mb-8 flex justify-center h-44 md:h-56 overflow-hidden border-t border-gray-200/80 bg-gray-50 relative">
                <div class="scale-[0.6] md:scale-[0.7] origin-top pt-4 w-full flex justify-center">
                  <DevOpsMinAnimation />
                </div>
              </div>
            </div>

            <!-- Column 3: Multi-Model -->
            <div class="w-[290px] sm:w-[390px] lg:w-full shrink-0 snap-align-start p-5 sm:p-8 flex flex-col justify-between min-h-[380px] lg:min-h-[440px] text-left border border-gray-200 lg:border-0 rounded-lg lg:rounded-none">
              <div>
                <div class="text-xs font-bold text-[#D97757] tracking-widest uppercase mb-3 font-mono">03 / MULTI-MODEL</div>
                <h3 class="font-display text-xl font-extrabold text-gray-900 mb-3 tracking-tight">Works With Every LLM</h3>
                <p class="text-gray-500 text-xs sm:text-sm leading-relaxed font-normal">
                  One shared memory layer across Claude, ChatGPT, and Gemini. If you explain a code pattern in ChatGPT, your Cursor agent retrieves it instantly when you ask.
                </p>
              </div>
              <div class="mt-6 -mx-6 sm:-mx-8 -mb-6 sm:-mb-8 flex justify-center h-44 md:h-56 overflow-hidden border-t border-gray-200/80 bg-gray-50 relative">
                <div class="scale-[0.8] md:scale-100 origin-top pt-4 w-full flex justify-center">
                  <ScatteredWorkMinAnimation />
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

<!-- Comparison Section (WHITE) -->
    <div id="comparison" data-theme="light" class="pt-6 md:pt-10 pb-0 bg-white relative z-25">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ WHY MEMWYRE</div>
          <div>[6/8]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-4 sm:mb-8"></div>

        <!-- Header Row (Title and Description) -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-16 mb-6 sm:mb-12 items-start lg:items-center">
          <div>
            <h2 class="hero-serif text-2xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)]">
              Context for humans, <span class="italic font-medium">not just <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">databases.</span></span>
            </h2>
          </div>
          <div>
            <p class="text-base text-gray-500 leading-relaxed font-normal">
              Mem0 and Zep are built as backend database infrastructure for AI agents. Memwyre is built as the out-of-the-box context layer for individual developers, power users, and the tools they work in daily.
            </p>
          </div>
        </div>

        <!-- Comparison Table Container -->
        <div class="hidden md:block w-auto -mx-8 sm:-mx-8 lg:-mx-12 md:overflow-x-hidden lg:overflow-x-auto border-t border-b sm:border-l sm:border-r border-gray-300/80 bg-white relative z-20">
          <table class="w-full lg:min-w-[800px] border-collapse text-left table-fixed">
            <thead>
              <tr class="border-b border-gray-300/80">
                <th class="py-4 sm:py-5 px-2.5 sm:px-6 text-xs uppercase font-bold tracking-wider text-gray-400 font-mono w-[30%]">Positioning Dimension</th>
                <th class="py-4 sm:py-5 px-2.5 sm:px-6 text-center relative w-[28%] bg-[#D97757]/5">
                  <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#D97757] text-white text-[8px] sm:text-[9px] font-extrabold tracking-widest px-2 sm:px-3 py-0.5 rounded-full uppercase shadow-sm whitespace-nowrap">RECOMMENDED</div>
                  <div class="flex items-center justify-center mt-1 h-8">
                    <img src="/logo.png" alt="Memwyre" class="h-7 w-auto dark:invert" />
                  </div>
                </th>
                <th class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-700 font-display text-sm lg:text-base font-bold w-[21%]">Mem0</th>
                <th class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-700 font-display text-sm lg:text-base font-bold w-[21%]">Zep AI</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-300/80">
              
              <!-- Primary Target -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Primary Customer</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Who the product is designed for</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5 font-bold text-[#D97757] text-xs sm:text-sm">
                  Individual Developers &amp; Power Users
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  AI Agent Developers
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  AI Agent Developers
                </td>
              </tr>

              <!-- Delivery Channel -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 17.25v1.007a3 3 0 01-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0115 18.257V17.25m6-12V15a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 15V5.25m18 0A2.25 2.25 0 0018.75 3H5.25A2.25 2.25 0 003 5.25m18 0V12a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 12V5.25" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Core Product Interface</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">How users access and manage context</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5 font-bold text-[#D97757] text-xs sm:text-sm">
                  Desktop Overlay, Browser, &amp; IDEs
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  Backend API &amp; SDKs only
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  Backend API &amp; SDKs only
                </td>
              </tr>

              <!-- Setup Time -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Time-to-Value Setup</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Time to connect tools and store first memory</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5 font-bold text-[#D97757] text-xs sm:text-sm">
                  &lt; 5 Minutes
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  Hours (Code &amp; Database Config)
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  Hours (Code &amp; Database Config)
                </td>
              </tr>

              <!-- Cross-App Portability -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 16.875V21m0-8.25v2.25m0-10.5v2.25M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125zM3.375 18h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125z" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Cross-Tool Memory Sync</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Auto-sharing memories across your workflows</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5 font-bold text-[#D97757] text-xs sm:text-sm">
                  Built-in &amp; Automatic
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  Requires custom syncing pipelines
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-500 text-xs sm:text-sm">
                  Requires custom syncing pipelines
                </td>
              </tr>

              <!-- Workspace Connectors -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Ready-To-Use Connectors</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Notion, Google Drive, GitHub sync capability</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5">
                  <div class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-orange-100 text-[#D97757]">
                    <svg class="w-3.5 h-3.5 stroke-[3]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-300 font-mono">
                  —
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-300 font-mono">
                  —
                </td>
              </tr>

              <!-- MCP Server Support -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5.25 5.25a3 3 0 00-3 3v8.25a3 3 0 003 3h13.5a3 3 0 003-3V8.25a3 3 0 00-3-3H5.25zM12 9.75v4.5m-2.25-2.25h4.5" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">MCP Client Support</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Out-of-the-box Cursor, Claude Desktop integration</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5">
                  <div class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-orange-100 text-[#D97757]">
                    <svg class="w-3.5 h-3.5 stroke-[3]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-300 font-mono">
                  —
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-300 font-mono">
                  —
                </td>
              </tr>

              <!-- Agent CLI Plugins -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M14.25 9.75L16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0020.25 18V6A2.25 2.25 0 0018 3.75H6A2.25 2.25 0 003.75 6v12A2.25 2.25 0 006 20.25z" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Agent CLI Plugins</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Native plugins for Claude Code and OpenClaw</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5">
                  <div class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-orange-100 text-[#D97757]">
                    <svg class="w-3.5 h-3.5 stroke-[3]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-300 font-mono">
                  —
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center text-gray-300 font-mono">
                  —
                </td>
              </tr>

              <!-- Self-Hostable -->
              <tr class="hover:bg-gray-50/50 transition-colors duration-150">
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 font-medium text-gray-900 text-xs sm:text-sm lg:text-base flex items-center gap-2 lg:gap-3">
                  <div class="text-gray-400 hidden lg:block">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-.778.099-1.533.284-2.253" />
                    </svg>
                  </div>
                  <div>
                    <div class="font-bold text-gray-900 text-xs sm:text-sm lg:text-base">Self-Hostable</div>
                    <div class="text-gray-400 text-[10px] sm:text-xs mt-0.5">Fully open-source deployment using Docker</div>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center bg-[#D97757]/5">
                  <div class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-orange-100 text-[#D97757]">
                    <svg class="w-3.5 h-3.5 stroke-[3]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center">
                  <div class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-gray-100 text-gray-700">
                    <svg class="w-3.5 h-3.5 stroke-[2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </td>
                <td class="py-4 sm:py-5 px-2.5 sm:px-6 text-center">
                  <div class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-gray-100 text-gray-700">
                    <svg class="w-3.5 h-3.5 stroke-[2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </td>
              </tr>

            </tbody>
          </table>
        </div>

        <!-- Mobile Comparison Table (visible on mobile only) -->
        <div class="block md:hidden mt-6 -mx-1 overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="border-b border-gray-200">
                <th class="py-3 pr-3 text-[10px] uppercase font-bold tracking-wider text-gray-400 font-mono w-[44%]">Feature</th>
                <th class="py-3 px-2 text-center w-[19%] bg-[#D97757]/8 relative">
                  <div class="absolute -top-2.5 left-1/2 -translate-x-1/2 bg-[#D97757] text-white text-[7px] font-extrabold tracking-widest px-2 py-0.5 rounded-full uppercase whitespace-nowrap">BEST</div>
                  <img src="/logo.png" alt="Memwyre" class="h-4 w-auto mx-auto mt-1" />
                </th>
                <th class="py-3 px-2 text-center text-gray-500 font-bold w-[19%]">Mem0</th>
                <th class="py-3 px-2 text-center text-gray-500 font-bold w-[18%]">Zep</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
              <!-- Primary Customer -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Consumer / Dev Focus</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- Core Product Interface -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Desktop / Browser Interface</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- Setup < 5 Minutes -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Setup &lt; 5 Minutes</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- Cross-Tool Memory Sync -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Cross-Tool Memory Sync</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- Workspace Connectors -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Workspace Connectors</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- MCP Client Support -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">MCP Client Support</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- Agent CLI Plugins -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Agent CLI Plugins</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
              <!-- Self-Hostable -->
              <tr>
                <td class="py-3 pr-3 text-gray-700 font-medium">Self-Hostable</td>
                <td class="py-3 px-2 text-center bg-[#D97757]/8">
                  <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#D97757] text-white text-[10px] font-bold">✓</span>
                </td>
                <td class="py-3 px-2 text-center text-gray-600 text-base font-bold">✓</td>
                <td class="py-3 px-2 text-center text-gray-300 text-base font-bold">✗</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    
<!-- Features Section (WHITE) -->
    <div id="features" data-theme="light" class="relative z-20 pt-6 sm:pt-8 pb-10 sm:pb-12 bg-white">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">

        <!-- 2-Column Tabbed Showcase -->
        <div ref="showcaseContainer" class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-start">
          
          <!-- Left Column: Tabs List -->
          <div class="lg:col-span-5 flex flex-col h-full">
            <!-- Breadcrumb Row -->
            <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4 px-1">
              <div>/ PRODUCT FEATURES</div>
              <div>[{{ activeTab + 1 }}/4]</div>
            </div>

            <!-- Divider Line below Breadcrumb -->
            <div class="-mx-6 sm:-mx-8 lg:-mx-12 lg:-mr-0 h-px bg-gray-300/80 pointer-events-none select-none mb-8"></div>

            <h2 class="hero-serif text-3xl sm:text-5xl lg:text-[56px] tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-4 md:mb-6 px-1">
              All the tools to <span class="italic font-medium">make AI <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">remember.</span></span>
            </h2>
            <p class="text-base text-gray-500 leading-relaxed font-normal mb-8 px-1">
              Every feature you need to capture, organize, and query your shared memory platform seamlessly across your workflow.
            </p>

            <!-- Tabs Navigation -->
            <div class="border-t border-gray-300/80 flex flex-col">
              <button
                v-for="(tab, index) in tabs"
                :key="index"
                @click="selectTab(index)"
                :class="[
                  'w-full text-left py-4 px-4 border-b border-gray-300/80 transition-all duration-300 flex items-center justify-between group relative border-l-2',
                  activeTab === index 
                    ? 'border-l-[#D97757] bg-gray-50/50 text-gray-900 font-bold' 
                    : 'border-l-transparent text-gray-400 hover:text-gray-600 hover:bg-gray-50/30'
                ]"
              >
                <div class="flex items-center gap-4">
                  <span :class="[
                    'text-xs font-mono font-bold transition-colors',
                    activeTab === index ? 'text-[#D97757]' : 'text-gray-300 group-hover:text-gray-400'
                  ]">{{ tab.num }}</span>
                  <span class="text-base tracking-tight">{{ tab.tabTitle }}</span>
                </div>
                <!-- Small orange indicator square when active -->
                <span v-if="activeTab === index" class="w-1.5 h-1.5 bg-[#D97757] rounded-sm shrink-0"></span>
                <!-- Progress bar line absolute at bottom -->
                <div
                  v-if="activeTab === index"
                  class="absolute bottom-0 left-0 h-[2px] bg-[#D97757] pointer-events-none"
                  :style="{ 
                    width: progressWidth + '%',
                    transition: progressWidth === 0 ? 'none' : 'width 50ms linear'
                  }"
                ></div>
              </button>
            </div>
          </div>

          <!-- Right Column: Active Visual & Details -->
          <div class="lg:col-span-7 flex flex-col">
            <!-- Premium Video Wrapper -->
            <div class="rounded overflow-hidden shadow-xl border border-gray-200 relative aspect-[16/10] bg-black">
              <video
                v-for="(tab, index) in tabs"
                :key="index"
                :ref="el => { if (el) videoRefs[index] = el }"
                v-show="activeTab === index"
                class="w-full h-full object-cover"
                muted
                playsinline
                :preload="activeTab === index ? 'auto' : 'none'"
                :src="activeTab === index || loadedTabs.has(index) ? tab.videoSrc : ''"
                @ended="onVideoEnded"
              >
              </video>
            </div>

            <!-- Active Tab Content Details -->
            <div class="mt-8 sm:mt-10 text-left px-1">
              <div class="text-xs font-bold text-[#D97757] tracking-widest uppercase mb-3 font-mono">
                {{ tabs[activeTab].label }}
              </div>
              <h3 class="font-display text-2xl sm:text-3xl font-extrabold text-gray-900 mb-4 tracking-tight">
                {{ tabs[activeTab].title }}
              </h3>
              <p class="text-gray-600 text-sm sm:text-base leading-relaxed max-w-xl">
                {{ tabs[activeTab].bodyText }}
              </p>
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    <!-- Get Started Installer Section (Standalone) -->
    <div class="relative z-20 bg-white pt-12 pb-12 sm:pt-16 sm:pb-16">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ INSTALLER</div>
          <div>[5/9]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <!-- Header Row (Title and Description) -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 mb-10 sm:mb-12 items-start lg:items-center">
          <div>
            <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)]">
              60-Second <span class="italic font-medium"><span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Setup.</span></span>
            </h2>
          </div>
          <div>
            <p class="text-base text-gray-500 leading-relaxed font-normal">
              No complex onboarding or data migrations. Install the MCP server and connect your workspace instantly.
            </p>
          </div>
        </div>

        <!-- Interactive Get Started Command Block (Pinecone Style) -->
        <div class="p-8 sm:p-10 bg-white border border-dashed border-gray-300 rounded-none relative overflow-hidden text-left shadow-sm">
          <!-- Corner Brackets -->
          <div class="absolute -top-1 -left-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -top-1 -right-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-6 border-b border-gray-200/60 pb-5">
            <div>
              <h4 class="text-xs uppercase font-bold tracking-widest text-gray-400">Get Started</h4>
            </div>
            
            <!-- Navigation Option Tabs -->
            <div class="flex flex-wrap gap-x-6 gap-y-2 items-center">
              <button 
                v-for="tab in getStartedTabs" 
                :key="tab.id"
                @click="activeGetStartedTab = tab.id"
                :class="activeGetStartedTab === tab.id ? 'border-b-2 border-[#D97757] text-[#D97757] font-semibold' : 'border-b-2 border-transparent text-gray-500 hover:text-gray-800'"
                class="pb-1 text-xs font-mono transition-all duration-200"
              >
                {{ '{' + tab.name + '}' }}
              </button>
            </div>
            
            <div>
              <a href="/docs/" target="_blank" class="text-xs font-semibold text-[#D97757] hover:underline inline-flex items-center gap-1">
                View Docs <svg class="w-3 h-3 text-[#D97757]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" /></svg>
              </a>
            </div>
          </div>

          <!-- Command Installer Codeblock -->
          <div class="relative bg-gray-50 border border-dashed border-gray-300 rounded-none p-4 font-mono text-xs sm:text-sm text-gray-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <!-- Corner Brackets -->
            <div class="absolute -top-1 -left-1 w-2.5 h-2.5 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -top-1 -right-1 w-2.5 h-2.5 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
            </div>

            <div class="flex items-center gap-2 overflow-x-auto whitespace-nowrap scrollbar-none py-1 select-all">
              <span class="text-[#D97757] select-none font-bold">$</span>
              <span>{{ getStartedCommand }}</span>
            </div>

            <button 
              @click="copyGetStartedCommand" 
              class="flex-shrink-0 self-end sm:self-auto inline-flex items-center justify-center gap-1.5 px-4.5 py-2 bg-white border border-gray-200 rounded-none text-xs font-bold text-gray-700 hover:bg-gray-50 transition-colors shadow-sm select-none"
            >
              <svg v-if="getStartedCopied" class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
              </svg>
              <svg v-else class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
              </svg>
              <span>{{ getStartedCopied ? 'Copied!' : 'Copy' }}</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    
<!-- How It Works Section -->
    <div id="how-it-works" ref="howItWorksSectionRef" data-theme="light" class="pt-6 pb-12 sm:pt-8 sm:pb-16 bg-white relative z-25">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ HOW IT WORKS</div>
          <div>[2/8]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <!-- Header Row (Title, Subtitle, and Docs Button) -->
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6">
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)]">
            How <span class="italic font-medium">Memwyre <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">works.</span></span>
          </h2>
          <a href="/docs/" target="_blank" class="mt-4 md:mt-0 w-auto px-6 py-2 bg-white text-[#050614] font-bold rounded border border-gray-300 hover:bg-gray-50 transition-all duration-300 text-sm inline-flex items-center justify-center">
            Read the docs
          </a>
        </div>
        <p class="max-w-3xl text-base text-gray-500 leading-relaxed font-normal mb-12">
          Memwyre is the unified memory layer built for your AI workflow. Save context once, and access it automatically across every tool.
        </p>

        <!-- 3-Column Bordered Card Grid -->
        <div 
          class="border border-gray-200/85 rounded-lg overflow-hidden bg-white relative z-20"
        >
          <div class="grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-gray-200/85">
            
            <!-- Column 1: Save Once -->
            <div 
              class="p-8 sm:p-10 flex flex-col justify-between min-h-[380px] transition-colors duration-300"
              :class="{ 'bg-gray-50/50': activeStep === 0 }"
            >
              <div>
                <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-6">01 . SAVE ONCE</div>
                <div class="mb-4">
                  <div class="text-xl sm:text-2xl font-bold text-[#D97757] tracking-tight">Instant</div>
                  <div class="text-sm sm:text-base font-semibold text-gray-900 leading-tight mt-1">context capture</div>
                </div>
                <p class="text-gray-500 text-sm leading-relaxed mb-6">
                  Save prompts, guidelines, or database schemas with one click. They stream directly to your shared memory layer.
                </p>
              </div>
              
              <div>
                <!-- Visual Element: Progressively Raising Bars -->
                <div class="flex items-end gap-2 w-full h-20 mb-4">
                  <div v-for="i in 8" :key="i" 
                    class="flex-1 bg-[#D97757] border border-black rounded-t transition-all duration-300 origin-bottom"
                    :style="{ 
                      height: (30 + i * 8) + '%', 
                      opacity: activeStep === 0 ? 0.95 : 0.3,
                      transform: `scaleY(${getIngestBarScaleY(i - 1)})`
                    }"></div>
                </div>
                <div class="text-xs tracking-widest uppercase font-bold font-mono text-gray-400">mcp &amp; browser streams</div>
              </div>
            </div>

            <!-- Column 2: AI Connects -->
            <div 
              class="p-8 sm:p-10 flex flex-col justify-between min-h-[380px] transition-colors duration-300"
              :class="{ 'bg-gray-50/50': activeStep === 1 }"
            >
              <div>
                <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-6">02 . AI CONNECTS</div>
                <div class="mb-4">
                  <div class="text-xl sm:text-2xl font-bold text-[#D97757] tracking-tight">Dynamic</div>
                  <div class="text-sm sm:text-base font-semibold text-gray-900 leading-tight mt-1">no manual tagging</div>
                </div>
                <p class="text-gray-500 text-sm leading-relaxed mb-6">
                  Our platform automatically parses facts, resolves entities, and links context in the background to build a connected memory graph.
                </p>
              </div>

              <div>
                <!-- Visual Element: Indexing Bar Graph -->
                <div class="flex items-end gap-2 w-full h-20 mb-4">
                  <div v-for="(height, idx) in [40, 65, 50, 85, 30, 75, 60, 45]" :key="idx" 
                    class="flex-1 bg-[#D97757] border border-black rounded-t transition-all duration-500 origin-bottom"
                    :class="{ 'animate-raise-random': activeStep === 1 }"
                    :style="{ 
                      height: height + '%', 
                      opacity: activeStep === 1 ? 0.95 : 0.3,
                      animationDelay: (idx * 0.07) + 's',
                      animationDuration: [1.1, 0.7, 1.3, 0.9, 1.2, 0.8, 1.4, 1.0][idx] + 's',
                      transform: activeStep === 1 ? 'none' : 'scaleY(0.5)'
                    }"></div>
                </div>
                <div class="text-xs tracking-widest uppercase font-bold font-mono text-gray-400">continuous background indexing</div>
              </div>
            </div>

            <!-- Column 3: Remember Everywhere -->
            <div 
              class="p-8 sm:p-10 flex flex-col justify-between min-h-[380px] transition-colors duration-300"
              :class="{ 'bg-gray-50/50': activeStep === 2 }"
            >
              <div>
                <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-6">03 . REMEMBER EVERYWHERE</div>
                <div class="mb-4">
                  <div class="text-xl sm:text-2xl font-bold text-[#D97757] tracking-tight">Instant</div>
                  <div class="text-sm sm:text-base font-semibold text-gray-900 leading-tight mt-1">context injection</div>
                </div>
                <p class="text-gray-500 text-sm leading-relaxed mb-6">
                  Query from Cursor composition, Claude Desktop, ChatGPT, or terminal. The correct context is injected without manual copy-pasting.
                </p>
              </div>

              <div>
                <!-- Visual Element: SVG Latency Area/Line Chart -->
                <div class="h-20 w-full relative pr-4 mb-4">
                  <svg viewBox="0 0 100 30" class="w-full h-full overflow-visible" preserveAspectRatio="none">
                    <defs>
                      <linearGradient id="queryGrad" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#D97757" :stop-opacity="activeStep === 2 ? 0.25 : 0.08" />
                        <stop offset="100%" stop-color="#D97757" stop-opacity="0" />
                      </linearGradient>
                      <clipPath id="queryClip">
                        <rect x="0" y="0" width="100" height="30" 
                          class="transition-transform duration-1000 ease-out origin-left" 
                          :style="{ transform: activeStep === 2 ? 'scaleX(1)' : 'scaleX(0)' }" />
                      </clipPath>
                    </defs>
                    <!-- Area -->
                    <path d="M0,30 Q25,20 50,15 T100,5 L100,30 Z" fill="url(#queryGrad)" clip-path="url(#queryClip)" />
                    <!-- Line -->
                    <path d="M0,30 Q25,20 50,15 T100,5" fill="none" stroke="#D97757" stroke-width="2" 
                      class="transition-all duration-1000 ease-out" 
                      :style="{ 
                        opacity: activeStep === 2 ? 0.9 : 0.3,
                        strokeDasharray: 120,
                        strokeDashoffset: activeStep === 2 ? 0 : 120
                      }" />
                    <!-- Dot -->
                    <circle cx="100" cy="5" r="3" fill="#D97757" 
                      class="transition-all duration-300 delay-[800ms]" 
                      :style="{ 
                        opacity: activeStep === 2 ? 1 : 0,
                        transform: activeStep === 2 ? 'scale(1)' : 'scale(0)',
                        transformOrigin: '100px 5px'
                      }" />
                  </svg>
                </div>
                <div class="text-xs tracking-widest uppercase font-bold font-mono text-gray-400">p99 query recall</div>
              </div>
            </div>

          </div>

          <!-- Bottom sliding progress indicator line -->
          <div class="w-full h-[3px] bg-gray-200/50 relative">
            <div 
              class="absolute top-0 bottom-0 h-full bg-[#D97757]"
              :style="{ 
                width: stepProgress + '%' 
              }"
            ></div>
          </div>
        </div>

      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    
<!-- Benchmark Section (LIGHT) -->
    <div id="benchmark" ref="benchmarkSectionRef" data-theme="light"
      class="relative pt-6 pb-12 sm:pt-8 sm:pb-16 text-gray-900 z-25">

      <div class="relative z-10 max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ BENCHMARK</div>
          <div>[4/8]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
          
          <!-- Left Column: Title, Subtitle, and Metrics -->
          <div class="lg:col-span-5 text-center lg:text-left flex flex-col items-center lg:items-start">
            <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-3">
              <span class="italic font-medium">LoCoMo <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Benchmark.</span></span>
            </h2>
            <p class="text-gray-500 text-sm sm:text-base font-medium mb-4">1,540 questions &bull; 5 categories</p>
            <p class="text-base text-gray-500 leading-relaxed font-normal mb-6 max-w-xl text-center lg:text-left">
              If your memory platform returns noisy facts or misses key details, your AI writes broken code. Retrieval quality dictates the quality of your AI outcomes. Here is how Memwyre's accuracy compares on the MemoryBench long-context evaluation dataset:
            </p>
            
            <div class="mb-8">
              <router-link to="/ai-memory-benchmark-locomo" class="inline-flex items-center gap-2 px-5 py-2.5 border border-gray-300 bg-white text-gray-700 rounded font-medium text-sm transition-all duration-300 hover:bg-gray-50 hover:border-gray-400 hover:text-gray-900 shadow-sm">
                <span>Read Research</span>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="w-4 h-4 text-gray-400">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                </svg>
              </router-link>
            </div>
            
            <!-- Metric Cards stacked vertically -->
            <div class="space-y-4 w-full max-w-md">
              <div class="relative flex items-center gap-5 bg-white border border-dashed border-gray-300 rounded p-5 shadow-sm transition-all duration-300 hover:border-gray-400 hover:shadow-md">
                <!-- Corner Brackets -->
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -top-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="text-[#D97757] text-4xl font-extrabold font-mono tracking-tight">73.5</div>
                <div class="text-left">
                  <div class="text-gray-900 font-bold text-base leading-tight">Overall Accuracy</div>
                  <div class="text-gray-500 text-xs tracking-widest uppercase font-semibold mt-0.5">Benchmark Score</div>
                </div>
              </div>
              <div class="relative flex items-center gap-5 bg-white border border-dashed border-gray-300 rounded p-5 shadow-sm transition-all duration-300 hover:border-gray-400 hover:shadow-md">
                <!-- Corner Brackets -->
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -top-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="text-gray-900 text-4xl font-extrabold font-mono tracking-tight">3000</div>
                <div class="text-left">
                  <div class="text-gray-900 font-bold text-base leading-tight">Mean Tokens</div>
                  <div class="text-gray-500 text-xs tracking-widest uppercase font-semibold mt-0.5">Average Context Size</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Bar Chart -->
          <div class="lg:col-span-7 w-full">
            <div class="relative p-3 border border-dashed border-gray-300 rounded bg-gray-50/50">
              <!-- Corner Brackets (Crosshairs) -->
              <div class="absolute -top-2 -left-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -top-2 -right-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-2 -left-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-2 -right-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>

              <div class="hidden md:block p-4 sm:p-8 relative w-full bg-white border border-gray-250 rounded shadow-sm">
                <!-- Horizontal dashed gridlines -->
                <div class="absolute inset-x-8 sm:inset-x-12 top-4 bottom-20 flex flex-col justify-between pointer-events-none z-0">
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                </div>

                <!-- Chart Area -->
                <div class="relative z-10 h-72 sm:h-96 flex items-end justify-between px-2 sm:px-6">
                  <!-- Category 1: Single-hop -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">53.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 53.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">80.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 80.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 2: Multi-hop -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">24.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 24.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">45.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 45.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 3: Open-domain -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">50.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 50.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">76.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 76.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 4: Temporal -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">48.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 48.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">74.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 74.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Bottom labels (X-axis) -->
                <div class="flex justify-between px-2 sm:px-6 border-t border-gray-200 pt-4 relative z-10 text-xs sm:text-sm font-medium text-gray-500">
                  <div class="flex-1 text-center">Single-hop</div>
                  <div class="flex-1 text-center">Multi-hop</div>
                  <div class="flex-1 text-center">Open-domain</div>
                  <div class="flex-1 text-center">Temporal</div>
                </div>

                <!-- Legend and Footer -->
                <div class="flex justify-between items-center mt-10 px-2 sm:px-6 relative z-10 text-xs tracking-wider uppercase font-bold">
                  <!-- Legend -->
                  <div class="flex items-center gap-6">
                    <div class="flex items-center gap-2">
                      <span class="w-3 h-3 bg-zinc-300 rounded-sm"></span>
                      <span class="text-gray-500">Old</span>
                    </div>
                    <div class="flex items-center gap-2">
                      <span class="w-3 h-3 bg-[#D97757] rounded-sm"></span>
                      <span class="text-gray-600">New</span>
                    </div>
                  </div>
                  <!-- Sublabel -->
                  <div class="text-gray-400 tracking-widest font-mono">LOCOMO</div>
                </div>

              </div>

              <!-- Mobile horizontal chart version (visible on mobile only) -->
              <div class="block md:hidden p-5 relative w-full bg-white border border-gray-250 rounded shadow-sm text-left">
                <h4 class="text-xs uppercase font-bold tracking-wider text-gray-400 font-mono mb-4">/ Accuracy Metrics</h4>
                
                <div class="space-y-4">
                  <!-- Category 1: Single-hop -->
                  <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs font-semibold text-gray-800">
                      <span>Single-hop</span>
                      <span class="font-mono text-[10px] text-gray-400">Old: 53.0% / <span class="text-[#D97757] font-bold">New: 80.0%</span></span>
                    </div>
                    <div class="space-y-1">
                      <!-- Old Bar -->
                      <div class="w-full bg-gray-150 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-zinc-300 h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '53.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.1) 6px, rgba(0, 0, 0, 0.1) 7px);"></div>
                      </div>
                      <!-- New Bar -->
                      <div class="w-full bg-[#D97757]/10 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-[#D97757] h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '80.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.25) 6px, rgba(0, 0, 0, 0.25) 7px);"></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 2: Multi-hop -->
                  <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs font-semibold text-gray-800">
                      <span>Multi-hop</span>
                      <span class="font-mono text-[10px] text-gray-400">Old: 24.0% / <span class="text-[#D97757] font-bold">New: 45.0%</span></span>
                    </div>
                    <div class="space-y-1">
                      <!-- Old Bar -->
                      <div class="w-full bg-gray-150 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-zinc-300 h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '24.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.1) 6px, rgba(0, 0, 0, 0.1) 7px);"></div>
                      </div>
                      <!-- New Bar -->
                      <div class="w-full bg-[#D97757]/10 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-[#D97757] h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '45.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.25) 6px, rgba(0, 0, 0, 0.25) 7px);"></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 3: Open-domain -->
                  <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs font-semibold text-gray-800">
                      <span>Open-domain</span>
                      <span class="font-mono text-[10px] text-gray-400">Old: 50.0% / <span class="text-[#D97757] font-bold">New: 76.0%</span></span>
                    </div>
                    <div class="space-y-1">
                      <!-- Old Bar -->
                      <div class="w-full bg-gray-150 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-zinc-300 h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '50.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.1) 6px, rgba(0, 0, 0, 0.1) 7px);"></div>
                      </div>
                      <!-- New Bar -->
                      <div class="w-full bg-[#D97757]/10 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-[#D97757] h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '76.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.25) 6px, rgba(0, 0, 0, 0.25) 7px);"></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 4: Temporal -->
                  <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs font-semibold text-gray-800">
                      <span>Temporal</span>
                      <span class="font-mono text-[10px] text-gray-400">Old: 48.0% / <span class="text-[#D97757] font-bold">New: 74.0%</span></span>
                    </div>
                    <div class="space-y-1">
                      <!-- Old Bar -->
                      <div class="w-full bg-gray-150 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-zinc-300 h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '48.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.1) 6px, rgba(0, 0, 0, 0.1) 7px);"></div>
                      </div>
                      <!-- New Bar -->
                      <div class="w-full bg-[#D97757]/10 h-2.5 rounded overflow-hidden relative">
                        <div class="bg-[#D97757] h-full rounded transition-all duration-1000 ease-out origin-left scale-x-0" :class="{ 'scale-x-100': animateBars }" :style="{ width: animateBars ? '74.0%' : '0%' }" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 6px, rgba(0, 0, 0, 0.25) 6px, rgba(0, 0, 0, 0.25) 7px);"></div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mobile Legend -->
                <div class="flex justify-between items-center mt-6 text-[10px] font-bold uppercase tracking-wider text-gray-400 font-mono">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5">
                      <span class="w-2.5 h-2.5 bg-zinc-300 rounded-sm"></span>
                      <span>Old</span>
                    </div>
                    <div class="flex items-center gap-1.5">
                      <span class="w-2.5 h-2.5 bg-[#D97757] rounded-sm"></span>
                      <span>New</span>
                    </div>
                  </div>
                  <span>LOCOMO</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    <!-- Memory vs RAG Section -->
    <div class="relative z-20 bg-white py-6 sm:py-8">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        <div ref="comparisonSectionRef" class="p-8 sm:p-10 bg-gradient-to-r from-white via-[#FAF9F6] to-[#FAF6F0] border border-dashed border-gray-300 rounded-none relative overflow-hidden text-left shadow-sm">
          <!-- Corner Brackets -->
          <div class="absolute -top-1 -left-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -top-1 -right-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 pointer-events-none">
            <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
            
            <!-- Left Column: Latency Chart -->
            <div class="lg:col-span-7 w-full flex flex-col items-start text-left">
              <h3 class="text-2xl sm:text-3xl font-bold tracking-tight mb-1 text-gray-900 font-display">Memory vs RAG</h3>
              <p class="text-gray-500 text-xs sm:text-sm font-medium mb-3">Latency (seconds)</p>
              
              <div class="relative w-full h-36 sm:h-56 mt-1 flex pb-6">
                <!-- Y-Axis Labels -->
                <div class="flex flex-col justify-between h-full text-[10px] sm:text-xs font-mono text-gray-400 pr-4 select-none">
                  <span>40</span>
                  <span>30</span>
                  <span>20</span>
                  <span>10</span>
                  <span>0</span>
                </div>
                
                <!-- Grid & Bars Container -->
                <div class="relative flex-1 h-full border-l border-gray-200">
                  <!-- Horizontal Grid Lines -->
                  <div class="absolute inset-0 flex flex-col justify-between pointer-events-none z-0">
                    <div class="w-full border-t border-gray-200/60"></div>
                    <div class="w-full border-t border-gray-200/60"></div>
                    <div class="w-full border-t border-gray-200/60"></div>
                    <div class="w-full border-t border-gray-200/60"></div>
                    <div class="w-full border-b border-gray-200"></div>
                  </div>
                  
                  <!-- Bars -->
                  <div class="relative z-10 h-full flex justify-around items-end px-4 sm:px-12">
                    <!-- Memory Bar -->
                    <div class="w-16 sm:w-24 h-full relative">
                      <span 
                        class="absolute left-1/2 -translate-x-1/2 text-[#D97757] font-bold text-xs sm:text-sm font-mono transition-all duration-1000 ease-out whitespace-nowrap" 
                        :class="{ 'opacity-100': animateComparisonBars, 'opacity-0': !animateComparisonBars }"
                        :style="{ bottom: animateComparisonBars ? 'calc(30% + 8px)' : '8px' }"
                      >
                        12s
                      </span>
                      <div 
                        class="w-full bg-[#D97757] rounded-t-md transition-all duration-1000 ease-out origin-bottom shadow-sm absolute bottom-0"
                        :style="{ height: animateComparisonBars ? '30%' : '0%' }"
                      ></div>
                      <span class="absolute -bottom-6 left-1/2 -translate-x-1/2 text-xs sm:text-sm text-gray-700 font-medium whitespace-nowrap">Memory</span>
                    </div>
                    
                    <!-- RAG Bar -->
                    <div class="w-16 sm:w-24 h-full relative">
                      <span 
                        class="absolute left-1/2 -translate-x-1/2 text-gray-400 font-bold text-xs sm:text-sm font-mono transition-all duration-1000 ease-out whitespace-nowrap" 
                        :class="{ 'opacity-100': animateComparisonBars, 'opacity-0': !animateComparisonBars }"
                        :style="{ bottom: animateComparisonBars ? 'calc(100% + 8px)' : '8px' }"
                      >
                        40s
                      </span>
                      <div 
                        class="w-full bg-gray-200 rounded-t-md transition-all duration-1000 ease-out origin-bottom shadow-sm absolute bottom-0"
                        :style="{ height: animateComparisonBars ? '100%' : '0%' }"
                      ></div>
                      <span class="absolute -bottom-6 left-1/2 -translate-x-1/2 text-xs sm:text-sm text-gray-550 font-medium whitespace-nowrap">RAG</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Right Column: Stats & view on X -->
            <div class="lg:col-span-5 flex flex-col items-start text-left lg:pl-6">
              <div class="text-[70px] sm:text-[85px] font-extrabold leading-none tracking-tighter mb-1 font-mono text-[#D97757]">{{ fewerTokensPercent }}%</div>
              <h4 class="text-xl sm:text-2xl font-bold tracking-tight mb-1 text-gray-900">Fewer tokens</h4>
              <p class="text-gray-500 text-xs sm:text-sm mb-5 max-w-sm">Compared to RAG baseline</p>
              
              <!-- VIEW ON X Button -->
              <a 
                href="https://x.com/Memwyre" 
                target="_blank"
                class="inline-flex items-center border border-black/20 hover:bg-black/5 text-gray-900 transition-colors duration-200 text-sm font-semibold tracking-wider rounded-none overflow-hidden select-none"
              >
                <span class="px-6 py-3 border-r border-black/20 uppercase">View on X</span>
                <span class="px-4 py-3 flex items-center justify-center">
                  <svg class="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </span>
              </a>
            </div>
            
          </div>
        </div>
      </div>
    </div>





    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    
<!-- Ecosystem Section (LIGHT BLEND) -->
    <div id="ecosystem" data-theme="light" class="relative pt-6 pb-12 sm:pt-8 sm:pb-16 bg-white z-25">

      <div class="relative z-10 max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ TECHNICAL SPECS</div>
          <div>[7/9]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 mb-10 sm:mb-12 items-start lg:items-center">
          <div>
            <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)]">
              Universal <span class="italic font-medium">shared <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">architecture.</span></span>
            </h2>
          </div>
          <div>
            <p class="text-base text-gray-500 leading-relaxed font-normal">
              Plugs into your editor and workflow using Model Context Protocol (MCP) and secure CLI plugin hooks.
            </p>
          </div>
        </div>

        <div class="flex lg:grid flex-nowrap lg:grid-cols-3 items-stretch gap-6 lg:gap-8 overflow-x-auto no-scrollbar scrollbar-none snap-x snap-mandatory -mx-8 lg:mx-0 px-8 lg:px-0 pb-6 lg:pb-0">
          <div
            @click="$router.push('/mcp')"
            class="w-[285px] sm:w-[370px] lg:w-full shrink-0 snap-align-start p-6 lg:p-10 bg-white border border-gray-300/80 rounded transition-all duration-300 relative overflow-hidden group hover:border-gray-400 cursor-pointer">
            <!-- Tilted MCP Background Icon -->
            <div
              class="absolute z-0 -top-12 -right-12 w-52 h-52 opacity-[0.10] group-hover:opacity-[0.16] rotate-[20deg] pointer-events-none transition-opacity duration-500 text-black">
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
            <h3 class="relative z-10 text-xl lg:text-2xl font-bold mb-4 mt-8 text-black">MCP Server</h3>
            <p class="relative z-10 text-sm lg:text-base text-gray-600 mb-8">
              Connect Memwyre directly to Claude Desktop or any MCP-compliant client. Give your AI assistant
              direct access to your knowledge base.
            </p>
            <div class="relative z-10 bg-gray-50 border border-dashed border-gray-300 rounded p-4 font-mono text-[11px] lg:text-xs text-gray-700">
              <!-- Corner Brackets -->
              <div class="absolute -top-1 -left-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -top-1 -right-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              $ npx -y mcp-remote https://server.memwyre.tech/mcp
            </div>
          </div>

          <div
            @click="$router.push('/extension')"
            class="w-[285px] sm:w-[370px] lg:w-full shrink-0 snap-align-start p-6 lg:p-10 bg-white border border-gray-300/80 rounded transition-all duration-300 relative overflow-hidden group hover:border-gray-400 cursor-pointer">
            <!-- Tilted Chrome Background Icon -->
            <img src="@/assets/chrome-logo-svgrepo-com.svg" alt=""
              class="absolute z-0 -top-14 -right-14 w-56 h-56 opacity-[0.10] group-hover:opacity-[0.16] rotate-[25deg] pointer-events-none transition-opacity duration-500" />

            <h3 class="relative z-10 text-xl lg:text-2xl font-bold mb-4 mt-8 text-black">Browser Extension</h3>
            <p class="relative z-10 text-sm lg:text-base text-gray-600 mb-8">
              The easiest way to feed context into your memory platform. Clip code snippets, documentation, or chats instantly.
            </p>
            <div
              class="relative z-10 inline-flex items-center gap-2 lg:gap-3 px-3 py-1.5 lg:px-4 lg:py-2 rounded border border-dashed border-gray-300 bg-gray-50 text-gray-800 text-xs lg:text-sm font-bold">
              <!-- Corner Brackets -->
              <div class="absolute -top-1 -left-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -top-1 -right-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-6 h-6" />
              <img src="@/assets/microsoft-edge-logo.svg" alt="Edge" class="w-6 h-6" />
              <span>Chrome &amp; Edge</span>
            </div>
          </div>

          <div
            @click="$router.push('/plugins')"
            class="w-[285px] sm:w-[370px] lg:w-full shrink-0 snap-align-start p-6 lg:p-10 bg-white border border-gray-300/80 rounded transition-all duration-300 relative overflow-hidden group hover:border-gray-400 cursor-pointer">
            <!-- Tilted OpenClaw Background Icon -->
            <img src="@/assets/openclaw-color.svg" alt=""
              class="absolute z-0 -top-12 -right-12 w-52 h-52 opacity-[0.10] group-hover:opacity-[0.16] rotate-[20deg] pointer-events-none transition-opacity duration-500" />

            <h3 class="relative z-10 text-xl lg:text-2xl font-bold mb-4 mt-8 text-black">OpenClaw Plugin</h3>
            <p class="relative z-10 text-sm lg:text-base text-gray-600 mb-8">
              Give autonomous agents persistent memory. The OpenClaw plugin lets AI agents save and recall context
              from your vault automatically.
            </p>
            <div class="relative z-10 bg-gray-50 border border-dashed border-gray-300 rounded p-4 font-mono text-[11px] lg:text-xs text-gray-700">
              <!-- Corner Brackets -->
              <div class="absolute -top-1 -left-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -top-1 -right-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 pointer-events-none">
                <div class="absolute top-1 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-1 top-0 h-full w-px bg-gray-400"></div>
              </div>
              $ openclaw plugins install @memwyre/openclaw
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    
<!-- Pricing Section -->
    <div id="pricing" data-theme="light" class="pt-6 pb-0 bg-white relative z-25">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ PRICING</div>
          <div>[8/9]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <!-- Title / Header info -->
        <div class="text-center mb-12 sm:mb-16">
          <p class="hero-serif text-4xl sm:text-5xl tracking-tight text-gray-900 leading-[1.1]">
            AI that works where <span class="italic font-medium">your team <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">works.</span></span>
          </p>
          <p class="mt-4 text-base text-gray-500 max-w-xl mx-auto">
            Simple, transparent pricing for individuals and teams. Start building your persistent AI memory layer today.
          </p>
        </div>

        <!-- 3-Column Bordered Grid matching "How It Works" Section -->
        <div class="lg:border-y lg:border-gray-300 rounded-none bg-white relative z-20 -mx-8 sm:-mx-8 lg:-mx-12">
          <div class="flex lg:grid flex-nowrap lg:grid-cols-3 items-stretch gap-6 lg:gap-0 overflow-x-auto no-scrollbar scrollbar-none snap-x snap-mandatory px-8 lg:px-0 py-4 lg:py-0">
            
            <!-- Free Plan -->
            <div class="w-[290px] sm:w-[390px] lg:w-full shrink-0 snap-align-start pt-6 px-5 pb-5 sm:pt-10 sm:px-10 lg:px-10 sm:pb-5 flex flex-col justify-between h-auto lg:h-full bg-white border border-gray-200 rounded-lg lg:border-0 lg:border-r lg:border-gray-300 lg:rounded-none">
              <div>
                <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-6">01 . FREE</div>
                <div class="mb-4">
                  <div class="text-4xl font-extrabold tracking-tight text-gray-900">$0</div>
                  <div class="text-xs tracking-widest uppercase font-bold font-mono text-gray-400 mt-1">forever</div>
                </div>
                <p class="text-gray-500 text-sm leading-relaxed mb-6">
                  A great way to get started with building your persistent AI memory layer.
                </p>

                <ul class="space-y-4 text-sm text-gray-600">
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Up to 50 memories</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Up to 10 document uploads</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Standard AI token budget</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>IDE Integration (MCP)</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Community Support</span>
                  </li>
                </ul>
              </div>

              <div class="mt-8">
                <router-link to="/signup/"
                  class="inline-flex w-full items-center justify-center rounded bg-gray-50 text-gray-900 border border-gray-200 px-4 py-3.5 text-sm font-bold hover:bg-gray-100 transition-all duration-300 hover:scale-[1.02]">
                  Get Started for Free
                </router-link>
              </div>
            </div>

            <!-- Pro Plan (Recommended) -->
            <div class="w-[290px] sm:w-[390px] lg:w-full shrink-0 snap-align-start pt-6 px-5 pb-5 sm:pt-10 sm:px-10 lg:px-10 sm:pb-5 flex flex-col justify-between h-auto lg:h-full bg-orange-50/10 relative border border-[#D97757]/30 rounded-lg lg:border-0 lg:border-r lg:border-gray-300 lg:rounded-none">
              <div>
                <div class="flex justify-between items-center mb-6">
                  <div class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">02 . PRO</div>
                  <span class="text-[9px] font-bold px-2 py-0.5 rounded bg-[#D97757] text-white uppercase font-mono tracking-wider">
                    Recommended
                  </span>
                </div>
                <div class="mb-4">
                  <div class="text-4xl font-extrabold tracking-tight text-gray-900">$12</div>
                  <div class="text-xs tracking-widest uppercase font-bold font-mono text-gray-400 mt-1">/ month</div>
                </div>
                <p class="text-gray-500 text-sm leading-relaxed mb-6">
                  Everything in Free, plus unlimited storage and priority features.
                </p>

                <div class="flex items-center mb-6">
                  <span class="text-[9px] font-mono font-bold uppercase tracking-widest text-gray-400 mr-3">Integrations</span>
                  <div class="flex items-center -space-x-2.5 isolate">
                    <!-- VS Code -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[10] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/vscode.svg" alt="VS Code" class="w-4.5 h-4.5 object-contain" title="VS Code" />
                    </div>
                    <!-- OpenAI -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[11] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/openai.svg" alt="OpenAI / ChatGPT" class="w-4.5 h-4.5 object-contain" title="OpenAI / ChatGPT" />
                    </div>
                    <!-- Claude Desktop -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[12] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/claude-color.svg" alt="Claude Desktop" class="w-4.5 h-4.5 object-contain" title="Claude Desktop" />
                    </div>
                    <!-- Gemini -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[13] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/gemini-color.svg" alt="Google Gemini" class="w-4.5 h-4.5 object-contain" title="Google Gemini" />
                    </div>
                    <!-- Notion -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[14] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-4.5 h-4.5 object-contain" title="Notion" />
                    </div>
                    <!-- Perplexity -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[15] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-4.5 h-4.5 object-contain" title="Perplexity" />
                    </div>
                    <!-- Claude Code -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[16] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/claudecode-color.svg" alt="Claude Code" class="w-4.5 h-4.5 object-contain" title="Claude Code" />
                    </div>
                    <!-- OpenClaw -->
                    <div class="w-7 h-7 rounded-full bg-white border border-gray-200/80 shadow-sm flex items-center justify-center p-1 relative z-[17] transition-all duration-300 hover:z-[40] hover:-translate-y-1">
                      <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-4.5 h-4.5 object-contain" title="OpenClaw" />
                    </div>
                  </div>
                </div>

                <ul class="space-y-4 text-sm text-gray-600">
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Unlimited memories &amp; documents</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Google Drive &amp; Notion sync</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Claude Code, OpenCode &amp; OpenClaw plugins</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Browser Extension &amp; MCP IDE Server</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Extended daily AI chat quota &amp; support</span>
                  </li>
                </ul>
              </div>

              <div class="mt-8">
                <router-link to="/signup/"
                  class="inline-flex w-full items-center justify-center rounded bg-black text-white px-4 py-3 text-sm font-bold shadow-md hover:bg-gray-800 transition-all duration-300 hover:scale-[1.02]">
                  Start Building Your Brain
                </router-link>
              </div>
            </div>

            <!-- Enterprise Plan -->
            <div class="w-[290px] sm:w-[390px] lg:w-full shrink-0 snap-align-start pt-6 px-5 pb-5 sm:pt-10 sm:px-10 lg:px-10 sm:pb-5 flex flex-col justify-between h-auto lg:h-full bg-white border border-gray-200 rounded-lg lg:border-0 lg:rounded-none">
              <div>
                <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-6">03 . ENTERPRISE</div>
                <div class="mb-4">
                  <div class="text-4xl font-extrabold tracking-tight text-gray-900">Custom</div>
                  <div class="text-xs tracking-widest uppercase font-bold font-mono text-gray-400 mt-1">volume pricing</div>
                </div>
                <p class="text-gray-500 text-sm leading-relaxed mb-6">
                  Tailored deployments for teams that need dedicated infrastructure, SSO, and volume pricing.
                </p>

                <ul class="space-y-4 text-sm text-gray-600">
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Everything in Pro</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Dedicated infrastructure &amp; SSO</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Custom integrations &amp; SLA</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Dedicated support</span>
                  </li>
                </ul>
              </div>

              <div class="mt-8">
                <a href="mailto:shivharehimansh@gmail.com?subject=Memwyre%20Enterprise%20Inquiry"
                  class="inline-flex w-full items-center justify-center rounded bg-gray-50 text-gray-900 border border-gray-200 px-4 py-3.5 text-sm font-bold hover:bg-gray-100 transition-all duration-300 hover:scale-[1.02]">
                  Contact Sales
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    
<!-- Blogs Section -->
    <div id="blog-section" data-theme="light" class="pt-16 pb-16 bg-white relative z-25">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12 text-center">
        <!-- Badge -->
        <div class="inline-flex items-center justify-center px-3 py-1 rounded border border-gray-200 text-xs font-semibold text-gray-800 bg-white shadow-sm font-mono tracking-wider mb-6">
          Blogs
        </div>
        
        <!-- Heading -->
        <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-12">
          Latest from the <span class="italic font-medium">Memwyre <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Blog</span></span>
        </h2>
        
        <!-- Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-12 text-left">
          
          <!-- Blog Card 1 -->
          <router-link to="/blog/mcp-persistent-memory" class="group flex flex-row md:flex-col items-start md:items-stretch gap-4 md:gap-0">
            <div class="w-24 h-16 md:w-full md:h-auto md:aspect-[16/10] shrink-0 rounded overflow-hidden border border-gray-200/85 bg-gray-50 flex items-center justify-center relative">
              <img 
                src="/blog-covers/mcp-persistent-memory.png" 
                alt="How to Give Claude Desktop Persistent Memory using MCP" 
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-[1.02]"
                @error="$event.target.src = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80'"
              />
            </div>
            <div class="flex-1">
              <h3 class="text-sm md:text-base lg:text-lg font-bold text-[rgb(1,1,16)] leading-snug group-hover:text-[#D97757] transition-colors duration-250 md:mt-5 md:mb-2 font-sans">
                How to Give Claude Desktop Persistent Memory using MCP
              </h3>
              <div class="text-[10px] md:text-xs text-gray-500 font-sans mt-1 md:mt-0">
                June 15, 2026 &nbsp;&bull;&nbsp; MCP Server
              </div>
            </div>
          </router-link>

          <!-- Blog Card 2 -->
          <router-link to="/blog/vscode-mcp-persistent-memory" class="group flex flex-row md:flex-col items-start md:items-stretch gap-4 md:gap-0">
            <div class="w-24 h-16 md:w-full md:h-auto md:aspect-[16/10] shrink-0 rounded overflow-hidden border border-gray-200/85 bg-gray-50 flex items-center justify-center relative">
              <img 
                src="/blog-covers/vscode-mcp-persistent-memory.png" 
                alt="How to Enable Persistent Codebase Memory in VS Code with MCP and Cline" 
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-[1.02]"
                @error="$event.target.src = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80'"
              />
            </div>
            <div class="flex-1">
              <h3 class="text-sm md:text-base lg:text-lg font-bold text-[rgb(1,1,16)] leading-snug group-hover:text-[#D97757] transition-colors duration-250 md:mt-5 md:mb-2 font-sans">
                How to Enable Persistent Codebase Memory in VS Code with MCP and Cline
              </h3>
              <div class="text-[10px] md:text-xs text-gray-500 font-sans mt-1 md:mt-0">
                June 02, 2026 &nbsp;&bull;&nbsp; MCP Server
              </div>
            </div>
          </router-link>

          <!-- Blog Card 3 -->
          <router-link to="/blog/claude-code-memory-ingestion" class="group flex flex-row md:flex-col items-start md:items-stretch gap-4 md:gap-0">
            <div class="w-24 h-16 md:w-full md:h-auto md:aspect-[16/10] shrink-0 rounded overflow-hidden border border-gray-200/85 bg-gray-50 flex items-center justify-center relative">
              <img 
                src="/blog-covers/claude-code-memory-ingestion.png" 
                alt="Building Persistent Terminal Sessions: Claude Code Memory Ingestion" 
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-[1.02]"
                @error="$event.target.src = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80'"
              />
            </div>
            <div class="flex-1">
              <h3 class="text-sm md:text-base lg:text-lg font-bold text-[rgb(1,1,16)] leading-snug group-hover:text-[#D97757] transition-colors duration-250 md:mt-5 md:mb-2 font-sans">
                Building Persistent Terminal Sessions: Claude Code Memory Ingestion
              </h3>
              <div class="text-[10px] md:text-xs text-gray-500 font-sans mt-1 md:mt-0">
                May 18, 2026 &nbsp;&bull;&nbsp; CLI Plugins
              </div>
            </div>
          </router-link>

        </div>
      </div>
    </div>

    
<!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    <div id="faq" data-theme="light" class="pt-6 pb-12 sm:pt-8 sm:pb-16 bg-white relative z-25">
      <div class="max-w-7xl mx-auto px-8 sm:px-8 lg:px-12">
        
        <!-- Section Header breadcrumb and details (Supermemory Style) -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ FAQ</div>
          <div>[8/8]</div>
        </div>

        <!-- Divider Line below Breadcrumb -->
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <!-- Header Row -->
        <div class="mb-10 text-left">
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)]">
            Questions &amp; <span class="italic font-medium">answers <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">resolved.</span></span>
          </h2>
        </div>

        <div class="border-t border-gray-200">
          <div v-for="(faq, index) in faqs" :key="index" class="border-b border-gray-200">
            <button @click="toggleFaq(index)" class="flex justify-between items-center w-full text-left py-5 group">
              <span class="text-base font-semibold text-gray-900 group-hover:text-[#D97757] transition-colors duration-200">{{
                faq.question }}</span>
              <span class="ml-4 flex-shrink-0 text-gray-400 font-light text-2xl leading-none transition-colors duration-200 group-hover:text-[#D97757]">
                <span v-if="faq.isOpen">&minus;</span>
                <span v-else>+</span>
              </span>
            </button>
            <div v-show="faq.isOpen" class="text-gray-500 pb-6 leading-relaxed text-sm sm:text-base pr-8">
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>

    <!-- Final CTA Section: Memory and Personality -->
    <div
      class="pt-6 pb-8 sm:pt-8 sm:pb-10 bg-white text-center relative overflow-hidden">
      <!-- Numeric background animation -->
      <NumericBgAnimation :invert="true" class="absolute inset-0 z-0 opacity-40" />

      <div class="max-w-7xl mx-auto px-6 relative z-10">
        <h2 class="hero-serif text-4xl sm:text-6xl lg:text-[72px] tracking-[-0.02em] leading-[1.05] text-[rgb(1,1,16)] mb-8 max-w-4xl mx-auto">
          The second brain <br class="hidden md:block" />
          <span class="block italic font-medium">for <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">your AI.</span></span>
        </h2>

        <div class="relative inline-flex p-3 mt-6 border border-dashed border-gray-300 rounded max-w-max mx-auto z-20">
          <!-- Corner Brackets (Crosshairs) -->
          <div class="absolute -top-2 -left-2 w-4 h-4 pointer-events-none">
            <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -top-2 -right-2 w-4 h-4 pointer-events-none">
            <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-2 -left-2 w-4 h-4 pointer-events-none">
            <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-2 -right-2 w-4 h-4 pointer-events-none">
            <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="flex flex-row items-center justify-start gap-3 sm:gap-4">
            <router-link to="/signup/"
              class="w-auto px-6 py-2.5 sm:px-8 sm:py-3 bg-black text-white font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md text-xs sm:text-base inline-flex items-center justify-center">
              Get Started
            </router-link>
            <router-link to="/#pricing"
              class="w-auto px-6 py-2.5 sm:px-8 sm:py-3 bg-white text-black font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-base inline-flex items-center justify-center">
              Compare Plans
            </router-link>
          </div>
        </div>
      </div>

      <SiteFooter />
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
import { computed, nextTick, ref, onMounted, onUnmounted } from 'vue';
import SiteFooter from '@/components/SiteFooter.vue';
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


// --- Hero Animation & Theme State ---
const heroAnimationMounted = ref(false);
const heroAnimationReady = ref(false);
let shouldRestoreDarkClass = false;

const heroAnimationStyle = computed(() => ({
  opacity: heroAnimationReady.value ? 1 : 0,
  transform: heroAnimationReady.value
    ? 'translate3d(0, 0, 0) scale(1)'
    : 'translate3d(18px, 0, 0) scale(0.985)',
}));

// --- Get Started Installer state & actions ---
const activeGetStartedTab = ref('claude');
const getStartedCopied = ref(false);

const getStartedTabs = [
  { id: 'claude', name: 'Claude Desktop' },
  { id: 'cursor', name: 'Cursor' },
  { id: 'vscode', name: 'VS Code' },
  { id: 'claudecode', name: 'Claude Code' },
  { id: 'codex', name: 'Codex' },
  { id: 'openclaw', name: 'OpenClaw' }
];

const getStartedCommand = computed(() => {
  const tab = activeGetStartedTab.value;
  if (tab === 'openclaw') {
    return 'openclaw plugins install @memwyre/openclaw-plugin';
  } else if (tab === 'claudecode') {
    return 'claude mcp add memwyre -- npx -y mcp-remote https://server.memwyre.tech/mcp';
  } else {
    return `npx -y install-memwyre --${tab}`;
  }
});

const copyGetStartedCommand = async () => {
  try {
    await navigator.clipboard.writeText(getStartedCommand.value);
    getStartedCopied.value = true;
    setTimeout(() => {
      getStartedCopied.value = false;
    }, 2000);
  } catch (err) {
    console.error('Failed to copy text: ', err);
  }
};

const heroCommandCopied = ref(false);
const copyHeroCommand = async () => {
  try {
    await navigator.clipboard.writeText('npx -y install-memwyre');
    heroCommandCopied.value = true;
    setTimeout(() => {
      heroCommandCopied.value = false;
    }, 2000);
  } catch (err) {
    console.error('Failed to copy text: ', err);
  }
};

// --- Benchmark Section Refs & Animation State ---
const animateBars = ref(false);
const benchmarkSectionRef = ref(null);
let benchmarkObserver = null;

// --- Comparison Section Refs & Animation State ---
const animateComparisonBars = ref(false);
const comparisonSectionRef = ref(null);
let comparisonObserver = null;
const fewerTokensPercent = ref(40);

// --- Auto-rotating Feature Showcase State & Logic ---
const activeTab = ref(0);
const progressWidth = ref(0);
const videoRefs = ref([]);
const loadedTabs = ref(new Set([0]));
const activeVideoRef = computed(() => videoRefs.value[activeTab.value]);
const showcaseContainer = ref(null);
let showcaseObserver = null;
const isVisible = ref(false);
let progressFrameId = null;

const tabs = ref([
  {
    num: '01',
    tabTitle: 'Omnipresent Overlay',
    videoSrc: '/demo1.mp4',
    label: '01 / OMNIPRESENT OVERLAY',
    title: 'Access it from any app',
    bodyText: 'Invoke Memwyre instantly over any app. Access your shared memory layer across ChatGPT, Claude, Notion, or email to capture thoughts mid-conversation and sync context in a single click.'
  },
  {
    num: '02',
    tabTitle: 'Cross-Post Context',
    videoSrc: '/demo2.mp4',
    label: '02 / CROSS-POST CONTEXT',
    title: 'Send to any AI in one click',
    bodyText: 'Find notes or past context instantly with semantic search, even without exact keywords. Launch references directly into your preferred LLM without manual copy-pasting.'
  },
  {
    num: '03',
    tabTitle: 'Contextual Chat',
    videoSrc: '/demo3.mp4',
    label: '03 / CONTEXTUAL CHAT',
    title: 'Chat with your notes',
    bodyText: 'Get answers grounded in your saved notes rather than generic web data. View precise inline citations for every source, leveraging an AI that already knows your context.'
  },
  {
    num: '04',
    tabTitle: 'Granular Control',
    videoSrc: '/demo4.mp4',
    label: '04 / GRANULAR CONTROL',
    title: 'You decide what\'s saved',
    bodyText: 'Preview, edit, and tag captured memories before saving to ensure they surface in the right context, while retaining full control over your private shared memory layer.'
  }
]);

const updateProgress = () => {
  const video = activeVideoRef.value;
  if (video && video.duration) {
    progressWidth.value = (video.currentTime / video.duration) * 100;
  } else {
    progressWidth.value = 0;
  }
  if (isVisible.value) {
    progressFrameId = requestAnimationFrame(updateProgress);
  }
};

const startProgressLoop = () => {
  stopProgressLoop();
  if (isVisible.value) {
    progressFrameId = requestAnimationFrame(updateProgress);
  }
};

const stopProgressLoop = () => {
  if (progressFrameId) {
    cancelAnimationFrame(progressFrameId);
    progressFrameId = null;
  }
  progressWidth.value = 0;
};

const playActiveVideo = (reset = false) => {
  videoRefs.value.forEach((vid, i) => {
    if (vid) {
      if (i === activeTab.value) {
        const targetSrc = tabs.value[i].videoSrc;
        const currentSrc = vid.currentSrc || vid.src || '';
        const isSrcLoaded = currentSrc.includes(targetSrc);
        
        if (!isSrcLoaded) {
          vid.load();
        }
        if (reset) {
          vid.currentTime = 0;
        }
        if (isVisible.value) {
          vid.play().catch(() => {});
        }
      } else {
        vid.pause();
        vid.currentTime = 0;
      }
    }
  });
};

const onVideoEnded = () => {
  const nextIndex = (activeTab.value + 1) % tabs.value.length;
  loadedTabs.value.add(nextIndex);
  loadedTabs.value = new Set(loadedTabs.value);
  activeTab.value = nextIndex;
  nextTick(() => {
    startProgressLoop();
    playActiveVideo(true);
  });
};

const selectTab = (index) => {
  loadedTabs.value.add(index);
  loadedTabs.value = new Set(loadedTabs.value);
  activeTab.value = index;
  progressWidth.value = 0;
  nextTick(() => {
    startProgressLoop();
    playActiveVideo(true);
  });
};

const setupShowcaseObserver = () => {
  showcaseObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          isVisible.value = true;
          loadedTabs.value.add(activeTab.value);
          loadedTabs.value = new Set(loadedTabs.value);
          startProgressLoop();
          nextTick(() => {
            playActiveVideo(false);
          });
        } else {
          isVisible.value = false;
          stopProgressLoop();
          if (activeVideoRef.value) {
            activeVideoRef.value.pause();
          }
        }
      });
    },
    { threshold: 0.15 }
  );

  if (showcaseContainer.value) {
    showcaseObserver.observe(showcaseContainer.value);
  }
};

const setupBenchmarkObserver = () => {
  benchmarkObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateBars.value = true;
          if (benchmarkObserver && benchmarkSectionRef.value) {
            benchmarkObserver.unobserve(benchmarkSectionRef.value);
          }
        }
      });
    },
    { threshold: 0.1 }
  );

  if (benchmarkSectionRef.value) {
    benchmarkObserver.observe(benchmarkSectionRef.value);
  }
};

const animateFewerTokens = () => {
  const start = 40;
  const end = 60;
  const duration = 3500; // 3.5 seconds (slower)
  const startTime = performance.now();

  const step = (now) => {
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    // Smooth easeInOutQuad
    const easeProgress = progress < 0.5 
      ? 2 * progress * progress 
      : 1 - Math.pow(-2 * progress + 2, 2) / 2;
    fewerTokensPercent.value = Math.round(start + (end - start) * easeProgress);

    if (progress < 1) {
      requestAnimationFrame(step);
    }
  };

  requestAnimationFrame(step);
};

const setupComparisonObserver = () => {
  comparisonObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateComparisonBars.value = true;
          animateFewerTokens();
          if (comparisonObserver && comparisonSectionRef.value) {
            comparisonObserver.unobserve(comparisonSectionRef.value);
          }
        }
      });
    },
    { threshold: 0.1 }
  );

  if (comparisonSectionRef.value) {
    comparisonObserver.observe(comparisonSectionRef.value);
  }
};

onUnmounted(() => {
  stopProgressLoop();
  stopHowItWorksLoop();
  if (showcaseObserver) showcaseObserver.disconnect();
  if (benchmarkObserver) benchmarkObserver.disconnect();
  if (howItWorksObserver) howItWorksObserver.disconnect();
  if (comparisonObserver) comparisonObserver.disconnect();
});

// --- Animations & Lifecycle Hooks ---
onMounted(() => {
  nextTick(() => {
    requestAnimationFrame(() => {
      heroAnimationMounted.value = true;
      requestAnimationFrame(() => {
        heroAnimationReady.value = true;
      });
    });
  });
  typeWriter();
  setupShowcaseObserver();
  setupBenchmarkObserver();
  setupComparisonObserver();
  setupHowItWorksObserver();
});


// 3. FAQ accordion
const faqs = ref([
  {
    question: "What exactly is Memwyre?",
    answer: "Memwyre is a unified AI memory platform that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It makes this knowledge instantly searchable and reusable by any tool.",
    isOpen: false
  },
  {
    question: "Is there a free plan?",
    answer: "Yes! Memwyre has a generous free tier that includes up to 50 memories, 10 document uploads, 30 AI chat messages, and full IDE integration via MCP. No credit card required — just sign up and start building your memory layer.",
    isOpen: false
  },
  {
    question: "How do I connect Memwyre to Cursor or VS Code?",
    answer: "You can connect Memwyre to Cursor, VS Code, or Claude Desktop using our official Model Context Protocol (MCP) server. This gives your AI assistant direct, real-time access to your entire shared memory layer.",
    isOpen: false
  },
  {
    question: "Do you offer a browser extension?",
    answer: "Yes! The Memwyre browser extension (available for Chrome and Edge) lets you instantly clip text, articles, and code snippets directly into your memory layer without breaking your flow.",
    isOpen: false
  },
  {
    question: "Is my data private and secure?",
    answer: "Absolutely. Your memory layer is fully private and encrypted. Your data is only accessible to you via authenticated sessions and your personal API keys.",
    isOpen: false
  },
  {
    question: "What is the OpenClaw plugin?",
    answer: "The OpenClaw plugin allows autonomous AI agents to read from and write to your Memwyre memory layer. This gives agents persistent memory across runs, letting them build on past debugging sessions and research.",
    isOpen: false
  },
  {
    question: "Why not just use ChatGPT's built-in memory?",
    answer: "ChatGPT memory is locked entirely inside ChatGPT. It cannot be accessed by Claude, Cursor, your terminal agents, or other LLMs. Memwyre acts as a universal, shared memory layer that works across all of these tools simultaneously.",
    isOpen: false
  },
  {
    question: "How is this different from traditional RAG?",
    answer: "Traditional RAG search takes static documents, chunks them, and searches for matches. Memwyre builds active, connected semantic profiles of your project guidelines, API models, and style rules, updating them dynamically in the background.",
    isOpen: false
  },
  {
    question: "How does Memwyre compare to Mem0 or Zep?",
    answer: "Mem0 and Zep are developer databases designed as backend infrastructure for teams building custom agents. Memwyre is a ready-to-use memory platform that connects directly to everyday consumer tools. You can view our detailed feature comparison table above.",
    isOpen: false
  }
]);

const toggleFaq = (index) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen;
};

// 2. Typing Effect
const typedText = ref("> How do I implement the new auth flow?");

const stepProgress = ref(0);
const activeStep = computed(() => {
  if (stepProgress.value < 33.333) return 0;
  if (stepProgress.value < 66.666) return 1;
  return 2;
});

const getIngestBarScaleY = (index) => {
  if (stepProgress.value >= 33.333) return 0.3;
  const normalizedProgress = (stepProgress.value / 33.333) * 100;
  const startThreshold = index * 6;
  const duration = 15;
  if (normalizedProgress < startThreshold) return 0.3;
  if (normalizedProgress > startThreshold + duration) return 1.0;
  const pct = (normalizedProgress - startThreshold) / duration;
  return 0.3 + pct * 0.7;
};

// --- Auto-rotating How It Works Grid ---
const howItWorksSectionRef = ref(null);
const isHowItWorksVisible = ref(false);
let howItWorksObserver = null;
let howItWorksFrameId = null;

let lastHowItWorksTime = 0;
const rotateSteps = (timestamp) => {
  if (!lastHowItWorksTime) lastHowItWorksTime = timestamp;
  const delta = timestamp - lastHowItWorksTime;
  lastHowItWorksTime = timestamp;

  if (isHowItWorksVisible.value) {
    stepProgress.value += (delta / 6000) * 100; // 6000ms for full loop (2000ms per step)
    if (stepProgress.value >= 100) {
      stepProgress.value = stepProgress.value % 100;
    }
  }

  if (isHowItWorksVisible.value) {
    howItWorksFrameId = requestAnimationFrame(rotateSteps);
  } else {
    lastHowItWorksTime = 0;
  }
};

const startHowItWorksLoop = () => {
  stopHowItWorksLoop();
  if (isHowItWorksVisible.value) {
    lastHowItWorksTime = 0;
    howItWorksFrameId = requestAnimationFrame(rotateSteps);
  }
};

const stopHowItWorksLoop = () => {
  if (howItWorksFrameId) {
    cancelAnimationFrame(howItWorksFrameId);
    howItWorksFrameId = null;
  }
  stepProgress.value = 0;
};

const setupHowItWorksObserver = () => {
  howItWorksObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          isHowItWorksVisible.value = true;
          startHowItWorksLoop();
        } else {
          isHowItWorksVisible.value = false;
          stopHowItWorksLoop();
        }
      });
    },
    { threshold: 0.15 }
  );

  if (howItWorksSectionRef.value) {
    howItWorksObserver.observe(howItWorksSectionRef.value);
  }
};

const typeWriter = () => {
  // No-op - text is now pre-typed
};

</script>

<style scoped>
@keyframes pulse-flow {
  0%, 100% { opacity: 0.25; transform: scaleX(1); }
  50% { opacity: 0.9; transform: scaleX(1.15); }
}



.animate-raise-random {
  animation: raise-random 1s infinite ease-in-out;
}
@keyframes raise-random {
  0%, 100% { transform: scaleY(0.5); }
  50% { transform: scaleY(1); }
}

html {
  scroll-behavior: smooth;
}

/* Force light mode — override dark theme CSS variables */
.hero-wash {
  /* background:
    radial-gradient(circle at 23% 14%, rgba(255, 231, 92, 0.72), transparent 30%),
    radial-gradient(circle at 74% 30%, rgba(255, 235, 125, 0.76), transparent 32%),
    radial-gradient(circle at 12% 86%, rgba(149, 205, 255, 0.68), transparent 34%),
    radial-gradient(circle at 88% 91%, rgba(175, 220, 255, 0.62), transparent 32%),
    linear-gradient(115deg, #fff7ca 0%, #fffdf4 43%, #eff8ff 100%); */
  background: white;
}

.hero-grain {
  /* background-image:
    linear-gradient(115deg, rgba(255, 255, 255, 0.6), transparent 52%),
    radial-gradient(circle at center, rgba(5, 6, 20, 0.05) 1px, transparent 1px);
  background-size: auto, 28px 28px; */
  display: none;
  opacity: 0.34;
}

.hero-animation-layer {
  opacity: 0;
  transform: translate3d(18px, 0, 0) scale(0.985);
  transition: opacity 900ms cubic-bezier(0.16, 1, 0.3, 1), transform 900ms cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

.hero-animation-layer.hero-animation-layer-ready {
  opacity: 1;
  transform: translate3d(0, 0, 0) scale(1);
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

@media (max-width: 512px) {
  .hero-visual {
    margin-top: -34px;
    transform: rotate(-19deg) scale(0.66);
    min-height: 330px;
  }
}

/* General mobile optimizations for all mobile screens */
@media (max-width: 512px) {
  .hero-wash {
    padding-top: 3rem !important;
    padding-bottom: 2rem !important;
    min-height: calc(100svh - 64px) !important;
  }

  .hero-wash .pt-20 {
    padding-top: 1.5rem !important;
  }

  .hero-wash h1 {
    font-size: 2.25rem !important;
    line-height: 1.25 !important;
  }

  .hero-wash h1 br {
    display: none !important;
  }

  .hero-wash p {
    margin-top: 0.75rem !important;
    font-size: 0.875rem !important;
    line-height: 1.45 !important;
  }

  .hero-wash .relative.inline-flex.p-3 {
    margin-top: 1rem !important;
    padding: 0.375rem !important;
  }

  /* Compact padding for sections to reduce scroll depth */
  #problem-framing,
  #llm-compatibility,
  #comparison,
  #features,
  #how-it-works,
  #benchmark,
  #ecosystem,
  #pricing,
  #blog-section,
  #faq {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
  }

  /* Compact section headings */
  #problem-framing h2,
  #llm-compatibility h2,
  #comparison h2,
  #features h2,
  #how-it-works h2,
  #benchmark h2,
  #ecosystem h2,
  #pricing h2,
  #blog-section h2,
  #faq h2 {
    font-size: 1.75rem !important;
    margin-bottom: 0.75rem !important;
    line-height: 1.2 !important;
  }

  /* Reduce margins on division lines */
  #problem-framing .mb-12,
  #llm-compatibility .mb-12,
  #comparison .mb-8,
  #features .mb-12,
  #how-it-works .mb-12,
  #benchmark .mb-8,
  #ecosystem .mb-16,
  #pricing .mb-12,
  #blog-section .mb-12,
  #faq .mb-16 {
    margin-bottom: 1.25rem !important;
  }
}

/* Specific optimizations for tall aspect ratio mobile viewports (19.5:9, 20:9, 21:9) */
@media (max-width: 512px) and (max-aspect-ratio: 9/17) {
  .hero-wash {
    min-height: calc(100svh - 64px) !important;
    padding-top: 4.5rem !important;
    padding-bottom: 4.5rem !important;
  }
  
  .hero-wash h1 {
    font-size: 2.375rem !important;
    line-height: 1.2 !important;
  }

  .hero-wash p {
    margin-top: 1.25rem !important;
    font-size: 0.95rem !important;
    line-height: 1.5 !important;
  }

  .hero-wash .relative.inline-flex.p-3 {
    margin-top: 2rem !important;
    padding: 0.5rem !important;
  }

  /* Give sections a bit more breathing room on tall flagships */
  #problem-framing,
  #llm-compatibility,
  #comparison,
  #features,
  #how-it-works,
  #benchmark,
  #ecosystem,
  #pricing,
  #blog-section,
  #faq {
    padding-top: 3.5rem !important;
    padding-bottom: 3.5rem !important;
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
