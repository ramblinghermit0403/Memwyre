<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />
    
    <main class="flex-1 overflow-hidden w-full max-w-4xl mx-auto py-10 px-4 sm:px-6 lg:px-8 flex flex-col h-full">
      <div class="flex-none">
          <div class="mb-8">
            <h1 class="text-3xl font-bold text-gray-900 dark:text-text-primary">Settings</h1>
          </div>

          <!-- Tab Header -->
          <div class="border-b border-gray-200 dark:border-border mb-8 overflow-x-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:'none'] [scrollbar-width:'none']">
              <nav class="-mb-px flex space-x-8">
                  <button 
                    @click="activeTab = 'general'"
                    :class="activeTab === 'general' ? 'border-[#D97757] text-[#D97757]' : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'"
                    class="whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm transition-colors"
                  >
                      General
                  </button>
                  <button 
                    @click="activeTab = 'integration'"
                    :class="activeTab === 'integration' ? 'border-[#D97757] text-[#D97757]' : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'"
                    class="whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm transition-colors"
                  >
                      Integrations
                  </button>
              </nav>
          </div>
      </div>

      <!-- Scrollable Content Area -->
      <div class="flex-1 overflow-y-auto min-h-0 pr-2 custom-scrollbar">
          <!-- General Tab -->
          <div v-show="activeTab === 'general'" class="bg-white dark:bg-surface shadow rounded-lg px-8 py-8 border border-gray-100 dark:border-border animate-fade-in relative">
               
               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white mb-6">Appearance</h3>
               <div class="space-y-6 mb-8">
                   <div class="flex items-center justify-between">
                      <div>
                        <span class="text-sm font-medium text-gray-900 dark:text-white">Theme</span>
                        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Customize the look and feel of your workspace.</p>
                      </div>
                      <ThemeToggle />
                   </div>
               </div>
               
               <hr class="border-gray-100 dark:border-border mb-8" />

               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white mb-6">Preferences</h3>
               <div class="space-y-6">
                    <!-- Auto-Approve Toggle -->
                    <div class="flex items-center justify-between">
                       <div>
                        <span class="text-sm font-medium text-gray-900 dark:text-white">Auto-Approve New Memories</span>
                        <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Automatically add created memories to the vector store without manual review.</p>
                      </div>
                      <button 
                        @click="toggleAutoApprove" 
                        :class="settings.auto_approve ? 'bg-[#D97757]' : 'bg-gray-200 dark:bg-gray-700'" 
                        class="relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757]"
                      >
                        <span 
                          aria-hidden="true" 
                          :class="settings.auto_approve ? 'translate-x-5' : 'translate-x-0'" 
                          class="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200"
                        ></span>
                      </button>
                    </div>
                    
                    <hr class="border-gray-100 dark:border-border" />
                    
                    <!-- Account Info -->
                    <div>
                       <h4 class="text-sm font-medium text-gray-900 dark:text-text-primary mb-4">Account</h4>
                       <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                           <div class="sm:col-span-4">
                               <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email address</label>
                               <div class="flex items-center gap-3">
                                   <input type="email" disabled :value="authStore.user?.email || 'user@example.com'" class="bg-gray-50 dark:bg-gray-700 block w-full sm:max-w-md sm:text-sm border-gray-300 dark:border-gray-600 rounded-md py-2 px-3 text-gray-500 dark:text-gray-400 cursor-not-allowed">
                                   <span v-if="authStore.user?.is_verified" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
                                       Verified
                                   </span>
                                   <span v-else class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200">
                                       Unverified
                                   </span>
                               </div>
                               <div v-if="authStore.user && !authStore.user.is_verified" class="mt-3">
                                   <p class="text-sm text-red-600 dark:text-red-400 mb-2">You must verify your email address to access core features.</p>
                                   <button @click="resendVerification" :disabled="resendingEmail" class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-md shadow-sm text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] disabled:opacity-50 disabled:cursor-not-allowed hover:cursor-pointer">
                                       <svg v-if="resendingEmail" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                                       {{ resendingEmail ? 'Sending...' : 'Resend Verification Email' }}
                                   </button>
                               </div>
                           </div>
                       </div>
                    </div>
               </div>
          </div>

          <!-- Integrations Tab -->
          <div v-show="activeTab === 'integration'" class="bg-white dark:bg-surface shadow rounded-lg px-8 py-8 border border-gray-100 dark:border-border animate-fade-in">
               <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-text-primary mb-2">Connected LLM Clients</h3>
               <p class="text-sm text-gray-500 dark:text-text-secondary mb-6">Manage external LLM providers and their permissions.</p>
               
               <!-- Keys List -->
               <div class="space-y-3 mb-8" v-if="keys.length > 0">
                    <div v-for="key in keys" :key="key.id" class="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg border border-gray-200 dark:border-gray-600">
                      <div class="flex items-center gap-3">
                        <div class="p-2 bg-white dark:bg-gray-600 rounded-md shadow-sm">
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" /></svg>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-medium text-gray-900 dark:text-text-primary capitalize">{{ key.provider }}</span>
                            <div class="flex gap-2 mt-0.5">
                                <span v-if="key.permissions.read" class="text-[10px] uppercase font-bold tracking-wider text-black dark:text-white">Read</span>
                                <span v-if="key.permissions.write" class="text-[10px] uppercase font-bold tracking-wider text-black dark:text-white">Write</span>
                            </div>
                        </div>
                      </div>
                      <button @click="deleteKey(key.id)" class="text-gray-400 hover:text-red-600 dark:text-gray-500 dark:hover:text-red-400 p-2 transition-colors">
                          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                      </button>
                    </div>
               </div>
               
                   <!-- API Keys Management -->
                   <div class="mb-8">
                       <div class="flex items-center justify-between mb-4">
                           <h4 class="text-sm font-medium text-gray-900 dark:text-text-primary">Your API Keys</h4>
                           <div class="flex items-center gap-2">
                               <button 
                                    @click="handleConnectClientClick"
                                    class="inline-flex items-center px-3 py-1.5 border border-gray-300 dark:border-gray-600 text-xs font-medium rounded text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 transition-colors shadow-sm"
                               >
                                   <svg class="w-4 h-4 mr-1.5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" /></svg>
                                   Connect MCP Client
                               </button>
                               <button 
                                    v-if="!showAddKeyForm"
                                    @click="showAddKeyForm = true"
                                    class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded text-white bg-[#D97757] hover:bg-[#C4654A] transition-colors shadow-sm"
                               >
                                   + Generate Key
                               </button>
                           </div>
                       </div>

                       <!-- Key Generation Form -->
                       <div v-if="showAddKeyForm" class="mb-6 bg-gray-50 dark:bg-gray-700/50 p-4 rounded-lg border border-gray-200 dark:border-gray-600 animate-fade-in">
                            <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Key Name (e.g. "VS Code")</label>
                            <div class="flex gap-2">
                                <input 
                                    v-model="newKeyName" 
                                    @keyup.enter="generateKey"
                                    type="text" 
                                    placeholder="Enter a name..." 
                                    class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-[#D97757] focus:border-[#D97757] sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white py-2 px-3"
                                />
                                <button 
                                    @click="generateKey"
                                    :disabled="generatingKey || !newKeyName"
                                    class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-[#D97757] hover:bg-[#C4654A] disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                                >
                                    <LoadingLogo v-if="generatingKey" size="sm" class="w-4 h-4" :isWhite="true" />
                                    <span v-else>Generate</span>
                                </button>
                                <button 
                                    @click="showAddKeyForm = false"
                                    class="inline-flex items-center px-3 py-2 border border-gray-300 dark:border-gray-600 text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 transition-colors"
                                >
                                    Cancel
                                </button>
                            </div>
                       </div>

                       <!-- NEW KEY DISPLAY (Important!) -->
                       <div v-if="justGeneratedKey" class="mb-6 bg-green-50 dark:bg-green-900/20 p-4 rounded-lg border border-green-200 dark:border-green-800 animate-fade-in">
                           <div class="flex items-start">
                               <div class="flex-shrink-0">
                                   <svg class="h-5 w-5 text-green-400" viewBox="0 0 20 20" fill="currentColor">
                                       <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                   </svg>
                               </div>
                               <div class="ml-3 w-full">
                                   <h3 class="text-sm font-medium text-green-800 dark:text-green-200">API Key Generated!</h3>
                                   <div class="mt-2 text-sm text-green-700 dark:text-green-300">
                                       <p class="mb-2">Please copy this key now. You won't be able to see it again.</p>
                                       <div class="flex items-center gap-2">
                                           <code class="block w-full bg-white dark:bg-black/20 p-2 rounded border border-green-200 dark:border-green-800 font-mono text-xs break-all select-all">{{ justGeneratedKey }}</code>
                                           <button @click="copyGeneratedKey" class="p-2 text-green-600 hover:text-green-800 dark:text-green-400 dark:hover:text-green-200">
                                               <svg v-if="!keyCopied" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
                                               <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                                           </button>
                                       </div>
                                   </div>
                               </div>
                           </div>
                           
                           <McpConnectionGuide 
                                v-if="showGuideForKey === justGeneratedKey" 
                                :apiKey="justGeneratedKey" 
                                @close="showGuideForKey = null"
                           />
                       </div>

                       <!-- Empty State -->
                       <div v-if="apiKeys.length === 0 && !showAddKeyForm" class="text-center py-8 bg-gray-50 dark:bg-gray-700/30 rounded-lg border-2 border-dashed border-gray-200 dark:border-gray-600">
                           <svg class="mx-auto h-10 w-10 text-gray-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" /></svg>
                           <h3 class="text-sm font-medium text-gray-900 dark:text-text-primary">No API Keys Found</h3>
                           <p class="mt-1 text-sm text-gray-500 dark:text-gray-400 max-w-sm mx-auto mb-5">Generate an API key to connect Memwyre to external AI clients like Claude Desktop or Cursor.</p>
                           <div class="flex justify-center gap-3">
                               <button @click="showAddKeyForm = true" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-[#D97757] hover:bg-[#C4654A] transition-colors shadow-sm">
                                   <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                                   Generate First Key
                               </button>
                           </div>
                       </div>

                       <!-- Global Connection Guide (used when handleConnectClientClick is called) -->
                       <div v-if="showGlobalGuide" class="mb-6 animate-fade-in">
                            <McpConnectionGuide 
                                apiKey="<YOUR_API_KEY>" 
                                @close="showGlobalGuide = false"
                           />
                       </div>

                       <!-- List -->
                       <div v-else class="space-y-3">
                            <div v-for="key in apiKeys" :key="key.id" class="flex items-center justify-between p-3 bg-white dark:bg-gray-700 rounded-lg border border-gray-200 dark:border-gray-600 shadow-sm transition-all hover:shadow-md">
                                <div class="flex items-center gap-3">
                                    <div class="p-2 bg-gray-100 dark:bg-gray-600 rounded-md">
                                        <svg class="w-5 h-5 text-gray-500 dark:text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" /></svg>
                                    </div>
                                    <div>
                                        <div class="flex items-center gap-2">
                                            <span class="font-medium text-gray-900 dark:text-text-primary">{{ key.name }}</span>
                                            <span v-if="!key.is_active" class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-gray-200 dark:bg-gray-600 text-gray-600 dark:text-gray-300">REVOKED</span>
                                        </div>
                                        <div class="text-xs text-gray-500 dark:text-text-secondary font-mono mt-0.5 flex items-center gap-2">
                                            <span>{{ key.prefix }} • Created {{ new Date(key.created_at).toLocaleDateString() }}</span>
                                            <button @click="showGuideForKey = showGuideForKey === ('<existing_key>') ? null : ('<existing_key>')" class="text-xs text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300 underline font-sans ml-2">Setup Guide</button>
                                        </div>
                                    </div>
                                </div>
                                <button @click="revokeKeyConfirm(key.id)" class="text-gray-400 hover:text-red-600 dark:text-gray-500 dark:hover:text-red-400 p-2 transition-colors" title="Revoke Key">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                </button>
                            </div>
                            
                            <McpConnectionGuide 
                                v-if="showGuideForKey === '<existing_key>'" 
                                apiKey="<YOUR_API_KEY>" 
                                @close="showGuideForKey = null" 
                                class="mt-4"
                            />
                       </div>
                   </div>

                    <!-- Hidden Form -->
                    <div v-if="false">
                        <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 mb-4">
                          <div>
                            <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-1">Provider</label>
                            <div class="relative">
                                <select v-model="newKey.provider" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-[#D97757] focus:border-[#D97757] sm:text-sm rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white appearance-none">
                                  <option value="openai">OpenAI</option>
                                  <option value="anthropic">Anthropic</option>
                                  <option value="gemini">Google Gemini</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 dark:text-gray-400">
                                     <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                                </div>
                            </div>
                          </div>
                          <div>
                            <label class="block text-xs font-medium text-gray-500 uppercase tracking-wider mb-1">API Key</label>
                            <input type="password" v-model="newKey.api_key" class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-[#D97757] focus:border-[#D97757] sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white py-2 px-3" placeholder="sk-..." />
                          </div>
                        </div>
                        
                        <div class="flex items-center gap-6 mb-6">
                           <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="newKey.permissions.read" class="rounded border-gray-300 text-black shadow-sm focus:border-[#D97757] focus:ring focus:ring-[#D97757] focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                            <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Allow Read</span>
                          </label>
                          <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="newKey.permissions.write" class="rounded border-gray-300 text-black shadow-sm focus:border-[#D97757] focus:ring focus:ring-[#D97757] focus:ring-opacity-50 dark:bg-gray-700 dark:border-gray-600">
                            <span class="ml-2 text-sm text-gray-600 dark:text-gray-300">Allow Write</span>
                          </label>
                        </div>
                        
                        <button 
                            @click="addKey" 
                            :disabled="addingKey"
                            class="w-full sm:w-auto inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] transition-colors disabled:opacity-70 disabled:cursor-not-allowed gap-2"
                        >
                            <LoadingLogo v-if="addingKey" size="sm" class="w-4 h-4" :isWhite="true" />
                            {{ addingKey ? 'Connecting...' : 'Connect Provider' }}
                        </button>
                    </div>

               
               <div class="mt-10 pt-8 border-t border-gray-100 dark:border-border">
                  <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-text-primary mb-2">Browser Extension Auth</h3>
                  <p class="text-sm text-gray-500 dark:text-text-secondary mb-6">Use this token to log in to the Brain Vault extension.</p>
                  
                  <div class="flex items-center gap-4">
                     <button @click="copyToken" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] transition-colors">
                       <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
                       <span v-if="tokenCopied">Copied!</span>
                       <span v-else>Copy Token</span>
                     </button>
                     <button @click="restartTour" class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 shadow-sm text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 transition-colors">
                       Restart Tour
                     </button>
                  </div>
               </div>
          </div>
      </div>
    </main>
    
    <ConfirmationModal
      :is-open="showDeleteModal"
      title="Remove Key"
      message="Are you sure you want to remove this API key? This action cannot be undone."
      confirm-text="Remove"
      :loading="deletingKey"
      @confirm="confirmDeleteKey"
      @cancel="showDeleteModal = false"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import api from '../services/api';
import apiKeysService from '../services/apiKeys'; // Import Service
import NavBar from '../components/NavBar.vue';
import ThemeToggle from '../components/ThemeToggle.vue';
import ConfirmationModal from '../components/ConfirmationModal.vue';
import McpConnectionGuide from '../components/McpConnectionGuide.vue';
import { useToast } from 'vue-toastification';

import LoadingLogo from '@/components/common/LoadingLogo.vue';

const authStore = useAuthStore();
const router = useRouter();
const toast = useToast();

const activeTab = ref('general');
const keys = ref([]);
const settings = ref({ auto_approve: true });
const newKey = ref({
  provider: 'openai',
  api_key: '',
  permissions: { read: true, write: false, auto_save: false }
});
const tokenCopied = ref(false);

const resendingEmail = ref(false);

const resendVerification = async () => {
    if (resendingEmail.value) return;
    resendingEmail.value = true;
    try {
        await api.post('/auth/resend-verification');
        toast.success("Verification email sent! Please check your inbox.");
    } catch (err) {
        toast.error(err.response?.data?.detail || "Failed to resend email.");
    } finally {
        resendingEmail.value = false;
    }
};

// Loading States
const addingKey = ref(false);
const deletingKey = ref(false);

// API Keys Logic
const apiKeys = ref([]);
const showAddKeyForm = ref(false);
const newKeyName = ref("");
const generatingKey = ref(false);
const justGeneratedKey = ref(null);
const keyCopied = ref(false);
const showGuideForKey = ref(null);
const showGlobalGuide = ref(false);

const handleConnectClientClick = () => {
    if (apiKeys.value.length === 0) {
        // Prompt them to create a key first
        showAddKeyForm.value = true;
        toast.info("Please generate an API key first to connect your client.");
    } else {
        // Show the generic global guide
        showGlobalGuide.value = true;
        // Scroll into view
        setTimeout(() => {
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        }, 100);
    }
};

const loadApiKeys = async () => {
    try {
        const res = await apiKeysService.listKeys();
        apiKeys.value = res.data;
    } catch (err) {
        console.error("Failed to list keys", err);
    }
};

const generateKey = async () => {
    if (!newKeyName.value) return;
    generatingKey.value = true;
    try {
        const res = await apiKeysService.createKey(newKeyName.value);
        justGeneratedKey.value = res.data.key;
        showGuideForKey.value = res.data.key;
        toast.success("API Key generated successfully");
        newKeyName.value = "";
        showAddKeyForm.value = false;
        loadApiKeys();
    } catch (err) {
        toast.error("Failed to generate key");
    } finally {
        generatingKey.value = false;
    }
};

const copyGeneratedKey = async () => {
    if (justGeneratedKey.value) {
        await navigator.clipboard.writeText(justGeneratedKey.value);
        keyCopied.value = true;
        toast.success("Key copied to clipboard");
        setTimeout(() => keyCopied.value = false, 2000);
    }
};

const revokeKeyConfirm = (id) => {
    keyToDelete.value = id; // Reuse existing modal logic
    showDeleteModal.value = true;
};

// ... existing logic ...

const loadSettings = async () => {
  try {
    const res = await api.get('/user/settings');
    settings.value = { ...settings.value, ...res.data };
  } catch (err) {
    console.error(err);
  }
};

const toggleAutoApprove = async () => {
  const newVal = !settings.value.auto_approve;
  settings.value.auto_approve = newVal;
  try {
    await api.patch('/user/settings', { auto_approve: newVal });
    toast.success("Settings updated");
  } catch (err) {
    settings.value.auto_approve = !newVal; // revert
    toast.error("Failed to update settings");
  }
};

const loadKeys = async () => {
  try {
    const res = await api.get('/user/llm-keys');
    keys.value = res.data;
  } catch (err) {
    console.error(err);
  }
};

const addKey = async () => {
  if (!newKey.value.api_key) return toast.error("API Key required");
  addingKey.value = true;
  try {
    await api.post('/user/llm-keys', newKey.value);
    toast.success("Key added");
    newKey.value.api_key = ""; // clear
    loadKeys();
  } catch (err) {
    toast.error("Failed to add key");
  } finally {
    addingKey.value = false;
  }
};

const keyToDelete = ref(null);
const showDeleteModal = ref(false);

const deleteKey = (id) => {
  keyToDelete.value = id;
  showDeleteModal.value = true;
};

const confirmDeleteKey = async () => {
    if (!keyToDelete.value) return;
    deletingKey.value = true;
    try {
        // HACK: Differentiate based on where it was called from. 
        // Ideally we'd have separate modals or pass a type.
        // Checking if ID exists in apiKeys list vs llm-keys list could work, 
        // but IDs might collide if integers.
        // For MVP, we'll try to delete from User Keys first, if not found then LLM keys?
        // BETTER: Check if it's in `apiKeys` array
        const isUserKey = apiKeys.value.some(k => k.id === keyToDelete.value);

        if (isUserKey) {
             await apiKeysService.revokeKey(keyToDelete.value);
             loadApiKeys();
        } else {
             await api.delete(`/user/llm-keys/${keyToDelete.value}`);
             loadKeys();
        }
        
        toast.success("Key removed");
        showDeleteModal.value = false;
        keyToDelete.value = null;
    } catch (err) {
        toast.error("Failed to remove key");
    } finally {
        deletingKey.value = false;
    }
};

const copyToken = async () => {
  if (!authStore.token) {
    return toast.error("No token available");
  }
  try {
    await navigator.clipboard.writeText(authStore.token);
    tokenCopied.value = true;
    toast.success("Token copied");
    setTimeout(() => {
      tokenCopied.value = false;
    }, 2000);
  } catch (err) {
    toast.error("Failed to copy token");
  }
};

const restartTour = () => {
    localStorage.removeItem('tour_completed');
    localStorage.setItem('tour_requested', 'true');
    toast.info("Tour reset. Returning to Dashboard...");
    setTimeout(() => router.push('/dashboard'), 1000);
};

// Initial load
loadKeys();
loadSettings();
loadApiKeys();
</script>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
