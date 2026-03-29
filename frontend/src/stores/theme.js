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

    // Watch for changes and update DOM/localStorage
    watch(isDark, (val) => {
        if (hasDocument) {
            if (val) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        }

        storage.setItem('theme', val ? 'dark' : 'light');
    }, { immediate: true });

    return {
        isDark,
        toggleTheme
    };
});
