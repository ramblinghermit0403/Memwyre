<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-6" style="background: linear-gradient(135deg, #FFF8F5 0%, #F5F0FF 100%);">
    <!-- Logo / Brand -->
    <div class="mb-8 flex items-center gap-2">
      <div class="w-9 h-9 rounded-xl bg-[#D97757] flex items-center justify-center shadow-md">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </div>
      <span class="text-xl font-bold text-gray-900" style="font-family: 'Inter', system-ui, sans-serif;">MemWyre</span>
    </div>

    <!-- Card -->
    <div class="w-full max-w-md">
      <!-- Loading state -->
      <div v-if="loading" class="bg-white rounded-3xl shadow-xl p-10 text-center border border-gray-100">
        <div class="w-20 h-20 mx-auto mb-6 rounded-full bg-[#FFF5F1] flex items-center justify-center">
          <svg class="w-10 h-10 text-[#D97757] animate-spin" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-900 mb-2">Verifying your email</h2>
        <p class="text-gray-500 text-sm">Just a moment, we're confirming your account...</p>
      </div>

      <!-- Success state -->
      <div v-else-if="success" class="bg-white rounded-3xl shadow-xl p-10 text-center border border-gray-100">
        <div class="w-20 h-20 mx-auto mb-6 rounded-full bg-green-50 flex items-center justify-center">
          <svg class="w-10 h-10 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-900 mb-2">Email verified!</h2>
        <p class="text-gray-500 text-sm mb-8">Your MemWyre account is now active. You can log in and start building your AI memory vault.</p>

        <router-link
          to="/login"
          class="block w-full py-3.5 rounded-xl font-bold text-white text-sm shadow-md transition-all"
          style="background: linear-gradient(135deg, #D97757, #C4654A);"
        >
          Go to Login
        </router-link>

        <p class="mt-4 text-xs text-gray-400">Already logged in? <router-link to="/dashboard" class="text-[#D97757] font-medium hover:underline">Go to Dashboard</router-link></p>
      </div>

      <!-- Error state -->
      <div v-else class="bg-white rounded-3xl shadow-xl p-10 text-center border border-gray-100">
        <div class="w-20 h-20 mx-auto mb-6 rounded-full bg-red-50 flex items-center justify-center">
          <svg class="w-10 h-10 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-900 mb-2">Verification failed</h2>
        <div class="bg-red-50 border border-red-100 rounded-xl px-4 py-3 mb-6">
          <p class="text-red-600 text-sm font-medium">{{ message }}</p>
        </div>
        <p class="text-gray-500 text-sm mb-6">The link may have expired or already been used. Request a new link from the onboarding screen after logging in.</p>

        <router-link
          to="/login"
          class="block w-full py-3.5 rounded-xl font-bold text-white text-sm shadow-md transition-all"
          style="background: linear-gradient(135deg, #D97757, #C4654A);"
        >
          Back to Login
        </router-link>
      </div>
    </div>

    <!-- Footer -->
    <p class="mt-8 text-xs text-gray-400">© {{ new Date().getFullYear() }} MemWyre. All rights reserved.</p>
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
    message.value = 'No verification token found in the URL. Please use the link from your email.';
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
    message.value = err?.message || 'Verification failed. The link may have expired.';
  } finally {
    loading.value = false;
  }
});
</script>
