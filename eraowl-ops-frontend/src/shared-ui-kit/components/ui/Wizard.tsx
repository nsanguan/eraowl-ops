import React, { useState } from 'react';

export interface WizardStep {
  id: string;
  title: string;
  subtitle?: string;
  content: React.ReactNode;
  isValid?: () => boolean | Promise<boolean>;
}

export interface WizardProps {
  steps: WizardStep[];
  onComplete: () => void;
  onCancel?: () => void;
  className?: string;
  title?: string;
}

export function Wizard({ steps, onComplete, onCancel, className = '', title = 'Wizard' }: WizardProps) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const [isProcessing, setIsProcessing] = useState(false);

  const currentStep = steps[currentStepIndex];
  const isLastStep = currentStepIndex === steps.length - 1;
  const isFirstStep = currentStepIndex === 0;

  const handleNext = async () => {
    if (currentStep.isValid) {
      setIsProcessing(true);
      const valid = await currentStep.isValid();
      setIsProcessing(false);
      if (!valid) return;
    }

    if (isLastStep) {
      onComplete();
    } else {
      setCurrentStepIndex(prev => prev + 1);
    }
  };

  const handlePrevious = () => {
    if (!isFirstStep) {
      setCurrentStepIndex(prev => prev - 1);
    }
  };

  return (
    <div className={`flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden ${className}`}>
      {/* Header */}
      <div className="bg-surface-container-low px-6 py-4 border-b border-outline-variant flex items-center justify-between">
        <h2 className="font-bold text-lg text-slate-900! dark:text-white!">{title}</h2>
        {onCancel && (
          <button 
            onClick={onCancel}
            className="p-1 text-outline hover:text-on-surface hover:bg-outline-variant/30 rounded-lg transition-colors"
          >
            <span className="material-symbols-outlined !text-[20px]">close</span>
          </button>
        )}
      </div>

      {/* Progress Indicator */}
      <div className="px-8 py-6 border-b border-outline-variant bg-surface-container-lowest">
        <div className="relative flex items-center justify-between">
          <div className="absolute left-0 top-1/2 -translate-y-1/2 w-full h-1 bg-surface-container-high rounded-full -z-10"></div>
          
          <div 
            className="absolute left-0 top-1/2 -translate-y-1/2 h-1 bg-primary rounded-full -z-10 transition-all duration-300"
            style={{ width: `${(currentStepIndex / (steps.length - 1)) * 100}%` }}
          ></div>

          {steps.map((step, idx) => {
            const isCompleted = idx < currentStepIndex;
            const isCurrent = idx === currentStepIndex;
            const isPending = idx > currentStepIndex;
            
            return (
              <div key={step.id} className="flex flex-col items-center gap-2 bg-surface-container-lowest px-2">
                <div 
                  className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm transition-colors border-2 ${
                    isCompleted ? 'bg-primary border-primary text-primary-foreground' :
                    isCurrent ? 'bg-surface-container-lowest border-primary text-primary' :
                    'bg-surface-container-lowest border-surface-container-high text-outline'
                  }`}
                >
                  {isCompleted ? <span className="material-symbols-outlined !text-[16px]">check</span> : idx + 1}
                </div>
                <div className="text-center w-24 absolute mt-10">
                  <div className={`text-[11px] font-bold tracking-tight ${isCurrent ? 'text-primary' : isCompleted ? 'text-on-surface' : 'text-outline'}`}>
                    {step.title}
                  </div>
                  {step.subtitle && (
                    <div className="text-[9px] text-outline truncate">{step.subtitle}</div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Content Area */}
      <div className="flex-1 p-8 overflow-y-auto min-h-[300px] mt-8">
        {currentStep.content}
      </div>

      {/* Footer / Actions */}
      <div className="px-6 py-4 bg-surface-container-low border-t border-outline-variant flex items-center justify-between">
        <div>
          {!isFirstStep && (
            <button 
              onClick={handlePrevious}
              disabled={isProcessing}
              className="px-5 py-2 text-sm font-bold border border-outline-variant rounded-lg hover:bg-outline-variant/30 text-on-surface transition-colors disabled:opacity-50 flex items-center gap-2"
            >
              <span className="material-symbols-outlined !text-[18px]">arrow_back</span>
              Previous
            </button>
          )}
        </div>
        <div className="flex items-center gap-3">
          {onCancel && (
            <button 
              onClick={onCancel}
              disabled={isProcessing}
              className="px-5 py-2 text-sm font-bold text-outline hover:text-on-surface transition-colors disabled:opacity-50"
            >
              Cancel
            </button>
          )}
          <button 
            onClick={handleNext}
            disabled={isProcessing}
            className="px-6 py-2 text-sm font-bold bg-primary text-primary-foreground rounded-lg hover:brightness-110 transition-all shadow-md shadow-primary/20 disabled:opacity-50 flex items-center gap-2"
          >
            {isProcessing ? (
              <span className="material-symbols-outlined !text-[18px] animate-spin">progress_activity</span>
            ) : isLastStep ? (
              <span className="material-symbols-outlined !text-[18px]">check_circle</span>
            ) : (
              <span className="material-symbols-outlined !text-[18px]">arrow_forward</span>
            )}
            {isLastStep ? 'Finish' : 'Next'}
          </button>
        </div>
      </div>
    </div>
  );
}
