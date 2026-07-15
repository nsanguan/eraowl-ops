import React, { useState, useCallback, useMemo } from 'react';

export interface TreeGridColumn<T> {
  id: string;
  header: string;
  width?: string;
  align?: 'left' | 'center' | 'right';
  accessor?: (row: T) => React.ReactNode;
  render?: (row: T) => React.ReactNode;
}

export interface TreeGridNode<T> {
  id: string;
  data: T;
  children?: TreeGridNode<T>[];
}

export interface TreeGridProps<T> {
  data: TreeGridNode<T>[];
  columns: TreeGridColumn<T>[];
  nodeLabelAccessor: (row: T) => React.ReactNode;
  nodeIconAccessor?: (row: T) => string;
  nodeDescriptionAccessor?: (row: T) => React.ReactNode;
  
  isLoading?: boolean;
  emptyMessage?: string;
  
  onEdit?: (row: T) => void;
  canEdit?: (row: T) => boolean;
  
  onDelete?: (row: T) => void;
  canDelete?: (row: T) => boolean;
  
  onAddChild?: (row: T) => void;
  canAddChild?: (row: T) => boolean;
  
  // Custom actions
  actions?: {
    label: string;
    icon: string;
    onClick: (row: T) => void;
    show?: (row: T) => boolean;
    className?: string;
  }[];
  
  // New features
  enableSelection?: boolean;
  onSelectionChange?: (selectedIds: Set<string>) => void;
  toolbarActions?: React.ReactNode;
}

function TreeGridRow<T>({ 
  node, depth, expanded, onToggle, columns, 
  nodeLabelAccessor, nodeIconAccessor, nodeDescriptionAccessor,
  onEdit, canEdit, onDelete, canDelete, onAddChild, canAddChild, actions,
  enableSelection, selectedIds, onSelect
}: {
  node: TreeGridNode<T>; depth: number; expanded: Set<string>; 
  onToggle: (id: string) => void;
  columns: TreeGridColumn<T>[];
  nodeLabelAccessor: (row: T) => React.ReactNode;
  nodeIconAccessor?: (row: T) => string;
  nodeDescriptionAccessor?: (row: T) => React.ReactNode;
  onEdit?: (row: T) => void;
  canEdit?: (row: T) => boolean;
  onDelete?: (row: T) => void;
  canDelete?: (row: T) => boolean;
  onAddChild?: (row: T) => void;
  canAddChild?: (row: T) => boolean;
  actions?: TreeGridProps<T>['actions'];
  enableSelection?: boolean;
  selectedIds: Set<string>;
  onSelect: (id: string, selected: boolean) => void;
}) {
  const isExpanded = expanded.has(node.id);
  const hasChildren = node.children && node.children.length > 0;
  
  const showEdit = onEdit && (!canEdit || canEdit(node.data));
  const showDelete = onDelete && (!canDelete || canDelete(node.data));
  const showAdd = onAddChild && (!canAddChild || canAddChild(node.data));
  const hasAnyAction = showEdit || showDelete || showAdd || (actions && actions.some(a => !a.show || a.show(node.data)));

  const iconName = nodeIconAccessor ? nodeIconAccessor(node.data) : (hasChildren ? 'account_tree' : 'integration_instructions');
  const isSelected = selectedIds.has(node.id);

  return (
    <>
      <tr className={`border-t border-outline-variant/30 hover:bg-surface-container-low transition-colors group ${isSelected ? 'bg-primary/5' : ''}`}>
        
        {/* Selection Checkbox */}
        {enableSelection && (
          <td className="w-10 px-3 py-2 text-center relative group/handle border-r border-outline-variant/30">
            <div className="absolute left-1 top-1/2 -translate-y-1/2 opacity-0 group-hover/handle:opacity-100 cursor-grab text-outline hover:text-primary transition-all">
              <span className="material-symbols-outlined !text-[14px]">drag_indicator</span>
            </div>
            <input 
              type="checkbox"
              checked={isSelected}
              onChange={(e) => onSelect(node.id, e.target.checked)}
              className="w-3 h-3 appearance-none border border-outline rounded-[2px] checked:bg-primary checked:border-primary checked:after:content-[''] checked:after:absolute checked:after:left-[3px] checked:after:top-[1px] checked:after:w-[4px] checked:after:h-[8px] checked:after:border-r-2 checked:after:border-b-2 checked:after:border-surface checked:after:rotate-45 relative cursor-pointer"
            />
          </td>
        )}

        {/* Special Tree Column */}
        <td className="px-4 py-2">
          <div className="flex items-center" style={{ paddingLeft: `${depth * 24}px` }}>
            {hasChildren ? (
              <button onClick={() => onToggle(node.id)} className="w-6 h-6 flex items-center justify-center text-outline hover:text-primary transition-colors hover:bg-primary/10 rounded mr-1">
                <span className="material-symbols-outlined !text-[16px]">{isExpanded ? 'expand_more' : 'chevron_right'}</span>
              </button>
            ) : (
              <div className="w-6 h-6 mr-1" />
            )}
            <span className="material-symbols-outlined !text-[14px] text-outline mr-2">
              {iconName}
            </span>
            <div className="flex flex-col">
              <span className="text-[12px] text-primary">{nodeLabelAccessor(node.data)}</span>
              {nodeDescriptionAccessor && (
                <span className="text-[11px] text-outline truncate max-w-[200px]">{nodeDescriptionAccessor(node.data)}</span>
              )}
            </div>
          </div>
        </td>
        
        {/* Custom Columns */}
        {columns.map(col => (
          <td key={col.id} className={`px-4 py-2 text-[12px] text-on-surface ${col.align === 'right' ? 'text-right' : col.align === 'center' ? 'text-center' : 'text-left'}`}>
            {col.render ? col.render(node.data) : col.accessor ? col.accessor(node.data) : (node.data as any)[col.id]}
          </td>
        ))}

        {/* Actions Column */}
        {(onEdit || onDelete || onAddChild || actions) && (
          <td className="px-2 py-2 text-center w-12">
            {hasAnyAction && (
              <div className="relative group/menu inline-block">
                <button className="w-6 h-6 rounded hover:bg-surface-container-high text-outline flex items-center justify-center">
                  <span className="material-symbols-outlined !text-[16px]">more_vert</span>
                </button>
                {/* pt-1 wrapper ensures hover doesn't drop when moving mouse down */}
                <div className="absolute right-0 top-full pt-1 opacity-0 group-hover/menu:opacity-100 pointer-events-none group-hover/menu:pointer-events-auto transition-opacity z-50 min-w-[150px] text-left">
                  <div className="bg-surface-container-highest border border-outline-variant shadow-lg rounded flex flex-col py-1">
                    {showAdd && (
                      <button onClick={() => onAddChild(node.data)} className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center gap-2">
                        <span className="material-symbols-outlined !text-[16px] text-outline">add</span>
                        Add Child
                      </button>
                    )}
                    {showEdit && (
                      <button onClick={() => onEdit(node.data)} className="px-3 py-1.5 text-[12px] text-on-surface hover:bg-surface-container-low transition-colors flex items-center gap-2">
                        <span className="material-symbols-outlined !text-[16px] text-outline">edit</span>
                        Edit
                      </button>
                    )}
                    {actions?.map(action => {
                      if (action.show && !action.show(node.data)) return null;
                      return (
                        <button key={action.label} onClick={() => action.onClick(node.data)} className={`px-3 py-1.5 text-[12px] hover:bg-surface-container-low transition-colors flex items-center gap-2 ${action.className || 'text-on-surface'}`}>
                          <span className="material-symbols-outlined !text-[16px] text-outline">{action.icon}</span>
                          {action.label}
                        </button>
                      )
                    })}
                    {showDelete && (
                      <>
                        {(showEdit || showAdd || (actions && actions.length > 0)) && <div className="h-px bg-outline-variant/50 my-1 mx-2" />}
                        <button onClick={() => onDelete(node.data)} className="px-3 py-1.5 text-[12px] text-error hover:bg-error/10 transition-colors flex items-center gap-2">
                          <span className="material-symbols-outlined !text-[16px]">delete</span>
                          Delete
                        </button>
                      </>
                    )}
                  </div>
                </div>
              </div>
            )}
          </td>
        )}
      </tr>
      {isExpanded && hasChildren && node.children!.map(child => (
        <TreeGridRow 
          key={child.id} node={child} depth={depth + 1} expanded={expanded} onToggle={onToggle} 
          columns={columns} nodeLabelAccessor={nodeLabelAccessor} nodeIconAccessor={nodeIconAccessor} nodeDescriptionAccessor={nodeDescriptionAccessor}
          onEdit={onEdit} canEdit={canEdit} onDelete={onDelete} canDelete={canDelete} onAddChild={onAddChild} canAddChild={canAddChild} actions={actions}
          enableSelection={enableSelection} selectedIds={selectedIds} onSelect={onSelect}
        />
      ))}
    </>
  );
}

export function TreeGrid<T>({ 
  data, columns, nodeLabelAccessor, nodeIconAccessor, nodeDescriptionAccessor,
  isLoading, emptyMessage = 'No data available.',
  onEdit, canEdit, onDelete, canDelete, onAddChild, canAddChild, actions,
  enableSelection, onSelectionChange, toolbarActions
}: TreeGridProps<T>) {
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [searchQuery, setSearchQuery] = useState('');

  // Filtering Logic
  const filteredData = useMemo(() => {
    if (!searchQuery) return data;
    const lowerQuery = searchQuery.toLowerCase();
    
    // Recursive filter: keep node if it matches, or if any children match
    const filterNodes = (nodes: TreeGridNode<T>[]): TreeGridNode<T>[] => {
      const result: TreeGridNode<T>[] = [];
      for (const node of nodes) {
        const matchesLabel = String(nodeLabelAccessor(node.data) || '').toLowerCase().includes(lowerQuery);
        const matchesDesc = nodeDescriptionAccessor ? String(nodeDescriptionAccessor(node.data) || '').toLowerCase().includes(lowerQuery) : false;
        
        let filteredChildren: TreeGridNode<T>[] = [];
        if (node.children) {
          filteredChildren = filterNodes(node.children);
        }
        
        if (matchesLabel || matchesDesc || filteredChildren.length > 0) {
          result.push({
            ...node,
            children: filteredChildren.length > 0 ? filteredChildren : node.children
          });
        }
      }
      return result;
    };
    
    return filterNodes(data);
  }, [data, searchQuery, nodeLabelAccessor, nodeDescriptionAccessor]);

  // When filtering, we automatically expand all nodes that match
  const currentExpanded = useMemo(() => {
    if (!searchQuery) return expanded;
    const allIds = new Set<string>();
    const traverse = (nodes: TreeGridNode<T>[]) => {
      nodes.forEach(n => {
        if (n.children && n.children.length > 0) {
          allIds.add(n.id);
          traverse(n.children);
        }
      });
    };
    traverse(filteredData);
    return allIds;
  }, [expanded, searchQuery, filteredData]);

  const toggleExpand = useCallback((id: string) => {
    if (searchQuery) return; // Prevent collapse while searching
    setExpanded(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  }, [searchQuery]);

  const expandAll = useCallback(() => {
    const allIds = new Set<string>();
    const traverse = (nodes: TreeGridNode<T>[]) => {
      nodes.forEach(n => {
        if (n.children && n.children.length > 0) {
          allIds.add(n.id);
          traverse(n.children);
        }
      });
    };
    traverse(filteredData);
    setExpanded(allIds);
  }, [filteredData]);

  const collapseAll = useCallback(() => {
    setExpanded(new Set());
    setSearchQuery(''); // Also clears search
  }, []);

  const handleSelect = useCallback((id: string, selected: boolean) => {
    setSelectedIds(prev => {
      const next = new Set(prev);
      if (selected) next.add(id);
      else next.delete(id);
      onSelectionChange?.(next);
      return next;
    });
  }, [onSelectionChange]);

  const handleSelectAll = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.checked) {
      const allIds = new Set<string>();
      const traverse = (nodes: TreeGridNode<T>[]) => {
        nodes.forEach(n => {
          allIds.add(n.id);
          if (n.children) traverse(n.children);
        });
      };
      traverse(filteredData);
      setSelectedIds(allIds);
      onSelectionChange?.(allIds);
    } else {
      setSelectedIds(new Set());
      onSelectionChange?.(new Set());
    }
  };

  const hasActionsColumn = !!(onEdit || onDelete || onAddChild || actions);

  return (
    <div className="bg-surface-container-lowest border border-outline-variant rounded shadow-sm flex flex-col overflow-hidden max-h-[calc(100vh-200px)]">
      {/* Enhanced Toolbar */}
      <div className="flex items-center justify-between px-3 py-2 border-b border-outline-variant/60 bg-surface-container-low/30">
        
        <div className="flex items-center gap-3">
          <div className="relative">
            <span className="material-symbols-outlined absolute left-2 top-1/2 -translate-y-1/2 text-outline !text-[16px]">search</span>
            <input 
              type="text" 
              placeholder="Search Tree..." 
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              className="pl-8 pr-3 py-1 bg-surface-container-lowest border border-outline-variant rounded text-[12px] text-on-surface focus:outline-none focus:border-primary w-64 placeholder:text-outline/70 transition-colors"
            />
          </div>

          <div className="flex items-center gap-1">
            <button onClick={expandAll} className="px-2 py-1 bg-surface-container-lowest border border-outline-variant rounded hover:bg-surface-container-highest transition-colors flex items-center justify-center group/btn" title="Expand All">
              <span className="material-symbols-outlined !text-[16px] text-outline group-hover/btn:text-on-surface">unfold_more</span>
            </button>
            <button onClick={collapseAll} className="px-2 py-1 bg-surface-container-lowest border border-outline-variant rounded hover:bg-surface-container-highest transition-colors flex items-center justify-center group/btn" title="Collapse All">
              <span className="material-symbols-outlined !text-[16px] text-outline group-hover/btn:text-on-surface">unfold_less</span>
            </button>
          </div>

          <div className="flex items-center bg-surface-container-lowest border border-outline-variant rounded overflow-hidden">
            <button className="px-2.5 py-1 bg-surface-container-high hover:bg-surface-container-highest transition-colors flex items-center justify-center">
              <span className="material-symbols-outlined !text-[16px] text-on-surface">account_tree</span>
            </button>
            <div className="w-px h-full bg-outline-variant" />
            <button className="px-2.5 py-1 hover:bg-surface-container-highest transition-colors flex items-center justify-center text-outline">
              <span className="material-symbols-outlined !text-[16px]">bar_chart</span>
            </button>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {toolbarActions}
          <div className="text-[11px] text-outline font-semibold ml-2">
            {filteredData.length} Root Nodes {searchQuery && '(Filtered)'}
          </div>
        </div>
      </div>

      {/* TreeGrid */}
      <div className="overflow-auto flex-1 bg-surface-container-lowest">
        <table className="w-full text-left border-collapse">
          <thead className="sticky top-0 z-20 shadow-[0_1px_0_var(--tw-shadow-color)] shadow-outline-variant/50">
            <tr className="bg-surface-container-high/90 backdrop-blur-sm">
              
              {enableSelection && (
                <th className="w-10 px-3 py-2 text-center border-r border-outline-variant/30 bg-surface-container-high">
                  <input 
                    type="checkbox"
                    onChange={handleSelectAll}
                    checked={selectedIds.size > 0}
                    className="w-3 h-3 appearance-none border border-outline rounded-[2px] checked:bg-primary checked:border-primary checked:after:content-[''] checked:after:absolute checked:after:left-[3px] checked:after:top-[1px] checked:after:w-[4px] checked:after:h-[8px] checked:after:border-r-2 checked:after:border-b-2 checked:after:border-surface checked:after:rotate-45 relative cursor-pointer"
                  />
                </th>
              )}

              <th className="px-4 py-2.5 text-[11px] font-bold text-on-surface tracking-tight bg-surface-container-high w-[300px]">Node</th>
              {columns.map(col => (
                <th key={col.id} className={`px-4 py-2.5 text-[11px] font-bold text-on-surface tracking-tight bg-surface-container-high ${col.width ? `w-[${col.width}]` : ''} ${col.align === 'right' ? 'text-right' : col.align === 'center' ? 'text-center' : 'text-left'}`}>
                  {col.header}
                </th>
              ))}
              {hasActionsColumn && (
                <th className="w-12 px-2 py-2.5 bg-surface-container-high text-center"></th>
              )}
            </tr>
          </thead>
          <tbody className="divide-y divide-outline-variant/30">
            {isLoading ? (
              <tr><td colSpan={columns.length + (enableSelection ? 3 : 2)} className="text-center py-12 text-outline text-sm">Loading data...</td></tr>
            ) : filteredData.length === 0 ? (
              <tr><td colSpan={columns.length + (enableSelection ? 3 : 2)} className="text-center py-12 text-outline text-sm">{emptyMessage}</td></tr>
            ) : filteredData.map(node => (
              <TreeGridRow 
                key={node.id} 
                node={node} 
                depth={0} 
                expanded={currentExpanded} 
                onToggle={toggleExpand}
                columns={columns}
                nodeLabelAccessor={nodeLabelAccessor}
                nodeIconAccessor={nodeIconAccessor}
                nodeDescriptionAccessor={nodeDescriptionAccessor}
                onEdit={onEdit} canEdit={canEdit} 
                onDelete={onDelete} canDelete={canDelete} 
                onAddChild={onAddChild} canAddChild={canAddChild}
                actions={actions}
                enableSelection={enableSelection}
                selectedIds={selectedIds}
                onSelect={handleSelect}
              />
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
