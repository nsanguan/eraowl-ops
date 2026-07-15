import React, { useState, useRef } from 'react';

export interface DropzoneUploadProps {
  onFilesAdded: (files: File[]) => void;
  accept?: string;
  multiple?: boolean;
  maxSize?: number; // bytes
  label?: string;
  hint?: string;
  className?: string;
}

export function DropzoneUpload({
  onFilesAdded,
  accept,
  multiple = true,
  maxSize,
  label = 'Upload Files',
  hint = 'Drag and drop files here, or click to browse',
  className = ''
}: DropzoneUploadProps) {
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDragEnter = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (!isDragging) setIsDragging(true);
  };

  const processFiles = (fileList: FileList | null) => {
    if (!fileList) return;
    let files = Array.from(fileList);
    
    if (maxSize) {
      files = files.filter(f => f.size <= maxSize);
    }
    
    if (files.length > 0) {
      onFilesAdded(files);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    processFiles(e.dataTransfer.files);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    processFiles(e.target.files);
    if (fileInputRef.current) {
      fileInputRef.current.value = ''; // Reset so same file can be selected again
    }
  };

  return (
    <div className={className}>
      {label && <label className="block text-xs font-bold text-on-surface-variant uppercase tracking-wider mb-2">{label}</label>}
      <div 
        className={`relative border-2 border-dashed rounded-xl p-8 text-center transition-all cursor-pointer flex flex-col items-center justify-center gap-4 ${
          isDragging 
            ? 'border-primary bg-primary/5 scale-[1.02]' 
            : 'border-outline-variant hover:border-primary/50 hover:bg-surface-container-low bg-surface-container-lowest'
        }`}
        onDragEnter={handleDragEnter}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
      >
        <input 
          ref={fileInputRef}
          type="file" 
          className="hidden" 
          accept={accept}
          multiple={multiple}
          onChange={handleChange}
        />
        
        <div className={`w-16 h-16 rounded-full flex items-center justify-center transition-colors ${isDragging ? 'bg-primary text-white shadow-lg shadow-primary/30' : 'bg-surface-container-high text-outline'}`}>
          <span className="material-symbols-outlined !text-[32px]">
            {isDragging ? 'upload_file' : 'cloud_upload'}
          </span>
        </div>
        
        <div>
          <p className={`font-bold text-lg mb-1 ${isDragging ? 'text-primary' : 'text-on-surface'}`}>
            {isDragging ? 'Drop files now' : 'Select Files'}
          </p>
          <p className="text-sm text-outline">
            {hint}
          </p>
        </div>
        
        {maxSize && (
          <div className="absolute bottom-3 right-4 text-[10px] font-semibold text-outline-variant uppercase">
            Max size: {(maxSize / (1024 * 1024)).toFixed(1)} MB
          </div>
        )}
      </div>
    </div>
  );
}
