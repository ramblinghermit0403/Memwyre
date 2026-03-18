import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            component: () => import('../views/PublicLayout.vue'),
            children: [
                {
                    path: '',
                    name: 'landing',
                    component: () => import('../views/LandingPage.vue'),
                    meta: { requiresAuth: false }
                },
                {
                    path: 'use-cases',
                    name: 'use-cases',
                    component: () => import('../views/UseCaseView.vue'),
                    meta: { requiresAuth: false }
                },
                {
                    path: 'privacy-policy',
                    name: 'privacy-policy',
                    component: () => import('../views/PrivacyPolicyView.vue'),
                    meta: { requiresAuth: false }
                },
                {
                    path: 'terms',
                    name: 'terms',
                    component: () => import('../views/TermsView.vue'),
                    meta: { requiresAuth: false }
                }
            ]
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/DashboardView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/inbox',
            name: 'inbox',
            component: () => import('../views/InboxView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/projects',
            name: 'projects',
            component: () => import('../views/ProjectsView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        {
            path: '/signup',
            name: 'register',
            component: () => import('../views/RegisterView.vue')
        },
        {
            path: '/verify-email',
            name: 'verify-email',
            component: () => import('../views/VerifyEmailView.vue')
        },
        {
            path: '/forgot-password',
            name: 'forgot-password',
            component: () => import('../views/ForgotPasswordView.vue')
        },
        {
            path: '/reset-password',
            name: 'reset-password',
            component: () => import('../views/ResetPasswordView.vue')
        },
        {
            path: '/settings',
            name: 'settings',
            component: () => import('../views/SettingsView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/editor/:id',
            name: 'editor',
            component: () => import('../views/EditorView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/prompts',
            name: 'prompts',
            component: () => import('../views/PromptGeneratorView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/map',
            name: 'map',
            component: () => import('../views/MemoryMapView.vue')
        },
        {
            path: '/chat',
            name: 'chat',
            component: () => import('../views/ChatView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/chat/:id',
            name: 'chat-session',
            component: () => import('../views/ChatView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/billing',
            name: 'billing',
            component: () => import('../views/BillingView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/admin/bypass',
            name: 'admin-bypass',
            component: () => import('../views/AdminBypassView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/redeem',
            name: 'redeem',
            component: () => import('../views/RedeemView.vue')
        }
    ]
});

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore();

    // If accessing a protected route and not authenticated, redirect to login
    if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        next({
            path: '/login',
            query: { redirect: to.fullPath }
        });
    }
    // If accessing restricted routes and not verified, redirect to settings
    else if (
        to.meta.requiresAuth &&
        authStore.isAuthenticated &&
        authStore.user &&
        !authStore.user.is_verified &&
        !['settings', 'dashboard'].includes(to.name)
    ) {
        next('/settings');
    }
    else {
        next();
    }
});

export default router;


