<template>
  <div class="min-h-screen bg-app flex flex-col items-center justify-center p-6 text-text-primary">
    <div class="max-w-md w-full bg-surface border border-border rounded-3xl p-8 shadow-xl text-center">
      <div class="w-16 h-16 bg-primary/10 text-primary rounded-2xl flex items-center justify-center mx-auto mb-6">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"></path></svg>
      </div>
      
      <h1 class="text-2xl font-bold mb-2">Redeem Invite</h1>
      
      <div v-if="loading" class="text-text-secondary py-8">
        Validating your invite token...
      </div>
      
      <div v-else-if="success" class="space-y-6">
        <p class="text-green-500 font-medium">
          {{ message }}
        </p>
        <router-link to="/dashboard" class="block w-full py-3 bg-primary text-white font-bold rounded-xl hover:bg-primary-600 transition-colors">
          Go to Dashboard
        </router-link>
      </div>
      
      <div v-else class="space-y-6">
        <p class="text-red-500 font-medium bg-red-50 dark:bg-red-900/20 p-4 rounded-lg">
          {{ message || 'Invalid or expired token.' }}
        </p>
        <router-link to="/" class="block text-text-secondary hover:text-primary">
          Return to Home
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const loading = ref(true);
const success = ref(false);
const message = ref('');

onMounted(async () => {
  const token = route.query.token;
  
  if (!token) {
    loading.value = false;
    message.value = 'No token provided in the URL.';
    return;
  }
  
  // If user is not logged in, redirect to login but preserve the token in the redirect query
  if (!authStore.isAuthenticated) {
    router.push({
      path: '/login',
      query: { redirect: `/redeem?token=${token}` }
    });
    return;
  }
  
  // Attempt to redeem
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/bypass/redeem`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.token}`
      },
      body: JSON.stringify({ token })
    });
    
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Failed to redeem token');
    
    success.value = true;
    message.value = data.message || 'Successfully unlocked Pro access!';
    
    // Refresh user context so the app knows they are Pro
    if (authStore.fetchUser) {
      await authStore.fetchUser();
    }
  } catch (err) {
    success.value = false;
    message.value = err.message;
  } finally {
    loading.value = false;
  }
});
</script>
