<template>
  <div class="min-h-screen flex items-center justify-center font-sans text-zinc-900 dark:text-zinc-100 bg-[#FDFCFB] dark:bg-[#1A1A1A] px-4 py-12 sm:px-6 lg:px-8">
    <div class="w-full max-w-[400px] space-y-8 animate-in fade-in duration-700">

      <!-- ─── STEP 1: Registration Form ─── -->
      <transition name="slide-up" mode="out-in">
        <div v-if="!showOtp" key="register" class="space-y-8">
          <div class="text-center">
            <div class="flex justify-center mb-6">
              <img src="/logo.png" alt="Memwyre" class="h-9 w-auto dark:invert opacity-90" />
            </div>
            <h2 class="text-[28px] font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 mb-2">
              Create an account
            </h2>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">
              Get started with your free account
            </p>
          </div>

          <form class="space-y-5" @submit.prevent="handleRegister">
            <div class="space-y-4">
              <div>
                <label for="name" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-1.5">Full name</label>
                <input id="name" name="name" type="text" autocomplete="name" required v-model="name"
                  class="appearance-none block w-full px-3.5 py-2.5 bg-white dark:bg-zinc-900 border border-zinc-300 dark:border-zinc-700 rounded-lg placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-zinc-900 dark:focus:ring-zinc-100 focus:border-transparent sm:text-sm transition-shadow duration-200"
                  placeholder="John Doe" />
              </div>

              <div>
                <label for="email-address" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-1.5">Email address</label>
                <input id="email-address" name="email" type="email" autocomplete="email" required v-model="email"
                  class="appearance-none block w-full px-3.5 py-2.5 bg-white dark:bg-zinc-900 border border-zinc-300 dark:border-zinc-700 rounded-lg placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-zinc-900 dark:focus:ring-zinc-100 focus:border-transparent sm:text-sm transition-shadow duration-200"
                  placeholder="you@example.com" />
              </div>

              <div>
                <label for="password" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-1.5">Password</label>
                <input id="password" name="password" type="password" autocomplete="new-password" required v-model="password"
                  class="appearance-none block w-full px-3.5 py-2.5 bg-white dark:bg-zinc-900 border border-zinc-300 dark:border-zinc-700 rounded-lg placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-zinc-900 dark:focus:ring-zinc-100 focus:border-transparent sm:text-sm transition-shadow duration-200"
                  placeholder="••••••••" />
                <div v-if="password.length > 0 && password.length < 8" class="mt-2 text-sm text-red-500 font-medium">
                  Password must be at least 8 characters.
                </div>
              </div>
            </div>

            <div id="turnstile-container" class="flex justify-center mt-4"></div>

            <div class="pt-2">
              <button type="submit" :disabled="loading || !turnstileToken"
                class="w-full flex justify-center items-center py-2.5 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] disabled:opacity-50 transition-colors duration-200">
                <LoadingLogo v-if="loading" size="sm" class="mr-2 h-4 w-4" />
                {{ loading ? 'Creating account...' : 'Create account' }}
              </button>
            </div>

            <div v-if="error" class="p-3 rounded-lg border border-red-200 dark:border-red-900/50 bg-red-50 dark:bg-red-900/10 mt-4">
              <p class="text-sm text-red-600 dark:text-red-400 font-medium text-center">{{ error }}</p>
            </div>

            <div class="relative my-6">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-zinc-200 dark:border-zinc-800"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-3 bg-[#FDFCFB] dark:bg-[#1A1A1A] text-zinc-500">Or continue with</span>
              </div>
            </div>

            <div class="flex flex-col gap-3">
              <button type="button" @click="loginWithProvider('google')"
                class="w-full inline-flex justify-center items-center py-2.5 px-4 rounded-lg border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-sm font-medium hover:bg-zinc-50 dark:hover:bg-zinc-800 transition-colors duration-200">
                <svg class="h-4 w-4 mr-2" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12.545,10.239v3.821h5.445c-0.712,2.315-2.647,3.972-5.445,3.972c-3.332,0-6.033-2.701-6.033-6.032s2.701-6.032,6.033-6.032c1.498,0,2.866,0.549,3.921,1.453l2.814-2.814C17.503,2.988,15.139,2,12.545,2C7.021,2,2.543,6.477,2.543,12s4.478,10,10.002,10c8.396,0,10.249-7.85,9.426-11.748L12.545,10.239z"/>
                </svg>
                Google
              </button>
              <button type="button" @click="loginWithProvider('github')"
                class="w-full inline-flex justify-center items-center py-2.5 px-4 rounded-lg border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-sm font-medium hover:bg-zinc-50 dark:hover:bg-zinc-800 transition-colors duration-200">
                <svg class="h-4 w-4 mr-2" fill="currentColor" viewBox="0 0 24 24">
                  <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                </svg>
                GitHub
              </button>
            </div>
          </form>

          <div class="text-center pt-2">
            <p class="text-sm text-zinc-600 dark:text-zinc-400">
              Already have an account?
              <router-link to="/login" class="font-medium text-zinc-900 dark:text-zinc-100 hover:underline underline-offset-4 decoration-zinc-300 dark:decoration-zinc-600 transition-colors">
                Sign in
              </router-link>
            </p>
          </div>
        </div>
      </transition>

      <!-- ─── STEP 2: OTP Verification ─── -->
      <transition name="slide-up" mode="out-in">
        <div v-if="showOtp" key="otp" class="space-y-8">
          <div class="text-center">
            <!-- Envelope icon -->
            <div class="mx-auto w-16 h-16 rounded-2xl bg-[#FFF5F1] flex items-center justify-center mb-6">
              <svg class="w-8 h-8 text-[#D97757]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
            </div>
            <h2 class="text-[26px] font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 mb-2">
              Check your email
            </h2>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">
              We sent a 6-digit code to <span class="font-semibold text-zinc-700 dark:text-zinc-300">{{ registeredEmail }}</span>
            </p>
            <p class="text-xs text-zinc-400 mt-1">It expires in 10 minutes.</p>
          </div>

          <form class="space-y-6" @submit.prevent="handleVerifyOtp">
            <!-- OTP input boxes -->
            <div>
              <label class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-3 text-center">Enter verification code</label>
              <div class="flex gap-2 justify-center">
                <input
                  v-for="(_, i) in otpDigits"
                  :key="i"
                  :ref="el => { if (el) otpRefs[i] = el }"
                  v-model="otpDigits[i]"
                  type="text"
                  inputmode="numeric"
                  maxlength="1"
                  @input="onOtpInput(i, $event)"
                  @keydown="onOtpKeydown(i, $event)"
                  @paste="onOtpPaste($event)"
                  class="w-12 h-14 text-center text-xl font-bold bg-white dark:bg-zinc-900 border-2 border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:border-[#D97757] focus:ring-2 focus:ring-[#D97757]/20 transition-all duration-150 text-zinc-900 dark:text-zinc-100"
                  :class="{ 'border-[#D97757]': otpDigits[i] }"
                />
              </div>
            </div>

            <div v-if="otpError" class="p-3 rounded-lg border border-red-200 dark:border-red-900/50 bg-red-50 dark:bg-red-900/10">
              <p class="text-sm text-red-600 dark:text-red-400 font-medium text-center">{{ otpError }}</p>
            </div>

            <button type="submit" :disabled="otpLoading || otpValue.length < 6"
              class="w-full flex justify-center items-center py-2.5 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] disabled:opacity-50 transition-colors duration-200">
              <LoadingLogo v-if="otpLoading" size="sm" class="mr-2 h-4 w-4" />
              {{ otpLoading ? 'Verifying...' : 'Verify & Continue' }}
            </button>

            <div class="text-center space-y-2">
              <p class="text-sm text-zinc-500 dark:text-zinc-400">Didn't receive the code?</p>
              <button type="button" @click="handleResendOtp" :disabled="resendCooldown > 0 || resendLoading"
                class="text-sm font-medium text-[#D97757] hover:text-[#C4654A] disabled:opacity-50 transition-colors">
                {{ resendLoading ? 'Sending...' : resendCooldown > 0 ? `Resend in ${resendCooldown}s` : 'Resend code' }}
              </button>
            </div>

            <div class="text-center">
              <button type="button" @click="goBack" class="text-sm text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-300 transition-colors">
                ← Use a different email
              </button>
            </div>
          </form>
        </div>
      </transition>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useToast } from 'vue-toastification';
import LoadingLogo from '@/components/common/LoadingLogo.vue';

const router = useRouter();
const authStore = useAuthStore();
const toast = useToast();

// ─── Step 1: Registration state ───
const name = ref('');
const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');
const turnstileToken = ref('');
const turnstileId = ref(null);

// ─── Step 2: OTP state ───
const showOtp = ref(false);
const registeredEmail = ref('');
const otpDigits = ref(['', '', '', '', '', '']);
const otpRefs = ref([]);
const otpError = ref('');
const otpLoading = ref(false);
const resendLoading = ref(false);
const resendCooldown = ref(0);
let _resendTimer = null;

const otpValue = computed(() => otpDigits.value.join(''));

const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

// ─── OTP box interaction ───
const onOtpInput = (index, event) => {
  const val = event.target.value.replace(/\D/g, '');
  otpDigits.value[index] = val.slice(-1);
  if (val && index < 5) {
    nextTick(() => otpRefs.value[index + 1]?.focus());
  }
};

const onOtpKeydown = (index, event) => {
  if (event.key === 'Backspace' && !otpDigits.value[index] && index > 0) {
    nextTick(() => otpRefs.value[index - 1]?.focus());
  }
};

const onOtpPaste = (event) => {
  event.preventDefault();
  const pasted = (event.clipboardData || window.clipboardData).getData('text').replace(/\D/g, '').slice(0, 6);
  pasted.split('').forEach((char, i) => {
    if (i < 6) otpDigits.value[i] = char;
  });
  nextTick(() => {
    const lastFilled = Math.min(pasted.length, 5);
    otpRefs.value[lastFilled]?.focus();
  });
};

// ─── Turnstile ───
const loginWithProvider = (provider) => {
  localStorage.setItem('lastProvider', provider);
  window.location.href = `${apiUrl}/auth/oauth/${provider}/login`;
};

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
  clearInterval(_resendTimer);
});

// ─── Step 1: Registration ───
const handleRegister = async () => {
  loading.value = true;
  error.value = '';
  try {
    const res = await fetch(`${apiUrl}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
        name: name.value,
        turnstile_token: turnstileToken.value
      })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Registration failed.');

    registeredEmail.value = data.email;

    if (data.is_verified) {
      // Whitelisted domain — log them in directly
      toast.success('Account created! Please log in.');
      router.push('/login');
      return;
    }

    // Show OTP screen
    showOtp.value = true;
    startResendCooldown();
    await nextTick();
    otpRefs.value[0]?.focus();
  } catch (err) {
    error.value = err.message || 'Registration failed. Please try again.';
    if (window.turnstile && turnstileId.value !== null) {
      window.turnstile.reset(turnstileId.value);
      turnstileToken.value = '';
    }
  } finally {
    loading.value = false;
  }
};

// ─── Step 2: OTP Verification ───
const handleVerifyOtp = async () => {
  if (otpValue.value.length < 6) return;
  otpLoading.value = true;
  otpError.value = '';
  try {
    const res = await fetch(`${apiUrl}/auth/verify-otp`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: registeredEmail.value, otp: otpValue.value })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Verification failed.');

    // Store tokens and log user in immediately
    authStore.setTokens(data.access_token, data.refresh_token);
    try { await authStore.fetchUser(); } catch (e) { /* use token claims */ }

    toast.success('Email verified! Welcome to Memwyre 🎉');
    router.push('/dashboard');
  } catch (err) {
    otpError.value = err.message || 'Verification failed. Please try again.';
    // Clear OTP boxes on wrong code
    otpDigits.value = ['', '', '', '', '', ''];
    await nextTick();
    otpRefs.value[0]?.focus();
  } finally {
    otpLoading.value = false;
  }
};

// ─── Resend OTP ───
const startResendCooldown = () => {
  resendCooldown.value = 30;
  _resendTimer = setInterval(() => {
    resendCooldown.value -= 1;
    if (resendCooldown.value <= 0) {
      clearInterval(_resendTimer);
      resendCooldown.value = 0;
    }
  }, 1000);
};

const handleResendOtp = async () => {
  if (resendCooldown.value > 0 || resendLoading.value) return;
  resendLoading.value = true;
  try {
    const res = await fetch(`${apiUrl}/auth/resend-otp`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: registeredEmail.value })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Failed to resend.');
    toast.success('New code sent! Check your email.');
    otpDigits.value = ['', '', '', '', '', ''];
    otpError.value = '';
    startResendCooldown();
    await nextTick();
    otpRefs.value[0]?.focus();
  } catch (err) {
    toast.error(err.message || 'Failed to resend code.');
  } finally {
    resendLoading.value = false;
  }
};

// ─── Go back to registration ───
const goBack = () => {
  showOtp.value = false;
  otpDigits.value = ['', '', '', '', '', ''];
  otpError.value = '';
  clearInterval(_resendTimer);
  resendCooldown.value = 0;
};
</script>

<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.slide-up-enter-from {
  opacity: 0;
  transform: translateY(16px);
}
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-16px);
}
</style>
