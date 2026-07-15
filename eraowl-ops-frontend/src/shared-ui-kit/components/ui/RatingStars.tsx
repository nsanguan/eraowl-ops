import { useState } from 'react';

export interface RatingStarsProps {
  value?: number;
  onChange?: (value: number) => void;
  max?: number;
  label?: string;
  disabled?: boolean;
  readOnly?: boolean;
  className?: string;
}

export function RatingStars({
  value = 0,
  onChange,
  max = 5,
  label,
  disabled = false,
  readOnly = false,
  className = ''
}: RatingStarsProps) {
  const [hoverValue, setHoverValue] = useState<number | null>(null);

  const displayValue = hoverValue !== null ? hoverValue : value;
  const interactive = !disabled && !readOnly;

  return (
    <div className={`flex flex-col gap-1.5 ${className}`}>
      {label && <label className="text-xs font-bold text-on-surface-variant uppercase tracking-wider">{label}</label>}
      <div 
        className={`flex items-center gap-1 ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
        onMouseLeave={() => interactive && setHoverValue(null)}
      >
        {Array.from({ length: max }).map((_, index) => {
          const starValue = index + 1;
          const isFilled = starValue <= displayValue;
          
          return (
            <button
              key={starValue}
              type="button"
              disabled={!interactive}
              onClick={() => interactive && onChange?.(starValue)}
              onMouseEnter={() => interactive && setHoverValue(starValue)}
              className={`p-1 rounded-full flex items-center justify-center transition-all ${
                interactive ? 'cursor-pointer hover:scale-110' : 'cursor-default'
              } ${isFilled ? 'text-yellow-500' : 'text-outline-variant'}`}
            >
              <span className={`material-symbols-outlined !text-[24px] ${isFilled ? 'font-variation-fill' : ''}`} style={{ fontVariationSettings: isFilled ? "'FILL' 1" : "'FILL' 0" }}>
                star
              </span>
            </button>
          );
        })}
        
        {/* Optional clear button if interactive and has value */}
        {interactive && value > 0 && (
          <button
            type="button"
            onClick={() => onChange?.(0)}
            className="p-1 ml-2 rounded-full text-outline hover:text-error hover:bg-error/10 transition-colors"
            title="Clear rating"
          >
            <span className="material-symbols-outlined !text-[16px]">close</span>
          </button>
        )}
      </div>
    </div>
  );
}
