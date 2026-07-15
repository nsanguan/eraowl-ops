import React, { useState } from 'react';

export interface Comment {
  id: string | number;
  author: string;
  avatarText?: string;
  avatarUrl?: string;
  timestamp: string | Date;
  content: string;
  isCurrentUser?: boolean;
}

export interface CommentsRegionProps {
  comments: Comment[];
  onSubmitComment?: (content: string) => Promise<void> | void;
  title?: string;
  placeholder?: string;
  className?: string;
}

export function CommentsRegion({
  comments,
  onSubmitComment,
  title = 'Comments',
  placeholder = 'Add a comment...',
  className = ''
}: CommentsRegionProps) {
  const [newComment, setNewComment] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newComment.trim() || !onSubmitComment) return;

    setIsSubmitting(true);
    try {
      await onSubmitComment(newComment);
      setNewComment('');
    } finally {
      setIsSubmitting(false);
    }
  };

  const formatDate = (val: string | Date) => {
    const d = new Date(val);
    return new Intl.DateTimeFormat('en-US', {
      month: 'short', day: 'numeric', year: 'numeric',
      hour: 'numeric', minute: '2-digit', hour12: true
    }).format(d);
  };

  return (
    <div className={`flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden ${className}`}>
      
      {/* Header */}
      {title && (
        <div className="bg-surface-container-low px-4 py-3 border-b border-outline-variant flex items-center justify-between">
          <h3 className="font-bold text-sm text-on-surface flex items-center gap-2">
            <span className="material-symbols-outlined !text-[18px]">forum</span>
            {title}
          </h3>
          <span className="text-xs font-bold bg-surface-container-high text-on-surface-variant px-2 py-0.5 rounded-full">
            {comments.length}
          </span>
        </div>
      )}

      {/* Comments List */}
      <div className="flex-1 overflow-y-auto max-h-[500px] p-4 flex flex-col gap-6 custom-scrollbar bg-surface-container-lowest">
        {comments.length === 0 ? (
          <div className="text-center text-sm text-outline italic py-8">
            No comments yet.
          </div>
        ) : (
          comments.map(comment => (
            <div key={comment.id} className={`flex gap-3 ${comment.isCurrentUser ? 'flex-row-reverse' : 'flex-row'}`}>
              
              {/* Avatar */}
              <div className="shrink-0 w-8 h-8 rounded-full overflow-hidden bg-primary/10 flex items-center justify-center text-primary font-bold text-xs border border-primary/20">
                {comment.avatarUrl ? (
                  <img src={comment.avatarUrl} alt={comment.author} className="w-full h-full object-cover" />
                ) : (
                  comment.avatarText || comment.author.substring(0, 2).toUpperCase()
                )}
              </div>

              {/* Comment Body */}
              <div className={`flex flex-col max-w-[85%] ${comment.isCurrentUser ? 'items-end' : 'items-start'}`}>
                <div className="flex items-baseline gap-2 mb-1 px-1">
                  <span className="text-xs font-bold text-on-surface">{comment.author}</span>
                  <span className="text-[10px] text-outline">{formatDate(comment.timestamp)}</span>
                </div>
                <div 
                  className={`px-4 py-2 rounded-2xl text-sm ${
                    comment.isCurrentUser 
                      ? 'bg-primary text-primary-foreground rounded-tr-sm' 
                      : 'bg-surface-container-low text-on-surface border border-outline-variant rounded-tl-sm'
                  }`}
                >
                  {/* Assuming plain text for now, could render markdown/html if needed */}
                  <p className="whitespace-pre-wrap break-words">{comment.content}</p>
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      {/* Reply Box */}
      {onSubmitComment && (
        <div className="p-4 bg-surface-container-lowest border-t border-outline-variant">
          <form onSubmit={handleSubmit} className="flex gap-2 relative">
            <textarea
              value={newComment}
              onChange={e => setNewComment(e.target.value)}
              placeholder={placeholder}
              disabled={isSubmitting}
              className="flex-1 bg-surface-container-low border border-outline-variant rounded-xl pl-4 pr-12 py-3 text-sm text-on-surface placeholder:text-outline outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all resize-none h-12 min-h-[48px] max-h-[120px]"
              rows={1}
              onInput={(e) => {
                const target = e.target as HTMLTextAreaElement;
                target.style.height = '48px';
                target.style.height = `${Math.min(target.scrollHeight, 120)}px`;
              }}
            />
            <button
              type="submit"
              disabled={!newComment.trim() || isSubmitting}
              className="absolute right-2 top-1.5 w-9 h-9 flex items-center justify-center rounded-full bg-primary text-primary-foreground disabled:opacity-30 disabled:bg-surface-container-high disabled:text-outline transition-colors hover:brightness-110"
            >
              {isSubmitting ? (
                <span className="material-symbols-outlined !text-[18px] animate-spin">progress_activity</span>
              ) : (
                <span className="material-symbols-outlined !text-[18px]">send</span>
              )}
            </button>
          </form>
        </div>
      )}
    </div>
  );
}
