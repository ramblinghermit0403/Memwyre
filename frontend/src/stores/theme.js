import { defineStore } from 'pinia';
import { ref, watch } from 'vue';

export const useThemeStore = defineStore('theme', () => {
    // Application is light-mode only.
    const isDark = ref(false);

    const toggleTheme = () => {
        // Keep strict light mode even if toggle is clicked.
        isDark.value = false;
    };

    watch(isDark, () => {
        document.documentElement.classList.remove('dark');
        document.documentElement.style.colorScheme = 'light';
        localStorage.setItem('theme', 'light');
    }, { immediate: true });

    return {
        isDark,
        toggleTheme
    };
});
