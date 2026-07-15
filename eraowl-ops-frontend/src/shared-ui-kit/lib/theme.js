const STORAGE_KEY = 'axonos-theme';
export function getTheme() {
    if (typeof document === 'undefined')
        return 'dark';
    return document.documentElement.classList.contains('dark') ? 'dark' : 'light';
}
export function setTheme(theme) {
    if (typeof document === 'undefined')
        return;
    if (theme === 'dark') {
        document.documentElement.classList.add('dark');
    }
    else {
        document.documentElement.classList.remove('dark');
    }
    try {
        localStorage.setItem(STORAGE_KEY, theme);
    }
    catch {
        // ignore
    }
}
export function toggleTheme() {
    const next = getTheme() === 'dark' ? 'light' : 'dark';
    setTheme(next);
    return next;
}
export function initTheme() {
    if (typeof document === 'undefined')
        return 'dark';
    let stored = null;
    try {
        stored = localStorage.getItem(STORAGE_KEY);
    }
    catch {
        // ignore
    }
    const theme = stored ?? 'dark';
    setTheme(theme);
    return theme;
}
//# sourceMappingURL=theme.js.map