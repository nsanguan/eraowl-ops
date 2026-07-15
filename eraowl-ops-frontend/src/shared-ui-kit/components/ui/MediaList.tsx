import React from 'react';

export interface MediaListItem {
  id: string | number;
  title: string;
  subtitle?: string;
  description?: string;
  avatarUrl?: string;
  avatarText?: string;
  badge?: string;
  badgeColor?: 'primary' | 'success' | 'warning' | 'error' | 'default';
  actions?: React.ReactNode;
  onClick?: (item: MediaListItem) => void;
}

export interface MediaListProps {
  items: MediaListItem[];
  className?: string;
  showDividers?: boolean;
}

export function MediaList({ items, className = '', showDividers = true }: MediaListProps) {
  
  const badgeColors = {
    primary: 'bg-primary/10 text-primary',
    success: 'bg-green-500/10 text-green-600',
    warning: 'bg-yellow-500/10 text-yellow-600',
    error: 'bg-error/10 text-error',
    default: 'bg-surface-container-high text-on-surface-variant'
  };

  return (
    <div className={`flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden ${className}`}>
      {items.map((item, idx) => {
        const isLast = idx === items.length - 1;
        const isClickable = !!item.onClick;

        return (
          <div 
            key={item.id}
            onClick={() => item.onClick?.(item)}
            className={`
              flex items-start sm:items-center gap-4 p-4 transition-colors
              ${showDividers && !isLast ? 'border-b border-outline-variant' : ''}
              ${isClickable ? 'cursor-pointer hover:bg-surface-container-low' : ''}
            `}
          >
            {/* Avatar / Media */}
            <div className="shrink-0 w-12 h-12 rounded-full overflow-hidden bg-primary/10 flex items-center justify-center text-primary font-bold text-lg border border-primary/20 shadow-sm mt-1 sm:mt-0">
              {item.avatarUrl ? (
                <img src={item.avatarUrl} alt={item.title} className="w-full h-full object-cover" />
              ) : item.avatarText ? (
                item.avatarText.substring(0, 2).toUpperCase()
              ) : (
                <span className="material-symbols-outlined !text-[24px]">image</span>
              )}
            </div>

            {/* Content */}
            <div className="flex-1 min-w-0 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div className="flex flex-col min-w-0">
                <div className="flex items-center gap-2">
                  <h4 className="text-sm font-bold text-on-surface truncate">{item.title}</h4>
                  {item.badge && (
                    <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider shrink-0 ${badgeColors[item.badgeColor || 'default']}`}>
                      {item.badge}
                    </span>
                  )}
                </div>
                {item.subtitle && (
                  <div className="text-xs font-semibold text-primary truncate mt-0.5">{item.subtitle}</div>
                )}
                {item.description && (
                  <p className="text-xs text-on-surface-variant line-clamp-2 mt-1">
                    {item.description}
                  </p>
                )}
              </div>

              {/* Trailing Actions */}
              {item.actions && (
                <div className="shrink-0 flex items-center gap-2 mt-2 sm:mt-0" onClick={(e) => e.stopPropagation()}>
                  {item.actions}
                </div>
              )}
            </div>
          </div>
        );
      })}
      
      {items.length === 0 && (
        <div className="p-8 text-center text-sm text-outline italic">
          No items to display.
        </div>
      )}
    </div>
  );
}
