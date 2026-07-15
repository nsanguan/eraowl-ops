import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Uncaught error:', error, errorInfo);
  }

  public render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback;
      }
      return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-surface-container-lowest text-on-surface p-6 text-center">
          <div className="bg-error/10 text-error p-4 rounded-full mb-6">
            <span className="material-symbols-outlined !text-[48px]">warning</span>
          </div>
          <h1 className="text-2xl font-bold mb-2 text-slate-900! dark:text-white!">Something went wrong</h1>
          <p className="text-slate-500! dark:text-slate-300! max-w-md mb-8">
            {this.state.error?.message || 'An unexpected error occurred while rendering this component.'}
          </p>
          <button
            onClick={() => window.location.reload()}
            className="px-6 py-2.5 bg-primary text-primary-foreground font-semibold rounded-lg hover:brightness-110 active:scale-95 transition-all shadow-lg"
          >
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
