import React from 'react';

export interface CardAction {
  label: string;
  icon?: string;
  onClick: (data: any) => void;
  primary?: boolean;
}

export interface CardItem {
  id: string | number;
  title: string;
  subtitle?: string;
  body?: string;
  icon?: string;
  iconColor?: string;
  badge?: string;
  badgeColor?: 'primary' | 'success' | 'warning' | 'error' | 'default';
  actions?: CardAction[];
  data?: any; // Original payload
}

export interface CardsRegionProps {
  items: CardItem[];
  columns?: 1 | 2 | 3 | 4 | 5 | 6;
  onCardClick?: (item: CardItem) => void;
  className?: string;
}

export function CardsRegion({ items, columns = 3, onCardClick, className = '' }: CardsRegionProps) {
  const gridCols = {
    1: 'grid-cols-1',
    2: 'grid-cols-1 sm:grid-cols-2',
    3: 'grid-cols-1 sm:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 sm:grid-cols-2 lg:grid-cols-4',
    5: 'grid-cols-2 md:grid-cols-3 lg:grid-cols-5',
    6: 'grid-cols-2 md:grid-cols-3 lg:grid-cols-6',
  }[columns];

  const badgeColors = {
    primary: 'bg-primary/10 text-primary',
    success: 'bg-green-500/10 text-green-600',
    warning: 'bg-yellow-500/10 text-yellow-600',
    error: 'bg-error/10 text-error',
    default: 'bg-outline-variant/30 text-outline'
  };

  return (
    <div className={`grid ${gridCols} gap-4 ${className}`}>
      {items.map(item => (
        <div 
          key={item.id}
          onClick={() => onCardClick?.(item)}
          className={`flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden hover:shadow-md transition-shadow ${onCardClick ? 'cursor-pointer hover:border-primary/50' : ''}`}
        >
          <div className="p-4 flex-1">
            <div className="flex items-start justify-between gap-3 mb-3">
              <div className="flex items-center gap-3 min-w-0">
                {item.icon && (
                  <div 
                    className="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" 
                    style={{ backgroundColor: `${item.iconColor || 'var(--primary)'}1A`, color: item.iconColor || 'var(--primary)' }}
                  >
                    <span className="material-symbols-outlined !text-[20px]">{item.icon}</span>
                  </div>
                )}
                <div className="min-w-0">
                  <h3 className="text-sm font-bold text-on-surface truncate">{item.title}</h3>
                  {item.subtitle && <p className="text-xs text-outline truncate">{item.subtitle}</p>}
                </div>
              </div>
              {item.badge && (
                <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider shrink-0 ${badgeColors[item.badgeColor || 'default']}`}>
                  {item.badge}
                </span>
              )}
            </div>
            {item.body && (
              <p className="text-xs text-on-surface-variant line-clamp-3">
                {item.body}
              </p>
            )}
          </div>
          
          {item.actions && item.actions.length > 0 && (
            <div className="px-4 py-3 bg-surface-container-low border-t border-outline-variant flex items-center justify-end gap-2 mt-auto">
              {item.actions.map((action, i) => (
                <button
                  key={i}
                  onClick={(e) => {
                    e.stopPropagation();
                    action.onClick(item.data || item);
                  }}
                  className={`px-3 py-1.5 text-xs font-bold rounded-lg transition-colors flex items-center gap-1.5 ${
                    action.primary 
                      ? 'bg-primary text-primary-foreground hover:brightness-110' 
                      : 'text-primary hover:bg-primary/10'
                  }`}
                >
                  {action.icon && <span className="material-symbols-outlined !text-[14px]">{action.icon}</span>}
                  {action.label}
                </button>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
