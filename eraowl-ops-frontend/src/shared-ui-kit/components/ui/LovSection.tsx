import { useState, useEffect, useMemo } from 'react';
import { createPortal } from 'react-dom';

export interface LovColumn {
  key: string;
  header: string;
  width?: string;
  render?: (row: any) => React.ReactNode;
}

export interface LovSectionProps {
  isOpen: boolean;
  onClose: () => void;
  onSelect: (row: any) => void;
  title: string;
  columns: LovColumn[];
  data: any[];
  searchOptions: { key: string; label: string }[];
}

export function LovSection({ isOpen, onClose, onSelect, title, columns, data, searchOptions }: LovSectionProps) {
  const [searchBy, setSearchBy] = useState(searchOptions[0]?.key || '');
  const [searchValue, setSearchValue] = useState('');
  const [appliedSearch, setAppliedSearch] = useState({ by: '', value: '' });
  const [selectedRowId, setSelectedRowId] = useState<string | null>(null);

  // Reset state when opened
  useEffect(() => {
    if (isOpen) {
      setSearchValue('');
      setAppliedSearch({ by: '', value: '' });
      setSelectedRowId(null);
      if (searchOptions.length > 0) {
        setSearchBy(searchOptions[0].key);
      }
    }
  }, [isOpen, searchOptions]);

  const filteredData = useMemo(() => {
    if (!appliedSearch.value) return data;
    return data.filter(row => {
      const val = row[appliedSearch.by];
      if (val == null) return false;
      return String(val).toLowerCase().includes(appliedSearch.value.toLowerCase());
    });
  }, [data, appliedSearch]);

  const handleGo = () => {
    setAppliedSearch({ by: searchBy, value: searchValue });
    setSelectedRowId(null); // reset selection on new search
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleGo();
    }
  };

  if (!isOpen) return null;

  return createPortal(
    <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
      <div className="bg-surface-container-lowest w-full max-w-4xl rounded-xl shadow-2xl border border-outline-variant flex flex-col max-h-[85vh] animate-in fade-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-outline-variant bg-surface-container-low rounded-t-xl">
          <h2 className="text-lg font-bold text-slate-900! dark:text-white! tracking-tight">Search and Select: {title}</h2>
          <button onClick={onClose} className="p-1 text-outline hover:text-on-surface hover:bg-outline-variant/30 rounded-lg transition-colors">
            <span className="material-symbols-outlined !text-[20px]">close</span>
          </button>
        </div>

        {/* Content */}
        <div className="p-6 flex-1 overflow-y-auto">
          {/* Search Area */}
          <div className="mb-6">
            <h3 className="text-sm font-bold text-on-surface mb-1">Search</h3>
            <p className="text-xs text-outline mb-4">
              To find your item, select a filter item in the pulldown list and enter a value in the text field, then select the "Go" button.
            </p>
            <div className="flex items-center gap-3">
              <label className="text-sm font-semibold text-on-surface-variant">Search By</label>
              <select 
                value={searchBy} 
                onChange={(e) => setSearchBy(e.target.value)}
                className="bg-surface-container border border-outline-variant rounded px-3 py-1.5 text-sm outline-none focus:border-primary text-on-surface"
              >
                {searchOptions.map(opt => (
                  <option key={opt.key} value={opt.key}>{opt.label}</option>
                ))}
              </select>
              <input 
                type="text" 
                value={searchValue} 
                onChange={(e) => setSearchValue(e.target.value)}
                onKeyDown={handleKeyDown}
                className="bg-surface-container border border-outline-variant rounded px-3 py-1.5 text-sm outline-none focus:border-primary text-on-surface w-64"
                placeholder="Enter value..."
              />
              <button 
                onClick={handleGo}
                className="px-4 py-1.5 bg-surface-container-high border border-outline-variant rounded text-sm font-bold hover:bg-outline-variant/30 transition-colors text-on-surface"
              >
                Go
              </button>
            </div>
          </div>

          {/* Results Area */}
          <div>
            <h3 className="text-sm font-bold text-on-surface mb-3">Results</h3>
            <div className="border border-outline-variant rounded-lg overflow-hidden bg-surface-container-lowest">
              <table className="w-full text-left border-collapse text-sm">
                <thead className="bg-surface-container-low border-b border-outline-variant">
                  <tr>
                    <th className="p-3 font-semibold text-center w-16">Select</th>
                    <th className="p-3 font-semibold text-center w-24">Quick Select</th>
                    {columns.map(col => (
                      <th key={col.key} className="p-3 font-semibold" style={{ width: col.width }}>
                        {col.header}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {filteredData.length === 0 ? (
                    <tr>
                      <td colSpan={columns.length + 2} className="p-8 text-center text-outline">
                        No results found.
                      </td>
                    </tr>
                  ) : (
                    filteredData.map((row, idx) => {
                      // We need a stable ID for the radio button. Assuming row.id or idx
                      const rowId = row.id || row.partner_id || String(idx);
                      const isSelected = selectedRowId === rowId;
                      return (
                        <tr 
                          key={rowId} 
                          className={`border-b border-outline-variant/30 hover:bg-primary/5 transition-colors cursor-pointer ${isSelected ? 'bg-primary/10' : ''}`}
                          onClick={() => setSelectedRowId(rowId)}
                          onDoubleClick={() => onSelect(row)}
                        >
                          <td className="p-3 text-center">
                            <input 
                              type="radio" 
                              name="lov_select" 
                              checked={isSelected}
                              onChange={() => setSelectedRowId(rowId)}
                              onClick={(e) => e.stopPropagation()}
                              className="accent-primary cursor-pointer w-4 h-4"
                            />
                          </td>
                          <td className="p-3 text-center">
                            <button 
                              onClick={(e) => { e.stopPropagation(); onSelect(row); }}
                              className="p-1 text-outline hover:text-primary transition-colors flex items-center justify-center w-full"
                              title="Quick Select"
                            >
                              <span className="material-symbols-outlined !text-[18px]">check_box</span>
                            </button>
                          </td>
                          {columns.map(col => (
                            <td key={col.key} className="p-3">
                              {col.render ? col.render(row) : row[col.key]}
                            </td>
                          ))}
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
          <div className="mt-4">
            <a href="#" className="text-xs text-primary hover:underline">About this Page</a>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-outline-variant bg-surface-container-low rounded-b-xl flex justify-end gap-3">
          <button 
            onClick={onClose}
            className="px-5 py-2 text-sm font-bold border border-outline-variant rounded-lg hover:bg-outline-variant/30 text-on-surface transition-colors"
          >
            Cancel
          </button>
          <button 
            onClick={() => {
              if (selectedRowId) {
                const row = filteredData.find((r, i) => (r.id || r.partner_id || String(i)) === selectedRowId);
                if (row) onSelect(row);
              }
            }}
            disabled={!selectedRowId}
            className="px-5 py-2 text-sm font-bold bg-primary text-primary-foreground rounded-lg hover:brightness-110 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            Select
          </button>
        </div>
      </div>
    </div>,
    document.body
  );
}
