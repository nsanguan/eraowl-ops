import React, { createContext, useContext, useEffect, useState } from 'react';

type ThemeMode = 'light' | 'dark' | 'system';

interface ThemeConfig {
  mode: ThemeMode;
  primaryColor: string | null;
  borderRadius: string | null;
}

interface ThemeContextType {
  config: ThemeConfig;
  setMode: (mode: ThemeMode) => void;
  setPrimaryColor: (color: string | null) => void;
  setBorderRadius: (radius: string | null) => void;
  resetTheme: () => void;
}

const DEFAULT_CONFIG: ThemeConfig = {
  mode: 'system',
  primaryColor: null,
  borderRadius: null,
};

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [config, setConfig] = useState<ThemeConfig>(() => {
    try {
      const stored = localStorage.getItem('axon-theme-config');
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (e) {
      console.error('Failed to load theme config from local storage', e);
    }
    return DEFAULT_CONFIG;
  });

  // Save to local storage on change
  useEffect(() => {
    localStorage.setItem('axon-theme-config', JSON.stringify(config));
  }, [config]);

  // Apply Mode (Light/Dark)
  useEffect(() => {
    const root = window.document.documentElement;
    root.classList.remove('light', 'dark');

    if (config.mode === 'system') {
      const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      root.classList.add(systemTheme);
    } else {
      root.classList.add(config.mode);
    }
  }, [config.mode]);

  // Apply Custom CSS Variables
  useEffect(() => {
    const root = window.document.documentElement;
    
    // Reset first
    root.style.removeProperty('--color-primary');
    root.style.removeProperty('--radius');
    
    if (config.primaryColor) {
      root.style.setProperty('--color-primary', config.primaryColor);
    }
    
    if (config.borderRadius) {
      root.style.setProperty('--radius', config.borderRadius);
    }
    
  }, [config.primaryColor, config.borderRadius]);

  const setMode = (mode: ThemeMode) => setConfig(prev => ({ ...prev, mode }));
  const setPrimaryColor = (color: string | null) => setConfig(prev => ({ ...prev, primaryColor: color }));
  const setBorderRadius = (radius: string | null) => setConfig(prev => ({ ...prev, borderRadius: radius }));
  const resetTheme = () => setConfig(DEFAULT_CONFIG);

  return (
    <ThemeContext.Provider value={{ config, setMode, setPrimaryColor, setBorderRadius, resetTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
}
