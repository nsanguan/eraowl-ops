import { useState, useRef, useEffect } from 'react';

export interface SmartSearchChip {
  id: string; // The value of the filter
  group: string; // The facet id, e.g. 'status'
  label: string; // The display label, e.g. 'APPROVED'
  groupLabel?: string; // e.g. 'Status'
}

export interface SmartSearchProps {
  query: string;
  onQueryChange: (q: string) => void;
  chips?: SmartSearchChip[];
  onRemoveChip?: (id: string, group: string) => void;
  dateAttributes?: { value: string; label: string }[];
  onDateAttributeSelect?: (attr: string) => void;
  placeholder?: string;
  className?: string;
}

export function SmartSearch({
  query,
  onQueryChange,
  chips = [],
  onRemoveChip,
  dateAttributes = [],
  onDateAttributeSelect,
  placeholder = "Search...",
  className = ""
}: SmartSearchProps) {
  const [isDateOpen, setIsDateOpen] = useState(false);
  const dateDropdownRef = useRef<HTMLDivElement>(null);

  // Close dropdown on click outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dateDropdownRef.current && !dateDropdownRef.current.contains(event.target as Node)) {
        setIsDateOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className={`flex flex-col border border-outline-variant rounded bg-surface-container-lowest focus-within:border-primary focus-within:ring-1 focus-within:ring-primary min-w-[280px] w-[350px] transition-all shadow-sm ${className}`}>
      {/* Top Row: Search Input and Calendar Icon */}
      <div className="flex items-center px-2 py-1.5 gap-1.5">
        <span className="material-symbols-outlined !text-[16px] text-outline shrink-0">search</span>
        <input
          type="text"
          value={query}
          onChange={e => onQueryChange(e.target.value)}
          placeholder={placeholder}
          className="bg-transparent border-none outline-none text-[12px] text-on-surface flex-1 placeholder:text-outline/50 min-w-0"
        />
        {dateAttributes.length > 0 && (
          <div className="relative flex items-center shrink-0" ref={dateDropdownRef}>
            <button 
              className={`p-1 hover:bg-surface-container-high rounded transition-colors flex items-center justify-center ${isDateOpen ? 'bg-surface-container-high text-primary' : 'text-outline'}`}
              onClick={() => setIsDateOpen(!isDateOpen)}
              title="Quick Date Filter"
            >
              <span className="material-symbols-outlined !text-[16px]">calendar_month</span>
            </button>
            {isDateOpen && (
              <div className="absolute right-0 top-full mt-1 bg-surface-container-highest border border-outline-variant shadow-lg rounded py-1 z-50 min-w-[200px]">
                <div className="px-3 py-1.5 text-[10px] font-bold text-outline uppercase tracking-wider border-b border-outline-variant/50 mb-1">
                  Select a Date Attribute
                </div>
                {dateAttributes.map(attr => (
                  <button
                    key={attr.value}
                    className="w-full text-left px-3 py-1.5 text-[12px] text-on-surface hover:bg-primary/10 hover:text-primary transition-colors flex items-center justify-between group"
                    onClick={() => {
                      onDateAttributeSelect?.(attr.value);
                      setIsDateOpen(false);
                    }}
                  >
                    {attr.label}
                    <span className="material-symbols-outlined !text-[14px] opacity-0 group-hover:opacity-100 transition-opacity">chevron_right</span>
                  </button>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      {/* Bottom Row: Chips */}
      {chips.length > 0 && (
        <div className="flex items-center flex-wrap gap-1.5 px-2 pb-2 pt-0.5 border-t border-outline-variant/30 bg-surface-container-lowest">
          {chips.map(chip => (
            <div 
              key={`${chip.group}-${chip.id}`}
              className="flex items-center gap-1 bg-surface-container-low border border-outline-variant/80 rounded pl-1.5 pr-1 py-0.5 text-[11px] text-on-surface shadow-sm"
              title={`${chip.groupLabel ? chip.groupLabel + ': ' : ''}${chip.label}`}
            >
              <span className="truncate max-w-[150px]">
                {chip.groupLabel ? <span className="font-semibold text-on-surface-variant">{chip.groupLabel} </span> : null}
                {chip.label}
              </span>
              {onRemoveChip && (
                <button 
                  onClick={() => onRemoveChip(chip.id, chip.group)}
                  className="hover:bg-error/10 hover:text-error rounded p-0.5 text-outline transition-colors flex items-center justify-center ml-0.5"
                >
                  <span className="material-symbols-outlined !text-[12px]">close</span>
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
