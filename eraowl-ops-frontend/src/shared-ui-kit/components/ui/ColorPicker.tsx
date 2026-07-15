import { forwardRef } from 'react';

export interface ColorPickerProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type' | 'onChange'> {
  value?: string;
  onChange?: (color: string) => void;
  label?: string;
  error?: string;
  className?: string;
  disabled?: boolean;
}

export const ColorPicker = forwardRef<HTMLInputElement, ColorPickerProps>(({
  value = '#000000',
  onChange,
  label,
  error,
  className = '',
  disabled,
  ...props
}, ref) => {
  return (
    <div className={`flex flex-col gap-1.5 ${className}`}>
      {label && <label className="text-xs font-bold text-on-surface-variant uppercase tracking-wider">{label}</label>}
      <div className={`relative flex items-center border rounded-lg overflow-hidden transition-colors ${error ? 'border-error' : 'border-outline-variant focus-within:border-primary focus-within:ring-1 focus-within:ring-primary'}`}>
        
        {/* Color Swatch / HTML5 Color Input Wrapper */}
        <div className="relative w-10 h-full border-r border-outline-variant shrink-0 bg-surface-container-low cursor-pointer">
          <input 
            type="color"
            value={value}
            onChange={(e) => onChange?.(e.target.value)}
            disabled={disabled}
            className={`absolute inset-0 w-full h-full opacity-0 cursor-pointer ${disabled ? 'cursor-not-allowed' : ''}`}
            tabIndex={-1}
          />
          <div 
            className={`absolute inset-1 rounded border border-black/10 shadow-inner ${disabled ? 'opacity-50' : ''}`}
            style={{ backgroundColor: value }}
          ></div>
        </div>

        {/* Text Input for HEX */}
        <input 
          type="text" 
          ref={ref}
          value={value}
          onChange={(e) => {
            const val = e.target.value;
            onChange?.(val);
          }}
          disabled={disabled}
          placeholder="#000000"
          className={`flex-1 min-w-0 px-3 py-2 text-sm font-semibold font-mono bg-surface-container-lowest text-on-surface outline-none ${disabled ? 'opacity-60 cursor-not-allowed bg-surface-container-low' : ''}`}
          {...props} 
        />
      </div>
      {error && <span className="text-xs text-error font-medium mt-1">{error}</span>}
    </div>
  );
});

ColorPicker.displayName = 'ColorPicker';
