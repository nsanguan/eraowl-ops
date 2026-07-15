import React, { useRef, useEffect } from 'react';

export interface RichTextEditorProps {
  value: string;
  onChange: (html: string) => void;
  label?: string;
  height?: string;
  placeholder?: string;
  className?: string;
  disabled?: boolean;
}

export function RichTextEditor({
  value,
  onChange,
  label,
  height = '200px',
  placeholder = 'Type here...',
  className = '',
  disabled = false
}: RichTextEditorProps) {
  const editorRef = useRef<HTMLDivElement>(null);

  // Sync initial value but don't overwrite if user is typing
  useEffect(() => {
    if (editorRef.current && value !== editorRef.current.innerHTML) {
      editorRef.current.innerHTML = value || '';
    }
  }, [value]);

  const execCommand = (command: string, arg?: string) => {
    if (disabled) return;
    document.execCommand(command, false, arg);
    if (editorRef.current) {
      onChange(editorRef.current.innerHTML);
    }
  };

  const handleInput = () => {
    if (editorRef.current) {
      onChange(editorRef.current.innerHTML);
    }
  };

  const ToolbarButton = ({ icon, command, arg, title }: { icon: string, command: string, arg?: string, title: string }) => (
    <button
      type="button"
      title={title}
      disabled={disabled}
      onClick={(e) => {
        e.preventDefault();
        execCommand(command, arg);
      }}
      className="w-8 h-8 flex items-center justify-center rounded hover:bg-surface-container-high text-outline hover:text-on-surface transition-colors disabled:opacity-30 disabled:cursor-not-allowed"
    >
      <span className="material-symbols-outlined !text-[18px]">{icon}</span>
    </button>
  );

  return (
    <div className={`flex flex-col gap-1.5 ${className}`}>
      {label && <label className="text-xs font-bold text-on-surface-variant uppercase tracking-wider">{label}</label>}
      <div className={`flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden focus-within:border-primary focus-within:ring-1 focus-within:ring-primary transition-all ${disabled ? 'opacity-60 cursor-not-allowed' : ''}`}>
        
        {/* Toolbar */}
        <div className="flex flex-wrap items-center gap-1 p-1 bg-surface-container-low border-b border-outline-variant">
          <ToolbarButton title="Bold" command="bold" icon="format_bold" />
          <ToolbarButton title="Italic" command="italic" icon="format_italic" />
          <ToolbarButton title="Underline" command="underline" icon="format_underlined" />
          <div className="w-px h-6 bg-outline-variant/50 mx-1"></div>
          <ToolbarButton title="Bulleted List" command="insertUnorderedList" icon="format_list_bulleted" />
          <ToolbarButton title="Numbered List" command="insertOrderedList" icon="format_list_numbered" />
          <div className="w-px h-6 bg-outline-variant/50 mx-1"></div>
          <ToolbarButton title="Align Left" command="justifyLeft" icon="format_align_left" />
          <ToolbarButton title="Align Center" command="justifyCenter" icon="format_align_center" />
          <ToolbarButton title="Align Right" command="justifyRight" icon="format_align_right" />
          <div className="w-px h-6 bg-outline-variant/50 mx-1"></div>
          <ToolbarButton title="Clear Formatting" command="removeFormat" icon="format_clear" />
        </div>

        {/* Editor Area */}
        <div 
          ref={editorRef}
          contentEditable={!disabled}
          onInput={handleInput}
          onBlur={handleInput}
          className="p-4 outline-none overflow-y-auto text-sm text-on-surface custom-scrollbar"
          style={{ minHeight: height, maxHeight: height }}
          data-placeholder={placeholder}
        />
        
        {/* CSS for placeholder since contentEditable doesn't support the attribute natively in an easy way without CSS pseudo-elements */}
        <style dangerouslySetInnerHTML={{ __html: `
          [contenteditable][data-placeholder]:empty:before {
            content: attr(data-placeholder);
            color: var(--outline, #888);
            pointer-events: none;
            display: block; /* For Firefox */
          }
        `}} />
      </div>
    </div>
  );
}
