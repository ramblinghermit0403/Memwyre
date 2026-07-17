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
          JULY 2026
        </div>
        
        <h1 class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white max-w-4xl">
          What is Context Engineering? <br />
          <span class="italic font-medium text-gray-900 dark:text-gray-100">The 2026 Guide to <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">AI Context Layers.</span></span>
        </h1>

        <div class="text-[10px] tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 pt-2">
          18 MINUTES READ
        </div>
      </div>

      <!-- Section Separator Line -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 dark:bg-gray-850 pointer-events-none select-none mb-12"></div>

      <!-- 3-Column Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-y-8 lg:gap-0 pb-24">
        
        <!-- Left Sidebar (Author Info & Social Sharing) -->
        <aside class="lg:col-span-2 lg:border-r border-gray-200 dark:border-zinc-800 lg:pr-8 pt-8 lg:pt-12 text-left">
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
            <div class="space-y-3 pt-6 border-t border-gray-100 dark:border-zinc-900">
              <div class="text-[11px] font-mono text-gray-400 dark:text-gray-500 tracking-wider uppercase font-bold">SHARE THIS ARTICLE</div>
              <div class="flex items-center gap-2">
                <a 
                  :href="`https://twitter.com/intent/tweet?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(pageTitle)}`" 
                  target="_blank"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] transition-all bg-white dark:bg-[#111]"
                >
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
                  </svg>
                </a>
                <button 
                  @click="copyLink"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] transition-all bg-white dark:bg-[#111] cursor-pointer"
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
              src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80" 
              alt="What is Context Engineering" 
              class="w-full h-full object-cover"
            />
          </div>

          <!-- Dynamic HTML Section Content -->
          <article class="markdown-content space-y-12">
            <p class="text-xl text-gray-600 dark:text-gray-300 leading-relaxed font-light">
              As Large Language Models stabilize into core engineering infrastructure, the focus has shifted from modifying the weights of models to orchestrating the context fed to them. Prompt engineering was a transient hack; context engineering is a lasting architectural paradigm.
            </p>

            <!-- TL;DR -->
            <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm">
              <!-- Corner Brackets -->
              <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="space-y-2">
                <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-wider">Quick Summary / TL;DR</div>
                <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed font-normal">
                  <strong>Answer:</strong> Context Engineering is the systematic practice of structuring, optimizing, and feeding runtime state data into LLMs. Instead of relying on brute-force context stuffing or basic vector search chunking, it uses relational entity graphs and Model Context Protocol (MCP) servers to select the exact, high-density context an agent needs, dropping processing latency and context costs by up to 80%.
                </p>
              </div>
            </div>

            <!-- Section 1: The Evolution -->
            <section id="evolution" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                1. The Evolution of AI Context Management
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                In the early days of generative AI, interacting with LLMs was highly conversational and transient. A user typed a prompt, the model generated a response, and the context window was wiped clean. If you needed the model to understand a specific codebase or framework constraint, you had to manually construct system instructions or paste files into the window before every query.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                As developers started adopting agentic coding assistants like Cursor, Claude Code, and Windsurf, this manual approach broke down. A developer does not work in a vacuum; they work within a complex ecosystem of library versions, runtime configs, database constraints, coding styles, and legacy architectural patterns. 
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Prompt engineering emerged as an early solution, but it is fundamentally limited. It focuses on *coaxing* the model to answer correctly by rewriting instructions. It does not solve the underlying data supply problem: how does the model know that a specific library version was updated in your backend yesterday? The answer is Context Engineering. This discipline shifts the problem from natural language instruction design to system-level data retrieval and orchestration.
              </p>
            </section>

            <!-- Section 2: The Mathematics of Context Windows -->
            <section id="math-of-context" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                2. The Mathematics of Context Windows: Costs, Latency, and Decay
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                With modern models boasting context windows of 200,000 to 2 million tokens, a common anti-pattern is "context stuffing"—dumping entire folders, logs, and database schemas into the prompt. While convenient, this approach is mathematically and financially unsustainable.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                First, let's examine the financial cost. Traditional API pricing is calculated linearly per input token. When using agents that run loops in the background (such as Claude Code or VS Code agentic loops), the agent issues multiple calls per task. If the context window is loaded with 100k tokens of codebase files, every iteration resends those 100k tokens.
              </p>

              <!-- Cost Table -->
              <div class="overflow-x-auto my-6 border border-gray-200 dark:border-zinc-800 rounded-xl">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-800">
                    <tr>
                      <th scope="col" class="px-6 py-3">Prompt Size</th>
                      <th scope="col" class="px-6 py-3">Cost per Call (Claude 3.5 Sonnet)</th>
                      <th scope="col" class="px-6 py-3">Cost per Agent Task (10 Iterations)</th>
                      <th scope="col" class="px-6 py-3">TTFT (Time-to-First-Token)</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-800 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">1,000 tokens (Precise Context)</td>
                      <td class="px-6 py-4">$0.003</td>
                      <td class="px-6 py-4">$0.03</td>
                      <td class="px-6 py-4">&lt; 150ms</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">50,000 tokens (Semi-Targeted)</td>
                      <td class="px-6 py-4">$0.15</td>
                      <td class="px-6 py-4">$1.50</td>
                      <td class="px-6 py-4">~ 800ms</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">200,000 tokens (Context Stuffing)</td>
                      <td class="px-6 py-4">$0.60</td>
                      <td class="px-6 py-4">$6.00</td>
                      <td class="px-6 py-4">2,500ms+</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Second, there is the issue of **computational complexity**. The core of the Transformer architecture is the self-attention mechanism. Standard attention requires comparing every token in the input sequence to every other token. This computation has a quadratic complexity:
              </p>
              <div class="my-6 p-4 bg-gray-50 dark:bg-zinc-900/50 rounded-lg text-center font-mono text-lg text-gray-950 dark:text-white">
                Complexity = \(\mathcal{O}(N^2)\)
              </div>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                where \(N\) represents the sequence length. While hardware optimizations (such as FlashAttention) reduce the constant factors, processing massive sequences still introduces substantial latency. For real-time applications like inline code autocomplete, waiting 2 seconds for a model to process a massive context window destroys the developer experience.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Third, model attention degrades in large contexts. The "Needle in a Haystack" (NIAH) benchmark shows that as sequence length grows, models are less likely to recall key facts located in the middle of the input stream. Context stuffing actively dilutes the model's focus, leading to code hallucinations and skipped instructions.
              </p>
            </section>

            <!-- Section 3: Core Paradigms: RAG vs. Hierarchical Entity Graphs -->
            <section id="paradigms" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                3. Core Paradigms: RAG vs. Hierarchical Entity Graphs
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                For standard document QA, developers rely on Retrieval-Augmented Generation (RAG). RAG splits text into static chunks, embeds them using a vector model, and retrieves relevant chunks via cosine similarity. While this is effective for flat prose, it is fundamentally incompatible with the relational structure of software codebases.
              </p>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                <div class="p-6 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-xl">
                  <h4 class="font-bold text-gray-900 dark:text-white mb-2">The RAG Fallacy in Codebases</h4>
                  <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                    RAG treats code as raw text. If you query a codebase for "payment processing", it will search for the string "payment processing" and return matches. However, it will completely miss imports, inherited styles, database schemas, and configuration dependencies that do not contain the exact matching words.
                  </p>
                </div>
                <div class="p-6 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-xl">
                  <h4 class="font-bold text-gray-900 dark:text-white mb-2">The Entity Graph Solution</h4>
                  <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                    Hierarchical Entity Graphs treat code as a network of structural dependencies. By parsing the Abstract Syntax Tree (AST), the graph maps files, classes, methods, imports, and variables. If you query the graph for a file, it traverses the network to retrieve its dependencies instantly.
                  </p>
                </div>
              </div>

              <!-- Graphic Relation Map -->
              <div class="border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl p-6 bg-white dark:bg-[#111] my-8">
                <h4 class="text-xs uppercase font-mono font-bold text-gray-400 dark:text-gray-500 mb-6 text-center">AST-to-Graph Representation</h4>
                <div class="flex flex-col md:flex-row items-center justify-center gap-4">
                  <div class="p-4 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded text-center">
                    <span class="text-xs font-mono text-[#D97757]">&lt;Class&gt;</span>
                    <div class="font-bold text-sm text-gray-900 dark:text-white mt-1">PaymentGateway</div>
                  </div>
                  <div class="text-[#D97757] font-mono text-xs">── calls ──&gt;</div>
                  <div class="p-4 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded text-center">
                    <span class="text-xs font-mono text-blue-500">&lt;Method&gt;</span>
                    <div class="font-bold text-sm text-gray-900 dark:text-white mt-1">validateSession()</div>
                  </div>
                  <div class="text-blue-500 font-mono text-xs">── reads ──&gt;</div>
                  <div class="p-4 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded text-center">
                    <span class="text-xs font-mono text-green-500">&lt;Schema&gt;</span>
                    <div class="font-bold text-sm text-gray-900 dark:text-white mt-1">UserSessionTable</div>
                  </div>
                </div>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                When you ask a graph-aware assistant about the `PaymentGateway`, it doesn't just scan for semantic similarity. It traverses the relations, pulling `validateSession()` and the table schema into the context. This multi-hop path reconstruction matches the way a human engineer navigates a project, ensuring the AI model writes code that perfectly integrates with all existing modules.
              </p>
            </section>

            <!-- Section 4: Implementing Context Engineering via MCP -->
            <section id="mcp" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                4. Implementing Context Engineering via the Model Context Protocol (MCP)
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                One of the major bottlenecks of early context systems was the lack of standard interfaces. Every tool had its own API, database connection string, and extraction script. This changed with the emergence of Anthropic's **Model Context Protocol (MCP)**.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                MCP acts as a universal bridge between local context sources (code repositories, databases, web tools) and LLM clients (Cursor, Claude Desktop, VS Code plugins). By separating the context client from the context provider, developers can run local MCP servers that securely expose internal state data to the model.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Below is a standard configuration example for a local MCP memory server (`claude_desktop_config.json`):
              </p>

              <!-- Code Block -->
              <div class="font-sans text-sm border border-gray-200 dark:border-zinc-800 rounded-xl overflow-hidden shadow-sm my-6">
                <div class="bg-gray-50 dark:bg-zinc-900 px-4 py-2 border-b border-gray-200 dark:border-zinc-800 flex justify-between items-center">
                  <span class="font-mono text-xs text-gray-500">claude_desktop_config.json</span>
                  <span class="text-xs text-gray-400 font-mono">JSON Config</span>
                </div>
                <pre class="p-4 bg-gray-950 dark:bg-black overflow-x-auto text-green-400 font-mono text-xs leading-relaxed"><code>{
  "mcpServers": {
    "memwyre-memory-server": {
      "command": "npx",
      "args": [
        "-y",
        "@memwyre/mcp-memory-server"
      ],
      "env": {
        "MEMWYRE_VAULT_PATH": "$HOME/.memwyre/vault",
        "MEMWYRE_AUTO_PRUNE": "true",
        "MEMWYRE_DECAY_RATE": "0.15"
      }
    }
  }
}</code></pre>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                During execution, when the user issues a prompt, the client (e.g., Claude Desktop) detects tool-calling capabilities. It queries the `memwyre-memory-server` to fetch the entity graph segment associated with the workspace. The server extracts the graph state, trims it down based on recent usage, and sends back a highly precise text segment containing codebase rules and structural relationships. This context is injected directly into the LLM's system prompt before the user query is sent to the cloud, ensuring complete data security and negligible API overhead.
              </p>
            </section>

            <!-- Section 5: Decay and Context Pruning Algorithms -->
            <section id="decay" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                5. Decay and Context Pruning Algorithms
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                As a codebase grows, your memory layer accumulates thousands of facts. If the memory engine retrieves every fact it has ever recorded, the context window will become polluted. For example, if you refactored your auth module from JWTs to session cookies two weeks ago, the model should no longer receive JWT-related context.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                To solve this, advanced memory layers implement cognitive **forgetting algorithms** modeled after human memory decay (the Ebbinghaus Curve). The weight \(W\) of a memory node at time \(t\) is calculated as:
              </p>
              <div class="my-6 p-4 bg-gray-50 dark:bg-zinc-900/50 rounded-lg text-center font-mono text-lg text-gray-950 dark:text-white">
                \(W(t) = W_0 \cdot e^{-\lambda t}\)
              </div>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                where \(W_0\) is the initial weight, \(\lambda\) is the decay rate constant, and \(t\) is the time elapsed (measured in conversation sessions or API calls) since the memory node was last accessed or reinforced.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Below is a mock implementation showing how a context engine handles decay calculation during retrieval:
              </p>

              <!-- Javascript Code Block -->
              <div class="font-sans text-sm border border-gray-200 dark:border-zinc-800 rounded-xl overflow-hidden shadow-sm my-6">
                <div class="bg-gray-50 dark:bg-zinc-900 px-4 py-2 border-b border-gray-200 dark:border-zinc-800 flex justify-between items-center">
                  <span class="font-mono text-xs text-gray-500">decay_manager.js</span>
                  <span class="text-xs text-gray-400 font-mono">Javascript</span>
                </div>
                <pre class="p-4 bg-gray-950 dark:bg-black overflow-x-auto text-green-400 font-mono text-xs leading-relaxed"><code>class MemoryDecayManager {
  constructor(decayRate = 0.15, pruneThreshold = 0.3) {
    this.decayRate = decayRate;
    this.pruneThreshold = pruneThreshold;
  }

  // Calculate decayed node weights
  calculateWeights(nodes, currentSessionIndex) {
    return nodes.map(node => {
      const elapsedSessions = currentSessionIndex - node.lastAccessedSession;
      const decayedWeight = node.initialWeight * Math.exp(-this.decayRate * elapsedSessions);
      
      return {
        ...node,
        weight: decayedWeight
      };
    }).filter(node => node.weight >= this.pruneThreshold);
  }
}</code></pre>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                When a memory is recalled, its `lastAccessedSession` value is updated to the current session index, resetting its decay path. Nodes that are never recalled slowly fade until their weight falls below the `pruneThreshold`, automatically pruning them from the retrieval vector. This dynamic decay loop guarantees your model receives clean, modern codebase context.
              </p>
            </section>

            <!-- Section 6: Ecosystem Comparison -->
            <section id="comparison" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white">
                6. Tooling Comparison: Memwyre vs. Mem0 vs. Zep
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Choosing the correct tool for your project depends on your architecture requirements. Below is a comparative analysis of the primary context engineering platforms on the market:
              </p>

              <!-- Comparison Table -->
              <div class="overflow-x-auto my-6 border border-gray-200 dark:border-zinc-800 rounded-xl">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-800">
                    <tr>
                      <th scope="col" class="px-6 py-3">Feature</th>
                      <th scope="col" class="px-6 py-3">Memwyre</th>
                      <th scope="col" class="px-6 py-3">Mem0</th>
                      <th scope="col" class="px-6 py-3">Zep AI</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-800 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">Primary Target Audience</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Individual Developers & IDEs</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Custom Agent Developers</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Custom Agent Developers</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">Integration Complexity</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Out-of-the-box (Zero Code)</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Requires Custom Backend Integrations</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Requires Custom Backend Integrations</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">Relational Entity Graph</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Yes (Natively Local)</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Graph on managed Cloud tier only</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">Yes (Graphiti Engine)</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-900 dark:text-white">Model Context Protocol (MCP)</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300 font-bold text-[#D97757]">Yes (Native Server)</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">No</td>
                      <td class="px-6 py-4 text-gray-900 dark:text-gray-300">No</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <!-- CTA and Internal Links -->
            <div class="border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl p-8 bg-white dark:bg-[#111] text-left relative mt-16 shadow-md font-sans">
              <!-- Corner Brackets -->
              <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>

              <h3 class="hero-serif text-xl sm:text-2xl text-gray-900 dark:text-white mb-3">
                Stop Repeating Your Codebase Context
              </h3>
              <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed mb-6">
                Connect your IDE to a local-first entity memory graph server. Set up Memwyre's universal context layer for free in under five minutes.
              </p>
              
              <div class="flex flex-wrap gap-4 items-center mb-8">
                <router-link to="/signup/" class="px-6 py-2.5 bg-[#050614] dark:bg-white text-white dark:text-black text-sm font-semibold rounded hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors shadow-sm">
                  Get Started Free
                </router-link>
                <router-link to="/ai-memory-benchmark-locomo" class="px-6 py-2.5 bg-white dark:bg-zinc-900 text-gray-900 dark:text-white border border-gray-300 dark:border-zinc-800 text-sm font-semibold rounded hover:bg-gray-50 dark:hover:bg-zinc-800 transition-colors">
                  View LoCoMo Benchmarks
                </router-link>
              </div>

              <div class="pt-6 border-t border-gray-150 dark:border-gray-800 grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs font-mono font-bold text-gray-400">
                <router-link to="/research" class="hover:text-[#D97757] uppercase">/ Research Hub</router-link>
                <router-link to="/mcp" class="hover:text-[#D97757] uppercase">/ MCP Integration</router-link>
                <router-link to="/memwyre-vs-mem0" class="hover:text-[#D97757] uppercase">/ Memwyre vs Mem0</router-link>
                <a href="https://docs.memwyre.tech" target="_blank" class="hover:text-[#D97757] uppercase">/ Documentation</a>
              </div>
            </div>
          </article>
        </main>

        <!-- Right Sidebar (Dynamic Table of Contents) -->
        <aside class="hidden lg:block lg:col-span-2 lg:border-l border-gray-200 dark:border-zinc-800 lg:pl-8 pt-12 text-left font-sans">
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
  { level: 2, text: '1. The Evolution of AI Context', slug: 'evolution' },
  { level: 2, text: '2. The Mathematics of Context Windows', slug: 'math-of-context' },
  { level: 2, text: '3. Core Paradigms: RAG vs. Graphs', slug: 'paradigms' },
  { level: 2, text: '4. Implementing Context via MCP', slug: 'mcp' },
  { level: 2, text: '5. Decay & Pruning Algorithms', slug: 'decay' },
  { level: 2, text: '6. Tooling Comparison', slug: 'comparison' }
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
const pageTitle = 'What is Context Engineering? - Memwyre Guide';

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
