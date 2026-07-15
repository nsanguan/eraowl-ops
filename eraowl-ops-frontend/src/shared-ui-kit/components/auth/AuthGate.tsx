import { useState, type ReactNode } from 'react';
import { useAuthStore } from '../../stores/auth';
import { LoginModal } from '../ui/LoginModal';

interface AuthGateProps {
  children: ReactNode;
}

export function AuthGate({ children }: AuthGateProps) {
  const token = useAuthStore((s) => s.token);
  const [loginOpen, setLoginOpen] = useState(!token);

  if (token) return <>{children}</>;

  return (
    <div className="flex h-screen w-full items-center justify-center bg-background">
      <div className="flex flex-col items-center gap-6 text-center max-w-sm">
        <div className="w-16 h-16 bg-primary rounded-2xl flex items-center justify-center text-primary-foreground font-black text-xl shadow-lg shadow-primary/20">AX</div>
        <div>
          <h1 className="text-2xl font-bold text-on-surface">Axon OS</h1>
          <p className="text-sm text-outline mt-1">Enterprise Resource Planning</p>
        </div>
        <button onClick={() => setLoginOpen(true)}
          className="px-10 py-3 bg-primary text-primary-foreground text-sm font-semibold rounded-xl hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20">
          Sign In
        </button>
        <LoginModal open={loginOpen} onClose={() => setLoginOpen(false)} />
      </div>
    </div>
  );
}
