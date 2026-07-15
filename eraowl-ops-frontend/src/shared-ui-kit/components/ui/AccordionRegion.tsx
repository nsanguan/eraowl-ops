import React, { useState } from 'react';

export interface AccordionItem {
  id: string;
  title: string;
  content: React.ReactNode;
  icon?: string;
  badge?: string;
}

export interface AccordionRegionProps {
  items: AccordionItem[];
  defaultExpandedIds?: string[];
  allowMultiple?: boolean;
  className?: string;
}

export function AccordionRegion({
  items,
  defaultExpandedIds = [],
  allowMultiple = true,
  className = ''
}: AccordionRegionProps) {
  const [expanded, setExpanded] = useState<Set<string>>(new Set(defaultExpandedIds));

  const togglePanel = (id: string) => {
    setExpanded(prev => {
      const next = new Set(allowMultiple ? prev : []);
      if (prev.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  return (
    <div className={`flex flex-col gap-2 ${className}`}>
      {items.map((item) => {
        const isExpanded = expanded.has(item.id);
        
        return (
          <div key={item.id} className="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden">
            <button
              type="button"
              onClick={() => togglePanel(item.id)}
              className="w-full px-4 py-3 flex items-center justify-between bg-surface-container-low hover:bg-surface-container transition-colors text-left select-none focus:outline-none focus-visible:ring-2 focus-visible:ring-primary/50"
            >
              <div className="flex items-center gap-3">
                {item.icon && (
                  <span className="material-symbols-outlined !text-[20px] text-outline">
                    {item.icon}
                  </span>
                )}
                <span className="font-bold text-on-surface">{item.title}</span>
                {item.badge && (
                  <span className="px-2 py-0.5 rounded-full bg-primary/10 text-primary text-[10px] font-bold uppercase tracking-wider">
                    {item.badge}
                  </span>
                )}
              </div>
              <span className={`material-symbols-outlined !text-[20px] text-outline transition-transform duration-300 ${isExpanded ? 'rotate-180' : ''}`}>
                expand_more
              </span>
            </button>
            
            <div 
              className={`transition-all duration-300 ease-in-out overflow-hidden`}
              style={{ maxHeight: isExpanded ? '1000px' : '0', opacity: isExpanded ? 1 : 0 }}
            >
              <div className="p-4 border-t border-outline-variant">
                {item.content}
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
