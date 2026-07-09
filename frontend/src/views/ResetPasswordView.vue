<template>
  <div class="min-h-screen bg-app flex flex-col items-center justify-center p-6 text-text-primary">
    <div class="max-w-md w-full bg-surface border border-border rounded-3xl p-8 shadow-xl animate-in fade-in duration-700">
      
        <div class="text-center mb-8">
            <h1 class="text-2xl font-bold mb-2">Reset Password</h1>
            <p class="text-sm text-text-secondary">Enter your new password below to regain access.</p>
        </div>

        <div v-if="success" class="space-y-6 text-center">
            <div class="w-16 h-16 bg-green-500/10 text-green-500 rounded-2xl flex items-center justify-center mx-auto mb-6">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <p class="text-green-500 font-medium">
              Your password has been reset successfully.
            </p>
            <router-link to="/login" class="block w-full py-3 bg-primary text-white font-bold rounded-xl hover:bg-primary-600 transition-colors">
              Log in now
            </router-link>
        </div>

        <form v-else @submit.prevent="handleSubmit" class="space-y-6">
            <template v-if="invalidToken">
                <div class="p-4 rounded-lg bg-red-50 text-red-600 text-center font-medium">
                    {{ message || 'Invalid or expired password reset link.' }}
                </div>
                <router-link to="/forgot-password" class="block w-full py-3 bg-surface-2 border border-border text-center font-bold rounded-xl hover:bg-surface-3 transition-colors mt-4">
                    Request new link
                </router-link>
            </template>
            <template v-else>
                <div>
                    <label for="password" class="block text-sm font-medium mb-1.5">New Password</label>
                    <input id="password" v-model="password" type="password" required class="w-full px-4 py-3 bg-surface-2 border border-border rounded-xl focus:ring-2 focus:ring-primary focus:border-transparent transition-shadow outline-none" placeholder="••••••••" />
                    <div v-if="password.length > 0 && password.length < 8" class="mt-2 text-sm text-red-500 font-medium">Password must be at least 8 characters.</div>
                </div>

                <button type="submit" :disabled="loading || password.length < 8" class="w-full py-3 bg-primary text-white font-bold rounded-xl hover:bg-primary-600 disabled:opacity-50 transition-colors mt-6">
                    {{ loading ? 'Resetting...' : 'Reset Password' }}
                </button>
                
                <div v-if="message" class="p-3 rounded-lg text-sm text-center text-red-500 bg-red-50 mt-4">
                    {{ message }}
                </div>
            </template>
        </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const password = ref('');
const loading = ref(false);
const success = ref(false);
const invalidToken = ref(false);
const message = ref('');
const token = ref('');

onMounted(() => {
  token.value = route.query.token;
  if (!token.value) {
    invalidToken.value = true;
    message.value = 'No reset token provided in the URL.';
  }
});

const handleSubmit = async () => {
  loading.value = true;
  message.value = '';
  
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'}/auth/reset-password`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token: token.value, new_password: password.value })
    });
    
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Reset failed');
    
    success.value = true;
  } catch (err) {
    if (err.message.includes('expired') || err.message.includes('Invalid')) {
        invalidToken.value = true;
    }
    message.value = err.message;
  } finally {
    loading.value = false;
  }
};
</script>
