import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

export interface AuthState {
  /** JWT token for API requests */
  token: string | null;
  /** Decoded user info from JWT */
  user: { sub?: string; role?: string; [key: string]: unknown } | null;
  /** Set the auth token and decode basic user info */
  setToken: (token: string) => void;
  /** Clear auth state (logout) */
  clearAuth: () => void;
  /** Get the Authorization header value */
  getAuthHeader: () => string | null;
}

/**
 * Decode JWT payload without verification (client-side display only).
 * Actual verification happens on the backend via JwtAuthGuard.
 */
function decodeJwtPayload(token: string): Record<string, unknown> | null {
  try {
    const parts = token.split('.');
    if (parts.length !== 3) return null;
    const payload = JSON.parse(atob(parts[1].replace(/-/g, '+').replace(/_/g, '/')));
    return payload;
  } catch {
    return null;
  }
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      token: null,
      user: null,

      setToken: (token: string) => {
        const payload = decodeJwtPayload(token);
        set({
          token,
          user: payload as AuthState['user'],
        });
      },

      clearAuth: () => {
        set({ token: null, user: null });
      },

      getAuthHeader: () => {
        const { token } = get();
        return token ? `Bearer ${token}` : null;
      },
    }),
    {
      name: 'axonos-auth',
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({ token: state.token, user: state.user }),
    },
  ),
);
