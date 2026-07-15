import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../../../api/client'
import useAuthStore from '../../../store/authStore'

export default function DiscussPage() {
  const [channels, setChannels] = useState([])
  const [activeChannel, setActiveChannel] = useState(null)
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [showCreate, setShowCreate] = useState(false)
  const [newName, setNewName] = useState('')
  const [newTopic, setNewTopic] = useState('')
  const user = useAuthStore((s) => s.user)
  const bottomRef = useRef(null)

  const fetchChannels = useCallback(async () => {
    try { const { data } = await api.get('/collaboration/channels'); setChannels(data || []) } catch {}
  }, [])

  const fetchMessages = useCallback(async (channelId) => {
    try {
      const { data } = await api.get(`/collaboration/channels/${channelId}/messages`, { params: { page: 1, page_size: 100 } })
      setMessages(data?.items || [])
    } catch { setMessages([]) }
  }, [])

  useEffect(() => { fetchChannels() }, [fetchChannels])

  useEffect(() => {
    if (activeChannel) fetchMessages(activeChannel.channel_id)
  }, [activeChannel, fetchMessages])

  useEffect(() => { bottomRef.current?.scrollIntoView({ behavior: 'smooth' }) }, [messages])

  const handleSend = async () => {
    if (!input.trim() || !activeChannel) return
    try {
      await api.post(`/collaboration/channels/${activeChannel.channel_id}/messages`, {
        content: input, author_name: user?.username || 'User',
      })
      setInput('')
      fetchMessages(activeChannel.channel_id)
    } catch {}
  }

  const handleCreateChannel = async () => {
    if (!newName.trim()) return
    try {
      await api.post('/collaboration/channels', { name: newName, topic: newTopic })
      setShowCreate(false); setNewName(''); setNewTopic('')
      fetchChannels()
    } catch {}
  }

  return (
    <div className="flex h-[calc(100vh-120px)] p-6 gap-4">
      <div className="w-64 bg-surface-container-lowest border border-outline-variant rounded-xl flex flex-col overflow-hidden shrink-0">
        <div className="flex items-center justify-between px-4 py-3 border-b border-outline-variant">
          <span className="text-xs font-bold text-on-surface uppercase tracking-wider">Channels</span>
          <button onClick={() => setShowCreate(true)} className="text-primary hover:text-primary/80">
            <span className="material-symbols-outlined text-[18px]">add</span>
          </button>
        </div>
        <div className="flex-1 overflow-y-auto">
          {channels.map((ch) => (
            <button key={ch.channel_id} onClick={() => setActiveChannel(ch)}
              className={`w-full text-left px-4 py-2.5 text-sm transition-colors flex items-center gap-2 ${
                activeChannel?.channel_id === ch.channel_id ? 'bg-primary/10 text-primary font-semibold' : 'text-on-surface hover:bg-surface-container-low'
              }`}>
              <span className="material-symbols-outlined text-[16px]">{ch.is_private ? 'lock' : 'tag'}</span>
              <span className="truncate">{ch.name}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 bg-surface-container-lowest border border-outline-variant rounded-xl flex flex-col overflow-hidden">
        {activeChannel ? (
          <>
            <div className="px-4 py-3 border-b border-outline-variant bg-surface-container-low">
              <div className="text-sm font-semibold text-on-surface"># {activeChannel.name}</div>
              {activeChannel.topic && <div className="text-xs text-outline mt-0.5">{activeChannel.topic}</div>}
            </div>
            <div className="flex-1 overflow-y-auto p-4 space-y-3">
              {messages.length === 0 && <p className="text-sm text-outline text-center py-8">No messages yet. Start the conversation!</p>}
              {messages.map((msg) => (
                <div key={msg.message_id} className="flex items-start gap-3">
                  <div className="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center text-[11px] font-bold text-primary shrink-0">
                    {(msg.author_name || 'U')[0].toUpperCase()}
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="text-xs font-semibold text-on-surface">{msg.author_name || 'User'}</span>
                      <span className="text-[10px] text-outline">{new Date(msg.created_at).toLocaleTimeString()}</span>
                    </div>
                    <p className="text-sm text-on-surface mt-0.5">{msg.content}</p>
                  </div>
                </div>
              ))}
              <div ref={bottomRef} />
            </div>
            <div className="p-3 border-t border-outline-variant">
              <div className="flex gap-2">
                <input type="text" value={input} onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                  placeholder={`Message #${activeChannel.name}`}
                  className="flex-1 px-3 py-2 bg-surface-bright border border-outline-variant rounded-lg text-sm text-on-surface focus:border-primary focus:ring-1 focus:ring-primary outline-none" />
                <button onClick={handleSend} className="px-3 py-2 bg-primary text-primary-foreground rounded-lg text-sm font-semibold hover:opacity-90 transition-opacity">Send</button>
              </div>
            </div>
          </>
        ) : (
          <div className="flex items-center justify-center flex-1 text-outline text-sm">Select a channel to start discussing</div>
        )}
      </div>

      {showCreate && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={() => setShowCreate(false)}>
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-md p-5" onClick={(e) => e.stopPropagation()}>
            <h2 className="text-lg font-bold text-slate-900! dark:text-white! mb-4">Create Channel</h2>
            <div className="space-y-3">
              <input type="text" value={newName} onChange={(e) => setNewName(e.target.value)} placeholder="Channel name"
                className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
              <input type="text" value={newTopic} onChange={(e) => setNewTopic(e.target.value)} placeholder="Topic (optional)"
                className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
            </div>
            <div className="flex justify-end gap-3 mt-5">
              <button onClick={() => setShowCreate(false)} className="px-4 py-2 text-sm font-semibold text-on-surface-variant bg-surface-container-low border border-outline-variant rounded-xl">Cancel</button>
              <button onClick={handleCreateChannel} className="px-4 py-2 text-sm font-semibold text-white bg-primary rounded-xl hover:opacity-90">Create</button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
