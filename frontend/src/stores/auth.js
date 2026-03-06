import { defineStore } from 'pinia';
import api from '../services/api';
import { jwtDecode } from "jwt-decode";

// --- Extension Token Relay ---
// Broadcasts auth state to the MemWyre browser extension via postMessage.
// auth_relay.js (content script) catches these and relays to the background script.
function broadcastToExtension(type, token, refreshToken, user) {
    const payload = { type };
    if (type === 'MEMWYRE_AUTH_SUCCESS') {
        payload.token = token;
        payload.refreshToken = refreshToken;
        payload.user = user ? JSON.parse(JSON.stringify(user)) : null;
    }
    // Retry with delays to handle race condition where content script hasn't loaded yet
    [0, 500, 1500].forEach(delay => {
        setTimeout(() => window.postMessage(payload, '*'), delay);
    });
}

// Global: when auth_relay.js loads late, it announces RELAY_READY.
// We respond by re-broadcasting the current auth state.
let _relayListenerAttached = false;
function attachRelayListener(store) {
    if (_relayListenerAttached) return;
    _relayListenerAttached = true;
    window.addEventListener('message', (event) => {
        if (event.source !== window) return;
        if (event.data?.type === 'MEMWYRE_RELAY_READY' && store.token) {
            broadcastToExtension('MEMWYRE_AUTH_SUCCESS', store.token, store.refreshToken, store.user);
        }
    });
}

export const useAuthStore = defineStore('auth', {
    state: () => {
        const token = localStorage.getItem('token');
        const refreshToken = localStorage.getItem('refreshToken');
        const hasCompletedOnboarding = localStorage.getItem('hasCompletedOnboarding') === 'true';
        let user = null;

        const decodeUser = (t) => {
            try {
                const decoded = jwtDecode(t);
                return {
                    id: decoded.sub,
                    email: decoded.email || decoded.sub,
                    name: decoded.name || (decoded.email || decoded.sub || '').split('@')[0],
                    is_verified: decoded.is_verified || false
                };
            } catch (e) {
                return null;
            }
        };

        if (token) {
            user = decodeUser(token);
            if (!user) localStorage.removeItem('token');
        }

        return {
            user,
            token: token || null,
            refreshToken: refreshToken || null,
            isAuthenticated: !!token,
            hasCompletedOnboarding,
        };
    },
    actions: {
        async login(email, password, turnstileToken) {
            try {
                const params = new URLSearchParams({ username: email, password });
                if (turnstileToken) {
                    params.append('turnstile_token', turnstileToken);
                }
                const response = await api.post('/auth/login', params,
                    { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
                );

                this.setTokens(response.data.access_token, response.data.refresh_token);
                return true;
            } catch (error) {
                console.error('Login failed:', error);
                throw error;
            }
        },

        setTokens(accessToken, refreshToken) {
            this.token = accessToken;
            this.refreshToken = refreshToken; // May be undefined if not provided
            this.isAuthenticated = true;

            localStorage.setItem('token', accessToken);
            if (refreshToken) {
                localStorage.setItem('refreshToken', refreshToken);
            }

            // buffer decode
            try {
                const decoded = jwtDecode(accessToken);
                this.user = {
                    id: decoded.sub,
                    email: decoded.email || decoded.sub,
                    name: decoded.name || (decoded.email || decoded.sub || '').split('@')[0],
                    is_verified: decoded.is_verified || false
                };
                localStorage.setItem('lastKnownUser', JSON.stringify(this.user));
            } catch (e) { console.error("Token decode failed", e); }

            // Broadcast to extension
            broadcastToExtension('MEMWYRE_AUTH_SUCCESS', accessToken, refreshToken, this.user);
            attachRelayListener(this);
        },

        async refresh() {
            if (!this.refreshToken) throw new Error("No refresh token");
            try {
                // Bypass interceptor to avoid infinite loop -> Create new instance or use fetch?
                // Actually if we use same api instance, we must flag this request to skip interceptor logic or handle it carefully.
                // Simpler: Use fetch or a naked axios call for refresh to avoid circular dependency in interceptors.
                const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
                const response = await fetch(`${apiUrl}/auth/refresh`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ refresh_token: this.refreshToken })
                });

                if (!response.ok) throw new Error("Refresh failed");
                const data = await response.json();

                this.setTokens(data.access_token, data.refresh_token || this.refreshToken);
                return data.access_token;
            } catch (e) {
                this.logout();
                throw e;
            }
        },

        async register(email, password, name, turnstileToken) {
            try {
                await api.post('/auth/register', { email, password, name, turnstile_token: turnstileToken });
                return true;
            } catch (error) {
                console.error('Registration failed:', error);
                throw error;
            }
        },
        logout() {
            this.user = null;
            this.token = null;
            this.refreshToken = null;
            this.isAuthenticated = false;
            this.hasCompletedOnboarding = false;
            localStorage.removeItem('token');
            localStorage.removeItem('refreshToken');
            localStorage.removeItem('hasCompletedOnboarding');

            // Notify extension to clear its tokens too
            broadcastToExtension('MEMWYRE_AUTH_LOGOUT');
        },
        completeOnboarding() {
            this.hasCompletedOnboarding = true;
            localStorage.setItem('hasCompletedOnboarding', 'true');
        }
    },
});
