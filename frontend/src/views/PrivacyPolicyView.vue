<template>
  <div class="privacy-policy-view bg-app text-text-primary min-h-screen py-24 px-4 sm:px-6 lg:px-8 font-sans selection:bg-primary selection:text-white dark:selection:bg-primary dark:selection:text-white transition-colors duration-300">
    <div class="max-w-6xl mx-auto flex flex-col md:flex-row gap-12 items-start">
      
      <!-- Sidebar Navigation -->
      <aside class="w-full md:w-64 shrink-0 sticky top-24 hidden md:block">
        <div class="mb-8">
          <router-link to="/" class="inline-flex items-center space-x-3 group">
            <img src="/image.svg" alt="MemWyre" class="w-10 h-10 rounded-xl group-hover:scale-105 transition-transform duration-300" />
            <span class="text-2xl font-bold tracking-tight text-text-primary group-hover:text-primary transition-colors">
              MemWyre
            </span>
          </router-link>
        </div>
        
        <nav class="space-y-1 border-l-2 border-primary/10 pl-4">
          <a href="#introduction" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Introduction</a>
          <a href="#data-collection" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Data Collection & Usage</a>
          <a href="#data-processing" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">How We Process Data</a>
          <a href="#third-parties" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Third-Party Subprocessors</a>
          <a href="#data-retention" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Data Retention & Deletion</a>
          <a href="#security" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Security Details</a>
          <a href="#contact" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Contact Information</a>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 bg-surface rounded-3xl shadow-xl border border-primary/10 p-8 sm:p-12 w-full">
        <!-- Mobile Header (Hidden on Desktop) -->
        <div class="mb-8 md:hidden text-center">
          <router-link to="/" class="inline-flex items-center justify-center space-x-3 group mb-6">
            <img src="/image.svg" alt="MemWyre" class="w-10 h-10 rounded-xl" />
            <span class="text-2xl font-bold tracking-tight text-text-primary">MemWyre</span>
          </router-link>
        </div>

        <div class="mb-12 border-b border-primary/10 pb-8">
          <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 text-text-primary">Privacy Policy</h1>
          <p class="text-primary font-bold uppercase tracking-widest text-sm">Last Updated: March 3, 2026</p>
        </div>

        <div class="prose prose-lg max-w-none text-text-secondary prose-headings:text-text-primary prose-a:text-primary hover:prose-a:text-primary-600 prose-strong:text-text-primary prose-headings:scroll-mt-32">
          
          <h2 id="introduction" class="text-2xl font-bold mb-6">Introduction</h2>
          <p class="mb-6 leading-relaxed">
            Welcome to MemWyre. This Privacy Policy explains how MemWyre ("we," "our," or "us") collects, uses, protects, and handles your personal and browsing data when you use the MemWyre web application, Chrome Extension, and MCP Servers (collectively, the "Service").
          </p>
          <p class="mb-6 leading-relaxed">
            Our core mission is to connect your browsing experience and AI chats securely to your personal MemWyre Brain Vault, acting as your second brain. We believe your data is yours—we just help you remember it.
          </p>

          <h2 id="data-collection" class="text-2xl font-bold mt-12 mb-6">Data Collection & Usage</h2>
          <p class="mb-6 leading-relaxed">
            To provide the core functionality of MemWyre, we collect the following types of information:
          </p>

          <div class="bg-surface-2 rounded-2xl p-8 mb-8 border border-primary/10 shadow-sm">
            <h3 class="text-xl font-bold mb-4 flex items-center text-text-primary">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
              Account Information
            </h3>
            <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
              <li>When you sign in using OAuth (e.g., Google or GitHub), we collect your basic profile information (Name, Email Address, and Avatar URL) to create and uniquely identify your MemWyre Workspace and Brain Vault.</li>
            </ul>

            <h3 class="text-xl font-bold mb-4 mt-8 flex items-center text-text-primary">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
              Extension Data (Active Tab / Scripting)
            </h3>
            <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
              <li>Our Chrome Extension requires "Active Tab" and "Scripting" permissions. These are used <strong>exclusively</strong> to extract text, chat history, and context from specific AI platforms (like ChatGPT, Claude, and Gemini) <em>only</em> when you explicitly interact with the extension.</li>
              <li>We do not continuously monitor or record your screen. We only capture the text of the webpage or chat you are currently viewing when you click the "Save to MemWyre" action.</li>
            </ul>

            <h3 class="text-xl font-bold mb-4 mt-8 flex items-center text-text-primary">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
              Chat Interactions
            </h3>
            <ul class="list-disc pl-6 space-y-3 text-text-secondary">
              <li>When using the Contextual Chat within the web app, we store your chat prompt history and the system's generated responses so you can resume previous sessions seamlessly.</li>
            </ul>
          </div>

          <h2 id="data-processing" class="text-2xl font-bold mt-12 mb-6">How We Process Data</h2>
          <p class="mb-4 leading-relaxed">
            Data saved into your MemWyre Brain Vault undergoes specific processing to enable search and chat features:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
            <li><strong>Vectorization:</strong> Text saved to your vault is chunked and processed through embedding models to generate high-dimensional vectors. This allows us to perform semantic search to retrieve relevant memories when you ask questions.</li>
            <li><strong>Context Injection:</strong> When you use our chat interface, we retrieve relevant memory chunks and securely include them as context in the prompt sent to the LLM (Large Language Model) to provide accurate, personalized answers.</li>
          </ul>

          <h2 id="third-parties" class="text-2xl font-bold mt-12 mb-6">Third-Party Subprocessors</h2>
          <p class="mb-4 leading-relaxed">
            MemWyre acts as a secure intermediary layer. We leverage best-in-class third-party providers ("Subprocessors") to fulfill AI requests and host infrastructure:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
            <li><strong>LLM Providers:</strong> To process your chats and generate embeddings, data is securely transmitted to providers like OpenAI, Anthropic, or Google DeepMind via their official APIs. <br/><em>Note: MemWyre uses enterprise/API endpoints. Data sent via these APIs is generally <strong>not</strong> used by these providers to train their public models, conforming to their B2B privacy terms.</em></li>
            <li><strong>Infrastructure:</strong> We use reputable cloud providers (such as Supabase for database/authentication, and AWS/GCP/Vercel for hosting) to strictly store and compute your data securely.</li>
          </ul>
          <p class="mb-6 leading-relaxed">
            We <strong>do not</strong> sell, trade, or rent your personally identifiable information or unified knowledge base to third-party marketers or data brokers.
          </p>

          <h2 id="data-retention" class="text-2xl font-bold mt-12 mb-6">Data Retention & Deletion</h2>
          <p class="mb-6 leading-relaxed">
            Your data remains in your Brain Vault for as long as your account is active. 
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
            <li><strong>Manual Deletion:</strong> You have full control from the Dashboard to delete individual memories, documents, or entire chat histories. Once deleted from the UI, they are permanently expunged from our active database and vector stores.</li>
            <li><strong>Account Deletion:</strong> If you wish to close your MemWyre account entirely, you may request account deletion via the App Settings. Upon deletion, all associated memories, metadata, vectors, and profile information will be permanently removed.</li>
          </ul>

          <h2 id="security" class="text-2xl font-bold mt-12 mb-6">Security Details</h2>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
            <li><strong>Encryption in Transit:</strong> All communications between your browser, the Extension, our MCP servers, and our API backend occur over secured, encrypted HTTPS/WSS protocols.</li>
            <li><strong>Encryption at Rest:</strong> Your data (including text snippets and vectors) is stored securely in modern, managed cloud databases that utilize encryption at rest.</li>
            <li><strong>Token Security:</strong> The Chrome extension uses local extension storage to securely hold your short-lived access tokens, which are never exposed to standard webpages you browse.</li>
          </ul>

          <h2 id="contact" class="text-2xl font-bold mt-12 mb-6">Contact Information</h2>
          <p class="mb-8 leading-relaxed">
            If you have any questions, concerns, or requests regarding this Privacy Policy, your data rights, or the MemWyre platform, please reach out to us at <a href="mailto:shivharehimansh@gmail.com" class="text-primary hover:text-primary-600 font-medium underline transition-colors">shivharehimansh@gmail.com</a>.
          </p>
        </div>
        
        <!-- Mobile Footer (Hidden on Desktop) -->
        <div class="mt-16 pt-8 border-t border-primary/10 text-center md:hidden">
          <router-link to="/" class="inline-flex items-center text-primary hover:text-primary-600 font-bold tracking-wide transition-colors group">
            <svg class="w-5 h-5 mr-2 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Home
          </router-link>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<style scoped>
html {
  scroll-behavior: smooth;
}
</style>
