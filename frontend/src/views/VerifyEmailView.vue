<template>
  <div class="min-h-screen bg-app flex flex-col items-center justify-center p-6 text-text-primary">
    <div class="max-w-md w-full bg-surface border border-border rounded-3xl p-8 shadow-xl text-center">
      <div class="w-16 h-16 bg-primary/10 text-primary rounded-2xl flex items-center justify-center mx-auto mb-6">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
      </div>
      
      <h2 class="text-2xl font-bold mb-2">{{ success ? 'Account verified' : 'Email Verification' }}</h2>
      
      <div v-if="loading" class="text-text-secondary py-8">
        Verifying your email address...
      </div>
      
      <div v-else-if="success" class="space-y-6">
        <p class="text-green-500 font-medium">
          {{ message }}
        </p>
        <router-link to="/login" class="block w-full py-3 bg-[#D97757] text-white font-bold rounded-xl hover:bg-[#C4654A] transition-colors">
          Log in
        </router-link>
      </div>
      
      <div v-else class="space-y-6">
        <p class="text-red-500 font-medium bg-red-50 p-4 rounded-lg">
          {{ message }}
        </p>
        <router-link to="/login" class="block text-text-secondary hover:text-primary">
          Return to login
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const loading = ref(true);
const success = ref(false);
const message = ref('');

onMounted(async () => {
  const token = route.query.token;
  if (!token) {
    loading.value = false;
    message.value = 'No verification token provided in the URL.';
    return;
  }
  
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'}/auth/verify-email`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token })
    });
    
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Verification failed');
    
    success.value = true;
    message.value = data.message || 'Your account has been verified. You can log in now.';
  } catch (err) {
    success.value = false;
    message.value = err?.message || 'Verification failed';
  } finally {
    loading.value = false;
  }
});
</script>
