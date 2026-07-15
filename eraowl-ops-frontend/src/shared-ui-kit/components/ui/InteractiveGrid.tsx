import { type ReactNode, useState, useRef, useEffect, useCallback } from 'react';

export interface GridColumn<T> {
  key: string;
  header: string;
  render?: (row: T) => ReactNode;
  className?: string;
  width?: string;
}

interface InteractiveGridProps<T> {
  title?: string;
  columns: GridColumn<T>[];
  data: T[];
  searchable?: boolean;
  onSearch?: (query: string) => void;
  customSearch?: ReactNode;
  onAddRow?: () => void;
  onEdit?: (row: T) => void;
  onDelete?: (row: T) => void;
  onSave?: () => void;
  onReset?: () => void;
  addLabel?: string;
  loading?: boolean;
  selectedIds?: Set<string>;
  onSelect?: (id: string) => void;
  onSelectAll?: () => void;
  idKey?: string;
  saving?: boolean;
  onEditToolbar?: () => void;
  onRowClick?: (row: T) => void;
  tableHeight?: string;
}

function useClickOutside(ref: React.RefObject<HTMLElement | null>, handler: () => void) {
  useEffect(() => {
    function onPointerDown(e: PointerEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        handler();
      }
    }
    document.addEventListener('pointerdown', onPointerDown);
    return () => document.removeEventListener('pointerdown', onPointerDown);
  }, [ref, handler]);
}

export function InteractiveGrid<T extends Record<string, any>>({
  title,
  columns,
  data,
  searchable,
  onSearch,
  customSearch,
  onAddRow,
  onEdit,
  onDelete,
  onSave,
  onReset,
  addLabel = 'Add Row',
  loading,
  selectedIds,
  onSelect,
  onSelectAll,
  idKey = 'id',
  saving,
  onEditToolbar,
  onRowClick,
  tableHeight,
}: InteractiveGridProps<T>) {
  const [searchQuery, setSearchQuery] = useState('');
  const [singleRowView, setSingleRowView] = useState<T | null>(null);
  const [colWidths, setColWidths] = useState<Record<string, number>>({});
  const thRefs = useRef<Record<string, HTMLTableCellElement | null>>({});
  const [openActions, setOpenActions] = useState(false);
  const actionsRef = useRef<HTMLDivElement>(null);
  const [rowMenuId, setRowMenuId] = useState<string | null>(null);
  const [rowMenuPos, setRowMenuPos] = useState<{ top: number; left: number }>({ top: 0, left: 0 });
  const rowMenuRef = useRef<HTMLDivElement>(null);

  const closeActions = useCallback(() => setOpenActions(false), []);
  const closeRowMenu = useCallback(() => { setRowMenuId(null); }, []);
  useClickOutside(actionsRef, closeActions);
  useClickOutside(rowMenuRef, closeRowMenu);

  const handleResizeStart = (e: React.MouseEvent, colKey: string) => {
    e.preventDefault();
    const startX = e.clientX;
    const th = thRefs.current[colKey];
    if (!th) return;
    const startWidth = th.getBoundingClientRect().width;

    const onMouseMove = (moveEvent: MouseEvent) => {
      moveEvent.preventDefault();
      const deltaX = moveEvent.clientX - startX;
      setColWidths(prev => ({
        ...prev,
        [colKey]: Math.max(50, startWidth + deltaX)
      }));
    };

    const onMouseUp = () => {
      document.removeEventListener('mousemove', onMouseMove);
      document.removeEventListener('mouseup', onMouseUp);
      document.body.style.cursor = '';
    };

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
    document.body.style.cursor = 'col-resize';
  };

  const [internalSelected, setInternalSelected] = useState<Set<string>>(new Set());
  const actualSelectedIds = selectedIds ?? internalSelected;
  const allSelected = data.length > 0 && actualSelectedIds.size === data.length;

  const handleSelect = (id: string) => {
    if (onSelect) {
      onSelect(id);
    } else {
      const newSet = new Set(internalSelected);
      if (newSet.has(id)) newSet.delete(id);
      else newSet.add(id);
      setInternalSelected(newSet);
    }
  };

  const handleSelectAll = () => {
    if (onSelectAll) {
      onSelectAll();
    } else {
      if (internalSelected.size === data.length && data.length > 0) {
        setInternalSelected(new Set());
      } else {
        setInternalSelected(new Set(data.map((r, i) => r[idKey] ?? String(i))));
      }
    }
  };

  return (
    <div className="border border-outline-variant rounded bg-surface-container-lowest flex flex-col overflow-hidden mb-6 shadow-sm eods-ig" style={{ fontFamily: 'var(--font-sans, Inter, sans-serif)' }}>
      {title && (
        <div className="px-4 py-2 border-b border-outline-variant/50 bg-surface-container-low/50">
          <h2 className="text-[13px] font-bold text-slate-900! dark:text-white! tracking-tight">{title}</h2>
        </div>
      )}

      {/* ── TOOLBAR ── */}
      <div className="flex items-center justify-between pl-24 pr-3 py-2 border-b border-outline-variant/60 bg-surface-container-low/30 overflow-visible flex-wrap gap-y-2">
        <div className="flex items-center gap-3 min-w-max">
          {customSearch ? (
            customSearch
          ) : searchable ? (
            <div className="flex items-center bg-surface-container-lowest border border-outline-variant rounded px-2 py-1 gap-1.5 focus-within:border-primary focus-within:ring-1 focus-within:ring-primary w-64">
              <span className="material-symbols-outlined !text-[16px] text-outline">search</span>
              <input type="text" value={searchQuery}
                onChange={e => { setSearchQuery(e.target.value); onSearch?.(e.target.value); }}
                placeholder="Search: All Text Columns"
                className="bg-transparent border-none outline-none text-[12px] text-on-surface w-full placeholder:text-outline/50" />
            </div>
          ) : null}

          {(searchable || customSearch) && <div className="h-5 w-px bg-outline-variant/50" />}

          {/* Views Toggle */}
          <div className="flex items-center bg-surface-container-lowest border border-outline-variant rounded overflow-hidden">
            <button className="px-2.5 py-1 bg-surface-container-high hover:bg-surface-container-highest transition-colors flex items-center justify-center">
              <span className="material-symbols-outlined !text-[16px] text-on-surface">grid_on</span>
            </button>
            <div className="w-px h-full bg-outline-variant" />
            <button className="px-2.5 py-1 hover:bg-surface-container-highest transition-colors flex items-center justify-center text-outline">
              <span className="material-symbols-outlined !text-[16px]">bar_chart</span>
            </button>
          </div>

          {/* Actions Dropdown */}
          <div className="relative" ref={actionsRef}>
            <button onClick={() => setOpenActions(prev => !prev)}
              className="flex items-center gap-1 px-3 py-1 bg-surface-container-lowest border border-outline-variant rounded hover:bg-surface-container-highest transition-colors text-[12px] font-semibold text-on-surface">
              Actions <span className="material-symbols-outlined !text-[16px]" style={{ transform: openActions ? 'rotate(180deg)' : 'none', transition: 'transform 150ms' }}>expand_more</span>
            </button>
            {openActions && (
              <div className="absolute left-0 top-full mt-1 bg-surface-container-highest border border-outline-variant shadow-lg rounded flex flex-col py-1 z-50 min-w-[200px]">
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">view_column</span>Columns</div>
                </button>
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">filter_alt</span>Filter</div>
                </button>
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">dataset</span>Data</div>
                  <span className="material-symbols-outlined !text-[16px] text-outline">chevron_right</span>
                </button>
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">format_paint</span>Format</div>
                  <span className="material-symbols-outlined !text-[16px] text-outline">chevron_right</span>
                </button>
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">select_all</span>Selection</div>
                  <span className="material-symbols-outlined !text-[16px] text-outline">chevron_right</span>
                </button>
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">bar_chart</span>Chart</div>
                </button>
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">article</span>Report</div>
                  <span className="material-symbols-outlined !text-[16px] text-outline">chevron_right</span>
                </button>
                <div className="h-px bg-outline-variant/50 my-1 mx-2" />
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">download</span>Download</div>
                </button>
                <div className="h-px bg-outline-variant/50 my-1 mx-2" />
                <button className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center justify-between w-full">
                  <div className="flex items-center gap-2"><span className="material-symbols-outlined !text-[16px] text-outline">help</span>Help</div>
                </button>
              </div>
            )}
          </div>

          <div className="h-5 w-px bg-outline-variant/50" />

          <div className="flex items-center gap-1.5">
            {onEditToolbar && (
              <button onClick={onEditToolbar} className="px-3 py-1 bg-surface-container-lowest border border-outline-variant rounded hover:bg-surface-container-highest transition-colors text-[12px] font-semibold text-on-surface disabled:opacity-50">Edit</button>
            )}
            {onSave && (
              <button onClick={onSave} disabled={saving}
                className="px-4 py-1 bg-on-surface text-surface border border-transparent rounded hover:bg-on-surface/90 transition-colors text-[12px] font-bold disabled:opacity-50 flex items-center gap-1">
                {saving ? 'Saving...' : 'Save'}
              </button>
            )}
            {onAddRow && (
              <button onClick={onAddRow}
                className="px-3 py-1 bg-surface-container-lowest border border-outline-variant rounded hover:bg-surface-container-highest transition-colors text-[12px] font-semibold text-on-surface">
                {addLabel}
              </button>
            )}
          </div>
        </div>

        <div className="pl-3">
          {onReset && (
            <button onClick={onReset}
              className="flex items-center gap-1 px-3 py-1 bg-surface-container-lowest border border-outline-variant rounded hover:bg-surface-container-highest transition-colors text-[12px] font-semibold text-outline">
              <span className="material-symbols-outlined !text-[16px] text-outline">restart_alt</span> Reset
            </button>
          )}
        </div>
      </div>

      {/* ── TABLE CONTAINER ── */}
      <div className="overflow-auto bg-surface-container-lowest flex-1 custom-scrollbar" style={{ maxHeight: tableHeight || '500px' }}>
        <table className="min-w-full text-left border-collapse" style={{ minWidth: columns.length > 6 ? `${columns.length * 130}px` : undefined }}>
          <thead className="sticky top-0 z-20 shadow-[0_1px_0_var(--tw-shadow-color)] shadow-outline-variant/50">
            <tr className="bg-surface-container-high/90 backdrop-blur-sm">
              <th className="w-10 px-3 py-2 text-center border-r border-outline-variant/30 bg-surface-container-high">
                <input type="checkbox" checked={allSelected} onChange={handleSelectAll}
                  className="rounded border-outline-variant accent-primary w-3.5 h-3.5 cursor-pointer" />
              </th>
              <th className="w-10 px-2 py-2 text-center border-r border-outline-variant/30 text-outline bg-surface-container-high">
                <span className="material-symbols-outlined !text-[16px]">menu</span>
              </th>
              {columns.map(col => {
                const computedWidth = colWidths[col.key] ? `${colWidths[col.key]}px` : col.width;
                return (
                  <th key={col.key} ref={el => { thRefs.current[col.key] = el; }}
                    className={`px-4 py-2.5 text-[11px] text-on-surface tracking-tight border-r border-outline-variant/30 last:border-r-0 relative group ${col.className ?? ''} bg-surface-container-high`}
                    style={computedWidth ? { width: computedWidth, minWidth: computedWidth, maxWidth: computedWidth } : undefined}>
                    <div className="truncate w-full">{col.header}</div>
                    <div className="absolute right-0 top-0 bottom-0 w-1.5 cursor-col-resize hover:bg-primary/50 opacity-0 group-hover:opacity-100 z-10 transition-colors"
                      onMouseDown={(e) => handleResizeStart(e, col.key)} />
                  </th>
                );
              })}
            </tr>
          </thead>
          <tbody className="divide-y divide-outline-variant/30">
            {loading ? (
              <tr><td colSpan={columns.length + 2} className="text-center py-12 text-outline text-sm">Loading...</td></tr>
            ) : data.length === 0 ? (
              <tr><td colSpan={columns.length + 2} className="text-center py-12 text-outline text-sm">No records found.</td></tr>
            ) : data.map((row, idx) => {
              const rid = row[idKey] ?? idx;
              return (
                <tr key={rid}
                  onClick={onRowClick ? () => onRowClick(row) : undefined}
                  className={`transition-colors ${onRowClick ? 'cursor-pointer hover:bg-primary/10' : 'cursor-default hover:bg-primary/5'}`}>
                  <td className="px-3 py-2 text-center border-r border-outline-variant/20" onClick={e => e.stopPropagation()}>
                    <input type="checkbox" checked={actualSelectedIds.has(rid)}
                      onChange={() => handleSelect(rid)}
                      className="rounded border-outline-variant accent-primary w-3.5 h-3.5 cursor-pointer" />
                  </td>
                  <td className="px-2 py-2 text-center border-r border-outline-variant/20 relative" onClick={e => { e.stopPropagation(); const btn = (e.currentTarget as HTMLElement).querySelector('button'); if (btn) { const r = btn.getBoundingClientRect(); setRowMenuPos({ top: r.top, left: r.right + 4 }); } setRowMenuId(prev => prev === rid ? null : rid); }}>
                    <button className="p-1 text-outline hover:text-on-surface rounded flex items-center justify-center w-full">
                      <span className="material-symbols-outlined !text-[16px]">more_vert</span>
                    </button>
                    {rowMenuId === rid && (
                      <div ref={rowMenuRef}
                        className="fixed bg-surface-container-highest border border-outline-variant shadow-lg rounded flex flex-col py-1 z-[60] min-w-[160px]"
                        style={{ left: rowMenuPos.left, top: rowMenuPos.top }}>
                        <button type="button" onClick={() => { setSingleRowView(row); setRowMenuId(null); }}
                          className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center gap-2 text-left w-full">
                          <span className="material-symbols-outlined !text-[16px]">visibility</span> View Details
                        </button>
                        {(onEdit || onDelete) && <div className="h-px bg-outline-variant/50 my-1 mx-2" />}
                        {onEdit && (
                          <button type="button" onClick={() => { onEdit(row); setRowMenuId(null); }}
                            className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center gap-2 text-left w-full">
                            <span className="material-symbols-outlined !text-[16px]">edit</span> Edit Row
                          </button>
                        )}
                        {onDelete && (
                          <button type="button" onClick={() => { onDelete(row); setRowMenuId(null); }}
                            className="px-3 py-1.5 text-[12px] text-error hover:bg-error/10 transition-colors flex items-center gap-2 text-left w-full">
                            <span className="material-symbols-outlined !text-[16px]">delete</span> Delete Row
                          </button>
                        )}
                      </div>
                    )}
                  </td>
                  {columns.map(col => {
                    const computedWidth = colWidths[col.key] ? `${colWidths[col.key]}px` : col.width;
                    return (
                      <td key={col.key}
                        className={`px-4 py-2 text-[12px] text-on-surface border-r border-outline-variant/20 last:border-r-0 overflow-hidden ${col.className ?? ''}`}
                        style={computedWidth ? { width: computedWidth, minWidth: computedWidth, maxWidth: computedWidth } : undefined}>
                        {col.render ? col.render(row) : String(row[col.key] ?? '\u2014')}
                      </td>
                    );
                  })}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* ── FOOTER ── */}
      <div className="flex items-center justify-between pl-24 pr-4 py-2 border-t border-outline-variant bg-surface-container-lowest text-[11px] text-outline">
        <div>{actualSelectedIds.size ? `${actualSelectedIds.size} rows selected` : ''}</div>
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1">
            <button className="p-1 hover:bg-surface-container-high rounded flex items-center justify-center disabled:opacity-30" disabled>
              <span className="material-symbols-outlined !text-[16px]">first_page</span>
            </button>
            <button className="p-1 hover:bg-surface-container-high rounded flex items-center justify-center disabled:opacity-30" disabled>
              <span className="material-symbols-outlined !text-[16px]">chevron_left</span>
            </button>
            <span className="px-2 py-1 bg-surface-container-high text-on-surface font-semibold rounded">1</span>
            <button className="p-1 hover:bg-surface-container-high rounded flex items-center justify-center disabled:opacity-30" disabled>
              <span className="material-symbols-outlined !text-[16px]">chevron_right</span>
            </button>
            <button className="p-1 hover:bg-surface-container-high rounded flex items-center justify-center disabled:opacity-30" disabled>
              <span className="material-symbols-outlined !text-[16px]">last_page</span>
            </button>
          </div>
          <span>1 - {Math.min(data.length, 15)} of {data.length}</span>
        </div>
      </div>

      {/* ── SINGLE ROW VIEW MODAL ── */}
      {singleRowView && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/50 p-4" onClick={() => setSingleRowView(null)}>
          <div className="bg-surface-container-lowest border border-outline-variant rounded-lg shadow-xl flex flex-col w-full max-w-3xl max-h-[90vh] overflow-hidden" style={{ fontFamily: 'var(--font-sans, Inter, sans-serif)' }} onClick={e => e.stopPropagation()}>
            <div className="flex items-center justify-between px-6 py-4 border-b border-outline-variant bg-surface-container-low shrink-0">
              <h2 className="text-[14px] font-bold text-slate-900! dark:text-white! tracking-tight">Row Details</h2>
              <button onClick={() => setSingleRowView(null)} className="p-1 hover:bg-surface-container-highest rounded-full text-outline transition-colors flex items-center justify-center">
                <span className="material-symbols-outlined !text-[18px]">close</span>
              </button>
            </div>
            <div className="p-6 overflow-y-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 bg-surface-container-lowest custom-scrollbar flex-1">
              {columns.map(col => {
                const val = col.render ? col.render(singleRowView) : singleRowView[col.key];
                return (
                  <div key={col.key} className="flex flex-col gap-1.5">
                    <label className="text-[11px] font-bold text-outline tracking-tight uppercase">{col.header}</label>
                    <div className="text-[12px] font-medium text-on-surface bg-surface-container-low/30 px-3 py-2.5 rounded border border-outline-variant/30 min-h-[38px] flex items-center overflow-hidden break-words whitespace-normal">
                      {val !== undefined && val !== null && val !== '' ? val : '\u2014'}
                    </div>
                  </div>
                );
              })}
            </div>
            <div className="px-4 py-3 border-t border-outline-variant bg-surface-container-low/50 flex justify-end">
              <button onClick={() => setSingleRowView(null)} className="px-4 py-1.5 bg-surface-container-highest border border-outline-variant rounded hover:bg-outline-variant/30 transition-colors text-[12px] font-semibold text-on-surface">Close</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
