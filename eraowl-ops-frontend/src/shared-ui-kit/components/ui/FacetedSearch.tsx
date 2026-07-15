import { useState } from 'react';

export type FacetType = 'checkbox' | 'radio' | 'range';

export interface FacetOption {
  value: string;
  label: string;
  count?: number;
}

export interface Facet {
  id: string;
  label: string;
  type: FacetType;
  options: FacetOption[];
}

export interface FacetedSearchProps {
  facets: Facet[];
  state: Record<string, string[]>;
  onChange: (newState: Record<string, string[]>) => void;
  onClear: () => void;
  className?: string;
  title?: string;
  onHide?: () => void;
}

export function FacetedSearch({
  facets,
  state,
  onChange,
  onClear,
  className = '',
  title = 'Filters',
  onHide
}: FacetedSearchProps) {
  const [collapsed, setCollapsed] = useState<Set<string>>(new Set());
  const [searchTerms, setSearchTerms] = useState<Record<string, string>>({});

  const toggleCollapse = (id: string) => {
    setCollapsed(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const handleOptionChange = (facetId: string, optionValue: string, checked: boolean, type: FacetType) => {
    const current = state[facetId] || [];
    let next: string[];

    if (type === 'radio') {
      next = checked ? [optionValue] : [];
    } else {
      // Checkbox or range (multi-select)
      if (checked) {
        next = [...current, optionValue];
      } else {
        next = current.filter(v => v !== optionValue);
      }
    }

    onChange({ ...state, [facetId]: next });
  };

  const handleClearFacet = (facetId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    const nextState = { ...state };
    delete nextState[facetId];
    onChange(nextState);
  };

  const activeFilterCount = Object.values(state).reduce((acc, curr) => acc + (curr?.length || 0), 0);

  return (
    <div className={`flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden ${className}`}>
      {/* Header */}
      <div className="bg-surface-container-low px-4 py-3 flex items-center justify-between border-b border-outline-variant">
        <h2 className="font-bold text-on-surface flex items-center gap-2">
          <span className="material-symbols-outlined !text-[20px]">filter_alt</span>
          {title}
        </h2>
        <div className="flex items-center gap-2">
          {activeFilterCount > 0 && (
            <button 
              onClick={onClear}
              className="text-xs font-bold text-primary hover:underline"
            >
              Clear All
            </button>
          )}
          {onHide && (
            <button 
              onClick={onHide} 
              className="p-1 -mr-1 hover:bg-surface-container-highest rounded text-outline transition-colors flex items-center justify-center" 
              title="Hide Filters"
            >
              <span className="material-symbols-outlined !text-[18px]">keyboard_double_arrow_left</span>
            </button>
          )}
        </div>
      </div>

      {/* Facets */}
      <div className="flex flex-col flex-1 overflow-y-auto">
        {facets.map((facet, idx) => {
          const isCollapsed = collapsed.has(facet.id);
          const activeValues = state[facet.id] || [];
          const hasActive = activeValues.length > 0;
          const searchTerm = searchTerms[facet.id] || '';
          
          const visibleOptions = facet.options.filter(opt => 
            opt.label.toLowerCase().includes(searchTerm.toLowerCase())
          );

          return (
            <div key={facet.id} className={`${idx !== facets.length - 1 ? 'border-b border-outline-variant/50' : ''}`}>
              {/* Facet Header */}
              <div 
                className="px-4 py-3 flex items-center justify-between cursor-pointer hover:bg-surface-container-low transition-colors group select-none"
                onClick={() => toggleCollapse(facet.id)}
              >
                <div className="flex items-center gap-2">
                  <span className={`material-symbols-outlined !text-[18px] text-outline transition-transform ${isCollapsed ? '-rotate-90' : ''}`}>
                    expand_more
                  </span>
                  <span className="font-bold text-sm text-on-surface">{facet.label}</span>
                  {hasActive && (
                    <span className="bg-primary/10 text-primary text-[10px] font-bold px-1.5 py-0.5 rounded-full">
                      {activeValues.length}
                    </span>
                  )}
                </div>
                {hasActive && (
                  <button 
                    onClick={(e) => handleClearFacet(facet.id, e)}
                    className="opacity-0 group-hover:opacity-100 p-1 hover:bg-surface-container-high rounded text-outline hover:text-error transition-all"
                    title="Clear"
                  >
                    <span className="material-symbols-outlined !text-[16px]">close</span>
                  </button>
                )}
              </div>

              {/* Facet Body */}
              {!isCollapsed && (
                <div className="px-4 pb-4 pt-1 flex flex-col gap-2">
                  {facet.options.length > 8 && (
                    <div className="relative mb-2">
                      <span className="material-symbols-outlined absolute left-2 top-1/2 -translate-y-1/2 text-outline !text-[14px]">search</span>
                      <input 
                        type="text" 
                        placeholder="Search..." 
                        value={searchTerm}
                        onChange={e => setSearchTerms(prev => ({ ...prev, [facet.id]: e.target.value }))}
                        className="w-full bg-surface-container pl-7 pr-3 py-1.5 text-xs rounded border border-outline-variant focus:border-primary outline-none transition-colors"
                      />
                    </div>
                  )}

                  <div className="flex flex-col gap-1.5 max-h-[200px] overflow-y-auto pr-2 custom-scrollbar">
                    {visibleOptions.length === 0 ? (
                      <div className="text-xs text-outline italic py-2">No options found.</div>
                    ) : (
                      visibleOptions.map(opt => {
                        const isChecked = activeValues.includes(opt.value);
                        return (
                          <label key={opt.value} className="flex items-start gap-2 cursor-pointer group/opt">
                            <div className="pt-0.5">
                              {facet.type === 'radio' ? (
                                <input 
                                  type="radio" 
                                  name={facet.id}
                                  checked={isChecked}
                                  onChange={e => handleOptionChange(facet.id, opt.value, e.target.checked, facet.type)}
                                  className="accent-primary w-3.5 h-3.5 cursor-pointer"
                                />
                              ) : (
                                <input 
                                  type="checkbox" 
                                  checked={isChecked}
                                  onChange={e => handleOptionChange(facet.id, opt.value, e.target.checked, facet.type)}
                                  className="accent-primary w-3.5 h-3.5 rounded-sm cursor-pointer"
                                />
                              )}
                            </div>
                            <div className="flex-1 flex items-center justify-between min-w-0">
                              <span className={`text-xs truncate ${isChecked ? 'font-semibold text-primary' : 'text-on-surface-variant group-hover/opt:text-on-surface transition-colors'}`}>
                                {opt.label}
                              </span>
                              {opt.count !== undefined && (
                                <span className="text-[10px] text-outline ml-2 bg-surface-container px-1.5 py-0.5 rounded">
                                  {opt.count}
                                </span>
                              )}
                            </div>
                          </label>
                        );
                      })
                    )}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
