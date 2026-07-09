<template>
  <div class="privacy-policy-view force-light bg-white text-gray-900 min-h-screen font-sans selection:bg-primary selection:text-white transition-colors duration-300 overflow-x-hidden">
    <div class="py-24 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto flex flex-col md:flex-row gap-12 items-start">
    
      
      <!-- Sidebar Navigation -->
      <aside class="w-full md:w-64 shrink-0 sticky top-24 hidden md:block">
        <div class="mb-8">
          <router-link to="/" class="inline-flex items-center space-x-3 group">
            <img src="/image.svg" alt="Memwyre" class="w-10 h-10 rounded-xl group-hover:scale-105 transition-transform duration-300" />
            <span class="text-2xl font-bold tracking-tight text-gray-900 group-hover:text-primary transition-colors">
              Memwyre
            </span>
          </router-link>
        </div>
        
        <nav class="space-y-1 border-l-2 border-primary/10 pl-4">
          <a href="#introduction" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Introduction</a>
          <a href="#data-collection" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Data Collection & Usage</a>
          <a href="#data-processing" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">How We Process Data</a>
          <a href="#third-parties" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Third-Party Subprocessors</a>
          <a href="#data-retention" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Data Retention & Deletion</a>
          <a href="#security" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Security Details</a>
          <a href="#contact" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Contact Information</a>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 bg-gray-50/50 rounded-3xl shadow-xl border border-primary/10 p-8 sm:p-12 w-full">
        <!-- Mobile Header (Hidden on Desktop) -->
        <div class="mb-8 md:hidden text-center">
          <router-link to="/" class="inline-flex items-center justify-center space-x-3 group mb-6">
            <img src="/image.svg" alt="Memwyre" class="w-10 h-10 rounded-xl" />
            <span class="text-2xl font-bold tracking-tight text-gray-900">Memwyre</span>
          </router-link>
        </div>

        <div class="mb-12 border-b border-primary/10 pb-8">
          <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 text-gray-900">Privacy Policy</h1>
          <p class="text-primary font-bold uppercase tracking-widest text-sm">Last Updated: March 3, 2026</p>
        </div>

        <div class="prose prose-lg max-w-none text-gray-600 prose-headings:text-gray-900 prose-a:text-primary hover:prose-a:text-primary-600 prose-strong:text-gray-900 prose-headings:scroll-mt-32">
          
          <h2 id="introduction" class="text-2xl font-bold mb-6">Introduction</h2>
          <p class="mb-6 leading-relaxed">
            Welcome to Memwyre. This Privacy Policy explains how Memwyre ("we," "our," or "us") collects, uses, protects, and handles your personal and browsing data when you use the Memwyre web application, Chrome Extension, and MCP Servers (collectively, the "Service").
          </p>
          <p class="mb-6 leading-relaxed">
            Our core mission is to connect your browsing experience and AI chats securely to your personal Memwyre Brain Vault, acting as your second brain. We believe your data is yours—we just help you remember it.
          </p>

          <h2 id="data-collection" class="text-2xl font-bold mt-12 mb-6">Data Collection & Usage</h2>
          <p class="mb-6 leading-relaxed">
            To provide the core functionality of Memwyre, we collect the following types of information:
          </p>

          <div class="bg-surface-2 rounded-2xl p-8 mb-8 border border-primary/10 shadow-sm">
            <h3 class="text-xl font-bold mb-4 flex items-center text-gray-900">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
              Account Information
            </h3>
            <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
              <li>When you sign in using OAuth (e.g., Google or GitHub), we collect your basic profile information (Name, Email Address, and Avatar URL) to create and uniquely identify your Memwyre Workspace and Brain Vault.</li>
            </ul>

            <h3 class="text-xl font-bold mb-4 mt-8 flex items-center text-gray-900">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
              Extension Data (Active Tab / Scripting)
            </h3>
            <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
              <li>Our Chrome Extension requires "Active Tab" and "Scripting" permissions. These are used <strong>exclusively</strong> to extract text, chat history, and context from specific AI platforms (like ChatGPT, Claude, and Gemini) <em>only</em> when you explicitly interact with the extension.</li>
              <li>We do not continuously monitor or record your screen. We only capture the text of the webpage or chat you are currently viewing when you click the "Save to Memwyre" action.</li>
            </ul>

            <h3 class="text-xl font-bold mb-4 mt-8 flex items-center text-gray-900">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
              Chat Interactions
            </h3>
            <ul class="list-disc pl-6 space-y-3 text-gray-600">
              <li>When using the Contextual Chat within the web app, we store your chat prompt history and the system's generated responses so you can resume previous sessions seamlessly.</li>
            </ul>
          </div>

          <h2 id="data-processing" class="text-2xl font-bold mt-12 mb-6">How We Process Data</h2>
          <p class="mb-4 leading-relaxed">
            Data saved into your Memwyre Brain Vault undergoes specific processing to enable search and chat features:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
            <li><strong>Vectorization:</strong> Text saved to your vault is chunked and processed through embedding models to generate high-dimensional vectors. This allows us to perform semantic search to retrieve relevant memories when you ask questions.</li>
            <li><strong>Context Injection:</strong> When you use our chat interface, we retrieve relevant memory chunks and securely include them as context in the prompt sent to the LLM (Large Language Model) to provide accurate, personalized answers.</li>
          </ul>

          <h2 id="third-parties" class="text-2xl font-bold mt-12 mb-6">Third-Party Subprocessors</h2>
          <p class="mb-4 leading-relaxed">
            Memwyre acts as a secure intermediary layer. We leverage best-in-class third-party providers ("Subprocessors") to fulfill AI requests and host infrastructure:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
            <li><strong>LLM Providers:</strong> To process your chats and generate embeddings, data is securely transmitted to providers like OpenAI, Anthropic, or Google DeepMind via their official APIs. <br/><em>Note: Memwyre uses enterprise/API endpoints. Data sent via these APIs is generally <strong>not</strong> used by these providers to train their public models, conforming to their B2B privacy terms.</em></li>
            <li><strong>Infrastructure:</strong> We use reputable cloud providers (such as Supabase for database/authentication, and AWS/GCP/Vercel for hosting) to strictly store and compute your data securely.</li>
          </ul>
          <p class="mb-6 leading-relaxed">
            We <strong>do not</strong> sell, trade, or rent your personally identifiable information or unified knowledge base to third-party marketers or data brokers.
          </p>

          <h2 id="data-retention" class="text-2xl font-bold mt-12 mb-6">Data Retention & Deletion</h2>
          <p class="mb-6 leading-relaxed">
            Your data remains in your Brain Vault for as long as your account is active. 
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
            <li><strong>Manual Deletion:</strong> You have full control from the Dashboard to delete individual memories, documents, or entire chat histories. Once deleted from the UI, they are permanently expunged from our active database and vector stores.</li>
            <li><strong>Account Deletion:</strong> If you wish to close your Memwyre account entirely, you may request account deletion via the App Settings. Upon deletion, all associated memories, metadata, vectors, and profile information will be permanently removed.</li>
          </ul>

          <h2 id="security" class="text-2xl font-bold mt-12 mb-6">Security Details</h2>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
            <li><strong>Encryption in Transit:</strong> All communications between your browser, the Extension, our MCP servers, and our API backend occur over secured, encrypted HTTPS/WSS protocols.</li>
            <li><strong>Encryption at Rest:</strong> Your data (including text snippets and vectors) is stored securely in modern, managed cloud databases that utilize encryption at rest.</li>
            <li><strong>Token Security:</strong> The Chrome extension uses local extension storage to securely hold your short-lived access tokens, which are never exposed to standard webpages you browse.</li>
          </ul>

          <h2 id="contact" class="text-2xl font-bold mt-12 mb-6">Contact Information</h2>
          <p class="mb-8 leading-relaxed">
            If you have any questions, concerns, or requests regarding this Privacy Policy, your data rights, or the Memwyre platform, please reach out to us at <a href="mailto:shivharehimansh@gmail.com" class="text-primary hover:text-primary-600 font-medium underline transition-colors">shivharehimansh@gmail.com</a>.
          </p>
        </div>
        
      </main>
    </div>

    <!-- Final CTA Section: Memory and Personality -->
    <div
      class="pt-20 pb-10 sm:pt-28 sm:pb-16 bg-white text-center px-6 relative overflow-hidden border-t border-black/5">
      <!-- Logo-masked numeric background (INVERTED for white bg) -->
      <LogoBgAnimation class="absolute inset-0 z-0 opacity-[0.08]" :invert="true" />

      <div class="max-w-5xl mx-auto relative z-10">
        <h2 class="font-display text-5xl sm:text-7xl lg:text-[7rem] font-medium tracking-tight mb-10 leading-[0.95]">
          <span
            class="bg-clip-text text-transparent bg-[repeating-linear-gradient(to_bottom,#111,#111_6px,white_6px,white_9px)]">
            The Second Brain
          </span><br />
          <span class="text-black">
            For Your AI.
          </span>
        </h2>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-5">
          <router-link to="/signup"
            class="w-full sm:w-auto px-10 py-4 bg-black text-white font-bold rounded-xl hover:bg-gray-800 transition-all duration-300 shadow-xl hover:scale-105">
            Start Building Your Brain
          </router-link>
          <router-link to="/pricing"
            class="w-full sm:w-auto px-10 py-4 bg-white text-black font-bold rounded-xl border border-black/10 hover:bg-black/5 transition-all duration-300 hover:border-black/20">
            Pricing
          </router-link>
        </div>
      </div>

      <div
        class="max-w-5xl mx-auto px-8 lg:px-12 mt-12 relative z-10 border-t border-black/5 pt-10 flex flex-col md:flex-row justify-between items-start gap-8 text-left">
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
            <a href="https://twitter.com/Memwyre" target="_blank"
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
            <img src="/image.svg" alt="Memwyre" class="w-6 h-6 rounded" />
            <span class="font-medium text-2xl text-black tracking-tight"
              style="font-family: 'Inter', system-ui, sans-serif;">Memwyre</span>
          </div>
          <p class="text-sm text-gray-500 max-w-xs leading-relaxed">
            Building the unified memory layer for the next generation of AI agents and professionals.
          </p>
          <p class="text-xs text-black/30 font-medium">© 2026 Memwyre. Crafted for clarity.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-12 sm:gap-16 w-full md:w-auto">
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Product</h4>
            <a href="/#features"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Features</a>
            <a href="/pricing" class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Pricing</a>
            <a href="/#ecosystem"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Ecosystem</a>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Products</h4>
            <router-link to="/extension"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Chrome Extension</router-link>
            <router-link to="/mcp"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">MCP</router-link>
            <router-link to="/plugins"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Plugins</router-link>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Support</h4>
            <a href="mailto:shivharehimansh@gmail.com"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Contact Us</a>
            <a href="https://x.com/Memwyre" target="_blank"
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
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import LogoBgAnimation from '@/components/landing/LogoBgAnimation.vue';

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<style scoped>
html {
  scroll-behavior: smooth;
}
</style>


<style scoped>
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
</style>
