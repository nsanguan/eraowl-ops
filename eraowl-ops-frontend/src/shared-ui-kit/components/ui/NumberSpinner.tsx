import { forwardRef, useState, useEffect } from 'react';

export interface NumberSpinnerProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type' | 'onChange'> {
  value?: number;
  onChange?: (value: number) => void;
  min?: number;
  max?: number;
  step?: number;
  label?: string;
  error?: string;
}

export const NumberSpinner = forwardRef<HTMLInputElement, NumberSpinnerProps>(({
  value,
  onChange,
  min = Number.MIN_SAFE_INTEGER,
  max = Number.MAX_SAFE_INTEGER,
  step = 1,
  label,
  error,
  className = '',
  disabled,
  ...props
}, ref) => {
  const [internalValue, setInternalValue] = useState<number | ''>(value ?? '');

  useEffect(() => {
    if (value !== undefined) {
      setInternalValue(value);
    }
  }, [value]);

  const handleIncrement = () => {
    if (disabled) return;
    const current = typeof internalValue === 'number' ? internalValue : 0;
    const next = Math.min(current + step, max);
    setInternalValue(next);
    onChange?.(next);
  };

  const handleDecrement = () => {
    if (disabled) return;
    const current = typeof internalValue === 'number' ? internalValue : 0;
    const next = Math.max(current - step, min);
    setInternalValue(next);
    onChange?.(next);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    if (val === '') {
      setInternalValue('');
      return;
    }
    const num = Number(val);
    if (!isNaN(num)) {
      setInternalValue(num);
      onChange?.(num);
    }
  };

  const handleBlur = () => {
    if (typeof internalValue === 'number') {
      let clamped = internalValue;
      if (internalValue < min) clamped = min;
      if (internalValue > max) clamped = max;
      if (clamped !== internalValue) {
        setInternalValue(clamped);
        onChange?.(clamped);
      }
    }
  };

  return (
    <div className={`flex flex-col gap-1.5 ${className}`}>
      {label && <label className="text-xs font-bold text-on-surface-variant uppercase tracking-wider">{label}</label>}
      <div className={`relative flex items-center border rounded-lg overflow-hidden transition-colors ${error ? 'border-error' : 'border-outline-variant focus-within:border-primary focus-within:ring-1 focus-within:ring-primary'}`}>
        <input 
          type="text" 
          inputMode="numeric"
          pattern="[0-9]*"
          ref={ref}
          value={internalValue}
          onChange={handleChange}
          onBlur={handleBlur}
          disabled={disabled}
          className={`flex-1 min-w-0 px-3 py-2 text-sm font-semibold bg-surface-container-lowest text-on-surface outline-none ${disabled ? 'opacity-60 cursor-not-allowed bg-surface-container-low' : ''}`}
          {...props} 
        />
        <div className="flex flex-col border-l border-outline-variant h-full w-8 shrink-0">
          <button 
            type="button" 
            onClick={handleIncrement}
            disabled={disabled || (typeof internalValue === 'number' && internalValue >= max)}
            className="flex-1 flex items-center justify-center bg-surface-container hover:bg-surface-container-high transition-colors disabled:opacity-50 disabled:cursor-not-allowed border-b border-outline-variant h-[50%]"
            tabIndex={-1}
          >
            <span className="material-symbols-outlined !text-[14px]">expand_less</span>
          </button>
          <button 
            type="button" 
            onClick={handleDecrement}
            disabled={disabled || (typeof internalValue === 'number' && internalValue <= min)}
            className="flex-1 flex items-center justify-center bg-surface-container hover:bg-surface-container-high transition-colors disabled:opacity-50 disabled:cursor-not-allowed h-[50%]"
            tabIndex={-1}
          >
            <span className="material-symbols-outlined !text-[14px]">expand_more</span>
          </button>
        </div>
      </div>
      {error && <span className="text-xs text-error font-medium mt-1">{error}</span>}
    </div>
  );
});

NumberSpinner.displayName = 'NumberSpinner';
