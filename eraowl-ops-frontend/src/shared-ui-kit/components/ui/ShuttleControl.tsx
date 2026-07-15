import { useState, useMemo } from 'react';

export interface ShuttleItem {
  id: string;
  label: string;
  description?: string;
}

export interface ShuttleControlProps {
  availableItems: ShuttleItem[];
  selectedItems: ShuttleItem[];
  onChange: (selectedIds: string[]) => void;
  availableLabel?: string;
  selectedLabel?: string;
  height?: string;
  className?: string;
}

export function ShuttleControl({
  availableItems,
  selectedItems,
  onChange,
  availableLabel = 'Available',
  selectedLabel = 'Selected',
  height = '300px',
  className = ''
}: ShuttleControlProps) {
  const [availableSelection, setAvailableSelection] = useState<Set<string>>(new Set());
  const [selectedSelection, setSelectedSelection] = useState<Set<string>>(new Set());
  const [searchAvailable, setSearchAvailable] = useState('');
  const [searchSelected, setSearchSelected] = useState('');

  // Remove already selected items from the available pool
  const selectedIds = useMemo(() => new Set(selectedItems.map(i => i.id)), [selectedItems]);
  const actualAvailable = useMemo(() => availableItems.filter(i => !selectedIds.has(i.id)), [availableItems, selectedIds]);

  const filteredAvailable = useMemo(() => {
    if (!searchAvailable) return actualAvailable;
    const lower = searchAvailable.toLowerCase();
    return actualAvailable.filter(i => i.label.toLowerCase().includes(lower) || i.description?.toLowerCase().includes(lower));
  }, [actualAvailable, searchAvailable]);

  const filteredSelected = useMemo(() => {
    if (!searchSelected) return selectedItems;
    const lower = searchSelected.toLowerCase();
    return selectedItems.filter(i => i.label.toLowerCase().includes(lower) || i.description?.toLowerCase().includes(lower));
  }, [selectedItems, searchSelected]);

  const toggleSelection = (id: string, isAvailable: boolean, multi: boolean) => {
    if (isAvailable) {
      setAvailableSelection(prev => {
        const next = new Set(multi ? prev : []);
        if (next.has(id)) next.delete(id);
        else next.add(id);
        return next;
      });
    } else {
      setSelectedSelection(prev => {
        const next = new Set(multi ? prev : []);
        if (next.has(id)) next.delete(id);
        else next.add(id);
        return next;
      });
    }
  };

  const handleMoveToSelected = () => {
    if (availableSelection.size === 0) return;
    const toMove = actualAvailable.filter(i => availableSelection.has(i.id));
    onChange([...selectedItems.map(i => i.id), ...toMove.map(i => i.id)]);
    setAvailableSelection(new Set());
  };

  const handleMoveToAvailable = () => {
    if (selectedSelection.size === 0) return;
    onChange(selectedItems.filter(i => !selectedSelection.has(i.id)).map(i => i.id));
    setSelectedSelection(new Set());
  };

  const handleMoveAllToSelected = () => {
    onChange([...selectedItems.map(i => i.id), ...filteredAvailable.map(i => i.id)]);
    setAvailableSelection(new Set());
  };

  const handleMoveAllToAvailable = () => {
    const visibleIds = new Set(filteredSelected.map(i => i.id));
    onChange(selectedItems.filter(i => !visibleIds.has(i.id)).map(i => i.id));
    setSelectedSelection(new Set());
  };

  const handleMoveUp = () => {
    if (selectedSelection.size === 0) return;
    const newItems = [...selectedItems];
    for (let i = 1; i < newItems.length; i++) {
      if (selectedSelection.has(newItems[i].id) && !selectedSelection.has(newItems[i - 1].id)) {
        [newItems[i - 1], newItems[i]] = [newItems[i], newItems[i - 1]];
      }
    }
    onChange(newItems.map(i => i.id));
  };

  const handleMoveDown = () => {
    if (selectedSelection.size === 0) return;
    const newItems = [...selectedItems];
    for (let i = newItems.length - 2; i >= 0; i--) {
      if (selectedSelection.has(newItems[i].id) && !selectedSelection.has(newItems[i + 1].id)) {
        [newItems[i], newItems[i + 1]] = [newItems[i + 1], newItems[i]];
      }
    }
    onChange(newItems.map(i => i.id));
  };

  const renderList = (items: ShuttleItem[], selection: Set<string>, isAvailable: boolean) => (
    <div className="flex flex-col flex-1 border border-outline-variant rounded-lg overflow-hidden bg-surface-container-lowest" style={{ height }}>
      <div className="bg-surface-container-low px-3 py-2 border-b border-outline-variant font-bold text-sm text-on-surface">
        {isAvailable ? availableLabel : selectedLabel} <span className="text-outline font-normal text-xs ml-1">({items.length})</span>
      </div>
      <div className="p-2 border-b border-outline-variant/50 bg-surface-container-lowest">
        <div className="relative">
          <span className="material-symbols-outlined absolute left-2 top-1/2 -translate-y-1/2 text-outline !text-[16px]">search</span>
          <input 
            type="text" 
            placeholder="Search..." 
            className="w-full bg-surface-container pl-8 pr-3 py-1.5 text-xs rounded border border-outline-variant focus:border-primary outline-none transition-colors"
            value={isAvailable ? searchAvailable : searchSelected}
            onChange={e => isAvailable ? setSearchAvailable(e.target.value) : setSearchSelected(e.target.value)}
          />
        </div>
      </div>
      <div className="flex-1 overflow-y-auto p-1 bg-surface-container-lowest">
        {items.length === 0 ? (
          <div className="h-full flex items-center justify-center text-xs text-outline italic">No items</div>
        ) : (
          <ul className="space-y-0.5">
            {items.map(item => {
              const isSelected = selection.has(item.id);
              return (
                <li 
                  key={item.id}
                  onClick={(e) => toggleSelection(item.id, isAvailable, e.ctrlKey || e.metaKey)}
                  onDoubleClick={() => {
                    if (isAvailable) {
                      onChange([...selectedItems.map(i => i.id), item.id]);
                      setAvailableSelection(prev => { const n = new Set(prev); n.delete(item.id); return n; });
                    } else {
                      onChange(selectedItems.filter(i => i.id !== item.id).map(i => i.id));
                      setSelectedSelection(prev => { const n = new Set(prev); n.delete(item.id); return n; });
                    }
                  }}
                  className={`px-3 py-2 rounded text-sm cursor-pointer select-none transition-colors border ${
                    isSelected 
                      ? 'bg-primary/10 border-primary/30 text-primary font-semibold' 
                      : 'border-transparent text-on-surface hover:bg-surface-container-high'
                  }`}
                >
                  <div>{item.label}</div>
                  {item.description && <div className={`text-[10px] mt-0.5 ${isSelected ? 'text-primary/70' : 'text-outline'}`}>{item.description}</div>}
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );

  return (
    <div className={`flex items-stretch gap-3 ${className}`}>
      {renderList(filteredAvailable, availableSelection, true)}
      
      <div className="flex flex-col items-center justify-center gap-2 pt-[76px] pb-4 px-1">
        <button type="button" onClick={handleMoveToSelected} disabled={availableSelection.size === 0}
          className="w-8 h-8 rounded-full border border-outline-variant flex items-center justify-center bg-surface-container hover:bg-surface-container-high hover:border-primary hover:text-primary transition-all disabled:opacity-30 disabled:cursor-not-allowed text-on-surface-variant" title="Move Selected">
          <span className="material-symbols-outlined !text-[18px]">chevron_right</span>
        </button>
        <button type="button" onClick={handleMoveAllToSelected} disabled={filteredAvailable.length === 0}
          className="w-8 h-8 rounded-full border border-outline-variant flex items-center justify-center bg-surface-container hover:bg-surface-container-high hover:border-primary hover:text-primary transition-all disabled:opacity-30 disabled:cursor-not-allowed text-on-surface-variant" title="Move All">
          <span className="material-symbols-outlined !text-[18px]">keyboard_double_arrow_right</span>
        </button>
        <div className="w-6 border-b border-outline-variant my-1"></div>
        <button type="button" onClick={handleMoveToAvailable} disabled={selectedSelection.size === 0}
          className="w-8 h-8 rounded-full border border-outline-variant flex items-center justify-center bg-surface-container hover:bg-surface-container-high hover:border-primary hover:text-primary transition-all disabled:opacity-30 disabled:cursor-not-allowed text-on-surface-variant" title="Remove Selected">
          <span className="material-symbols-outlined !text-[18px]">chevron_left</span>
        </button>
        <button type="button" onClick={handleMoveAllToAvailable} disabled={filteredSelected.length === 0}
          className="w-8 h-8 rounded-full border border-outline-variant flex items-center justify-center bg-surface-container hover:bg-surface-container-high hover:border-primary hover:text-primary transition-all disabled:opacity-30 disabled:cursor-not-allowed text-on-surface-variant" title="Remove All">
          <span className="material-symbols-outlined !text-[18px]">keyboard_double_arrow_left</span>
        </button>
      </div>

      {renderList(filteredSelected, selectedSelection, false)}

      <div className="flex flex-col items-center justify-center gap-2 pt-[76px] pb-4 px-1">
        <button type="button" onClick={handleMoveUp} disabled={selectedSelection.size === 0}
          className="w-8 h-8 rounded-full border border-outline-variant flex items-center justify-center bg-surface-container hover:bg-surface-container-high hover:border-primary hover:text-primary transition-all disabled:opacity-30 disabled:cursor-not-allowed text-on-surface-variant" title="Move Up">
          <span className="material-symbols-outlined !text-[18px]">expand_less</span>
        </button>
        <button type="button" onClick={handleMoveDown} disabled={selectedSelection.size === 0}
          className="w-8 h-8 rounded-full border border-outline-variant flex items-center justify-center bg-surface-container hover:bg-surface-container-high hover:border-primary hover:text-primary transition-all disabled:opacity-30 disabled:cursor-not-allowed text-on-surface-variant" title="Move Down">
          <span className="material-symbols-outlined !text-[18px]">expand_more</span>
        </button>
      </div>
    </div>
  );
}
