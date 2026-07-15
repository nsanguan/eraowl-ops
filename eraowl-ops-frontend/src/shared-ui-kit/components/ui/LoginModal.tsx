import { useState, type FormEvent } from 'react';
import { useAuthStore } from '../../stores/auth';
import { GATEWAY_URL } from '../../lib/gateway';

interface LoginModalProps {
  open: boolean;
  onClose: () => void;
}

export function LoginModal({ open, onClose }: LoginModalProps) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const setToken = useAuthStore((s) => s.setToken);

  if (!open) return null;

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const res = await fetch(`${GATEWAY_URL}/api/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });
      if (!res.ok) {
        const msg = (await res.json().catch(() => null))?.message || 'Login failed';
        throw new Error(msg);
      }
      const data = await res.json();
      setToken(data.access_token);
      onClose();
      window.location.reload();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/40 backdrop-blur-sm">
      <div className="bg-background border border-outline-variant rounded-2xl shadow-2xl w-full max-w-sm p-8">
        <div className="flex items-center gap-3 mb-6">
          <div className="w-10 h-10 bg-primary rounded-xl flex items-center justify-center text-primary-foreground font-black text-sm">AX</div>
          <div>
            <h2 className="text-lg font-semibold text-slate-900! dark:text-white!">Axon OS</h2>
            <p className="text-[10px] uppercase tracking-widest text-slate-500! dark:text-slate-300!">Enterprise Sign In</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="text-[10px] font-semibold uppercase tracking-wider text-outline block mb-1.5">Username</label>
            <input
              type="text" value={username} onChange={(e) => setUsername(e.target.value)}
              className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-4 py-3 text-sm text-on-surface placeholder:text-outline/50 focus:ring-2 focus:ring-primary outline-none transition-all"
              placeholder="admin" autoFocus
            />
          </div>
          <div>
            <label className="text-[10px] font-semibold uppercase tracking-wider text-outline block mb-1.5">Password</label>
            <input
              type="password" value={password} onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-4 py-3 text-sm text-on-surface placeholder:text-outline/50 focus:ring-2 focus:ring-primary outline-none transition-all"
              placeholder="••••••••"
            />
          </div>

          {error && (
            <p className="text-[11px] text-error font-semibold bg-error/5 px-3 py-2 rounded-lg">{error}</p>
          )}

          <div className="flex gap-3 pt-2">
            <button type="button" onClick={onClose}
              className="flex-1 px-4 py-2.5 text-[11px] font-semibold rounded-lg border border-outline-variant text-on-surface-variant hover:bg-surface-container-high transition-all">
              Cancel
            </button>
            <button type="submit" disabled={loading || !username || !password}
              className="flex-1 px-4 py-2.5 bg-primary text-primary-foreground text-[11px] font-semibold rounded-lg hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20 disabled:opacity-50 disabled:cursor-not-allowed">
              {loading ? 'Signing in...' : 'Sign In'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
