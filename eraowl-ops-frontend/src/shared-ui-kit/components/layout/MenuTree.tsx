import { useState } from 'react';

export interface MenuTreeNode {
  object_id: string;
  parent_object_id: string | null;
  object_code: string;
  object_name: string;
  object_type: string;
  module: string | null;
  route: string | null;
  icon: string | null;
  sort_order: number | null;
  children: MenuTreeNode[];
}

interface MenuTreeProps {
  nodes: MenuTreeNode[];
  currentPath: string;
  onNavigate: (href: string) => void;
  mapIcon: (iconName: string) => string;
  level?: number;
}

export function MenuTree({ nodes, currentPath, onNavigate, mapIcon, level = 0 }: MenuTreeProps) {
  if (!nodes || nodes.length === 0) return null;

  return (
    <div className="flex flex-col w-full">
      {nodes.map((node) => (
        <MenuTreeNodeItem
          key={node.object_id}
          node={node}
          currentPath={currentPath}
          onNavigate={onNavigate}
          mapIcon={mapIcon}
          level={level}
        />
      ))}
    </div>
  );
}

interface MenuTreeNodeItemProps {
  node: MenuTreeNode;
  currentPath: string;
  onNavigate: (href: string) => void;
  mapIcon: (iconName: string) => string;
  level: number;
}

function MenuTreeNodeItem({ node, currentPath, onNavigate, mapIcon, level }: MenuTreeNodeItemProps) {
  const hasChildren = node.children && node.children.length > 0;
  
  // Auto-expand if the current path matches this node or any of its descendants
  const isDescendantActive = (n: MenuTreeNode, path: string): boolean => {
    if (n.route && (path === n.route || path.startsWith(n.route))) return true;
    return n.children.some(child => isDescendantActive(child, path));
  };
  
  const isActive = node.route ? (currentPath === node.route || currentPath.startsWith(node.route)) : false;
  const descendantActive = hasChildren ? isDescendantActive(node, currentPath) : false;
  
  const [isExpanded, setIsExpanded] = useState<boolean>(descendantActive);

  const handleClick = () => {
    if (hasChildren) {
      setIsExpanded(!isExpanded);
      // Optional: if a folder also has a route, we could navigate, but usually folders just expand
      if (node.route) {
        onNavigate(node.route);
      }
    } else if (node.route) {
      onNavigate(node.route);
    }
  };

  const paddingLeft = `${(level * 12) + 16}px`;

  return (
    <div className="flex flex-col">
      <a
        className={`flex items-center gap-3 py-2 cursor-pointer transition-colors ${
          isActive
            ? 'border-l-4 border-primary bg-surface-container-high text-primary'
            : 'text-on-surface-variant hover:bg-surface-container-low border-l-4 border-transparent'
        } ${level === 0 ? 'mt-1' : ''}`}
        style={{ paddingLeft }}
        onClick={handleClick}
      >
        <div className="flex items-center justify-center w-5">
          {hasChildren ? (
            <span
              className={`material-symbols-outlined text-[16px] transition-transform duration-200 ${
                isExpanded ? 'rotate-90' : ''
              }`}
              style={{ fontFamily: "'Material Symbols Outlined'" }}
            >
              chevron_right
            </span>
          ) : (
            <span className="w-[16px]"></span> // Empty spacer for leaf nodes to align with folders
          )}
        </div>
        
        {node.icon && (
          <span className="material-symbols-outlined !text-[18px]" style={{ fontFamily: "'Material Symbols Outlined'" }}>
            {mapIcon(node.icon)}
          </span>
        )}
        
        <span
          className={`${level === 0 ? 'text-[11.5px] font-semibold' : 'text-[11px]'} flex-1`}
          style={{ fontFamily: 'var(--font-sans, Inter, sans-serif)', fontVariantLigatures: 'normal' }}
        >
          {node.object_name}
        </span>
      </a>

      {hasChildren && isExpanded && (
        <div className="flex flex-col">
          <MenuTree
            nodes={node.children}
            currentPath={currentPath}
            onNavigate={onNavigate}
            mapIcon={mapIcon}
            level={level + 1}
          />
        </div>
      )}
    </div>
  );
}
