import type { ReactNode } from 'react';

interface PageHeaderProps {
  title: string;
  subtitle?: string;
  actions?: ReactNode;
}

export function PageHeader({ title, subtitle, actions }: PageHeaderProps) {
  return (
    <div className="flex flex-col md:flex-row md:items-center justify-between mb-8">
      <div>
        <h1 className="text-3xl font-bold text-slate-900! dark:text-white!">{title}</h1>
        {subtitle && <p className="text-sm text-slate-500! dark:text-slate-300! mt-1">{subtitle}</p>}
      </div>
      {actions && (
        <div className="mt-4 md:mt-0 flex items-center space-x-3">
          {actions}
        </div>
      )}
    </div>
  );
}
