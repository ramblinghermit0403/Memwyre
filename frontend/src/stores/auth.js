import { defineStore } from 'pinia';
import api from '../services/api';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        token: localStorage.getItem('token') || null,
        isAuthenticated: !!localStorage.getItem('token'),
    }),
    actions: {
        async login(email, password) {
            try {
                const response = await api.post('/auth/login',
                    new URLSearchParams({ username: email, password }),
                    { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
                );
                this.token = response.data.access_token;
                this.isAuthenticated = true;
                localStorage.setItem('token', this.token);
                // Fetch user details if needed, or decode token
                // For now, we just set isAuthenticated
                return true;
            } catch (error) {
                console.error('Login failed:', error);
                throw error;
            }
        },
        async register(email, password) {
            try {
                await api.post('/auth/register', { email, password });
                return true;
            } catch (error) {
                console.error('Registration failed:', error);
                throw error;
            }
        },
        logout() {
            this.user = null;
            this.token = null;
            this.isAuthenticated = false;
            localStorage.removeItem('token');
        },
    },
});
