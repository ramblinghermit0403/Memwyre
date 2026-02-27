<template>
  <div class="privacy-policy-view bg-gray-50 min-h-screen py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto bg-white rounded-xl shadow-sm border border-gray-100 p-8 sm:p-12">
      <div class="mb-10 text-center">
        <router-link to="/" class="inline-block mb-6">
          <div class="flex items-center justify-center space-x-2">
            <div class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white font-bold text-xl shadow-inner">
              M
            </div>
            <span class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-indigo-600 to-purple-600 tracking-tight">
              MemWyre
            </span>
          </div>
        </router-link>
        <h1 class="text-4xl font-extrabold text-gray-900 tracking-tight mb-2">Privacy Policy</h1>
        <p class="text-gray-500 font-medium">Effective Date: Feb 27, 2026</p>
      </div>

      <div class="prose prose-indigo prose-lg mx-auto text-gray-600">
        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Introduction</h2>
        <p class="mb-6 leading-relaxed">
          This Privacy Policy applies to the MemWyre Chrome Extension ("Extension"). Our goal is to connect your browsing experience and AI chats securely to your personal MemWyre Brain Vault.
        </p>

        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Data Collection and Usage</h2>
        <p class="mb-4 leading-relaxed">
          The MemWyre Extension requires specific permissions to function. We only collect the data necessary to provide the core service of saving "memories" and conversation context.
        </p>

        <div class="bg-gray-50 rounded-lg p-6 mb-6 border border-gray-100">
          <h3 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
            <svg class="w-5 h-5 mr-2 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
            Active Tab / Scripting
          </h3>
          <ul class="list-disc pl-5 space-y-2 mb-4">
            <li>The extension uses these permissions to extract text, chat history, and context from specific AI platforms (such as ChatGPT, Claude, Gemini, Perplexity) when you explicitly initiate an action.</li>
            <li><strong>Usage:</strong> This data is strictly used to create a memory or search context in your MemWyre unified knowledge base. It is securely transmitted to the MemWyre API (<code>api.memwyre.com</code>).</li>
          </ul>

          <h3 class="text-lg font-semibold text-gray-900 mb-3 mt-6 flex items-center">
            <svg class="w-5 h-5 mr-2 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
            Storage
          </h3>
          <ul class="list-disc pl-5 space-y-2">
            <li>We use local extension storage to securely store your authentication token (Access Token).</li>
            <li><strong>Usage:</strong> This token is used solely to authenticate your requests against the MemWyre API.</li>
          </ul>
        </div>

        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Data Sharing and Third Parties</h2>
        <p class="mb-6 leading-relaxed">
          We <strong>do not</strong> sell, trade, or otherwise transfer your personally identifiable information or saved browsing data to outside parties. All data transmitted from the Extension is sent directly to your MemWyre account backend via secure HTTPS.
        </p>

        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">User Control</h2>
        <p class="mb-4 leading-relaxed">You maintain full control over the data processed by the Extension:</p>
        <ul class="list-disc pl-5 space-y-2 mb-6">
          <li>Data extraction from a webpage only happens upon your explicit interaction (e.g., clicking on the extension icon or using its context menus).</li>
          <li>You can revoke access by uninstalling the Extension at any time, which also clears the locally stored authentication token.</li>
        </ul>

        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Contact Information</h2>
        <p class="mb-6 leading-relaxed">
          If you have any questions regarding this Privacy Policy or the MemWyre Extension, you may contact us through standard support channels on our platform at <a href="https://app.memwyre.com" class="text-indigo-600 hover:text-indigo-800 underline">app.memwyre.com</a>.
        </p>
      </div>
      
      <div class="mt-12 pt-8 border-t border-gray-100 text-center">
        <router-link to="/" class="inline-flex items-center text-indigo-600 hover:text-indigo-800 font-medium transition-colors">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          Back to Home
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
// Privacy Policy View
</script>

<style scoped>
/* Optional scoped styles if needed, though Tailwind covers most */
</style>
