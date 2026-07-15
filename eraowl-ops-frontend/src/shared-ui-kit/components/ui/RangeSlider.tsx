import { forwardRef } from 'react';

export interface RangeSliderProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type' | 'onChange'> {
  value?: number;
  onChange?: (value: number) => void;
  min?: number;
  max?: number;
  step?: number;
  label?: string;
  showValue?: boolean;
  disabled?: boolean;
  className?: string;
}

export const RangeSlider = forwardRef<HTMLInputElement, RangeSliderProps>(({
  value = 0,
  onChange,
  min = 0,
  max = 100,
  step = 1,
  label,
  showValue = true,
  disabled = false,
  className = '',
  ...props
}, ref) => {
  
  const percentage = ((value - min) / (max - min)) * 100;

  return (
    <div className={`flex flex-col gap-2 ${className}`}>
      {(label || showValue) && (
        <div className="flex items-center justify-between">
          {label && <label className="text-xs font-bold text-on-surface-variant uppercase tracking-wider">{label}</label>}
          {showValue && <span className="text-xs font-bold text-primary">{value}</span>}
        </div>
      )}
      
      <div className="relative flex items-center h-6">
        {/* Track background */}
        <div className="absolute w-full h-1.5 bg-surface-container-high rounded-full overflow-hidden">
          {/* Fill progress */}
          <div 
            className={`h-full rounded-full ${disabled ? 'bg-outline-variant' : 'bg-primary'}`}
            style={{ width: `${Math.max(0, Math.min(100, percentage))}%` }}
          ></div>
        </div>
        
        {/* Native range input overlay (styled to only show thumb) */}
        <input 
          type="range"
          ref={ref}
          value={value}
          onChange={(e) => onChange?.(Number(e.target.value))}
          min={min}
          max={max}
          step={step}
          disabled={disabled}
          className={`absolute w-full h-full opacity-0 cursor-pointer ${disabled ? 'cursor-not-allowed' : ''}`}
          style={{ zIndex: 10 }}
          {...props} 
        />
        
        {/* Custom Thumb (purely visual, positioned by percentage) */}
        <div 
          className={`absolute w-4 h-4 rounded-full bg-white border-2 shadow-sm pointer-events-none transform -translate-x-1/2 ${
            disabled ? 'border-outline-variant' : 'border-primary'
          }`}
          style={{ left: `${Math.max(0, Math.min(100, percentage))}%` }}
        ></div>
      </div>
    </div>
  );
});

RangeSlider.displayName = 'RangeSlider';
