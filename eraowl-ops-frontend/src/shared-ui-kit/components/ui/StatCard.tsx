import type { ReactNode } from 'react';

interface StatCardProps {
  title: string;
  value: string | number;
  icon?: ReactNode;
  trend?: { value: string; positive: boolean };
  variant?: 'primary' | 'error' | 'tertiary' | 'secondary' | 'warning';
}

const variantDot: Record<string, string> = {
  primary: 'bg-primary',
  error: 'bg-destructive',
  tertiary: 'bg-tertiary',
  secondary: 'bg-secondary',
  warning: 'bg-warning',
};

export function StatCard({ title, value, icon, trend, variant = 'primary' }: StatCardProps) {
  return (
    <div className="neo-card" role="region" aria-label={title}>
      <div className="flex justify-between items-start mb-4">
        <div className="w-12 h-12 rounded-xl neo-inset flex items-center justify-center">
          {icon || <div className={`w-3 h-3 rounded-full ${variantDot[variant]}`} />}
        </div>
        {trend && (
          <span
            className={`text-xs font-bold px-2 py-1 rounded-lg ${
              trend.positive
                ? 'text-success bg-success/10'
                : 'text-destructive bg-destructive/10'
            }`}
          >
            {trend.value}
          </span>
        )}
      </div>
      <p className="text-sm font-medium text-muted-foreground">{title}</p>
      <h3 className="text-2xl font-bold text-foreground mt-1">{value}</h3>
    </div>
  );
}
