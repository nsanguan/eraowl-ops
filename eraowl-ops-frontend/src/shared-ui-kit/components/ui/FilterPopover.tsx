import { useState, useRef, useEffect, type ReactNode } from 'react';

export interface FilterState {
  globalSearch: string;
  fieldFilters: Record<string, string>;
}

export interface FilterColumn {
  key: string;
  label: string;
}

export interface SearchFilterBarProps {
  inputValue: string;
  onInputChange: (value: string) => void;
  onSearch: (query: string) => void;
  onClear: () => void;
  onOpenFilter?: () => void;
  activeFilterCount?: number;
  placeholder?: string;
  lastQuery?: string;
  children?: ReactNode;
}

export function SearchFilterBar({
  inputValue,
  onInputChange,
  onSearch,
  onClear,
  onOpenFilter,
  activeFilterCount = 0,
  placeholder = 'Search...',
  lastQuery,
  children,
}: SearchFilterBarProps) {
  return (
    <div className="p-4 bg-surface-container border border-outline-variant rounded-xl">
      <div className="flex flex-col sm:flex-row gap-3">
        <div className="flex-1 relative">
          <div className="absolute inset-y-0 left-3.5 flex items-center pointer-events-none text-outline">
            <span className="material-symbols-outlined !text-[18px]">search</span>
          </div>
          <input
            className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg py-2.5 pl-10 pr-3.5 text-sm focus:ring-2 focus:ring-primary outline-none transition-all"
            placeholder={placeholder}
            type="text"
            value={inputValue}
            onChange={(e) => onInputChange(e.target.value)}
            onKeyDown={(e) => { if (e.key === 'Enter') onSearch(inputValue); }}
          />
        </div>
        <button
          className="px-4 py-2.5 bg-primary text-primary-foreground rounded-lg font-semibold text-[11px] flex items-center gap-2 hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20"
          onClick={() => onSearch(inputValue)}
        >
          <span className="material-symbols-outlined !text-[16px]">search</span>
          <span>Search</span>
        </button>
        {onOpenFilter && (
          <button
            className={`px-4 py-2.5 rounded-lg text-[11px] font-semibold flex items-center gap-2 transition-all relative ${
              activeFilterCount > 0
                ? 'bg-primary/10 text-primary border border-primary/30'
                : 'bg-surface-container-lowest border border-outline-variant text-outline hover:bg-surface-container-high'
            }`}
            onClick={onOpenFilter}
          >
            <span className="material-symbols-outlined !text-[16px]">tune</span>
            <span>Filters</span>
            {activeFilterCount > 0 && (
              <span className="min-w-[18px] h-[18px] inline-flex items-center justify-center rounded-full bg-primary text-primary-foreground text-[9px] font-bold px-1">
                {activeFilterCount}
              </span>
            )}
          </button>
        )}
        {lastQuery && (
          <button
            onClick={onClear}
            className="px-4 py-2.5 bg-surface-container-lowest border border-outline-variant rounded-lg text-[11px] font-semibold text-outline hover:text-on-surface flex items-center gap-2 transition-all"
          >
            <span className="material-symbols-outlined !text-[14px]">close</span>
            <span>Clear</span>
          </button>
        )}
        {children}
      </div>
    </div>
  );
}

interface FilterPopoverProps {
  columns: FilterColumn[];
  filter: FilterState;
  onChange: (filter: FilterState) => void;
  onApply?: (filter: FilterState) => void;
  onClose?: () => void;
  isOpen?: boolean;
  emptyFilter?: FilterState;
}

export function FilterModal({
  columns,
  filter,
  onChange,
  onApply,
  onClose,
  isOpen,
  emptyFilter,
}: FilterPopoverProps) {
  if (!isOpen) return null;

  const empty = emptyFilter ?? { globalSearch: '', fieldFilters: {} };
  const dirty = JSON.stringify(filter) !== JSON.stringify(empty);

  const handleReset = () => {
    onChange(empty);
  };

  const handleApply = () => {
    onApply?.(filter);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-[10vh]">
      <div className="absolute inset-0 bg-black/30 backdrop-blur-sm" onClick={onClose} />
      <div className="relative bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-2xl max-h-[80vh] overflow-y-auto mx-4">
        {/* Header */}
        <div className="sticky top-0 bg-surface-container z-10 flex items-center justify-between px-6 py-5 border-b border-outline-variant/30 rounded-t-2xl">
          <div className="flex items-center gap-3">
            <span className="material-symbols-outlined text-2xl text-primary">tune</span>
            <div>
              <h2 className="text-lg font-bold text-slate-900! dark:text-white!">Advanced Filters</h2>
              <p className="text-xs text-slate-500! dark:text-slate-300!">Refine results by any field</p>
            </div>
          </div>
          <button onClick={onClose} className="w-10 h-10 rounded-xl bg-surface-container-lowest border border-outline-variant flex items-center justify-center text-outline hover:text-on-surface transition-colors">
            <span className="material-symbols-outlined">close</span>
          </button>
        </div>

        {/* Body */}
        <div className="px-6 py-5 space-y-4">
          <div>
            <label className="block text-[10px] text-outline font-semibold mb-1.5 uppercase tracking-wider">Global Search</label>
            <div className="relative">
              <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline !text-[16px]">search</span>
              <input className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg pl-9 pr-3 py-2.5 text-sm focus:ring-2 focus:ring-primary outline-none transition-all"
                     type="text" placeholder="Search any field..."
                     value={filter.globalSearch}
                     onChange={(e) => onChange({ ...filter, globalSearch: e.target.value })} />
            </div>
          </div>
          <div className="border-t border-outline-variant/30" />
          <div className="space-y-3.5">
            <p className="text-[10px] text-outline font-semibold uppercase tracking-wider">Filter by Field</p>
            {columns.length === 0 && (
              <p className="text-sm text-outline italic">No filterable fields available</p>
            )}
            {columns.map((col) => (
              <div key={col.key}>
                <label className="block text-[11px] text-on-surface-variant font-semibold mb-1 tracking-wider">{col.label}</label>
                <input className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-3 py-2.5 text-sm focus:ring-2 focus:ring-primary outline-none transition-all"
                       type="text" placeholder={`Filter ${col.label.toLowerCase()}...`}
                       value={filter.fieldFilters[col.key] ?? ''}
                       onChange={(e) => onChange({
                         ...filter,
                         fieldFilters: { ...filter.fieldFilters, [col.key]: e.target.value }
                       })} />
              </div>
            ))}
          </div>
        </div>

        {/* Footer */}
        <div className="sticky bottom-0 bg-surface-container border-t border-outline-variant/30 px-6 py-4 rounded-b-2xl flex items-center justify-between">
          <button
            onClick={handleReset}
            disabled={!dirty}
            className="px-4 py-2 rounded-lg text-[11px] font-semibold text-outline hover:text-on-surface transition-colors disabled:opacity-30 flex items-center gap-2"
          >
            <span className="material-symbols-outlined !text-[14px]">restart_alt</span>
            <span>Reset All</span>
          </button>
          <div className="flex items-center gap-3">
            <button
              onClick={onClose}
              className="px-5 py-2 rounded-lg text-[11px] font-semibold text-outline bg-surface-container-lowest border border-outline-variant hover:bg-surface-container-high transition-colors"
            >
              Cancel
            </button>
            <button
              onClick={handleApply}
              className="px-6 py-2 rounded-lg text-[11px] font-bold text-primary-foreground bg-primary hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20 flex items-center gap-2"
            >
              <span className="material-symbols-outlined !text-[14px]">filter_alt</span>
              <span>Apply Filters</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export function FilterPopover({
  columns,
  filter,
  onChange,
}: FilterPopoverProps) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const hasActiveFilter = filter.globalSearch || Object.values(filter.fieldFilters).some(Boolean);
  const activeCount = [filter.globalSearch ? 1 : 0, ...Object.values(filter.fieldFilters).filter(Boolean)].filter(Boolean).length;

  return (
    <div ref={ref} className="relative">
      <button onClick={() => setOpen(!open)}
              className={`p-2.5 rounded-lg border transition-all relative ${
                hasActiveFilter
                  ? 'bg-primary/10 border-primary/30 text-primary'
                  : 'border-outline-variant text-outline hover:bg-surface-container-high'
              }`}
              title="Filter records">
        <span className="material-symbols-outlined !text-[18px]">tune</span>
        {hasActiveFilter && (
          <span className="absolute -top-1.5 -right-1.5 w-4 h-4 bg-primary text-primary-foreground text-[9px] font-bold rounded-full flex items-center justify-center">
            {activeCount}
          </span>
        )}
      </button>
      {open && (
        <div className="absolute right-0 top-full mt-2 w-80 bg-surface-container border border-outline-variant rounded-xl shadow-xl z-50 p-4 space-y-4">
          <div className="flex items-center gap-2.5 border-b border-outline-variant/30 pb-3 mb-1">
            <span className="material-symbols-outlined text-primary !text-[18px]">tune</span>
            <div>
              <p className="text-[12px] font-bold text-on-surface">Filters</p>
              <p className="text-[10px] text-outline">Quick filter by field</p>
            </div>
          </div>
          <div>
            <label className="block text-[10px] text-outline font-semibold mb-1.5 uppercase tracking-wider">Global Search</label>
            <div className="relative">
              <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline !text-[16px]">search</span>
              <input className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg pl-9 pr-3 py-2 text-sm focus:ring-2 focus:ring-primary outline-none transition-all"
                     type="text" placeholder="Search any field..."
                     value={filter.globalSearch}
                     onChange={(e) => onChange({ ...filter, globalSearch: e.target.value })} />
            </div>
          </div>
          <div className="border-t border-outline-variant/30" />
          <div className="space-y-3">
            <p className="text-[10px] text-outline font-semibold uppercase tracking-wider">Filter by Field</p>
            {columns.map((col) => (
              <div key={col.key}>
                <label className="block text-[10px] text-on-surface-variant font-semibold mb-1 tracking-wider">{col.label}</label>
                <input className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-primary outline-none transition-all"
                       type="text" placeholder={`Filter ${col.label.toLowerCase()}...`}
                       value={filter.fieldFilters[col.key] ?? ''}
                       onChange={(e) => onChange({
                         ...filter,
                         fieldFilters: { ...filter.fieldFilters, [col.key]: e.target.value }
                       })} />
              </div>
            ))}
          </div>
          {hasActiveFilter && (
            <button onClick={() => onChange({ globalSearch: '', fieldFilters: {} })}
                    className="w-full text-center text-[11px] text-outline hover:text-on-surface font-semibold py-2 transition-colors border-t border-outline-variant/30 pt-3">
              Clear all filters
            </button>
          )}
        </div>
      )}
    </div>
  );
}

export function applyFilter<T extends Record<string, unknown>>(
  data: T[],
  filter: FilterState
): T[] {
  return data.filter((item) => {
    if (filter.globalSearch) {
      const q = filter.globalSearch.toLowerCase();
      const matches = Object.values(item).some((val) =>
        String(val ?? '').toLowerCase().includes(q)
      );
      if (!matches) return false;
    }
    for (const [key, value] of Object.entries(filter.fieldFilters)) {
      if (value) {
        const itemVal = String(item[key] ?? '').toLowerCase();
        if (!itemVal.includes(value.toLowerCase())) return false;
      }
    }
    return true;
  });
}
