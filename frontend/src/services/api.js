import axios from 'axios';
import router from '../router';
import Swal from 'sweetalert2';
// Delay store import or use inside interceptor
// import { useAuthStore } from '../stores/auth'; // Removed top-level import

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add a request interceptor to inject the token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
    failedQueue.forEach(prom => {
        if (error) {
            prom.reject(error);
        } else {
            prom.resolve(token);
        }
    });
    failedQueue = [];
};

// Add a response interceptor to handle 401 errors
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        // Handle 403 Subscription Required OR Free Tier Limit Reached
        if (error.response && error.response.status === 403) {
            const detailMsg = error.response.data?.detail || '';
            const isLimitError = detailMsg.toLowerCase().includes('limit') || detailMsg.toLowerCase().includes('subscription') || detailMsg.toLowerCase().includes('pro');

            if (isLimitError) {
                const detailMsg = error.response.data?.detail || 'Active subscription required. Please upgrade to Pro.';

                Swal.fire({
                    icon: 'warning',
                    title: 'Upgrade Required',
                    text: detailMsg,
                    confirmButtonColor: '#3b82f6',
                    confirmButtonText: 'View Upgrade Options'
                }).then(() => {
                    router.push('/billing');
                });

                return Promise.reject(error);
            }
        }

        // Handle 413 Payload Too Large (For size limits)
        if (error.response && error.response.status === 413) {
            const detailMsg = error.response.data?.detail || 'This file exceeds your current plan limits.';

            Swal.fire({
                icon: 'error',
                title: 'Limit Exceeded',
                text: detailMsg,
                confirmButtonColor: '#3b82f6'
            });

            return Promise.reject(error);
        }

        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            if (isRefreshing) {
                return new Promise(function (resolve, reject) {
                    failedQueue.push({ resolve, reject });
                }).then(token => {
                    originalRequest.headers['Authorization'] = 'Bearer ' + token;
                    return api(originalRequest);
                }).catch(err => {
                    return Promise.reject(err);
                });
            }

            originalRequest._retry = true;
            isRefreshing = true;

            // Dynamic import to avoid circular dependency
            const { useAuthStore } = await import('../stores/auth');
            const authStore = useAuthStore();

            try {
                const newToken = await authStore.refresh();
                isRefreshing = false;
                processQueue(null, newToken);
                originalRequest.headers['Authorization'] = 'Bearer ' + newToken;
                return api(originalRequest);
            } catch (err) {
                isRefreshing = false;
                processQueue(err, null);
                authStore.logout();
                router.push({
                    path: '/login',
                    query: { redirect: router.currentRoute.value.fullPath }
                });
                return Promise.reject(err);
            }
        }
        return Promise.reject(error);
    }
);

export default api;
