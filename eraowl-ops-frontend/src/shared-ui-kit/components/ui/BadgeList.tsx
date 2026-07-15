import React from 'react';

export interface BadgeItem {
  id: string | number;
  label: string;
  value: string | number;
  icon?: string;
  color?: 'primary' | 'success' | 'warning' | 'error' | 'info' | 'default';
  onClick?: (item: BadgeItem) => void;
}

export interface BadgeListProps {
  items: BadgeItem[];
  layout?: 'horizontal' | 'grid';
  className?: string;
}

export function BadgeList({ items, layout = 'horizontal', className = '' }: BadgeListProps) {
  const colorStyles = {
    primary: 'bg-primary/10 text-primary border-primary/20 hover:border-primary/50',
    success: 'bg-green-500/10 text-green-600 border-green-500/20 hover:border-green-500/50',
    warning: 'bg-yellow-500/10 text-yellow-600 border-yellow-500/20 hover:border-yellow-500/50',
    error: 'bg-error/10 text-error border-error/20 hover:border-error/50',
    info: 'bg-blue-500/10 text-blue-600 border-blue-500/20 hover:border-blue-500/50',
    default: 'bg-surface-container-high text-on-surface border-outline-variant hover:border-outline'
  };

  const containerClasses = layout === 'horizontal' 
    ? 'flex flex-wrap items-center gap-4' 
    : 'grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4';

  return (
    <div className={`${containerClasses} ${className}`}>
      {items.map(item => {
        const color = item.color || 'default';
        const isClickable = !!item.onClick;
        const baseClasses = `flex flex-col items-center justify-center p-3 rounded-xl border transition-all ${colorStyles[color]} ${isClickable ? 'cursor-pointer hover:shadow-md transform hover:-translate-y-0.5' : ''}`;
        
        return (
          <div 
            key={item.id} 
            className={`${baseClasses} ${layout === 'horizontal' ? 'min-w-[120px]' : ''}`}
            onClick={() => item.onClick?.(item)}
          >
            {item.icon && (
              <span className="material-symbols-outlined !text-[24px] mb-1 opacity-80">{item.icon}</span>
            )}
            <span className="text-2xl font-black tracking-tight mb-0.5">{item.value}</span>
            <span className="text-[10px] font-bold uppercase tracking-wider opacity-80 text-center">{item.label}</span>
          </div>
        );
      })}
    </div>
  );
}
