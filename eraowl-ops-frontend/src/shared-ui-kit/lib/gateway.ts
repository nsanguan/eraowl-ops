import { useAuthStore } from '../stores/auth';

const host = typeof window !== 'undefined' ? window.location.hostname : 'localhost';
export const GATEWAY_URL = import.meta.env.VITE_GATEWAY_URL ?? `http://${host}:4200`;

function randomId(): string {
  if (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function') {
    return crypto.randomUUID();
  }
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16);
  });
}

export async function mcpCall<T = unknown>(
  method: string,
  params?: Record<string, unknown>,
): Promise<T> {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  };

  // Attach JWT auth token if available
  const authHeader = useAuthStore.getState().getAuthHeader();
  if (authHeader) {
    headers['Authorization'] = authHeader;
  }

  const res = await fetch(`${GATEWAY_URL}/api/mcp`, {
    method: 'POST',
    headers,
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: randomId(),
      method,
      params: params ?? {},
    }),
  });

  // Handle 401 — clear stale token and redirect to login
  if (res.status === 401) {
    useAuthStore.getState().clearAuth();
    throw new Error('Authentication required. Please log in.');
  }

  const json = await res.json();

  if (json.error) {
    throw new Error(`MCP Error [${json.error.code}]: ${json.error.message}`);
  }

  return json.result as T;
}
