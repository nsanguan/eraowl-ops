import React from 'react';

export interface ProgressBarProps {
  value: number; // 0 to 100
  label?: string;
  showValue?: boolean;
  status?: 'primary' | 'success' | 'warning' | 'error';
  size?: 'sm' | 'md' | 'lg';
  animated?: boolean;
  className?: string;
}

export function ProgressBar({
  value,
  label,
  showValue = true,
  status = 'primary',
  size = 'md',
  animated = false,
  className = ''
}: ProgressBarProps) {
  const percentage = Math.max(0, Math.min(100, value));

  const sizeClasses = {
    sm: 'h-1.5',
    md: 'h-2.5',
    lg: 'h-4'
  };

  const statusColors = {
    primary: 'bg-primary',
    success: 'bg-green-500',
    warning: 'bg-yellow-500',
    error: 'bg-error'
  };

  return (
    <div className={`flex flex-col gap-1.5 ${className}`}>
      {(label || showValue) && (
        <div className="flex items-center justify-between mb-0.5">
          {label && <span className="text-xs font-bold text-on-surface">{label}</span>}
          {showValue && <span className="text-xs font-bold text-on-surface-variant">{Math.round(percentage)}%</span>}
        </div>
      )}
      <div className={`w-full bg-surface-container-high rounded-full overflow-hidden ${sizeClasses[size]}`}>
        <div 
          className={`h-full rounded-full transition-all duration-500 ease-out ${statusColors[status]} ${animated ? 'animate-pulse' : ''}`}
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
    </div>
  );
}
