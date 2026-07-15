import { forwardRef } from 'react';

export interface DateRangePickerProps {
  startDate?: string;
  endDate?: string;
  onChange?: (range: { startDate: string; endDate: string }) => void;
  minDate?: string;
  maxDate?: string;
  label?: string;
  error?: string;
  disabled?: boolean;
  className?: string;
}

export const DateRangePicker = forwardRef<HTMLDivElement, DateRangePickerProps>(({
  startDate = '',
  endDate = '',
  onChange,
  minDate,
  maxDate,
  label,
  error,
  disabled,
  className = ''
}, ref) => {
  const handleStartChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onChange?.({ startDate: e.target.value, endDate });
  };

  const handleEndChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onChange?.({ startDate, endDate: e.target.value });
  };

  return (
    <div ref={ref} className={`flex flex-col gap-1.5 ${className}`}>
      {label && <label className="text-xs font-bold text-on-surface-variant uppercase tracking-wider">{label}</label>}
      
      <div className={`flex items-center gap-2 ${disabled ? 'opacity-60 cursor-not-allowed' : ''}`}>
        <div className={`relative flex-1 flex items-center border rounded-lg overflow-hidden transition-colors ${error ? 'border-error' : 'border-outline-variant focus-within:border-primary focus-within:ring-1 focus-within:ring-primary'}`}>
          <div className="pl-3 text-outline flex items-center justify-center">
            <span className="material-symbols-outlined !text-[18px]">calendar_month</span>
          </div>
          <input 
            type="date"
            value={startDate}
            onChange={handleStartChange}
            min={minDate}
            max={endDate || maxDate}
            disabled={disabled}
            className={`w-full px-3 py-2 text-sm font-semibold bg-surface-container-lowest text-on-surface outline-none ${disabled ? 'bg-surface-container-low cursor-not-allowed' : ''}`}
          />
        </div>

        <span className="text-outline-variant font-bold text-sm px-1">-</span>

        <div className={`relative flex-1 flex items-center border rounded-lg overflow-hidden transition-colors ${error ? 'border-error' : 'border-outline-variant focus-within:border-primary focus-within:ring-1 focus-within:ring-primary'}`}>
          <div className="pl-3 text-outline flex items-center justify-center">
            <span className="material-symbols-outlined !text-[18px]">calendar_month</span>
          </div>
          <input 
            type="date"
            value={endDate}
            onChange={handleEndChange}
            min={startDate || minDate}
            max={maxDate}
            disabled={disabled}
            className={`w-full px-3 py-2 text-sm font-semibold bg-surface-container-lowest text-on-surface outline-none ${disabled ? 'bg-surface-container-low cursor-not-allowed' : ''}`}
          />
        </div>
      </div>
      
      {error && <span className="text-xs text-error font-medium mt-1">{error}</span>}
    </div>
  );
});

DateRangePicker.displayName = 'DateRangePicker';
