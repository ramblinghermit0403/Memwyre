<template>
  <div class="relative min-h-screen bg-white dark:bg-[#0c0c0c] pt-28 pb-0 font-sans">
    <!-- Grid Blueprint background line effects -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.03] dark:opacity-[0.05]">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:40px_40px]"></div>
    </div>

    <!-- Global Vertical Grid Lines -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10 animate-fade-in">
      
      <!-- Back Navigation Header -->
      <div class="pt-6 mb-8">
        <router-link 
          to="/research" 
          class="inline-flex items-center gap-2 text-xs uppercase tracking-wider font-semibold text-gray-500 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
        >
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full border border-gray-300 dark:border-zinc-800 text-[10px]">&larr;</span>
          All articles
        </router-link>
      </div>

      <!-- Header Section -->
      <div class="space-y-4 mb-8 text-left">
        <div class="text-xs font-bold uppercase tracking-wider text-[#D97757] font-mono">
          RESEARCH / GUIDES 
          <span class="text-gray-300 dark:text-gray-700 mx-2">/</span> 
          JUNE 24, 2026
        </div>
        
        <h1 class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white">
          What is AI Memory? <br />
          <span class="italic font-medium text-gray-900 dark:text-gray-100">The Architecture of <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Long-Term Context.</span></span>
        </h1>

        <div class="text-[10px] tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 pt-2">
          15 MINUTES READ
        </div>
      </div>

      <!-- Section Separator Line -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 dark:bg-gray-850 pointer-events-none select-none"></div>

      <!-- 3-Column Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-y-8 lg:gap-0 pb-24">
        
        <!-- Left Sidebar (Author Info & Social Sharing) -->
        <aside class="lg:col-span-2 lg:border-r border-gray-200 dark:border-gray-800 lg:pr-8 pt-8 lg:pt-12 text-left">
          <div class="sticky top-24 space-y-8">
            <!-- Author Card -->
            <div class="flex items-center gap-3">
              <img 
                src="https://avatars.githubusercontent.com/u/170114968?v=4" 
                alt="Memwyre Research Lab" 
                class="w-10 h-10 rounded-full object-cover border border-gray-200 dark:border-zinc-800"
                @error="$event.target.src = 'https://ui-avatars.com/api/?name=Memwyre+Research+Lab&background=f3f4f6&color=333'"
              />
              <span class="text-sm font-semibold text-gray-900 dark:text-white">
                Memwyre Research Lab
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

        <!-- Middle Column (Banner & Article Body) -->
        <main class="lg:col-span-8 px-0 lg:px-8 pt-0 lg:pt-12 text-left">
          <!-- Cover Image -->
          <div class="w-full aspect-[2/1] rounded-xl overflow-hidden mb-10 bg-gray-50 border border-gray-150 dark:bg-zinc-900/30 dark:border-zinc-800/80">
            <img 
              src="https://images.unsplash.com/photo-1507668077129-56e32842fceb?auto=format&fit=crop&w=1200&q=80" 
              alt="What is AI Memory" 
              class="w-full h-full object-cover"
            />
          </div>

          <!-- Dynamic HTML Section Content -->
          <article class="markdown-content space-y-12">
            <p class="text-xl text-gray-600 dark:text-gray-300 leading-relaxed font-light">
              As LLMs transition from chatbots to agentic developers, the cost of statelessness has become unsustainable. Traditional retrieval systems fail to capture state, while massive context windows lead to high latency and cognitive degradation. This guide analyzes the engineering principles behind persistent, long-term AI memory.
            </p>

            <!-- TL;DR -->
            <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm">
              <!-- Corner Brackets -->
              <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="space-y-2">
                <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-wider">Quick Summary / TL;DR</div>
                <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed font-normal">
                  <strong>Answer:</strong> AI memory is a persistent context layer that tracks developer facts, preferences, and workspace rules across sessions. By combining hierarchical entity graphs, logarithmic forgetting curves, and recency-aware vector linkage, it eliminates stateless context window bloat and reduces agent cost by up to 78%.
                </p>
              </div>
            </div>

            <!-- Section 1: Introduction -->
            <section id="introduction" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                1. The Stateless AI Era and Its Limitations
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                For the first generation of generative AI tools, the paradigm was entirely transactional. You wrote a prompt, the model generated a response, and once the connection was terminated, the entire context vanished. If you opened a new window or restarted your terminal session, the model returned to its baseline state, knowing nothing about you, your project, or your preferred architectural patterns.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                This statelessness was acceptable when AI was used for one-off tasks like drafting emails, summaries, or writing simple sorting functions. However, as developers and teams began incorporating tools like Cursor, Claude Code, and VS Code agentic extensions into their core workflows, the stateless nature of LLMs became an active bottleneck. 
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                In a typical professional environment, developer context is multi-faceted: it consists of coding styles, library preferences, past bugs, database schemas, local APIs, and specific workspace constraints. In a stateless paradigm, the user must repeatedly copy-paste instructions, write custom markdown prompt instructions in every project directory, or feed massive file lists into the chatbot context on startup. The model is forced to reconstruct your mental map from scratch every single time you hit enter.
              </p>
            </section>

            <!-- Section 2: The Context Buffer Trap -->
            <section id="context-window" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                2. The Context Buffer Trap: Cost, Latency, and Memory Loss
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                To combat statelessness, AI providers began increasing context windows, expanding from 4,000 tokens in early GPT models to 200,000 and even 2 million tokens in Google's Gemini models. While a massive context window allows you to upload an entire codebase at once, relying on it as a surrogate for "long-term memory" introduces three distinct engineering challenges:
              </p>
              
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-8">
                <div class="p-6 bg-white dark:bg-[#111] border border-gray-200 dark:border-zinc-800 rounded-xl text-left">
                  <div class="text-[#D97757] font-mono font-bold text-xs uppercase tracking-wider mb-2">01 / Cost Overhead</div>
                  <h4 class="font-bold text-lg mb-2 text-gray-950 dark:text-white">Linear Token Costs</h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">
                    As context grows, every token sent in the prompt is billed repeatedly. A 100k context session costs 100x more per prompt than a 1k session.
                  </p>
                </div>
                <div class="p-6 bg-white dark:bg-[#111] border border-gray-200 dark:border-zinc-800 rounded-xl text-left">
                  <div class="text-[#D97757] font-mono font-bold text-xs uppercase tracking-wider mb-2">02 / Latency Spike</div>
                  <h4 class="font-bold text-lg mb-2 text-gray-950 dark:text-white">Processing Overhead</h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">
                    Attention mechanism calculations grow quadratically ($O(N^2)$) or line-linearly, leading to noticeable delays for every token processed.
                  </p>
                </div>
                <div class="p-6 bg-white dark:bg-[#111] border border-gray-200 dark:border-zinc-800 rounded-xl text-left">
                  <div class="text-[#D97757] font-mono font-bold text-xs uppercase tracking-wider mb-2">03 / Attention Decay</div>
                  <h4 class="font-bold text-lg mb-2 text-gray-950 dark:text-white">Lost in the Middle</h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">
                    Studies show LLMs struggle to recall information buried in the middle of giant context windows, reducing general output accuracy.
                  </p>
                </div>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                When using agentic tools like Claude Code, the agent must inspect terminal outputs, read files, and write scripts. If the agent retains all logs and files in its active context, the token usage compounds rapidly. Within 10-15 terminal prompts, the session can consume hundreds of thousands of tokens, slowing response time and draining API budgets. Thus, agentic systems need a way to store memory out-of-band and query only the precise memories that are relevant to the immediate task.
              </p>
            </section>

            <!-- Section 3: Defining AI Memory -->
            <section id="defining-memory" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                3. Defining AI Memory: Episodic, Semantic, and Procedural Memory
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                To build a persistent layer, we must model AI memory after human cognitive systems. Human memory is categorized into three types, which can be mapped directly to software implementations for LLM agents:
              </p>
              <ul class="list-disc pl-6 space-y-3 text-gray-700 dark:text-gray-300">
                <li>
                  <strong>Episodic Memory (Chat History & Experiences)</strong>: Represents the chronological log of user interactions and agent runs. It records past debugging sessions, conversations, and specific decisions. In software, this is represented by structured chat logs stored in a database and indexed by session ID.
                </li>
                <li>
                  <strong>Semantic Memory (Knowledge & Facts)</strong>: The static and evolving understanding of entities, codebases, frameworks, and architecture. For example: "The database uses PostgreSQL, and we handle database migrations via Prisma." This knowledge is stored in vector databases and graph indexes.
                </li>
                <li>
                  <strong>Procedural Memory (Rules & Workflows)</strong>: How the agent executes tasks. For example, the specific shell scripts needed to compile the project, the style guidelines for styling components, or testing commands. This is configured in instructions, custom tools, and profile configurations.
                </li>
              </ul>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                By combining these three memory types, a memory engine enables an agent to say: "I remember we debugged a PostgreSQL timeout error three sessions ago by tuning the pool size. I will apply that same configuration to the new Redis connector session."
              </p>
            </section>

            <!-- Section 4: Memory Graphs vs Flat Vectors -->
            <section id="under-the-hood" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                4. Under the Hood: Memory Graphs vs Flat Vector Search
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Standard vector databases operate by converting text into floating-point embeddings and performing cosine similarity searches. While this works for simple question-answering, it fails for complex codebase context. A vector search represents a flat comparison. It retrieves individual chunks of text that match the query's semantic meaning, but loses the relationships between entities.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                For example, if you ask: "Why is the authentication middleware throwing a 403 error on the billing endpoint?", a flat vector database might retrieve the `auth_middleware.js` file and a billing endpoint documentation page. However, it cannot connect the entity relationship that "the billing endpoint depends on the role validation function inside auth_middleware, which was updated by Himansh yesterday."
              </p>
              
              <!-- Graphic Block -->
              <div class="border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl p-6 bg-white dark:bg-[#111] my-8 text-center">
                <h4 class="text-xs uppercase font-mono font-bold text-gray-400 dark:text-gray-500 mb-6">Semantic Linkage Map: Memory Graph Approach</h4>
                <div class="flex flex-col md:flex-row items-center justify-around gap-6">
                  <div class="p-4 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded w-full md:w-1/4">
                    <div class="font-bold text-sm text-gray-900 dark:text-white">Entity: BillingRoute</div>
                    <div class="text-xs text-gray-500 mt-1">/api/billing.js</div>
                  </div>
                  <div class="text-[#D97757] font-mono text-xs">
                    ── depends_on (Active Relation) ──&gt;
                  </div>
                  <div class="p-4 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded w-full md:w-1/4">
                    <div class="font-bold text-sm text-gray-900 dark:text-white">Entity: AuthMiddleware</div>
                    <div class="text-xs text-gray-500 mt-1">roleValidation()</div>
                  </div>
                  <div class="text-blue-500 font-mono text-xs">
                    ── modified_by (Change Relation) ──&gt;
                  </div>
                  <div class="p-4 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded w-full md:w-1/4">
                    <div class="font-bold text-sm text-gray-900 dark:text-white">User: Developer</div>
                    <div class="text-xs text-gray-500 mt-1">Himansh (Prisma update)</div>
                  </div>
                </div>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                A **Memory Graph** structures knowledge as nodes (entities, concepts, files) and edges (relationships, dependencies, edits). When a new conversation occurs, the memory engine extracts new entities, merges them with existing nodes, updates their weight based on usage frequency, and constructs links between them. During retrieval, the model queries both the vector database (for semantic similarity) and traverses the adjacent nodes on the graph (for relationship context). This hybrid graph-vector approach provides a multi-hop reasoning capability that flat vectors cannot match.
              </p>
            </section>

            <!-- Section 5: The Forgetting Curve -->
            <section id="decay-function" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                5. The Forgetting Curve: Memory Pruning and Decay Functions
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                An infinite memory is as useless as no memory. If an AI agent retains every single command, typo, intermediate print statement, and temporary error message, the context will eventually become cluttered with noise. To maintain relevance, a modern AI memory system must implement a **forgetting curve** (or memory pruning algorithm).
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                In Memwyre, memory pruning is governed by a decay function that calculates the "importance score" (`I`) of a memory node over time (`t`). The formula incorporates the initial importance rating (`I₀`), the decay constant (`λ`), and the reinforcement frequency (`R`, representing how often the memory is queried or updated):
              </p>
              <div class="my-6 p-6 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded text-center">
                <span class="text-lg font-mono font-semibold text-gray-800 dark:text-gray-200">
                  I(t) = I₀ · e^(-λt) · (1 + ln(1 + R))
                </span>
              </div>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                If a memory node is created during a debugging session but is never referenced again, its score decays exponentially. Once it falls below a specific threshold, the memory is archived out of the active index. Conversely, if the user repeatedly queries the same fact or works on the same codebase area, the reinforcement constant (`R`) increases, boosting the importance score and locking the node in the active retrieval index.
              </p>
            </section>

            <!-- Section 6: AI Memory vs Traditional RAG -->
            <section id="rag-vs-memory" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                6. AI Memory vs. Traditional RAG
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                A common question is: "Why not just use a standard RAG pipeline?" The table below details the architectural and practical differences between a generic RAG setup and a stateful AI Memory vault like Memwyre.
              </p>

              <div class="overflow-x-auto my-8 border border-gray-200 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] shadow-sm">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-850">
                    <tr>
                      <th scope="col" class="px-6 py-4">Feature</th>
                      <th scope="col" class="px-6 py-4">Traditional RAG</th>
                      <th scope="col" class="px-6 py-4">Memwyre AI Memory</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-850 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Knowledge State</td>
                      <td class="px-6 py-4">Static document upload. Requires manual re-indexing.</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Evolving. Learns context from developer chat logs dynamically.</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Context Structure</td>
                      <td class="px-6 py-4">Flat vector chunks. No entity connections.</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Entity-relationship memory graph. Knows how files and projects connect.</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Retrieval Logic</td>
                      <td class="px-6 py-4">Cosine similarity only. Out-of-order context.</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Sub-300ms. Pruned cache lookup + graph traverse.</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Integration Scope</td>
                      <td class="px-6 py-4">API endpoints or isolated chatbots.</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">IDE Plugins (Cursor, VS Code), MCP Clients, terminal plugins, and browser extension.</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-950 dark:text-white">Decay / Cleaning</td>
                      <td class="px-6 py-4">No decay. Old outdated data competes with new updates.</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Active forgetting curves. Prunes out irrelevant old logs and duplicates automatically.</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Traditional RAG works best for searching static libraries, such as tax laws, company handbooks, or API documentations. It is fundamentally a search engine. AI Memory, on the other hand, is a cognitive assistant companion. It sits in your development environment, listens to your terminal interactions, updates its knowledge map in real time, and helps the model make contextual connections across project boundaries.
              </p>
            </section>

            <!-- Section 7: Developer Setup Guide -->
            <section id="implementation" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                7. Developer Setup: Bringing Long-Term Memory to Your IDE
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                The easiest way to integrate a memory layer into your development workflow is via the **Model Context Protocol (MCP)**. MCP is an open-standard protocol introduced by Anthropic that allows local IDE applications to securely query external data sources. Below is a guide to connecting Memwyre's persistent memory server to your development environment.
              </p>

              <div class="relative p-6 bg-gray-900 text-gray-100 rounded-xl border border-gray-800 font-mono text-xs my-6 text-left">
                <!-- Tab Header -->
                <div class="flex items-center justify-between pb-3 border-b border-gray-800 mb-4 text-gray-400">
                  <span>mcp-config.json</span>
                  <span class="text-emerald-400">JSON</span>
                </div>
                <pre class="overflow-x-auto leading-relaxed"><code>{
  "mcpServers": {
    "memwyre-memory": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://server.memwyre.tech/mcp", "--header", "Authorization:Bearer bv_sk_..."],
      "env": {
        "MEMWYRE_WORKSPACE_ID": "default"
      }
    }
  }
}</code></pre>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                By adding this block to your local MCP configurations (e.g. inside `claude_desktop_config.json` or Cursor's MCP setup window), the AI assistant receives direct access to two native tools:
              </p>
              <ul class="list-disc pl-6 space-y-2 text-gray-700 dark:text-gray-300">
                <li>
                  <code>query_memory(text)</code>: Prompts the memory graph and vector index to fetch relevant historical facts, rules, and structures.
                </li>
                <li>
                  <code>save_memory(fact, relations)</code>: Directs the engine to extract entities and store a new permanent insight in the graph.
                </li>
              </ul>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                For example, when you end a session, you can simply type: "Save to memory that we decided to bypass CORS warnings during dev by configuring proxy settings in local.env." Next time you open a project, the model will automatically pull that context when configuring routes.
              </p>
            </section>

            <!-- Section 8: The Memory Networks of 2026 -->
            <section id="future" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                8. The Memory Networks of 2026
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                As we progress through 2026, the complexity of developer AI tasks will continue to compound. The next major frontier is multi-agent synchronization. In advanced developer setups, you are no longer interacting with a single assistant. You have a code editing agent, a testing agent running tests in the background, a code review agent in GitHub PRs, and a product manager agent updating issue tickets.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Without a shared memory network, these agents remain isolated, repeating the same mistakes and asking duplicate questions. A unified memory layer allows them to communicate asynchronously. When the test agent discovers a bug and saves the solution to the memory graph, the code editing agent pulls that context to fix related file dependencies. Memory changes from a personal storage drawer into a cooperative developer brain.
              </p>
            </section>

            <!-- CTA and Internal Links -->
            <div class="border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl p-8 bg-white dark:bg-[#111] text-left relative mt-16 shadow-md">
              <!-- Corner Brackets -->
              <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>

              <h3 class="hero-serif text-xl sm:text-2xl text-gray-900 dark:text-white mb-3">
                Give Your AI Assistant a Brain
              </h3>
              <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed mb-6">
                Stop repeating project context, coding rules, and database schemas. Set up Memwyre's universal memory layer for free in under five minutes.
              </p>
              
              <div class="flex flex-wrap gap-4 items-center mb-8">
                <router-link to="/signup/" class="px-6 py-2.5 bg-[#050614] dark:bg-white text-white dark:text-black text-sm font-semibold rounded hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors shadow-sm">
                  Get Started Free
                </router-link>
                <router-link to="/ai-memory-benchmark-locomo" class="px-6 py-2.5 bg-white dark:bg-zinc-900 text-gray-900 dark:text-white border border-gray-300 dark:border-zinc-800 text-sm font-semibold rounded hover:bg-gray-50 dark:hover:bg-zinc-800 transition-colors">
                  View LoCoMo Benchmarks
                </router-link>
              </div>

              <div class="pt-6 border-t border-gray-150 dark:border-gray-800 grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs font-mono font-bold text-gray-450">
                <router-link to="/research" class="hover:text-[#D97757] uppercase">/ Research Hub</router-link>
                <router-link to="/mcp" class="hover:text-[#D97757] uppercase">/ MCP Integration</router-link>
                <router-link to="/comparisons/memwyre-vs-mem0" class="hover:text-[#D97757] uppercase">/ Memwyre vs Mem0</router-link>
                <a href="/docs/" class="hover:text-[#D97757] uppercase">/ Documentation</a>
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
                :class="{ 'text-[#D97757] font-semibold': activeSection === heading.slug, 'pl-4 text-xs opacity-80': heading.level === 3 }"
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
import { ref, onMounted, onUnmounted, computed } from 'vue';
import SiteFooter from '@/components/SiteFooter.vue';

const activeSection = ref('');
const toc = [
  { level: 2, text: '1. The Stateless AI Era', slug: 'introduction' },
  { level: 2, text: '2. The Context Buffer Trap', slug: 'context-window' },
  { level: 2, text: '3. What is AI Memory?', slug: 'defining-memory' },
  { level: 2, text: '4. Memory Graphs vs Flat Vectors', slug: 'under-the-hood' },
  { level: 2, text: '5. The Forgetting Curve', slug: 'decay-function' },
  { level: 2, text: '6. AI Memory vs Traditional RAG', slug: 'rag-vs-memory' },
  { level: 2, text: '7. Developer Setup Guide', slug: 'implementation' },
  { level: 2, text: '8. The Memory Networks of 2026', slug: 'future' }
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

// Meta helpers
const pageUrl = computed(() => typeof window !== 'undefined' ? window.location.href : '');
const pageTitle = 'What is AI Memory? - Memwyre Guide';

const copyLink = () => {
  if (typeof window !== 'undefined') {
    navigator.clipboard.writeText(window.location.href);
    alert('Link copied to clipboard!');
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
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
