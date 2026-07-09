<template>
  <div class="min-h-screen bg-app flex flex-col items-center justify-center p-6 text-text-primary">
    <div class="max-w-md w-full bg-surface border border-border rounded-3xl p-8 shadow-xl animate-in fade-in duration-700">
      
        <div class="text-center mb-8">
            <h1 class="text-2xl font-bold mb-2">Forgot Password</h1>
            <p class="text-sm text-text-secondary">Enter your email and we'll send you a link to reset your password.</p>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6">
            <div>
                <label for="email" class="block text-sm font-medium mb-1.5">Email address</label>
                <input id="email" v-model="email" type="email" required class="w-full px-4 py-3 bg-surface-2 border border-border rounded-xl focus:ring-2 focus:ring-primary focus:border-transparent transition-shadow outline-none" placeholder="you@example.com" />
            </div>

            <div id="turnstile-container" class="flex justify-center mt-4"></div>

            <button type="submit" :disabled="loading || !turnstileToken" class="w-full py-3 bg-primary text-white font-bold rounded-xl hover:bg-primary-600 disabled:opacity-50 transition-colors">
                {{ loading ? 'Sending...' : 'Send Reset Link' }}
            </button>
            
            <div v-if="message" :class="error ? 'text-red-500 bg-red-50' : 'text-green-500 bg-green-50'" class="p-3 rounded-lg text-sm text-center">
                {{ message }}
            </div>
            
            <div class="text-center pt-2">
                <router-link to="/login" class="text-sm font-medium text-text-secondary hover:text-primary transition-colors">
                    Back to login
                </router-link>
            </div>
        </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const email = ref('');
const loading = ref(false);
const message = ref('');
const error = ref(false);

const turnstileToken = ref('');
const turnstileId = ref(null);

onMounted(() => {
  window.onTurnstileSuccess = (token) => {
    turnstileToken.value = token;
  };

  const loadTurnstile = () => {
    if (window.turnstile) {
        turnstileId.value = window.turnstile.render('#turnstile-container', {
            sitekey: import.meta.env.VITE_TURNSTILE_SITE_KEY || '1x00000000000000000000AA',
            callback: window.onTurnstileSuccess
        });
    }
  };

  if (!document.getElementById('turnstile-script')) {
    const script = document.createElement('script');
    script.id = 'turnstile-script';
    script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
    script.async = true;
    script.defer = true;
    script.onload = loadTurnstile;
    document.head.appendChild(script);
  } else {
    setTimeout(loadTurnstile, 200);
  }
});

onUnmounted(() => {
  if (window.turnstile && turnstileId.value !== null) {
      window.turnstile.remove(turnstileId.value);
  }
});

const handleSubmit = async () => {
  loading.value = true;
  message.value = '';
  error.value = false;
  
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'}/auth/forgot-password`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, turnstile_token: turnstileToken.value })
    });
    
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Request failed');
    
    error.value = false;
    message.value = data.message || 'Check your email for the reset link.';
    email.value = '';
  } catch (err) {
    error.value = true;
    message.value = err.message;
  } finally {
    loading.value = false;
    if (window.turnstile && turnstileId.value !== null) {
       window.turnstile.reset(turnstileId.value);
       turnstileToken.value = '';
    }
  }
};
</script>
