<template>
  <div class="px-6 py-8 max-w-4xl mx-auto text-text-primary">
    <h2 class="text-3xl font-bold mb-8">Admin: Payment Bypass</h2>
    
    <div class="space-y-8">
      <!-- Invite Link -->
      <div class="p-6 bg-surface border border-border rounded-2xl shadow-sm">
        <h3 class="text-xl font-bold mb-4">Generate Invite Link</h3>
        <p class="text-sm text-text-secondary mb-4">Create a secure link to bypass the payment wall for a new or existing user.</p>
        
        <div class="flex gap-4">
          <input v-model="targetEmail" type="email" placeholder="Optional: Target Email" class="flex-1 px-4 py-2 bg-surface-2 border border-border rounded-lg text-text-primary focus:outline-none focus:border-primary" />
          <button @click="generateInvite" :disabled="loadingInvite" class="px-6 py-2 bg-primary text-white font-bold rounded-lg hover:bg-primary-600 disabled:opacity-50">
            {{ loadingInvite ? 'Generating...' : 'Generate Link' }}
          </button>
        </div>
        
        <div v-if="inviteLink" class="mt-4 p-4 bg-primary/10 border border-primary/20 rounded-lg flex items-center justify-between gap-4">
          <code class="text-sm font-mono text-primary break-all">{{ inviteLink }}</code>
          <button @click="copyLink" class="px-4 py-1.5 bg-surface text-primary border border-primary/30 rounded text-sm hover:bg-primary/5">
            {{ copied ? 'Copied!' : 'Copy' }}
          </button>
        </div>
      </div>

      <!-- Direct Override -->
      <div class="p-6 bg-surface border border-border rounded-2xl shadow-sm">
        <h3 class="text-xl font-bold mb-4">Direct Auto-Upgrade</h3>
        <p class="text-sm text-text-secondary mb-4">Instantly upgrade an existing registered user to Pro without an invite link.</p>
        
        <div class="flex gap-4">
          <input v-model="directEmail" type="email" placeholder="User's Exact Email" class="flex-1 px-4 py-2 bg-surface-2 border border-border rounded-lg text-text-primary focus:outline-none focus:border-primary" />
          <button @click="applyDirect" :disabled="loadingDirect" class="px-6 py-2 border border-primary text-primary font-bold rounded-lg hover:bg-primary/10 disabled:opacity-50">
            {{ loadingDirect ? 'Applying...' : 'Upgrade User' }}
          </button>
        </div>
        
        <div v-if="directMessage" class="mt-4 text-sm font-medium" :class="directError ? 'text-red-500' : 'text-green-500'">
          {{ directMessage }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();
const targetEmail = ref('');
const inviteLink = ref('');
const loadingInvite = ref(false);
const copied = ref(false);

const directEmail = ref('');
const loadingDirect = ref(false);
const directMessage = ref('');
const directError = ref(false);

const generateInvite = async () => {
  loadingInvite.value = true;
  copied.value = false;
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/admin/bypass/invite`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.token}`
      },
      body: JSON.stringify({ target_email: targetEmail.value || null })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Failed to generate invite');
    
    const baseUrl = window.location.origin;
    inviteLink.value = `${baseUrl}/redeem?token=${data.token}`;
  } catch (err) {
    alert(err.message);
  } finally {
    loadingInvite.value = false;
  }
};

const copyLink = async () => {
  if (!inviteLink.value) return;
  try {
    await navigator.clipboard.writeText(inviteLink.value);
    copied.value = true;
    setTimeout(() => { copied.value = false }, 2000);
  } catch (err) {
    console.error('Failed to copy', err);
  }
};

const applyDirect = async () => {
  if (!directEmail.value) return;
  loadingDirect.value = true;
  directMessage.value = '';
  directError.value = false;
  
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/admin/bypass/apply`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.token}`
      },
      body: JSON.stringify({ email: directEmail.value })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Failed to apply bypass');
    
    directMessage.value = data.message;
    directEmail.value = '';
  } catch (err) {
    directError.value = true;
    directMessage.value = err.message;
  } finally {
    loadingDirect.value = false;
  }
};
</script>
