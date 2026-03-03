<template>
  <div class="terms-view bg-app text-text-primary min-h-screen py-24 px-4 sm:px-6 lg:px-8 font-sans selection:bg-primary selection:text-white dark:selection:bg-primary dark:selection:text-white transition-colors duration-300">
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
          <a href="#acceptance" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Acceptance of Terms</a>
          <a href="#description" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Description of Service</a>
          <a href="#accounts" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">User Accounts</a>
          <a href="#billing" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Subscriptions & Billing</a>
          <a href="#acceptable-use" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Acceptable Use Policy</a>
          <a href="#intellectual-property" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Intellectual Property</a>
          <a href="#limitation" class="block py-2 text-sm font-medium text-text-secondary hover:text-primary transition-colors">Limitation of Liability</a>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 bg-surface rounded-3xl shadow-xl border border-primary/10 p-8 sm:p-12 w-full">
        <!-- Mobile Header -->
        <div class="mb-8 md:hidden text-center">
          <router-link to="/" class="inline-flex items-center justify-center space-x-3 group mb-6">
            <img src="/image.svg" alt="MemWyre" class="w-10 h-10 rounded-xl" />
            <span class="text-2xl font-bold tracking-tight text-text-primary">MemWyre</span>
          </router-link>
        </div>

        <div class="mb-12 border-b border-primary/10 pb-8">
          <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 text-text-primary">Terms of Service</h1>
          <p class="text-primary font-bold uppercase tracking-widest text-sm">Last Updated: March 3, 2026</p>
        </div>

        <div class="prose prose-lg max-w-none text-text-secondary prose-headings:text-text-primary prose-a:text-primary hover:prose-a:text-primary-600 prose-strong:text-text-primary prose-headings:scroll-mt-32">
          
          <h2 id="acceptance" class="text-2xl font-bold mb-6">Acceptance of Terms</h2>
          <p class="mb-6 leading-relaxed">
            By registering for an account, accessing the MemWyre web application, downloading the Chrome Extension, or utilizing the MCP Server (collectively, the "Service"), you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use the Service.
          </p>

          <h2 id="description" class="text-2xl font-bold mt-12 mb-6">Description of Service</h2>
          <p class="mb-6 leading-relaxed">
            MemWyre is an AI context aggregator and "second brain" platform. It allows users to save text snippets, links, and chat transcripts into a unified knowledge base, process those memories into searchable vectors, and interact with Large Language Models (LLMs) using that knowledge as context.
          </p>

          <h2 id="accounts" class="text-2xl font-bold mt-12 mb-6">User Accounts & Security</h2>
          <p class="mb-4 leading-relaxed">
            To use the Service, you must authenticate via supported providers (e.g., Google OAuth). You are responsible for:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
            <li>Maintaining the security of your authentication accounts.</li>
            <li>All activity that occurs within your MemWyre Workspace.</li>
            <li>Ensuring that the data you save to MemWyre using our extensions or MCP servers does not violate third-party terms or local laws.</li>
          </ul>

          <h2 id="billing" class="text-2xl font-bold mt-12 mb-6">Subscriptions, Limits, & Billing</h2>
          <div class="bg-surface-2 rounded-2xl p-8 mb-8 border border-primary/10 shadow-sm">
            <h3 class="text-xl font-bold mb-4 flex items-center text-text-primary">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" /></svg>
              Billing Terms
            </h3>
            <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
              <li>MemWyre operates on a subscription model (e.g., the Pro Plan). Billing constitutes a recurring payment charged securely via our payment provider (Stripe).</li>
              <li>You may cancel your subscription at any time via the Billing dashboard. Access will continue until the end of the current paid billing cycle.</li>
              <li>Except where mandated by law, subscription fees are non-refundable.</li>
            </ul>

            <h3 class="text-xl font-bold mb-4 mt-8 flex items-center text-text-primary">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
              Usage Limits (Fair Use)
            </h3>
            <ul class="list-disc pl-6 space-y-3 text-text-secondary">
              <li>To ensure platform stability for all users, Pro Plans are subject to soft limits. This currently includes a standard daily budget of <strong>100,000 AI Model Tokens</strong> and over <strong>1,000,000 Token Storage capacity</strong> for your Brain Vault.</li>
              <li>MemWyre reserves the right to rate-limit or pause accounts that consistently exceed these budgets in a manner deemed abusive or disruptive to the service infrastructure.</li>
            </ul>
          </div>

          <h2 id="acceptable-use" class="text-2xl font-bold mt-12 mb-6">Acceptable Use Policy</h2>
          <p class="mb-4 leading-relaxed">
            You agree not to misuse the MemWyre service. Specifically, you will not:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-text-secondary">
            <li>Reverse engineer, decompile, or attempt to extract the source code or inner workings of the MemWyre web application, API, or Extension.</li>
            <li>Use the API or MCP Servers for automated scraping, mass data harvesting, or any programmatic abuse outside of the intended integration use cases.</li>
            <li>Store illegal content, malware, or highly sensitive regulated data (such as HIPAA-protected health information) as MemWyre is not compliant for such specialized regulatory storage.</li>
          </ul>

          <h2 id="intellectual-property" class="text-2xl font-bold mt-12 mb-6">Intellectual Property</h2>
          <p class="mb-6 leading-relaxed">
            <strong>Your Data:</strong> You retain full ownership of all text, links, and documents you input into the MemWyre Service. MemWyre claims no ownership rights over your personal Brain Vault context.
          </p>
          <p class="mb-6 leading-relaxed">
            <strong>MemWyre IP:</strong> The Service, including its design, logos, UI/UX, database schemas, API logic, and the MemWyre MCP protocol integrations, are the exclusive intellectual property of MemWyre and its creators.
          </p>

          <h2 id="limitation" class="text-2xl font-bold mt-12 mb-6">Limitation of Liability</h2>
          <p class="mb-6 leading-relaxed italic border-l-4 border-primary/20 pl-4 py-2">
            The Service is provided "AS IS" and on an "AS AVAILABLE" basis. We make no warranties regarding the accuracy of AI-generated responses, the permanent availability of specific Third-Party LLM models, or the absolute prevention of data loss. In no event shall MemWyre be liable for indirect, incidental, special, consequential, or punitive damages arising from your use of the Service.
          </p>
        </div>
        
        <!-- Mobile Footer -->
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
aside {
  height: calc(100vh - 120px);
}
</style>
