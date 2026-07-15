import React from 'react';

export interface HeroRegionProps {
  title: string;
  subtitle?: string;
  icon?: string;
  iconBgColor?: string;
  iconColor?: string;
  actions?: React.ReactNode;
  breadcrumbs?: React.ReactNode;
  className?: string;
  backgroundImage?: string;
}

export function HeroRegion({
  title,
  subtitle,
  icon,
  iconBgColor = 'var(--primary)',
  iconColor = '#ffffff',
  actions,
  breadcrumbs,
  className = '',
  backgroundImage
}: HeroRegionProps) {
  
  const bgStyle = backgroundImage 
    ? { backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover', backgroundPosition: 'center' }
    : {};

  return (
    <div 
      className={`relative w-full rounded-xl overflow-hidden bg-surface-container-low border border-outline-variant shadow-sm ${className}`}
      style={bgStyle}
    >
      {/* Overlay if there's a background image to ensure text is readable */}
      {backgroundImage && (
        <div className="absolute inset-0 bg-gradient-to-r from-surface-container-lowest via-surface-container-lowest/80 to-transparent"></div>
      )}

      <div className="relative p-6 sm:p-8 flex flex-col md:flex-row gap-6 md:items-center justify-between z-10">
        
        <div className="flex flex-col gap-4 max-w-3xl">
          {breadcrumbs && (
            <div className="text-xs font-semibold text-outline tracking-wide">
              {breadcrumbs}
            </div>
          )}
          
          <div className="flex items-center gap-4">
            {icon && (
              <div 
                className="w-12 h-12 sm:w-16 sm:h-16 rounded-xl flex items-center justify-center shrink-0 shadow-md"
                style={{ backgroundColor: iconBgColor, color: iconColor }}
              >
                <span className="material-symbols-outlined !text-[32px] sm:!text-[40px]">{icon}</span>
              </div>
            )}
            
            <div className="flex flex-col">
              <h1 className="text-2xl sm:text-3xl font-black tracking-tight text-slate-900! dark:text-white!">
                {title}
              </h1>
              {subtitle && (
                <p className="text-sm sm:text-base text-slate-500! dark:text-slate-300! mt-1 font-medium">
                  {subtitle}
                </p>
              )}
            </div>
          </div>
        </div>

        {actions && (
          <div className="flex flex-wrap items-center gap-3 shrink-0 mt-4 md:mt-0">
            {actions}
          </div>
        )}
      </div>
    </div>
  );
}
