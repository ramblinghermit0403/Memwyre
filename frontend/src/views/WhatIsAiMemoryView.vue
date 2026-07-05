<template>
  <div class="min-h-screen bg-[#FDFCFB] text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ RESEARCH / GUIDES</div>
          <div>EST. READING TIME: 15 MIN</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Main Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 pb-24">
        
        <!-- Sticky Sidebar Table of Contents (Desktop Only) -->
        <aside class="hidden lg:block lg:col-span-3 sticky top-24 self-start">
          <div class="border border-dashed border-gray-300 rounded p-6 bg-white shadow-sm relative">
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

            <h4 class="text-xs uppercase tracking-wider font-mono font-bold text-gray-400 mb-4">Table of Contents</h4>
            <nav class="space-y-3 font-sans text-sm">
              <a href="#introduction" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">1. The Stateless AI Era</a>
              <a href="#context-window" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">2. The Context Buffer Trap</a>
              <a href="#defining-memory" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">3. What is AI Memory?</a>
              <a href="#under-the-hood" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">4. Memory Graphs vs Flat Vectors</a>
              <a href="#decay-function" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">5. The Forgetting Curve</a>
              <a href="#rag-vs-memory" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">6. AI Memory vs Traditional RAG</a>
              <a href="#implementation" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">7. Developer Setup Guide</a>
              <a href="#future" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">8. The Memory Networks of 2026</a>
            </nav>
            <div class="mt-8 pt-6 border-t border-gray-200">
              <div class="text-[11px] font-mono text-gray-400 leading-relaxed uppercase tracking-wider font-bold">AUTHOR</div>
              <div class="text-xs font-semibold text-gray-900 mt-1">Memwyre Research Lab</div>
              <div class="text-[10px] text-gray-500 font-mono mt-0.5">PUBLISHED: JUNE 2026</div>
            </div>
          </div>
        </aside>

        <!-- Article Content -->
        <article class="lg:col-span-9 max-w-none text-left space-y-12">
          
          <!-- Title & Intro -->
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
              What is AI Memory? <br />
              <span class="italic font-medium text-gray-900">The Architecture of <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Long-Term Context.</span></span>
            </h1>
            <p class="text-xl text-gray-600 leading-relaxed font-light">
              As LLMs transition from chatbots to agentic developers, the cost of statelessness has become unsustainable. Traditional retrieval systems fail to capture state, while massive context windows lead to high latency and cognitive degradation. This guide analyzes the engineering principles behind persistent, long-term AI memory.
            </p>
          </div>

          <!-- TL;DR -->
          <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm">
            <!-- Corner Brackets -->
            <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="space-y-2">
              <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-wider">Quick Summary / TL;DR</div>
              <p class="text-sm text-gray-600 leading-relaxed font-normal">
                <strong>Answer:</strong> AI memory is a persistent context layer that tracks developer facts, preferences, and workspace rules across sessions. By combining hierarchical entity graphs, logarithmic forgetting curves, and recency-aware vector linkage, it eliminates stateless context window bloat and reduces agent cost by up to 78%.
              </p>
            </div>
          </div>

          <div class="w-full h-px bg-gray-200 my-8"></div>

          <!-- Section 1: Introduction -->
          <section id="introduction" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              1. The Stateless AI Era and Its Limitations
            </h2>
            <p class="text-gray-700 leading-relaxed">
              For the first generation of generative AI tools, the paradigm was entirely transactional. You wrote a prompt, the model generated a response, and once the connection was terminated, the entire context vanished. If you opened a new window or restarted your terminal session, the model returned to its baseline state, knowing nothing about you, your project, or your preferred architectural patterns.
            </p>
            <p class="text-gray-700 leading-relaxed">
              This statelessness was acceptable when AI was used for one-off tasks like drafting emails, summaries, or writing simple sorting functions. However, as developers and teams began incorporating tools like Cursor, Claude Code, and VS Code agentic extensions into their core workflows, the stateless nature of LLMs became an active bottleneck. 
            </p>
            <p class="text-gray-700 leading-relaxed">
              In a typical professional environment, developer context is multi-faceted: it consists of coding styles, library preferences, past bugs, database schemas, local APIs, and specific workspace constraints. In a stateless paradigm, the user must repeatedly copy-paste instructions, write custom markdown prompt instructions in every project directory, or feed massive file lists into the chatbot context on startup. The model is forced to reconstruct your mental map from scratch every single time you hit enter.
            </p>
          </section>

          <!-- Section 2: The Context Buffer Trap -->
          <section id="context-window" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              2. The Context Buffer Trap: Cost, Latency, and Memory Loss
            </h2>
            <p class="text-gray-700 leading-relaxed">
              To combat statelessness, AI providers began increasing context windows, expanding from 4,000 tokens in early GPT models to 200,000 and even 2 million tokens in Google's Gemini models. While a massive context window allows you to upload an entire codebase at once, relying on it as a surrogate for "long-term memory" introduces three distinct engineering challenges:
            </p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-8">
              <div class="p-6 bg-white border border-gray-200 rounded text-left">
                <div class="text-[#D97757] font-mono font-bold text-xs uppercase tracking-wider mb-2">01 / Cost Overhead</div>
                <h4 class="font-bold text-lg mb-2">Linear Token Costs</h4>
                <p class="text-sm text-gray-500 leading-relaxed">
                  As context grows, every token sent in the prompt is billed repeatedly. A 100k context session costs 100x more per prompt than a 1k session.
                </p>
              </div>
              <div class="p-6 bg-white border border-gray-200 rounded text-left">
                <div class="text-[#D97757] font-mono font-bold text-xs uppercase tracking-wider mb-2">02 / Latency Spike</div>
                <h4 class="font-bold text-lg mb-2">Processing Overhead</h4>
                <p class="text-sm text-gray-500 leading-relaxed">
                  Attention mechanism calculations grow quadratically ($O(N^2)$) or line-linearly, leading to noticeable delays for every token processed.
                </p>
              </div>
              <div class="p-6 bg-white border border-gray-200 rounded text-left">
                <div class="text-[#D97757] font-mono font-bold text-xs uppercase tracking-wider mb-2">03 / Attention Decay</div>
                <h4 class="font-bold text-lg mb-2">Lost in the Middle</h4>
                <p class="text-sm text-gray-500 leading-relaxed">
                  Studies show LLMs struggle to recall information buried in the middle of giant context windows, reducing general output accuracy.
                </p>
              </div>
            </div>

            <p class="text-gray-700 leading-relaxed">
              When using agentic tools like Claude Code, the agent must inspect terminal outputs, read files, and write scripts. If the agent retains all logs and files in its active context, the token usage compounds rapidly. Within 10-15 terminal prompts, the session can consume hundreds of thousands of tokens, slowing response time and draining API budgets. Thus, agentic systems need a way to store memory out-of-band and query only the precise memories that are relevant to the immediate task.
            </p>
          </section>

          <!-- Section 3: Defining AI Memory -->
          <section id="defining-memory" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              3. Defining AI Memory: Episodic, Semantic, and Procedural Memory
            </h2>
            <p class="text-gray-700 leading-relaxed">
              To build a persistent layer, we must model AI memory after human cognitive systems. Human memory is categorized into three types, which can be mapped directly to software implementations for LLM agents:
            </p>
            <ul class="list-disc pl-6 space-y-3 text-gray-700">
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
            <p class="text-gray-700 leading-relaxed">
              By combining these three memory types, a memory engine enables an agent to say: "I remember we debugged a PostgreSQL timeout error three sessions ago by tuning the pool size. I will apply that same configuration to the new Redis connector session."
            </p>
          </section>

          <!-- Section 4: Memory Graphs vs Flat Vectors -->
          <section id="under-the-hood" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              4. Under the Hood: Memory Graphs vs Flat Vector Search
            </h2>
            <p class="text-gray-700 leading-relaxed">
              Standard vector databases operate by converting text into floating-point embeddings and performing cosine similarity searches. While this works for simple question-answering, it fails for complex codebase context. A vector search represents a flat comparison. It retrieves individual chunks of text that match the query's semantic meaning, but loses the relationships between entities.
            </p>
            <p class="text-gray-700 leading-relaxed">
              For example, if you ask: "Why is the authentication middleware throwing a 403 error on the billing endpoint?", a flat vector database might retrieve the `auth_middleware.js` file and a billing endpoint documentation page. However, it cannot connect the entity relationship that "the billing endpoint depends on the role validation function inside auth_middleware, which was updated by Himansh yesterday."
            </p>
            
            <!-- Graphic Block -->
            <div class="border border-dashed border-gray-300 rounded p-6 bg-white my-8 text-center">
              <h4 class="text-xs uppercase font-mono font-bold text-gray-400 mb-6">Semantic Linkage Map: Memory Graph Approach</h4>
              <div class="flex flex-col md:flex-row items-center justify-around gap-6">
                <div class="p-4 bg-gray-50 border border-gray-200 rounded w-full md:w-1/4">
                  <div class="font-bold text-sm">Entity: BillingRoute</div>
                  <div class="text-xs text-gray-500 mt-1">/api/billing.js</div>
                </div>
                <div class="text-[#D97757] font-mono text-xs">
                  ── depends_on (Active Relation) ──&gt;
                </div>
                <div class="p-4 bg-gray-50 border border-gray-200 rounded w-full md:w-1/4">
                  <div class="font-bold text-sm">Entity: AuthMiddleware</div>
                  <div class="text-xs text-gray-500 mt-1">roleValidation()</div>
                </div>
                <div class="text-blue-500 font-mono text-xs">
                  ── modified_by (Change Relation) ──&gt;
                </div>
                <div class="p-4 bg-gray-50 border border-gray-200 rounded w-full md:w-1/4">
                  <div class="font-bold text-sm">User: Developer</div>
                  <div class="text-xs text-gray-500 mt-1">Himansh (Prisma update)</div>
                </div>
              </div>
            </div>

            <p class="text-gray-700 leading-relaxed">
              A **Memory Graph** structures knowledge as nodes (entities, concepts, files) and edges (relationships, dependencies, edits). When a new conversation occurs, the memory engine extracts new entities, merges them with existing nodes, updates their weight based on usage frequency, and constructs links between them. During retrieval, the model queries both the vector database (for semantic similarity) and traverses the adjacent nodes on the graph (for relationship context). This hybrid graph-vector approach provides a multi-hop reasoning capability that flat vectors cannot match.
            </p>
          </section>

          <!-- Section 5: The Forgetting Curve -->
          <section id="decay-function" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              5. The Forgetting Curve: Memory Pruning and Decay Functions
            </h2>
            <p class="text-gray-700 leading-relaxed">
              An infinite memory is as useless as no memory. If an AI agent retains every single command, typo, intermediate print statement, and temporary error message, the context will eventually become cluttered with noise. To maintain relevance, a modern AI memory system must implement a **forgetting curve** (or memory pruning algorithm).
            </p>
            <p class="text-gray-700 leading-relaxed">
              In Memwyre, memory pruning is governed by a decay function that calculates the "importance score" (`I`) of a memory node over time (`t`). The formula incorporates the initial importance rating (`I₀`), the decay constant (`λ`), and the reinforcement frequency (`R`, representing how often the memory is queried or updated):
            </p>
            <div class="my-6 p-6 bg-gray-50 border border-gray-200 rounded text-center">
              <span class="text-lg font-mono font-semibold text-gray-800">
                I(t) = I₀ · e^(-λt) · (1 + ln(1 + R))
              </span>
            </div>
            <p class="text-gray-700 leading-relaxed">
              If a memory node is created during a debugging session but is never referenced again, its score decays exponentially. Once it falls below a specific threshold, the memory is archived out of the active index. Conversely, if the user repeatedly queries the same fact or works on the same codebase area, the reinforcement constant (`R`) increases, boosting the importance score and locking the node in the active retrieval index.
            </p>
          </section>

          <!-- Section 6: AI Memory vs Traditional RAG -->
          <section id="rag-vs-memory" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              6. AI Memory vs. Traditional RAG
            </h2>
            <p class="text-gray-700 leading-relaxed">
              A common question is: "Why not just use a standard RAG pipeline?" The table below details the architectural and practical differences between a generic RAG setup and a stateful AI Memory vault like Memwyre.
            </p>

            <div class="overflow-x-auto my-8 border border-gray-200 rounded bg-white shadow-sm">
              <table class="w-full text-sm text-left text-gray-500">
                <thead class="text-xs uppercase bg-gray-50 text-gray-700 border-b border-gray-200">
                  <tr>
                    <th scope="col" class="px-6 py-4">Feature</th>
                    <th scope="col" class="px-6 py-4">Traditional RAG</th>
                    <th scope="col" class="px-6 py-4">Memwyre AI Memory</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 font-sans">
                  <tr>
                    <td class="px-6 py-4 font-bold text-gray-950">Knowledge State</td>
                    <td class="px-6 py-4">Static document upload. Requires manual re-indexing.</td>
                    <td class="px-6 py-4 text-gray-900">Evolving. Learns and updates context from developer chat logs dynamically.</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold text-gray-950">Context Structure</td>
                    <td class="px-6 py-4">Flat vector chunks. No entity connections.</td>
                    <td class="px-6 py-4 text-gray-900">Entity-relationship memory graph. Knows how files and projects connect.</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold text-gray-950">Retrieval Latency</td>
                    <td class="px-6 py-4">High (often 800ms - 1.5s due to heavy semantic search).</td>
                    <td class="px-6 py-4 text-gray-900 font-bold text-[#D97757]">Sub-300ms. Pruned cache lookup + graph traverse.</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold text-gray-950">Integration Scope</td>
                    <td class="px-6 py-4">API endpoints or isolated chatbots.</td>
                    <td class="px-6 py-4 text-gray-900">IDE Plugins (Cursor, VS Code), MCP Clients, terminal plugins, and browser extension.</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold text-gray-950">Decay / Cleaning</td>
                    <td class="px-6 py-4">No decay. Old outdated data competes with new updates.</td>
                    <td class="px-6 py-4 text-gray-900">Active forgetting curves. Prunes out irrelevant old logs and duplicates automatically.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p class="text-gray-700 leading-relaxed">
              Traditional RAG works best for searching static libraries, such as tax laws, company handbooks, or API documentations. It is fundamentally a search engine. AI Memory, on the other hand, is a cognitive assistant companion. It sits in your development environment, listens to your terminal interactions, updates its knowledge map in real time, and helps the model make contextual connections across project boundaries.
            </p>
          </section>

          <!-- Section 7: Developer Setup Guide -->
          <section id="implementation" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              7. Developer Setup: Bringing Long-Term Memory to Your IDE
            </h2>
            <p class="text-gray-700 leading-relaxed">
              The easiest way to integrate a memory layer into your development workflow is via the **Model Context Protocol (MCP)**. MCP is an open-standard protocol introduced by Anthropic that allows local IDE applications to securely query external data sources. Below is a guide to connecting Memwyre's persistent memory server to your development environment.
            </p>

            <div class="relative p-6 bg-gray-900 text-gray-100 rounded border border-gray-800 font-mono text-xs my-6 text-left">
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

            <p class="text-gray-700 leading-relaxed">
              By adding this block to your local MCP configurations (e.g. inside `claude_desktop_config.json` or Cursor's MCP setup window), the AI assistant receives direct access to two native tools:
            </p>
            <ul class="list-disc pl-6 space-y-2 text-gray-700">
              <li>
                <code>query_memory(text)</code>: Prompts the memory graph and vector index to fetch relevant historical facts, rules, and structures.
              </li>
              <li>
                <code>save_memory(fact, relations)</code>: Directs the engine to extract entities and store a new permanent insight in the graph.
              </li>
            </ul>
            <p class="text-gray-700 leading-relaxed">
              For example, when you end a session, you can simply type: "Save to memory that we decided to bypass CORS warnings during dev by configuring proxy settings in local.env." Next time you open a project, the model will automatically pull that context when configuring routes.
            </p>
          </section>

          <!-- Section 8: The Memory Networks of 2026 -->
          <section id="future" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900">
              8. The Memory Networks of 2026
            </h2>
            <p class="text-gray-700 leading-relaxed">
              As we progress through 2026, the complexity of developer AI tasks will continue to compound. The next major frontier is multi-agent synchronization. In advanced developer setups, you are no longer interacting with a single assistant. You have a code editing agent, a testing agent running tests in the background, a code review agent in GitHub PRs, and a product manager agent updating issue tickets.
            </p>
            <p class="text-gray-700 leading-relaxed">
              Without a shared memory network, these agents remain isolated, repeating the same mistakes and asking duplicate questions. A unified memory layer allows them to communicate asynchronously. When the test agent discovers a bug and saves the solution to the memory graph, the code editing agent pulls that context to fix related file dependencies. Memory changes from a personal storage drawer into a cooperative developer brain.
            </p>
          </section>

          <!-- CTA and Internal Links -->
          <div class="border border-dashed border-gray-300 rounded p-8 bg-white text-left relative mt-16 shadow-md">
            <!-- Corner Brackets -->
            <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>

            <h3 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-3">
              Give Your AI Assistant a Brain
            </h3>
            <p class="text-gray-500 text-sm leading-relaxed mb-6">
              Stop repeating project context, coding rules, and database schemas. Set up Memwyre's universal memory layer for free in under five minutes.
            </p>
            
            <div class="flex flex-wrap gap-4 items-center">
              <router-link to="/signup" class="px-6 py-2.5 bg-[#050614] text-white text-sm font-semibold rounded hover:bg-gray-800 transition-colors shadow-sm">
                Get Started Free
              </router-link>
              <router-link to="/ai-memory-benchmark-locomo" class="px-6 py-2.5 bg-white text-gray-900 border border-gray-300 text-sm font-semibold rounded hover:bg-gray-50 transition-colors">
                View LoCoMo Benchmarks
              </router-link>
            </div>

            <div class="mt-8 pt-6 border-t border-gray-150 grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs font-mono font-bold text-gray-400">
              <router-link to="/research" class="hover:text-[#D97757] uppercase">/ Research Hub</router-link>
              <router-link to="/mcp-memory" class="hover:text-[#D97757] uppercase">/ MCP Integration</router-link>
              <router-link to="/memwyre-vs-mem0" class="hover:text-[#D97757] uppercase">/ Memwyre vs Mem0</router-link>
              <a href="/docs/" class="hover:text-[#D97757] uppercase">/ Documentation</a>
            </div>
          </div>

        </article>

      </div>
    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import SiteFooter from '@/components/SiteFooter.vue';
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
}
</style>
