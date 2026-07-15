import { cn } from '../../lib/utils';

export type StatusVariant =
  | 'available' | 'allocated' | 'hold' | 'warning' | 'synced'
  | 'created' | 'loading' | 'loaded' | 'stored' | 'sync_error'
  | 'shipped' | 'completed' | 'exception' | 'pending'
  | 'active' | 'fulfilled' | 'cancelled' | 'failed';

const variantStyles: Record<StatusVariant, string> = {
  available: 'bg-success/15 text-success',
  allocated: 'bg-blue-100 text-blue-800',
  hold: 'bg-destructive/15 text-destructive',
  warning: 'bg-warning/15 text-warning-foreground',
  synced: 'bg-purple-100 text-purple-800',
  created: 'bg-muted text-muted-foreground',
  loading: 'bg-cyan-100 text-cyan-800',
  loaded: 'bg-success/15 text-success',
  stored: 'bg-blue-100 text-blue-800',
  sync_error: 'bg-destructive/15 text-destructive',
  shipped: 'bg-indigo-100 text-indigo-800',
  completed: 'bg-success/15 text-success',
  exception: 'bg-warning/15 text-warning-foreground',
  pending: 'bg-warning/15 text-warning-foreground',
  active: 'bg-success/15 text-success',
  fulfilled: 'bg-success/15 text-success',
  cancelled: 'bg-muted text-muted-foreground/60',
  failed: 'bg-destructive/15 text-destructive',
};

const labelOverrides: Record<string, string> = {
  sync_error: 'SYNC ERROR',
};

interface StatusChipProps {
  status: StatusVariant;
  label?: string;
}

export function StatusChip({ status, label }: StatusChipProps) {
  const displayLabel =
    label || labelOverrides[status] || status.charAt(0).toUpperCase() + status.slice(1);
  return (
    <span className={cn('status-chip', variantStyles[status])} role="status">
      {displayLabel}
    </span>
  );
}
