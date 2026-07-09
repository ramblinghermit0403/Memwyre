<script setup>
import { ref } from 'vue';
const copiedText = ref('');
const copyCommand = (cmd) => {
  navigator.clipboard.writeText(cmd);
  copiedText.value = cmd;
  setTimeout(() => {
    copiedText.value = '';
  }, 2000);
};
</script>

<template>
  <div class="min-h-screen bg-app text-text-primary pt-24 pb-20 font-sans selection:bg-primary selection:text-white dark:selection:bg-primary dark:selection:text-white">
    
    <!-- 1. HERO SECTION -->
    <div class="min-h-[calc(100vh-6rem)] max-w-5xl mx-auto px-6 lg:px-8 mb-32 flex items-center">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center w-full">
            <div class="space-y-8">
                <h1 class="hero-serif text-6xl font-extrabold tracking-tighter leading-none">
                    Your AI Forgets.<br>
                    <span class="text-primary">Memwyre Remembers.</span>
                </h1>
                <p class="text-xl text-text-secondary leading-relaxed max-w-lg">
                    Memwyre captures everything you do with AI—research, code, decisions—and turns it into persistent, accessible knowledge tailored to your workflow.
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <router-link to="/signup" class="px-8 py-4 bg-primary text-white text-lg font-bold rounded hover:bg-primary-600 transition-colors text-center">
                        See How It Works
                    </router-link>
                    <a href="mailto:shivharehimansh@gmail.com" class="px-8 py-4 border border-primary/30 text-text-primary text-lg font-bold rounded hover:bg-primary/10 transition-colors text-center">
                        Talk to Us
                    </a>
                </div>

                <!-- Command Installer Codeblock in Hero -->
                <div class="relative bg-zinc-50 dark:bg-zinc-900 border border-dashed border-zinc-200 dark:border-zinc-800 rounded-none p-3.5 font-mono text-[11px] sm:text-xs text-zinc-600 dark:text-zinc-400 flex items-center justify-between gap-3 max-w-sm mt-6 select-none">
                  <!-- Corner Brackets -->
                  <div class="absolute -top-1 -left-1 w-2 h-2 pointer-events-none border-t border-l border-zinc-400"></div>
                  <div class="absolute -top-1 -right-1 w-2 h-2 pointer-events-none border-t border-r border-zinc-400"></div>
                  <div class="absolute -bottom-1 -left-1 w-2 h-2 pointer-events-none border-b border-l border-zinc-400"></div>
                  <div class="absolute -bottom-1 -right-1 w-2 h-2 pointer-events-none border-b border-r border-zinc-400"></div>
                  <div class="flex items-center gap-1.5 overflow-x-auto whitespace-nowrap scrollbar-none select-all py-0.5">
                    <span class="text-[#D97757] select-none font-bold">$</span>
                    <span>npx -y install-memwyre</span>
                  </div>
                  <button 
                    @click="copyCommand('npx -y install-memwyre')" 
                    class="text-[#D97757] hover:text-[#C4654A] font-semibold text-[10px] sm:text-xs tracking-wider uppercase shrink-0 transition-colors cursor-pointer select-none"
                  >
                    {{ copiedText === 'npx -y install-memwyre' ? 'Copied' : 'Copy' }}
                  </button>
                </div>
            </div>
            
            <!-- Visual Diagram -->
            <div class="relative min-h-[500px] w-full max-w-xl mx-auto flex items-center justify-center p-10 overflow-visible group">
                <!-- Ambient Glow -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-primary/15 dark:bg-primary/25 rounded-full blur-[100px] opacity-60 group-hover:opacity-100 transition-opacity duration-1000"></div>

                <!-- SVG Connection Lines + Traveling Dots -->
                <svg class="absolute inset-0 w-full h-full z-0 pointer-events-none" viewBox="0 0 500 500" fill="none">
                    <!-- Static dotted lines — alternating short/long -->
                    <line x1="250" y1="45" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="440" y1="140" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="355" y1="410" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="115" y1="455" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="55" y1="260" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />
                    <line x1="130" y1="90" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6" opacity="0.2" />

                    <!-- Traveling dots (sequential) -->
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="0s" path="M250,45 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="0.5s" path="M440,140 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0.5s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="1s" path="M355,410 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="1s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="1.5s" path="M115,455 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="1.5s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="2s" path="M55,260 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2s" />
                    </circle>
                    <circle r="4" fill="var(--primary)" opacity="0.8">
                        <animateMotion dur="3s" repeatCount="indefinite" begin="2.5s" path="M130,90 L250,250" />
                        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.5s" />
                    </circle>
                </svg>
                
                <!-- Central Node: Memwyre -->
                <div class="relative z-10 flex flex-col items-center justify-center transform group-hover:scale-105 transition-all duration-500">
                    <img src="/image.svg" alt="Memwyre" class="w-20 h-20 mb-3" />
                    <span class="text-lg font-bold tracking-tight text-text-primary">Memwyre</span>
                </div>

                <!-- Icons: alternating IN (close ~15%) / OUT (far ~2%) from edges -->
                <!-- 12 o'clock — IN (close) -->
                <div class="absolute top-[1%] left-1/2 -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1">
                    <img src="@/assets/claude-color.svg" alt="Claude" class="w-14 h-14" />
                    <div class="text-sm font-bold">Claude</div>
                </div>
                <!-- 2 o'clock — OUT (far) -->
                <div class="absolute top-[18%] right-[1%] flex flex-col items-center gap-1 z-10 animate-float-2">
                    <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-14 h-14" />
                    <div class="text-sm font-bold">Gemini</div>
                </div>
                <!-- 4 o'clock — IN (close) -->
                <div class="absolute bottom-[12%] right-[15%] flex flex-col items-center gap-1 z-10 animate-float-3">
                    <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-14 h-14" />
                    <div class="text-sm font-bold">Perplexity</div>
                </div>
                <!-- 7 o'clock — OUT (far) -->
                <div class="absolute bottom-[1%] left-[14%] flex flex-col items-center gap-1 z-10 animate-float-1" style="animation-delay: 0.7s;">
                    <img src="@/assets/openai.svg" alt="ChatGPT" class="w-14 h-14 dark:invert" />
                    <div class="text-sm font-bold">ChatGPT</div>
                </div>
                <!-- 9 o'clock — IN (close) -->
                <div class="absolute top-[44%] left-[1%] flex flex-col items-center gap-1 z-10 animate-float-2" style="animation-delay: 0.5s;">
                    <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-14 h-14" />
                    <div class="text-sm font-bold">OpenClaw</div>
                </div>
                <!-- 10 o'clock — OUT (far) -->
                <div class="absolute top-[8%] left-[12%] flex flex-col items-center gap-1 z-10 animate-float-3" style="animation-delay: 1s;">
                    <img src="@/assets/Google-Antigravity-Icon-Full-Color.png" alt="Antigravity" class="w-14 h-14" />
                    <div class="text-sm font-bold">Antigravity</div>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. THE PROBLEM -->
    <div class="bg-surface-2 py-32 border-y border-primary/10">
        <div class="max-w-4xl mx-auto px-6 lg:px-8 text-center">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-8">The Disconnect</h2>
             <blockquote class="text-4xl md:text-5xl font-bold leading-tight mb-16">
                â€œAI is everywhere in our workflow â€” <span class="bg-primary text-white px-2">but none of it sticks.</span>â€
            </blockquote>
             
             <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left">
                 <div class="p-6 bg-surface rounded-2xl border border-border shadow-sm hover:shadow-md hover:border-primary/30 transition-all duration-300">
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
                 <div class="p-6 bg-surface rounded-2xl border border-border shadow-sm hover:shadow-md hover:border-primary/30 transition-all duration-300">
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
                 <div class="p-6 bg-surface rounded-2xl border border-border shadow-sm hover:shadow-md hover:border-primary/30 transition-all duration-300">
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
                 <div class="p-6 bg-surface rounded-2xl border border-border shadow-sm hover:shadow-md hover:border-primary/30 transition-all duration-300">
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
             </div>
        </div>
    </div>

    <!-- 3. DETAILED USE CASES (Grid) -->
    <div class="py-32 max-w-5xl mx-auto px-6 lg:px-8">
        <div class="text-center mb-20">
             <h2 class="text-4xl lg:text-5xl font-extrabold mb-6">Designed for How You Work</h2>
             <p class="text-xl text-text-secondary max-w-2xl mx-auto">
                 Memwyre isn't just a note app. It's a cognitive bridging tool built for the specific ways different professionals leverage AI.
             </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            
            <!-- Use Case 1: Software Engineers -->
            <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl bg-surface flex flex-col hover:border-primary transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 dark:bg-primary/20 rounded-xl flex items-center justify-center text-primary border border-primary/15 dark:border-primary/20 shadow-sm">
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
            <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl bg-surface flex flex-col hover:border-primary transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 dark:bg-primary/20 rounded-xl flex items-center justify-center text-primary border border-primary/15 dark:border-primary/20 shadow-sm">
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
            <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl bg-surface flex flex-col hover:border-primary transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 dark:bg-primary/20 rounded-xl flex items-center justify-center text-primary border border-primary/15 dark:border-primary/20 shadow-sm">
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
                        <p class="text-text-secondary mt-1">Gather market signals and parse user feedback documents centrally. Query your second brain to rapidly draft PRDs and business cases grounded in existing, tracked research.</p>
                    </div>
                </div>
            </div>

             <!-- Use Case 4: Students & Learners -->
            <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl bg-surface flex flex-col hover:border-primary transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 dark:bg-primary/20 rounded-xl flex items-center justify-center text-primary border border-primary/15 dark:border-primary/20 shadow-sm">
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
            <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl bg-surface flex flex-col hover:border-primary transition-colors lg:col-span-2">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 dark:bg-primary/20 rounded-xl flex items-center justify-center border border-[#D97757]/15 dark:border-[#D97757]/20 shadow-sm">
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


    <!-- 5. BEFORE vs AFTER -->
    <div class="bg-surface text-text-primary py-32 border-y border-primary/10">
        <div class="px-6 lg:px-8 max-w-5xl mx-auto">
             <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold">The Memwyre Impact</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-1 rounded-3xl overflow-hidden bg-surface border border-primary/20">
                <div class="p-12 bg-surface flex flex-col h-full">
                    <h3 class="text-xl font-bold uppercase tracking-widest text-gray-500 mb-8 flex items-center gap-3">
                        <svg class="w-6 h-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        Without Memwyre
                    </h3>
                    <ul class="space-y-8 text-lg text-gray-400 flex-grow">
                        <li class="flex items-start gap-4">
                            <span class="text-gray-600 mt-1">01</span>
                            <span>AI usage is <strong>ephemeral</strong>. The moment you close the tab, the context and reasoning are lost forever.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-gray-600 mt-1">02</span>
                            <span>Knowledge is <strong>siloed</strong>. Your code snippets live in one app, your PDFs in another, and chat logs in a third.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-gray-600 mt-1">03</span>
                            <span><strong>Redundant effort</strong>. You repeat the same prompt chains and rewrite the same boilerplate because previous answers are inaccessible.</span>
                        </li>
                    </ul>
                </div>
                
                <div class="p-12 bg-primary/10 flex flex-col h-full">
                    <h3 class="text-xl font-bold uppercase tracking-widest text-text-primary mb-8 flex items-center gap-3">
                         <svg class="w-6 h-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        With Memwyre
                    </h3>
                     <ul class="space-y-8 text-lg text-gray-200 flex-grow">
                         <li class="flex items-start gap-4">
                            <span class="text-primary/50 mt-1">01</span>
                            <span>AI work <strong>compounds</strong>. Every interaction, ingested document, and captured link builds a smarter personal baseline.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-primary/50 mt-1">02</span>
                            <span>Knowledge is <strong>unified</strong>. Everything is searchable, related, and available instantly via chat or MCP integration.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-primary/50 mt-1">03</span>
                            <span><strong>Zero cold starts</strong>. Context persists. You resume complex workflows exactly where you left them, saving hours of ramp-up time.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 6. BUSINESS IMPACT / BOTTOM LINE -->
    <div class="py-20 bg-surface-2 border-b border-primary/10">
         <div class="max-w-5xl mx-auto px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold mb-12">The Bottom Line</h2>
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

     <!-- 9. CLOSING CTA -->
    <div class="py-32 text-center px-6 lg:px-8 bg-app">
         <h2 class="text-4xl lg:text-5xl font-extrabold tracking-tight mb-4 text-text-primary">You already use AI.</h2>
         <p class="text-2xl text-text-secondary mb-12">Make sure it actually remembers you.</p>
         
         <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/signup" class="px-10 py-5 bg-primary text-white text-xl font-bold rounded hover:bg-primary-600 transition-colors shadow-xl">
                Start Building Your Brain
            </router-link>
            <a href="mailto:shivharehimansh@gmail.com" class="px-10 py-5 border border-primary/30 text-text-primary text-xl font-bold rounded hover:bg-primary/10 transition-colors">
                Contact Sales
            </a>
        </div>
    </div>

  </div>
</template>

<style scoped>
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.animate-float-1 { animation: float 4s ease-in-out infinite; }
.animate-float-2 { animation: float 5s ease-in-out infinite reverse; }
.animate-float-3 { animation: float 6s ease-in-out infinite; }
.hero-serif {
    font-family: 'DM Serif Text', serif;
}
</style>
