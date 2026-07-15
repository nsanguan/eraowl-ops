import React from 'react';

export interface SegmentedOption {
  value: string;
  label: string;
  icon?: string;
  disabled?: boolean;
}

export interface SegmentedControlProps {
  options: SegmentedOption[];
  value: string;
  onChange: (value: string) => void;
  size?: 'sm' | 'md' | 'lg';
  fullWidth?: boolean;
  disabled?: boolean;
  className?: string;
}

export function SegmentedControl({
  options,
  value,
  onChange,
  size = 'md',
  fullWidth = false,
  disabled = false,
  className = ''
}: SegmentedControlProps) {
  
  const sizeClasses = {
    sm: 'text-xs py-1 px-3',
    md: 'text-sm py-1.5 px-4',
    lg: 'text-base py-2 px-6'
  };

  return (
    <div className={`inline-flex items-center bg-surface-container rounded-lg p-1 border border-outline-variant ${fullWidth ? 'w-full flex' : ''} ${className}`}>
      {options.map((option) => {
        const isSelected = value === option.value;
        const isDisabled = disabled || option.disabled;
        
        return (
          <button
            key={option.value}
            type="button"
            disabled={isDisabled}
            onClick={() => onChange(option.value)}
            className={`
              relative flex items-center justify-center gap-2 font-bold transition-all rounded-md select-none
              ${fullWidth ? 'flex-1' : ''}
              ${sizeClasses[size]}
              ${isDisabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}
              ${isSelected 
                ? 'bg-surface-container-lowest text-primary shadow-sm ring-1 ring-black/5' 
                : 'text-on-surface hover:text-on-surface hover:bg-surface-container-low'
              }
            `}
          >
            {option.icon && (
              <span className={`material-symbols-outlined ${size === 'sm' ? '!text-[16px]' : size === 'md' ? '!text-[18px]' : '!text-[20px]'}`}>
                {option.icon}
              </span>
            )}
            {option.label}
          </button>
        );
      })}
    </div>
  );
}
