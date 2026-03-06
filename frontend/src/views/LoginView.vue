<template>
  <div class="min-h-screen flex items-center justify-center font-sans text-zinc-900 dark:text-zinc-100 bg-[#FDFCFB] dark:bg-[#1A1A1A] px-4 py-12 sm:px-6 lg:px-8">
    <div class="w-full max-w-[400px] space-y-8 animate-in fade-in duration-700">
      
      <!-- Standard Login Form -->
      <div v-if="!lastKnownUser" class="space-y-8">
          <div class="text-center">
             <div class="mx-auto h-12 w-12 flex items-center justify-center mb-6">
                 <img src="/image.svg" alt="MemWyre" class="h-10 w-10 object-contain invert dark:invert-0 opacity-90" />
             </div>
             <h2 class="text-[28px] font-semibold tracking-tight text-zinc-900 dark:text-zinc-50">
                Log in to MemWyre
             </h2>
          </div>

          <form class="space-y-5" @submit.prevent="handleLogin">
             <div class="space-y-4">
                 <div>
                    <label for="email-address" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-1.5">Email address</label>
                    <input id="email-address" name="email" type="email" autocomplete="email" required v-model="email" class="appearance-none block w-full px-3.5 py-2.5 bg-white dark:bg-zinc-900 border border-zinc-300 dark:border-zinc-700 rounded-lg placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-zinc-900 dark:focus:ring-zinc-100 focus:border-transparent sm:text-sm transition-shadow duration-200" placeholder="name@example.com" />
                 </div>
                 
                 <div>
                    <div class="flex items-center justify-between mb-1.5">
                        <label for="password" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300">Password</label>
                        <router-link to="/forgot-password" class="text-sm font-medium text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors">
                            Forgot password?
                        </router-link>
                    </div>
                    <input id="password" name="password" type="password" autocomplete="current-password" required v-model="password" class="appearance-none block w-full px-3.5 py-2.5 bg-white dark:bg-zinc-900 border border-zinc-300 dark:border-zinc-700 rounded-lg placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-zinc-900 dark:focus:ring-zinc-100 focus:border-transparent sm:text-sm transition-shadow duration-200" placeholder="••••••••" />
                    <div v-if="password.length > 0 && password.length < 8" class="mt-2 text-sm text-red-500 font-medium">Password must be at least 8 characters.</div>
                 </div>
             </div>

             <div id="turnstile-container" class="flex justify-center mt-4"></div>

             <div class="pt-2">
                 <button type="submit" :disabled="loading || !turnstileToken" class="w-full flex justify-center items-center py-2.5 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] disabled:opacity-50 transition-colors duration-200">
                    <LoadingLogo v-if="loading" size="sm" class="mr-2 h-4 w-4" />
                    {{ loading ? 'Authenticating...' : 'Continue' }}
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
                 <button type="button" @click="loginWithProvider('google')" class="w-full inline-flex justify-center items-center py-2.5 px-4 rounded-lg border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-sm font-medium hover:bg-zinc-50 dark:hover:bg-zinc-800 transition-colors duration-200">
                     <svg class="h-4 w-4 mr-2" viewBox="0 0 24 24" fill="currentColor"><path d="M12.545,10.239v3.821h5.445c-0.712,2.315-2.647,3.972-5.445,3.972c-3.332,0-6.033-2.701-6.033-6.032s2.701-6.032,6.033-6.032c1.498,0,2.866,0.549,3.921,1.453l2.814-2.814C17.503,2.988,15.139,2,12.545,2C7.021,2,2.543,6.477,2.543,12s4.478,10,10.002,10c8.396,0,10.249-7.85,9.426-11.748L12.545,10.239z"/></svg>
                     Google
                 </button>
                 <button type="button" @click="loginWithProvider('github')" class="w-full inline-flex justify-center items-center py-2.5 px-4 rounded-lg border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-sm font-medium hover:bg-zinc-50 dark:hover:bg-zinc-800 transition-colors duration-200">
                     <svg class="h-4 w-4 mr-2" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                     GitHub
                 </button>
             </div>
          </form>

          <div class="text-center pt-2">
             <p class="text-sm text-zinc-600 dark:text-zinc-400">
                 Don't have an account? 
                 <router-link to="/signup" class="font-medium text-zinc-900 dark:text-zinc-100 hover:underline underline-offset-4 decoration-zinc-300 dark:decoration-zinc-600 transition-colors">
                 Sign up
                 </router-link>
             </p>
          </div>
      </div>

      <!-- Continue As User UI -->
      <div v-else class="text-center space-y-8">
          <div class="flex justify-center flex-col items-center">
               <div class="h-24 w-24 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100 flex items-center justify-center text-4xl font-medium border border-zinc-200 dark:border-zinc-700 mb-6">
                   {{ lastKnownUser.name ? lastKnownUser.name.charAt(0) : 'U' }}
               </div>
               
               <h2 class="text-[28px] font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 mb-1">
                   Welcome back, {{ lastKnownUser.name }}
               </h2>
               <p class="text-zinc-500 font-medium">{{ lastKnownUser.email }}</p>
          </div>
          

          <div class="pt-4">
              <button @click="continueAsUser" class="w-full flex justify-center items-center py-2.5 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-[#D97757] hover:bg-[#C4654A] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D97757] transition-colors duration-200">
                   Continue as {{ lastKnownUser.name.split(' ')[0] }}
              </button>
          </div>
          
          <div class="pt-4 border-t border-zinc-200 dark:border-zinc-800">
              <button @click="switchAccount" class="text-sm font-medium text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors">
                  Not you? Switch account
              </button>
          </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter, useRoute } from 'vue-router';
import { useToast } from 'vue-toastification';
import axios from 'axios'; // Ensure axios is imported or use api service
import LoadingLogo from '@/components/common/LoadingLogo.vue';

const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');
const turnstileToken = ref('');
const turnstileId = ref(null);

const authStore = useAuthStore();
const router = useRouter();
const route = useRoute();
const toast = useToast();

const loginWithProvider = (provider) => {
    localStorage.setItem('lastProvider', provider);
    // Redirect to backend OAuth initiation
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
    window.location.href = `${apiUrl}/auth/oauth/${provider}/login`;
};


const handleLogin = async () => {
  loading.value = true;
  error.value = '';
  try {
    await authStore.login(email.value, password.value, turnstileToken.value);
    localStorage.setItem('lastProvider', 'email'); 
    toast.success(`Welcome back, ${authStore.user.name}!`);
    const redirectPath = route.query.redirect || '/dashboard';
    router.push(redirectPath);
  } catch (err) {
    if (err.response && err.response.data && err.response.data.detail) {
        error.value = err.response.data.detail;
    } else if (err.message) {
        error.value = err.message;
    } else {
        error.value = 'Invalid email or password. Please try again.';
    }
    console.error("Login Error Details:", err);
    if (window.turnstile && turnstileId.value !== null) {
       window.turnstile.reset(turnstileId.value);
       turnstileToken.value = '';
    }
  } finally {
    loading.value = false;
  }
};

const lastKnownUser = ref(null);
const lastProvider = ref(null);

const handleGoogleOneTapResponse = async (response) => {
    try {
        // Send credential to backend
        const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
        const res = await fetch(`${apiUrl}/auth/google-one-tap`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ credential: response.credential })
        });
        
        if (!res.ok) throw new Error('Google One Tap Failed');
        
        const data = await res.json();
        authStore.setTokens(data.access_token, data.refresh_token);
        localStorage.setItem('lastProvider', 'google');
        toast.success(`Welcome back, ${authStore.user.name}!`);
        
        const redirectPath = route.query.redirect || '/dashboard';
        router.push(redirectPath);
    } catch (e) {
        console.error("Google One Tap Error", e);
        // Fail silently or show toast
    }
};

onMounted(() => {
    // Check for tokens (OAuth Callback)
    const accessToken = route.query.access_token;
    const refreshToken = route.query.refresh_token;
    
    if (accessToken) {
        authStore.setTokens(accessToken, refreshToken);
        toast.success(`Welcome back, ${authStore.user.name}!`);
        
        // Remove tokens from URL
        const query = { ...route.query };
        delete query.access_token;
        delete query.refresh_token;
        router.replace({ query });
        
        const redirectPath = query.redirect || '/dashboard';
        router.push(redirectPath);
        return;
    }

    // Check for "Continue as..."
    try {
        const storedUser = localStorage.getItem('lastKnownUser');
        const storedProvider = localStorage.getItem('lastProvider');
        if (storedUser && storedProvider) {
            lastKnownUser.value = JSON.parse(storedUser);
            lastProvider.value = storedProvider;
        }
    } catch(e) {}

    // Initialize Turnstile
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

    // Initialize Google One Tap
    if (window.google) {
        const clientId = import.meta.env.VITE_GOOGLE_CLIENT_ID;
        console.log("Initializing One Tap with Client ID:", clientId ? clientId.substring(0, 10) + '...' : 'MISSING');
        
        window.google.accounts.id.initialize({
            client_id: clientId || "", 
            callback: handleGoogleOneTapResponse,
            auto_select: true, // Attempt to auto-sign in
            use_fedcm_for_prompt: true // Opt-in to FedCM
        });
        window.google.accounts.id.prompt((notification) => {
             if (notification.isNotDisplayed()) {
                 console.log("One Tap not displayed reason:", notification.getNotDisplayedReason());
             } else if (notification.isSkippedMoment()) {
                 console.log("One Tap skipped reason:", notification.getSkippedReason());
             }
        });
    }
});

onUnmounted(() => {
  if (window.turnstile && turnstileId.value !== null) {
      window.turnstile.remove(turnstileId.value);
  }
});

const continueAsUser = () => {
    if (lastProvider.value && lastProvider.value !== 'email') {
        loginWithProvider(lastProvider.value);
    } else {
        switchAccount();
        email.value = lastKnownUser.value?.email || '';
    }
};

const switchAccount = () => {
    lastKnownUser.value = null;
    lastProvider.value = null;
    localStorage.removeItem('lastKnownUser');
    localStorage.removeItem('lastProvider');
};
</script>

<style scoped>
/* Minimal styles, no custom animations needed for now */
</style>
