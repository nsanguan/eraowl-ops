import React from 'react';

export interface TimelineEvent {
  id: string | number;
  title: string;
  timestamp: string | Date;
  user?: string;
  description?: string;
  icon?: string;
  status?: 'success' | 'warning' | 'error' | 'info' | 'default';
}

export interface TimelineRegionProps {
  events: TimelineEvent[];
  className?: string;
}

export function TimelineRegion({ events, className = '' }: TimelineRegionProps) {
  const statusColors = {
    success: 'bg-green-500 text-white',
    warning: 'bg-yellow-500 text-white',
    error: 'bg-error text-white',
    info: 'bg-blue-500 text-white',
    default: 'bg-surface-container-high text-on-surface-variant'
  };

  const borderColors = {
    success: 'border-green-500',
    warning: 'border-yellow-500',
    error: 'border-error',
    info: 'border-blue-500',
    default: 'border-surface-container-high'
  };

  const formatDate = (val: string | Date) => {
    const d = new Date(val);
    return new Intl.DateTimeFormat('en-US', {
      month: 'short', day: 'numeric', year: 'numeric',
      hour: 'numeric', minute: '2-digit', hour12: true
    }).format(d);
  };

  return (
    <div className={`relative ${className}`}>
      {/* Vertical Line */}
      <div className="absolute left-6 top-4 bottom-4 w-0.5 bg-outline-variant/50"></div>

      <div className="flex flex-col gap-6">
        {events.map((event, idx) => {
          const status = event.status || 'default';
          return (
            <div key={event.id} className="relative flex gap-4 items-start group">
              {/* Icon Marker */}
              <div className={`relative z-10 w-12 h-12 rounded-full flex items-center justify-center shrink-0 border-4 border-surface ${statusColors[status]}`}>
                {event.icon ? (
                  <span className="material-symbols-outlined !text-[20px]">{event.icon}</span>
                ) : (
                  <div className="w-2.5 h-2.5 rounded-full bg-current"></div>
                )}
              </div>

              {/* Content Card */}
              <div className="flex-1 mt-1 bg-surface-container-lowest border border-outline-variant rounded-xl p-4 shadow-sm hover:shadow-md transition-shadow group-hover:border-primary/30 relative">
                {/* Pointer arrow */}
                <div className="absolute top-4 -left-2 w-4 h-4 bg-surface-container-lowest border-l border-b border-outline-variant transform rotate-45 group-hover:border-primary/30"></div>
                
                <div className="flex justify-between items-start gap-4 mb-2">
                  <h3 className="font-bold text-sm text-on-surface">{event.title}</h3>
                  <span className="text-xs font-semibold text-outline shrink-0 whitespace-nowrap">
                    {formatDate(event.timestamp)}
                  </span>
                </div>
                
                {event.user && (
                  <div className="flex items-center gap-1.5 mb-2 text-xs text-primary font-semibold">
                    <span className="material-symbols-outlined !text-[14px]">person</span>
                    {event.user}
                  </div>
                )}
                
                {event.description && (
                  <p className="text-sm text-on-surface-variant leading-relaxed">
                    {event.description}
                  </p>
                )}
              </div>
            </div>
          );
        })}
        {events.length === 0 && (
          <div className="text-center text-outline italic text-sm py-8">
            No events to display.
          </div>
        )}
      </div>
    </div>
  );
}
