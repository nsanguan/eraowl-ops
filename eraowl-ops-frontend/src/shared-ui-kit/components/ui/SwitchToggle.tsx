import { forwardRef } from 'react';

export interface SwitchToggleProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type' | 'onChange' | 'size'> {
  checked?: boolean;
  onChange?: (checked: boolean) => void;
  label?: string;
  labelPosition?: 'left' | 'right';
  size?: 'sm' | 'md' | 'lg';
}

export const SwitchToggle = forwardRef<HTMLInputElement, SwitchToggleProps>(({
  checked = false,
  onChange,
  label,
  labelPosition = 'right',
  size = 'md',
  className = '',
  disabled,
  ...props
}, ref) => {
  const sizeClasses = {
    sm: 'w-8 h-4 after:w-3 after:h-3',
    md: 'w-11 h-6 after:w-5 after:h-5',
    lg: 'w-14 h-8 after:w-7 after:h-7'
  };

  const translateClasses = {
    sm: 'peer-checked:after:translate-x-4',
    md: 'peer-checked:after:translate-x-5',
    lg: 'peer-checked:after:translate-x-6'
  };

  const textClasses = {
    sm: 'text-xs',
    md: 'text-sm',
    lg: 'text-base'
  };

  const toggle = (
    <label className={`relative inline-flex items-center ${disabled ? 'cursor-not-allowed opacity-60' : 'cursor-pointer'} ${className}`}>
      <input 
        type="checkbox" 
        className="sr-only peer" 
        checked={checked} 
        onChange={(e) => onChange?.(e.target.checked)}
        disabled={disabled}
        ref={ref}
        {...props} 
      />
      <div className={`
        ${sizeClasses[size]} 
        bg-surface-container-high peer-focus:outline-none peer-focus:ring-2 peer-focus:ring-primary/50 
        rounded-full peer peer-checked:after:border-white after:content-[''] after:absolute 
        after:top-[2px] after:left-[2px] after:bg-white after:border-outline-variant after:border 
        after:rounded-full after:transition-all peer-checked:bg-primary ${translateClasses[size]}
      `}></div>
    </label>
  );

  if (!label) return toggle;

  return (
    <div className={`flex items-center gap-3 ${disabled ? 'opacity-60 cursor-not-allowed' : ''}`}>
      {labelPosition === 'left' && <span className={`font-semibold text-on-surface ${textClasses[size]}`}>{label}</span>}
      {toggle}
      {labelPosition === 'right' && <span className={`font-semibold text-on-surface ${textClasses[size]}`}>{label}</span>}
    </div>
  );
});

SwitchToggle.displayName = 'SwitchToggle';
