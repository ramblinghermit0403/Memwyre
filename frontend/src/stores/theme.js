import { defineStore } from 'pinia';
import { ref, watch } from 'vue';

function getStorage() {
    if (typeof localStorage !== 'undefined') return localStorage;
    return {
        getItem: () => null,
        setItem: () => { },
    };
}

export const useThemeStore = defineStore('theme', () => {
    const storage = getStorage();
    const hasWindow = typeof window !== 'undefined';
    const hasDocument = typeof document !== 'undefined';

    // Initialize from localStorage or system preference
    const savedTheme = storage.getItem('theme');
    const systemDark = hasWindow && typeof window.matchMedia === 'function'
        ? window.matchMedia('(prefers-color-scheme: dark)').matches
        : false;

    const isDark = ref(savedTheme === 'dark' || (!savedTheme && systemDark));

    const toggleTheme = () => {
        isDark.value = !isDark.value;
    };

    function updateDomTheme(val) {
        if (!hasDocument) return;

        // Never apply dark mode class to html element when on public routes (landing page, pricing, blog, etc.)
        const pathname = hasWindow ? window.location.pathname : '';
        const isPublicPage = pathname === '/' || 
            ['/pricing', '/blog', '/use-cases', '/terms', '/privacy-policy', '/contact', '/connectors', '/mcp', '/plugins', '/extension', '/research', '/memwyre-vs-', '/chatgpt-memory', '/claude-memory', '/cursor-memory', '/mcp-memory', '/what-is-ai-memory', '/ai-memory-benchmark-locomo'].some(p => pathname.startsWith(p));

        if (val && !isPublicPage) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    }

    // Watch for changes and update DOM/localStorage
    watch(isDark, (val) => {
        updateDomTheme(val);
        storage.setItem('theme', val ? 'dark' : 'light');
    }, { immediate: true });

    return {
        isDark,
        toggleTheme
    };
});
