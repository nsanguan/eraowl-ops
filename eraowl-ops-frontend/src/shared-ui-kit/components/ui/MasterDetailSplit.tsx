import React, { useState } from 'react';

export interface MasterDetailSplitProps {
  masterContent: React.ReactNode;
  detailContent: React.ReactNode;
  masterTitle?: string;
  detailTitle?: string;
  orientation?: 'horizontal' | 'vertical';
  masterWidth?: string; // For horizontal (e.g., '30%', '400px')
  masterHeight?: string; // For vertical (e.g., '40%', '300px')
  className?: string;
}

export function MasterDetailSplit({
  masterContent,
  detailContent,
  masterTitle = 'Master',
  detailTitle = 'Details',
  orientation = 'horizontal',
  masterWidth = '35%',
  masterHeight = '40%',
  className = ''
}: MasterDetailSplitProps) {
  
  if (orientation === 'vertical') {
    return (
      <div className={`flex flex-col gap-4 ${className}`}>
        <div 
          className="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden flex flex-col"
          style={{ height: masterHeight, minHeight: '200px' }}
        >
          {masterTitle && (
            <div className="bg-surface-container-low px-4 py-2 border-b border-outline-variant font-bold text-sm text-on-surface">
              {masterTitle}
            </div>
          )}
          <div className="flex-1 overflow-auto">
            {masterContent}
          </div>
        </div>
        
        <div className="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden flex flex-col flex-1 min-h-[300px]">
          {detailTitle && (
            <div className="bg-surface-container-low px-4 py-2 border-b border-outline-variant font-bold text-sm text-on-surface">
              {detailTitle}
            </div>
          )}
          <div className="flex-1 overflow-auto">
            {detailContent}
          </div>
        </div>
      </div>
    );
  }

  // Horizontal layout
  return (
    <div className={`flex flex-col md:flex-row gap-4 h-full ${className}`}>
      <div 
        className="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden flex flex-col shrink-0"
        style={{ width: '100%', maxWidth: '100%' }}
        // In responsive view, we let it be 100% width, in md+ we use masterWidth
      >
        <style dangerouslySetInnerHTML={{ __html: `
          @media (min-width: 768px) {
            .master-split-left { width: ${masterWidth} !important; }
          }
        `}} />
        <div className="master-split-left h-full flex flex-col w-full">
          {masterTitle && (
            <div className="bg-surface-container-low px-4 py-2 border-b border-outline-variant font-bold text-sm text-on-surface">
              {masterTitle}
            </div>
          )}
          <div className="flex-1 overflow-auto">
            {masterContent}
          </div>
        </div>
      </div>
      
      <div className="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden flex flex-col flex-1 min-w-0">
        {detailTitle && (
          <div className="bg-surface-container-low px-4 py-2 border-b border-outline-variant font-bold text-sm text-on-surface flex items-center justify-between">
            <span>{detailTitle}</span>
          </div>
        )}
        <div className="flex-1 overflow-auto">
          {detailContent}
        </div>
      </div>
    </div>
  );
}
