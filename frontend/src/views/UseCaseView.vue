<template>
  <div class="min-h-screen bg-white dark:bg-black text-black dark:text-white pt-24 pb-20 font-sans selection:bg-gray-200 dark:selection:bg-gray-800">
    
    <!-- 1. HERO SECTION -->
    <div class="max-w-7xl mx-auto px-6 lg:px-8 mb-32">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-8">
                <h1 class="text-6xl font-black tracking-tighter leading-none">
                    Your AI Forgets.<br>
                    <span class="text-gray-400">Memwyre Remembers.</span>
                </h1>
                <p class="text-xl text-gray-500 dark:text-gray-400 leading-relaxed max-w-lg">
                    Memwyre captures everything you do with AI—research, code, decisions—and turns it into persistent, accessible knowledge tailored to your workflow.
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <router-link to="/register" class="px-8 py-4 bg-black dark:bg-white text-white dark:text-black text-lg font-bold rounded-full hover:opacity-90 transition-opacity text-center">
                        See How It Works
                    </router-link>
                    <a href="mailto:sales@memwyre.tech" class="px-8 py-4 border border-gray-200 dark:border-gray-800 text-black dark:text-white text-lg font-bold rounded-full hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors text-center">
                        Talk to Us
                    </a>
                </div>
            </div>
            
            <!-- Visual Diagram -->
            <div class="relative min-h-[400px] w-full max-w-lg mx-auto rounded-3xl bg-gray-50 dark:bg-black border border-gray-200 dark:border-gray-800 flex items-center justify-center p-8 overflow-hidden group shadow-2xl">
                <!-- Ambient Glow -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-blue-500/20 dark:bg-blue-500/30 rounded-full blur-[80px] opacity-60 group-hover:opacity-100 transition-opacity duration-1000"></div>
                
                <!-- Central Node: Memwyre Brain -->
                <div class="relative z-10 w-32 h-32 rounded-3xl bg-white/90 dark:bg-black/90 backdrop-blur-xl border border-gray-200 dark:border-gray-700 shadow-2xl flex flex-col items-center justify-center transform group-hover:scale-105 transition-all duration-500">
                    <svg class="w-10 h-10 text-black dark:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                    <span class="text-sm font-bold tracking-tight text-black dark:text-white">Brain</span>
                </div>

                <!-- Floating Elements -->
                <div class="absolute top-8 left-8 p-3 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xl flex items-center gap-3 animate-float-1">
                    <div class="w-8 h-8 rounded-full bg-blue-50 dark:bg-blue-900/50 flex items-center justify-center text-blue-600 dark:text-blue-400">
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                    </div>
                    <div class="text-sm font-bold shadow-sm">You</div>
                </div>

                <div class="absolute top-12 right-6 p-3 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xl flex items-center gap-3 animate-float-2">
                    <div class="w-8 h-8 rounded-full bg-purple-50 dark:bg-purple-900/50 flex items-center justify-center text-purple-600 dark:text-purple-400">
                         <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
                    </div>
                    <div class="text-sm font-bold shadow-sm">AI Tools</div>
                </div>

                <div class="absolute bottom-16 left-6 p-3 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xl flex items-center gap-3 animate-float-3">
                    <div class="w-8 h-8 rounded-full bg-green-50 dark:bg-green-900/50 flex items-center justify-center text-green-600 dark:text-green-400">
                         <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
                    </div>
                    <div class="text-sm font-bold shadow-sm">IDE / Web</div>
                </div>

                <div class="absolute bottom-8 right-8 p-3 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xl flex flex-col items-start gap-1 animate-float-2">
                    <div class="flex items-center gap-2 mb-1">
                        <div class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
                        <div class="text-xs text-gray-500 font-bold uppercase tracking-wider">Context</div>
                    </div>
                    <div class="text-sm font-bold shadow-sm">Future Sessions</div>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. THE PROBLEM -->
    <div class="bg-gray-50 dark:bg-gray-900/30 py-32 border-y border-gray-100 dark:border-gray-900">
        <div class="max-w-4xl mx-auto px-6 lg:px-8 text-center">
             <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-8">The Disconnect</h2>
             <blockquote class="text-4xl md:text-5xl font-bold leading-tight mb-16">
                “AI is everywhere in our workflow — <span class="bg-black text-white dark:bg-white dark:text-black px-2">but none of it sticks.</span>”
            </blockquote>
             
             <div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
                 <div class="p-6 border-l-4 border-black dark:border-white bg-white dark:bg-black shadow-sm rounded-r-xl">
                     <div class="font-bold text-lg mb-2 text-black dark:text-white">Ephemeral Interactions</div>
                     <p class="text-gray-500 dark:text-gray-400 leading-relaxed">You use AI across dozens of tools, but those valuable sessions vanish the moment tabs close.</p>
                 </div>
                 <div class="p-6 border-l-4 border-gray-300 dark:border-gray-700 bg-white/50 dark:bg-black/50 rounded-r-xl">
                     <div class="font-bold text-lg mb-2 text-black dark:text-white">Locked Insights</div>
                     <p class="text-gray-500 dark:text-gray-400 leading-relaxed">Crucial context, code snippets, and structured parameters live trapped inside isolated chat logs.</p>
                 </div>
                 <div class="p-6 border-l-4 border-gray-300 dark:border-gray-700 bg-white/50 dark:bg-black/50 rounded-r-xl">
                     <div class="font-bold text-lg mb-2 text-black dark:text-white">Context Reset</div>
                     <p class="text-gray-500 dark:text-gray-400 leading-relaxed">After a weekend away, the reasoning behind prior complex AI outputs is gone. You start from zero.</p>
                 </div>
                 <div class="p-6 border-l-4 border-black dark:border-white bg-white dark:bg-black shadow-sm rounded-r-xl">
                     <div class="font-bold text-lg mb-2 text-black dark:text-white">Redundant Work</div>
                     <p class="text-gray-500 dark:text-gray-400 leading-relaxed">You repeat the same research and re-prompt the same patterns again and again, wasting time.</p>
                 </div>
             </div>
        </div>
    </div>

    <!-- 3. DETAILED USE CASES (Grid) -->
    <div class="py-32 max-w-7xl mx-auto px-6 lg:px-8">
        <div class="text-center mb-20">
             <h2 class="text-4xl lg:text-5xl font-black mb-6">Designed for How You Work</h2>
             <p class="text-xl text-gray-500 dark:text-gray-400 max-w-2xl mx-auto">
                 Memwyre isn't just a note app. It's a cognitive bridging tool built for the specific ways different professionals leverage AI.
             </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            
            <!-- Use Case 1: Software Engineers -->
            <div class="p-10 border border-gray-200 dark:border-gray-800 rounded-3xl bg-white dark:bg-black flex flex-col hover:border-black dark:hover:border-white transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-gray-50 dark:bg-gray-900 rounded-xl flex items-center justify-center text-black dark:text-white border border-gray-100 dark:border-gray-800 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Software Engineers</h3>
                </div>
                <div class="space-y-6 flex-grow">
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-red-500 mb-2">The Problem</h4>
                        <p class="text-gray-600 dark:text-gray-400">Losing the context of deep debugging sessions, complex architectural choices made with AI, and scattered, hard-won code snippets.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-green-500 mb-2">Memwyre Solution</h4>
                        <p class="text-black dark:text-gray-200 font-medium">Connect your IDE directly via MCP.</p>
                        <p class="text-gray-600 dark:text-gray-400 mt-1">Past bug fixes, API specs, and AI chats become instantly searchable context for your next coding session, right inside Cursor or VS Code.</p>
                    </div>
                </div>
            </div>

            <!-- Use Case 2: Researchers & Analysts -->
            <div class="p-10 border border-gray-200 dark:border-gray-800 rounded-3xl bg-white dark:bg-black flex flex-col hover:border-black dark:hover:border-white transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-gray-50 dark:bg-gray-900 rounded-xl flex items-center justify-center text-black dark:text-white border border-gray-100 dark:border-gray-800 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Researchers & Analysts</h3>
                </div>
                <div class="space-y-6 flex-grow">
                     <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-red-500 mb-2">The Problem</h4>
                        <p class="text-gray-600 dark:text-gray-400">Drowning in open tabs, PDFs, and disjointed articles. Key insights and thematic connections are easily lost or siloed across tools.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-green-500 mb-2">Memwyre Solution</h4>
                        <p class="text-black dark:text-gray-200 font-medium">Instantly capture and synthesize.</p>
                        <p class="text-gray-600 dark:text-gray-400 mt-1">The Browser Extension grabs highlights while Unified Ingestion parses PDFs. Use conversational chat to synthesize findings across a massive, private body of research.</p>
                    </div>
                </div>
            </div>

             <!-- Use Case 3: Product Managers -->
            <div class="p-10 border border-gray-200 dark:border-gray-800 rounded-3xl bg-white dark:bg-black flex flex-col hover:border-black dark:hover:border-white transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-gray-50 dark:bg-gray-900 rounded-xl flex items-center justify-center text-black dark:text-white border border-gray-100 dark:border-gray-800 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Product Managers</h3>
                </div>
                <div class="space-y-6 flex-grow">
                     <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-red-500 mb-2">The Problem</h4>
                        <p class="text-gray-600 dark:text-gray-400">Competitor research, user feedback analysis, and feature brainstorming are scattered across various docs and ephemeral AI chat histories.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-green-500 mb-2">Memwyre Solution</h4>
                        <p class="text-black dark:text-gray-200 font-medium">A unified signal inbox.</p>
                        <p class="text-gray-600 dark:text-gray-400 mt-1">Gather market signals and parse user feedback documents centrally. Query your second brain to rapidly draft PRDs and business cases grounded in existing, tracked research.</p>
                    </div>
                </div>
            </div>

             <!-- Use Case 4: Students & Learners -->
            <div class="p-10 border border-gray-200 dark:border-gray-800 rounded-3xl bg-white dark:bg-black flex flex-col hover:border-black dark:hover:border-white transition-colors">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-gray-50 dark:bg-gray-900 rounded-xl flex items-center justify-center text-black dark:text-white border border-gray-100 dark:border-gray-800 shadow-sm">
                        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                    </div>
                    <h3 class="text-2xl font-bold">Students & Learners</h3>
                </div>
                <div class="space-y-6 flex-grow">
                     <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-red-500 mb-2">The Problem</h4>
                        <p class="text-gray-600 dark:text-gray-400">Forgetting the precise details of long YouTube tutorials, complex research papers, and online courses shortly after consuming them.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-green-500 mb-2">Memwyre Solution</h4>
                        <p class="text-black dark:text-gray-200 font-medium">Active recall on demand.</p>
                        <p class="text-gray-600 dark:text-gray-400 mt-1">Ingest YouTube video transcripts and course materials. Use conversational chat to actively test your knowledge or ask highly specific follow-up questions months later.</p>
                    </div>
                </div>
            </div>

        </div>
    </div>


    <!-- 5. BEFORE vs AFTER -->
    <div class="bg-black text-white py-32 border-y border-gray-900">
        <div class="px-6 lg:px-8 max-w-6xl mx-auto">
             <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold">The Memwyre Impact</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-1 rounded-3xl overflow-hidden bg-gray-900 border border-gray-800">
                <div class="p-12 bg-black flex flex-col h-full">
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
                
                <div class="p-12 bg-gray-900/50 flex flex-col h-full">
                    <h3 class="text-xl font-bold uppercase tracking-widest text-white mb-8 flex items-center gap-3">
                         <svg class="w-6 h-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        With Memwyre
                    </h3>
                     <ul class="space-y-8 text-lg text-gray-200 flex-grow">
                         <li class="flex items-start gap-4">
                            <span class="text-green-500/50 mt-1">01</span>
                            <span>AI work <strong>compounds</strong>. Every interaction, ingested document, and captured link builds a smarter personal baseline.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-green-500/50 mt-1">02</span>
                            <span>Knowledge is <strong>unified</strong>. Everything is searchable, related, and available instantly via chat or MCP integration.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-green-500/50 mt-1">03</span>
                            <span><strong>Zero cold starts</strong>. Context persists. You resume complex workflows exactly where you left them, saving hours of ramp-up time.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 6. BUSINESS IMPACT / BOTTOM LINE -->
    <div class="py-20 bg-gray-50 dark:bg-white/5 border-b border-gray-200 dark:border-gray-900">
         <div class="max-w-5xl mx-auto px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold mb-12">The Bottom Line</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-16">
                <div>
                     <div class="text-2xl font-bold mb-2">Faster</div>
                     <div class="text-sm text-gray-500">Context Switching</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Fewer</div>
                     <div class="text-sm text-gray-500">Repeated Prompts</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Stronger</div>
                     <div class="text-sm text-gray-500">Knowledge Retrieval</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Lasting</div>
                     <div class="text-sm text-gray-500">Personal Memory</div>
                </div>
            </div>
            <div class="inline-block p-6 border border-gray-300 dark:border-gray-700 rounded-2xl bg-white dark:bg-black shadow-sm text-lg font-medium text-gray-700 dark:text-gray-300 max-w-2xl">
                Memwyre turns your disjointed AI tool usage into an organized, compounding knowledge asset.
            </div>
         </div>
    </div>

     <!-- 9. CLOSING CTA -->
    <div class="py-32 text-center px-6 lg:px-8 bg-white dark:bg-black">
         <h2 class="text-4xl lg:text-5xl font-extrabold tracking-tight mb-4 text-black dark:text-white">You already use AI.</h2>
         <p class="text-2xl text-gray-500 dark:text-gray-400 mb-12">Make sure it actually remembers you.</p>
         
         <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/register" class="px-10 py-5 bg-black dark:bg-white text-white dark:text-black text-xl font-bold rounded-full hover:scale-105 transition-transform shadow-xl">
                Start Building Your Brain
            </router-link>
            <a href="mailto:sales@memwyre.tech" class="px-10 py-5 border border-gray-200 dark:border-gray-800 text-black dark:text-white text-xl font-bold rounded-full hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors">
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
</style>
