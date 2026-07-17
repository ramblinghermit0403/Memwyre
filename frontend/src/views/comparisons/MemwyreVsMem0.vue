<template>
  <div class="relative min-h-screen bg-white dark:bg-[#0c0c0c] pt-28 pb-0 font-sans">
    <!-- Grid Blueprint background line effects -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.03] dark:opacity-[0.05]">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:40px_40px]"></div>
    </div>

    <!-- Global Vertical Grid Lines -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 z-10 animate-fade-in">
      
      <!-- Back Navigation Header -->
      <div class="pt-6 mb-8">
        <router-link 
          to="/" 
          class="inline-flex items-center gap-2 text-xs uppercase tracking-wider font-semibold text-gray-500 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
        >
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full border border-gray-300 dark:border-zinc-800 text-[10px]">&larr;</span>
          Back to Home
        </router-link>
      </div>

      <!-- Header Section -->
      <div class="space-y-4 mb-8 text-left max-w-4xl">
        <div class="text-xs font-bold uppercase tracking-wider text-[#D97757] font-mono">
          COMPARISONS 
          <span class="text-gray-300 dark:text-gray-700 mx-2">/</span> 
          MEMWYRE VS MEM0
        </div>
        
        <h1 class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white">
          Memwyre vs Mem0: <br />
          <span class="italic font-medium text-gray-900 dark:text-gray-100">Which is Right for <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Long-Term Context?</span></span>
        </h1>

        <div class="text-[10px] tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 pt-2">
          UPDATED 2026
        </div>
      </div>

      <!-- Section Separator Line -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 dark:bg-gray-850 pointer-events-none select-none"></div>

      <!-- Main Content Layout (3-Column Blog Article Template) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-y-8 lg:gap-0 pb-24">
        
        <!-- Left Sidebar (Author Info & Social Sharing) -->
        <aside class="lg:col-span-2 lg:border-r border-gray-200 dark:border-gray-800 lg:pr-8 pt-8 lg:pt-12 text-left">
          <div class="sticky top-24 space-y-8">
            <!-- Author Card -->
            <div class="flex items-center gap-3">
              <img 
                src="https://avatars.githubusercontent.com/u/170114968?v=4" 
                alt="Himansh Shivhare" 
                class="w-10 h-10 rounded-full object-cover border border-gray-200 dark:border-zinc-800"
                @error="$event.target.src = 'https://ui-avatars.com/api/?name=Himansh+Shivhare&background=f3f4f6&color=333'"
              />
              <span class="text-sm font-semibold text-gray-900 dark:text-white">
                Himansh Shivhare
              </span>
            </div>

            <!-- Share Buttons -->
            <div class="space-y-3 pt-6 border-t border-gray-100 dark:border-gray-900">
              <div class="text-[11px] font-mono text-gray-400 dark:text-gray-500 tracking-wider uppercase font-bold">SHARE THIS ARTICLE</div>
              <div class="flex items-center gap-2">
                <a 
                  :href="`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(pageUrl)}`" 
                  target="_blank"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] dark:hover:text-[#D97757] transition-all bg-white dark:bg-[#111]"
                >
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
                  </svg>
                </a>
                <a 
                  :href="`https://twitter.com/intent/tweet?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(pageTitle)}`" 
                  target="_blank"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] dark:hover:text-[#D97757] transition-all bg-white dark:bg-[#111]"
                >
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
                  </svg>
                </a>
                <button 
                  @click="copyLink"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] dark:hover:text-[#D97757] transition-all bg-white dark:bg-[#111] cursor-pointer"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </aside>

        <main class="lg:col-span-8 px-0 lg:px-8 pt-0 lg:pt-12 text-left">
          <article class="markdown-content space-y-12">
            
            <!-- Quick Verdict / TL;DR -->
            <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm">
              <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="space-y-2">
                <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-wider">Quick Verdict</div>
                <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed font-normal">
                  <strong>Answer:</strong> If you need a ready-to-use entity graph memory layer for developer tools like Cursor, Claude Desktop, or VS Code via MCP with ultra-fast retrieval, choose <strong>Memwyre</strong>. If you are building a custom Python/Node backend application and need an API-first memory layer with multi-level scoping (User/Session/Agent) out of the box, choose <strong>Mem0</strong>. While Mem0 locks its advanced graph features behind an expensive tiered subscription ($99/mo to $299/mo), Memwyre provides hierarchical graph context natively optimized for active workspace environments for a flat $12/month.
                </p>
              </div>
            </div>

            <!-- At a Glance Table -->
            <section id="at-a-glance" class="scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white mb-6">
                At a Glance Comparison
              </h2>
              <div class="overflow-x-auto border border-gray-200 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] shadow-sm">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-850">
                    <tr>
                      <th scope="col" class="px-6 py-4">Capability</th>
                      <th scope="col" class="px-6 py-4">Memwyre</th>
                      <th scope="col" class="px-6 py-4">Mem0</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-850 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Primary Customer</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Individual Developers & Power Users</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">AI Agent Developers</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Core Product Interface</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Desktop Overlay, Browser, & IDEs</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Backend API & SDKs only</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Time-to-Value Setup</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">&lt; 5 Minutes</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Hours (Code & Database Config)</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Cross-Tool Memory Sync</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Built-in & Automatic</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Requires custom syncing pipelines</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Ready-To-Use Connectors</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Yes</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">No</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">MCP Client Support</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Yes</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">No</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Agent CLI Plugins</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Yes</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">No</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Self-Hostable</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Yes</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Yes</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <!-- What is Section -->
            <div class="grid md:grid-cols-2 gap-8 my-12">
              <div class="p-6 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-xl">
                <h3 class="hero-serif text-xl font-bold text-gray-900 dark:text-white mb-4">What is Memwyre?</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
                  Memwyre is a developer-first AI memory layer built entirely around a hierarchical entity graph. It is designed specifically to act as the "second brain" for your AI coding tools, including Claude Desktop, Cursor, and VS Code via the Model Context Protocol (MCP).
                </p>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed">
                  Instead of simply dumping text into a vector database, Memwyre structures knowledge as relationships. This enables complex multi-hop reasoning, meaning your AI can infer how changing an API endpoint affects frontend state management, purely from retained context.
                </p>
              </div>
              <div class="p-6 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-xl">
                <h3 class="hero-serif text-xl font-bold text-gray-900 dark:text-white mb-4">What is Mem0?</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
                  Mem0 (formerly Embedchain) is an API-first memory layer designed for developers building custom AI applications. It provides SDKs in Python and Node.js that make it easy to add long-term memory to custom chatbots or AI agents.
                </p>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed">
                  Mem0 excels when you are writing the backend code for an AI application and need a drop-in API to store what users say. However, it requires significant manual orchestration to integrate directly into active developer environments or existing IDEs.
                </p>
              </div>
            </div>

            <!-- Deep-Dive Feature Comparison -->
            <section id="deep-dive" class="space-y-8 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white border-b border-gray-200 dark:border-zinc-800 pb-4">
                Deep-Dive Feature Comparison
              </h2>

              <div class="space-y-6">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">1. Architecture: Knowledge Graph vs Flat Vectors</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed bg-[#D97757]/10 p-4 rounded border border-[#D97757]/20 font-medium">
                  <strong>The Answer:</strong> Memwyre uses an entity-relationship graph by default, ensuring multi-hop reasoning for complex codebase queries. Mem0 offers hybrid retrieval and multi-level memory (User/Session/Agent scopes), but its graph memory capabilities are tied to its commercial managed platform.
                </p>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                  The foundation of any AI memory system dictates how well it can scale as context grows. Mem0 excels at scoping context—allowing developers to separate short-term session memory from long-term user or agent memory via their API. However, its standard open-source approach involves chunking text, embedding it, and performing a cosine similarity search. While this works well for simple questions, it breaks down rapidly in developer environments. When a developer asks, "How does the auth flow work?", the AI needs to pull context from middleware files, frontend components, and database schemas simultaneously.
                </p>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                  Memwyre builds an active entity graph. It maps relationships (e.g., "AuthService" <em>depends on</em> "JWTUtility"). When querying, it traverses these nodes, guaranteeing high context fidelity. Mem0 has recently introduced graph memory and hybrid retrieval, but it is gated behind their commercial managed platform, forcing open-source users to rely on basic RAG.
                </p>
              </div>

              <div class="space-y-6 mt-12">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">2. Performance & Benchmarks</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed bg-[#D97757]/10 p-4 rounded border border-[#D97757]/20 font-medium">
                  <strong>The Answer:</strong> Memwyre achieves highly optimized retrieval performance via active pruning, while Mem0 relies on standard queries without automatic graph optimization.
                </p>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                  In production AI agents, memory retrieval performance directly impacts the user experience. If a user types a prompt in Claude Desktop, waiting extra time just for the context to load before the model starts generating feels sluggish. Memwyre's hierarchical entity graph combined with our LoCoMo benchmark-tested decay functions ensures that only active context is loaded, keeping response times incredibly fast.
                </p>
              </div>

              <div class="space-y-6 mt-12">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">3. Deployment & Self-Hosting</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed bg-[#D97757]/10 p-4 rounded border border-[#D97757]/20 font-medium">
                  <strong>The Answer:</strong> Mem0 offers open-source self-hosting for basic vector memory but locks managed graph memory to the cloud. Memwyre offers local-first MCP graph memory directly on your machine.
                </p>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                  Data privacy is critical for enterprise codebases. Mem0 allows you to run its vector store locally via its open-source package, but if you want advanced graph memory capabilities, you must use their managed cloud platform. Memwyre flips this model: our MCP server runs entirely on your local machine, keeping your codebase knowledge graph within your environment, and only syncing encrypted metadata to the cloud if you choose to enable multi-device sync.
                </p>
              </div>

              <div class="space-y-6 mt-12">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">4. IDE & Workflow Integration (MCP)</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed bg-[#D97757]/10 p-4 rounded border border-[#D97757]/20 font-medium">
                  <strong>The Answer:</strong> Memwyre is built for immediate integration into existing developer tools via native MCP servers and direct IDE plugins. Mem0 is built as an SDK for custom codebases.
                </p>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                  If you want your Cursor AI, Windsurf, or Claude Desktop to remember your project rules, Memwyre is the clear choice. Memwyre implements the Model Context Protocol (MCP) natively. Mem0 is designed for a different persona—providing Python and JavaScript SDKs for engineers building their own AI products.
                </p>
              </div>

              <div class="space-y-6 mt-12">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">5. Pruning and Forgetting Mechanisms</h3>
                <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed bg-[#D97757]/10 p-4 rounded border border-[#D97757]/20 font-medium">
                  <strong>The Answer:</strong> Memwyre utilizes an active Ebbinghaus exponential decay formula to naturally forget outdated context. Mem0 requires manual DELETE or UPDATE API calls.
                </p>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                  As memory grows, "context pollution" becomes a fatal flaw. Memwyre solves this through temporal decay. Memories that are not accessed or reinforced slowly lose weight in the graph. Mem0 relies on a CRUD paradigm, forcing your application logic to explicitly issue update commands when facts change.
                </p>
              </div>
            </section>

            <!-- Final Recommendation -->
            <section id="recommendation" class="scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white mb-6">
                Final Recommendation
              </h2>
              <div class="space-y-6">
                <div class="border-l-2 border-[#D97757] pl-6 py-2">
                  <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-2">Choose Memwyre if...</h3>
                  <p class="text-gray-600 dark:text-gray-400 text-sm leading-relaxed">You are a developer looking to augment your <strong>own daily tools</strong>. If you want Cursor IDE, Claude Desktop, or VS Code to remember your project's architectural decisions automatically via MCP, Memwyre is the out-of-the-box solution engineered specifically for this use case.</p>
                </div>
                <div class="border-l-2 border-gray-300 dark:border-zinc-700 pl-6 py-2">
                  <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-2">Choose Mem0 if...</h3>
                  <p class="text-gray-600 dark:text-gray-400 text-sm leading-relaxed">You are an engineer building an <strong>AI application for other users</strong>. If you are coding a customer service chatbot and need a backend database to store conversation history programmatically via Python, Mem0's SDKs are the correct choice.</p>
                </div>
              </div>
            </section>

            <!-- FAQ Section -->
            <section id="faq" class="scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white mb-6">
                Frequently Asked Questions
              </h2>
              <div class="space-y-4" itemscope itemtype="https://schema.org/FAQPage">
                
                <div class="border border-gray-200 dark:border-zinc-800 rounded-xl p-5 bg-white dark:bg-[#111]" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                  <h3 class="text-base font-bold text-gray-900 dark:text-white mb-2" itemprop="name">Does Memwyre replace Mem0?</h3>
                  <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p class="text-sm text-gray-600 dark:text-gray-400" itemprop="text">No, they serve different purposes. Memwyre is a client-side context manager for developers to use with their IDEs via MCP. Mem0 is a backend API infrastructure for developers building memory into custom applications.</p>
                  </div>
                </div>

                <div class="border border-gray-200 dark:border-zinc-800 rounded-xl p-5 bg-white dark:bg-[#111]" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                  <h3 class="text-base font-bold text-gray-900 dark:text-white mb-2" itemprop="name">Which is better for Cursor IDE memory?</h3>
                  <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p class="text-sm text-gray-600 dark:text-gray-400" itemprop="text">Memwyre natively supports the Model Context Protocol (MCP), allowing Cursor to read and write directly to your entity graph. Mem0 does not offer a native zero-config Cursor integration.</p>
                  </div>
                </div>

                <div class="border border-gray-200 dark:border-zinc-800 rounded-xl p-5 bg-white dark:bg-[#111]" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                  <h3 class="text-base font-bold text-gray-900 dark:text-white mb-2" itemprop="name">Is graph memory better than vector memory?</h3>
                  <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p class="text-sm text-gray-600 dark:text-gray-400" itemprop="text">Yes, for codebase context. Vector memory struggles with multi-hop reasoning across multiple files. Graph memory maps relationships between codebase entities, making it vastly superior for complex developer environments.</p>
                  </div>
                </div>

              </div>
            </section>

            <!-- CTA -->
            <div class="border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl p-8 bg-[#050614] dark:bg-white text-left relative mt-16 shadow-md">
              <div class="hero-serif text-xl sm:text-2xl !text-white dark:!text-gray-900 mb-3">
                Stop starting from scratch.
              </div>
              <div class="!text-gray-400 dark:!text-gray-600 text-sm leading-relaxed mb-6">
                Give your AI agents persistent, graph-based memory today. Works instantly with Claude Desktop, Cursor, and VS Code via MCP.
              </div>
              
              <div class="flex flex-wrap gap-4 items-center">
                <router-link to="/signup/" class="px-6 py-2.5 bg-[#D97757] text-white text-sm font-semibold rounded hover:bg-[#c4684a] transition-colors shadow-sm">
                  Start Free Trial
                </router-link>
              </div>
            </div>

          </article>
        </main>

        <!-- Right Sidebar (Dynamic Table of Contents) -->
        <aside class="hidden lg:block lg:col-span-2 lg:border-l border-gray-200 dark:border-gray-800 lg:pl-8 pt-12 text-left">
          <div class="sticky top-24 space-y-4">
            <div class="text-[11px] font-mono text-gray-400 dark:text-gray-500 tracking-wider uppercase font-bold">ON THIS PAGE</div>
            <nav class="space-y-3 text-sm relative pl-4 border-l border-gray-100 dark:border-zinc-900">
              <a 
                v-for="heading in toc" 
                :key="heading.slug" 
                :href="`#${heading.slug}`" 
                class="block font-medium text-gray-500 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors leading-snug relative"
                :class="{ 'text-[#D97757] font-semibold': activeSection === heading.slug }"
              >
                <!-- Active Indicator vertical line -->
                <div 
                  v-if="activeSection === heading.slug" 
                  class="absolute -left-[17px] top-0 bottom-0 w-0.5 bg-[#D97757]"
                ></div>
                {{ heading.text }}
              </a>
            </nav>
          </div>
        </aside>

      </div>
    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import SiteFooter from '@/components/SiteFooter.vue';

const pageUrl = computed(() => typeof window !== 'undefined' ? window.location.href : '');
const pageTitle = computed(() => typeof document !== 'undefined' ? document.title : '');

const copyLink = () => {
  if (typeof window !== 'undefined' && navigator.clipboard) {
    navigator.clipboard.writeText(window.location.href);
  }
};

const activeSection = ref('');
const toc = [
  { text: 'At a Glance', slug: 'at-a-glance' },
  { text: 'Deep-Dive Features', slug: 'deep-dive' },
  { text: 'Final Recommendation', slug: 'recommendation' },
  { text: 'FAQ', slug: 'faq' }
];

// Scrollspy Observer
let observer = null;
onMounted(() => {
  if (typeof window !== 'undefined') {
    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          activeSection.value = entry.target.id;
        }
      });
    }, {
      root: null,
      rootMargin: '0px 0px -75% 0px',
      threshold: 0
    });

    const headings = document.querySelectorAll('.scroll-mt-20');
    headings.forEach((h) => {
      observer.observe(h);
    });
  }
});

onUnmounted(() => {
  if (observer) observer.disconnect();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
  font-variant-numeric: lining-nums;
  font-feature-settings: "lnum" 1;
}

.markdown-content h2,
.markdown-content h3 {
  font-family: 'Playfair Display', Georgia, serif;
  color: #111827;
  line-height: 1.25;
  margin-top: 36px;
  margin-bottom: 16px;
  scroll-margin-top: 100px;
}

.dark .markdown-content h2,
.dark .markdown-content h3 {
  color: #f3f4f6;
}
</style>
