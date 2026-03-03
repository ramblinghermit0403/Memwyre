<template>
    <div class="relative min-h-screen bg-app text-text-primary transition-colors duration-300 font-sans overflow-x-hidden selection:bg-primary selection:text-white dark:selection:bg-primary dark:selection:text-white *:selection:bg-primary *:selection:text-white">

    
    <!-- Hero Video Background -->
    <!-- Hero Video Background -->
    <div class="absolute top-0 right-[-5%] w-full lg:w-[60%] h-[800px] z-0 pointer-events-none overflow-hidden">
        <video 
            src="/hero.mp4" 
            autoplay 
            muted 
            playsinline
            class="w-full h-full object-cover video-blend"
        ></video>
    </div>

    <!-- Hero Section -->
    <div class="relative z-10 pt-32 pb-12 lg:pt-40 lg:pb-24 px-6 lg:px-8 max-w-7xl mx-auto">
      <div class="flex flex-col items-start text-left">
        <!-- Hero Content -->
        <div class="max-w-4xl">
            <h1 class="text-5xl md:text-6xl lg:text-8xl font-extrabold tracking-tighter leading-[0.9] text-text-primary mb-8">
            Your Second Brain,<br>
            <span class="bg-primary text-white px-1 lg:px-4 leading-normal">Supercharged.</span>
            </h1>
            <p class="text-lg md:text-xl lg:text-2xl text-text-secondary leading-relaxed mb-12 max-w-2xl">
            Central memory for your digital life. Sync your context across any tool. Secure storage for the AI age.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-start">
            <router-link to="/register" class="px-8 py-4 bg-primary text-white text-lg font-bold rounded-full hover:bg-primary-600 hover:translate-y-[-2px] transition-all duration-300 flex items-center justify-center gap-2">
                Start Building
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
            </router-link>
            <a href="#features" class="px-8 py-4 border border-primary/30 text-text-primary text-lg font-bold rounded-full hover:bg-primary/10 transition-colors flex items-center justify-center">
                How it works
            </a>
            </div>
        </div>
      </div>
    </div>

    <!-- Features Grid -->
    <div id="features" class="py-16 px-6 lg:px-8 max-w-7xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-x-8 gap-y-16">
        <div class="group">
          <div class="w-12 h-12 flex items-center justify-center border border-primary/20 rounded-xl mb-6 group-hover:bg-primary group-hover:text-white transition-colors duration-300">
             <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" /></svg>
          </div>
          <h3 class="text-2xl font-bold mb-3">Memory Inbox</h3>
          <p class="text-text-secondary leading-relaxed">
            A unified holding area for all your incoming thoughts, links, and snippets. Capture instantly from any device and let AI organize it later.
          </p>
        </div>

        <div class="group">
          <div class="w-12 h-12 flex items-center justify-center border border-[#D97757]/20 rounded-xl mb-6 group-hover:bg-[#D97757] group-hover:text-white transition-colors duration-300">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
          </div>
          <h3 class="text-2xl font-bold mb-3">Contextual Chat</h3>
          <p class="text-gray-500 dark:text-gray-400 leading-relaxed">
            Don't just search—converse. Ask questions and get answers grounded in your own notes, documents, and code snippets.
          </p>
        </div>

        <div class="group">
          <div class="w-12 h-12 flex items-center justify-center border border-[#D97757]/20 rounded-xl mb-6 group-hover:bg-[#D97757] group-hover:text-white transition-colors duration-300">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
          </div>
          <h3 class="text-2xl font-bold mb-3">Unified Ingestion</h3>
          <p class="text-gray-500 dark:text-gray-400 leading-relaxed">
            Bring everything together. Import PDFs, scrape web pages, add YouTube videos, and sync your notes into one central vault.
          </p>
        </div>
      </div>
    </div>

    <!-- Workflow Section -->
     <div id="workflow" class="py-16 border-y-0 border-transparent">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="mb-20">
          <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Workflow</h2>
          <p class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight">Structured for flow.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-12">
                <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200 dark:text-gray-700">01</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Ingestion via Browser/MCP</h3>
                        <p class="text-text-secondary">Capture the web as you browse or connect directly from your IDE using our Model Context Protocol.</p>
                    </div>
                </div>
                 <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200 dark:text-gray-700">02</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Context Organization</h3>
                        <p class="text-text-secondary">AI automatically parses, tags, and stores your documents, notes, and links, building your central brain.</p>
                    </div>
                </div>
                 <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200 dark:text-gray-700">03</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Seamless AI Chat</h3>
                        <p class="text-text-secondary">Retrieve context naturally through our UI or via your own local LLMs configured with your MemWyre MCP.</p>
                    </div>
                </div>
            </div>
            
            <div class="relative group">
                <div class="absolute -inset-1 bg-gradient-to-r from-primary/30 to-primary/10 dark:from-primary/20 dark:to-primary/5 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
                <div class="relative bg-surface dark:bg-surface border border-primary/10 dark:border-primary/20 rounded-2xl p-8 shadow-2xl">
                    <div class="font-mono text-sm space-y-4">
                        <div class="flex items-center gap-2 border-b border-primary/10 dark:border-primary/20 pb-4 mb-4">
                            <span class="w-3 h-3 rounded-full bg-primary"></span>
                            <span class="text-text-muted">Ask MemWyre</span>
                        </div>
                        <p class="text-gray-800 dark:text-gray-200 min-h-[50px]">
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
    <div id="ecosystem" class="py-16 px-6 lg:px-8 max-w-7xl mx-auto">
        <div class="max-w-3xl mb-20">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Ecosystem</h2>
             <p class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-6">Built to extend.</p>
             <p class="text-lg md:text-xl text-text-secondary">MemWyre isn't a silo. It powers your entire workflow through standard protocols.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
             <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl hover:border-primary transition-colors duration-300">
                 <div class="w-12 h-12 bg-primary text-white rounded-lg flex items-center justify-center mb-6">
                     <svg class="w-8 h-8" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 84.8528L85.8822 16.9706C95.2548 7.59798 110.451 7.59798 119.823 16.9706V16.9706C129.196 26.3431 129.196 41.5391 119.823 50.9117L68.5581 102.177" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                        <path d="M69.2652 101.47L119.823 50.9117C129.196 41.5391 144.392 41.5391 153.765 50.9117L154.118 51.2652C163.491 60.6378 163.491 75.8338 154.118 85.2063L92.7248 146.6C89.6006 149.724 89.6006 154.789 92.7248 157.913L105.331 170.52" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                        <path d="M102.853 33.9411L52.6482 84.1457C43.2756 93.5183 43.2756 108.714 52.6482 118.087V118.087C62.0208 127.459 77.2167 127.459 86.5893 118.087L136.794 67.8822" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                     </svg>
                 </div>
                 <h3 class="text-2xl font-bold mb-4">MCP Server</h3>
                 <p class="text-text-secondary mb-8">
                     Connect MemWyre directly to Claude Desktop or any MCP-compliant client. Give your AI assistant direct access to your second brain.
                 </p>
                 <div class="bg-surface-2 rounded-lg p-4 font-mono text-xs text-text-secondary">
                     $ npx -y @memwyre/mcp-server
                 </div>
             </div>

             <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl hover:border-primary transition-colors duration-300">
                 <div class="w-12 h-12 bg-primary text-white rounded-lg flex items-center justify-center mb-6 font-bold text-xl">
                      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>
                 </div>
                 <h3 class="text-2xl font-bold mb-4">Browser Extension</h3>
                 <p class="text-text-secondary mb-8">
                     Capture the web as you browse. Save articles, documentation, or code snippets instantly without breaking your flow.
                 </p>
                 <div class="flex items-center gap-2 text-sm font-bold">
                     <span>Available for Chrome & Edge</span>
                     <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                 </div>
             </div>

             <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl hover:border-primary transition-colors duration-300">
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

    <!-- Use Cases Hero Section -->
    <div class="py-20 px-6 lg:px-8 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-8">
                <h2 class="text-base font-bold uppercase tracking-widest text-text-muted mb-4">Why MemWyre</h2>
                <p class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black tracking-tighter leading-[1.1]">
                    Your AI Forgets.<br>
                    <span class="text-primary">Memwyre Remembers.</span>
                </p>
                <p class="text-2xl text-text-secondary leading-relaxed max-w-xl">
                    Memwyre helps you capture everything you do with AI—research, code, decisions—and turns it into persistent, accessible knowledge tailored to your workflow.
                </p>
            </div>
            
            <!-- Visual Diagram -->
            <div class="relative min-h-[400px] md:min-h-[500px] w-full max-w-xl mx-auto flex items-center justify-center p-4 md:p-10 overflow-visible group">
                <!-- Ambient Glow -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 md:w-80 h-64 md:h-80 bg-primary/15 dark:bg-primary/25 rounded-full blur-[100px] opacity-60 group-hover:opacity-100 transition-opacity duration-1000"></div>

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
    <div class="bg-surface-2 py-20 border-y border-primary/10">
        <div class="max-w-4xl mx-auto px-6 lg:px-8 text-center">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-8">The Disconnect</h2>
             <blockquote class="text-3xl sm:text-4xl md:text-5xl font-bold leading-tight mb-16">
                “AI is everywhere in our workflow — <span class="bg-primary text-white px-2">but none of it sticks.</span>”
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

    <!-- Use Cases Section -->
    <div id="use-cases" class="py-16 px-6 lg:px-8 max-w-7xl mx-auto">
        <div class="text-center mb-20">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Use Cases</h2>
             <p class="text-4xl lg:text-5xl font-extrabold tracking-tight mb-6">Designed for How You Work</p>
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
                        <p class="text-text-secondary">Forgetting the precise details of long YouTube tutorials, complex research papers, and online courses shortly after consuming them.</p>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold uppercase tracking-widest text-primary/70 mb-2">Memwyre Solution</h4>
                        <p class="text-text-primary font-medium">Active recall on demand.</p>
                        <p class="text-text-secondary mt-1">Ingest YouTube video transcripts and course materials. Use conversational chat to actively test your knowledge or ask highly specific follow-up questions months later.</p>
                    </div>
                </div>
            </div>

            <!-- Use Case 5: DevOps & Automation Engineers (OpenClaw) -->
            <div class="p-10 border border-primary/15 dark:border-primary/20 rounded-3xl bg-surface flex flex-col hover:border-primary transition-colors lg:col-span-2">
                <div class="flex items-center gap-4 mb-8">
                    <div class="w-14 h-14 bg-primary/10 dark:bg-primary/20 rounded-xl flex items-center justify-center border border-primary/15 dark:border-primary/20 shadow-sm">
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

    <!-- Before vs After -->
    <div class="bg-surface text-text-primary py-16 border-y border-primary/10">
        <div class="px-6 lg:px-8 max-w-6xl mx-auto">
             <div class="text-center mb-16">
                <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Impact</h2>
                <p class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight">The Memwyre Difference</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-1 rounded-3xl overflow-hidden bg-surface border border-primary/20">
                <div class="p-6 md:p-12 bg-surface flex flex-col h-full">
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
                
                <div class="p-6 md:p-12 bg-primary/10 flex flex-col h-full">
                    <h3 class="text-xl font-bold uppercase tracking-widest text-text-primary mb-8 flex items-center gap-3">
                         <svg class="w-6 h-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        With Memwyre
                    </h3>
                     <ul class="space-y-8 text-lg text-text-secondary flex-grow">
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

    <!-- Bottom Line -->
    <div class="py-16 border-b border-primary/10">
         <div class="max-w-5xl mx-auto px-6 lg:px-8 text-center">
            <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Results</h2>
            <p class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-12">The Bottom Line</p>
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

    <!-- Pricing Section -->
    <div id="pricing" class="py-16 border-y-0 border-transparent bg-surface-2">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <div class="text-center mb-16">
                 <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Pricing</h2>
                 <p class="text-4xl font-extrabold tracking-tight">Simple, transparent plans.</p>
            </div>

            <div class="max-w-xl mx-auto">
                <!-- Pro Plan -->
                <div class="p-8 border-2 border-primary rounded-3xl bg-surface flex flex-col h-full relative">
                    <div class="absolute top-0 right-8 transform -translate-y-1/2 bg-primary text-white px-4 py-1 rounded-full text-xs font-bold tracking-wide uppercase">MemWyre Pro</div>
                    <h3 class="text-2xl font-bold mb-2">Unlimited</h3>
                    <div class="text-4xl font-extrabold mb-6">$10<span class="text-lg text-text-muted font-normal">/mo</span></div>
                    <p class="text-text-secondary mb-8 flex-grow">Everything you need to build and maintain your complete second brain.</p>
                    <ul class="space-y-4 mb-8 text-left">
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-primary shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">1M+ token storage</span></li>
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-primary shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">100K daily AI token budget</span></li>
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-[#D97757] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">PDF, YouTube & web page ingestion</span></li>
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-[#D97757] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">MCP Server for IDE integration</span></li>
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-[#D97757] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">Browser Extension (Chrome & Edge)</span></li>
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-[#D97757] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">OpenClaw agent plugin access</span></li>
                        <li class="flex items-center gap-3"><svg class="w-5 h-5 text-[#D97757] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg><span class="text-sm font-medium">Priority support</span></li>
                    </ul>
                    <router-link to="/register" class="w-full py-4 text-center bg-primary text-white font-bold rounded-xl hover:bg-primary-600 transition-colors">Get Started</router-link>
                </div>
            </div>
        </div>
    </div>

    <!-- FAQ Section -->
    <div id="faq" class="py-16 px-6 lg:px-8 max-w-3xl mx-auto">
        <div class="text-center mb-16">
             <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">FAQ</h2>
             <p class="text-4xl font-extrabold tracking-tight">Common questions.</p>
        </div>

        <div class="space-y-4">
            <div v-for="(faq, index) in faqs" :key="index" class="border-b border-primary/15 dark:border-primary/20 pb-4">
                <button @click="toggleFaq(index)" class="flex justify-between items-center w-full text-left py-4 group">
                    <span class="text-lg font-bold group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-colors">{{ faq.question }}</span>
                    <span class="ml-4 flex-shrink-0">
                        <svg v-if="faq.isOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" /></svg>
                        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                    </span>
                </button>
                <div v-show="faq.isOpen" class="text-text-secondary pb-4 leading-relaxed">
                    {{ faq.answer }}
                </div>
            </div>
        </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const faqs = ref([
    {
        question: "Is my data secure?",
        answer: "Yes. Your memory vault is fully private. We use industry-standard encryption, and your ingested documents, links, and snippets are only accessible via your securely authenticated API keys and web sessions.",
        isOpen: false
    },
    {
        question: "Which AI models do you support?",
        answer: "MemWyre supports a wide variety of state-of-the-art models for extraction and conversational RAG. Paid plans gain access to premium models to provide higher accuracy responses.",
        isOpen: false
    },
    {
        question: "Are there plan limits?",
        answer: "Currently, MemWyre operates solely on the Unlimited Pro plan. This tier gives you full feature access to unlimited chats, memories, and documents, along with priority support to power your complete second brain.",
        isOpen: false
    },
     {
        question: "How does the MCP integration work?",
        answer: "The Model Context Protocol (MCP) server securely connects your local AI IDEs (like Cursor/VS Code) and Claude Desktop directly to your MemWyre brain, allowing the assistant to pull from your proprietary context in real-time.",
        isOpen: false
    }
]);

const toggleFaq = (index) => {
    faqs.value[index].isOpen = !faqs.value[index].isOpen;
};

// --- Animations ---
onMounted(() => {
    // Start Typing Effect
    typeWriter();
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
