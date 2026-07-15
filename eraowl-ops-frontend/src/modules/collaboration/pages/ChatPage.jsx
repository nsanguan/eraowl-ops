import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../../../api/client'
import useAuthStore from '../../../store/authStore'

const MOCK_USERS = [
  { id: 'u001', name: 'Sarah Chen', status: 'online' },
  { id: 'u002', name: 'Mike O.', status: 'away' },
  { id: 'u003', name: 'Jen L.', status: 'offline' },
  { id: 'u004', name: 'Alex Rivera', status: 'online' },
  { id: 'u005', name: 'Tom W.', status: 'away' },
]

export default function ChatPage() {
  const [conversations, setConversations] = useState([])
  const [activeConv, setActiveConv] = useState(null)
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const user = useAuthStore((s) => s.user)
  const bottomRef = useRef(null)

  const fetchConv = useCallback(async () => {
    try { const { data } = await api.get('/collaboration/dm-conversations'); setConversations(data || []) } catch {}
  }, [])

  const fetchMessages = useCallback(async (convId) => {
    try { const { data } = await api.get(`/collaboration/dm-conversations/${convId}/messages`, { params: { page: 1, page_size: 100 } }); setMessages(data?.items || []) } catch { setMessages([]) }
  }, [])

  useEffect(() => { fetchConv() }, [fetchConv])
  useEffect(() => { if (activeConv) fetchMessages(activeConv.conversation_id) }, [activeConv, fetchMessages])
  useEffect(() => { bottomRef.current?.scrollIntoView({ behavior: 'smooth' }) }, [messages])

  const handleSend = async () => {
    if (!input.trim() || !activeConv) return
    try {
      await api.post(`/collaboration/dm-conversations/${activeConv.conversation_id}/messages`, { content: input, sender_name: user?.username || 'Me' })
      setInput(''); fetchMessages(activeConv.conversation_id)
    } catch {}
  }

  const statusDot = (s) =>
    s === 'online' ? 'bg-success' : s === 'away' ? 'bg-warning' : 'bg-outline-variant'

  return (
    <div className="flex h-[calc(100vh-120px)] p-6 gap-4">
      <div className="w-64 bg-surface-container-lowest border border-outline-variant rounded-xl flex flex-col overflow-hidden shrink-0">
        <div className="px-4 py-3 border-b border-outline-variant text-xs font-bold text-on-surface uppercase tracking-wider">Direct Messages</div>
        <div className="flex-1 overflow-y-auto">
          {MOCK_USERS.map((mu) => (
            <button key={mu.id} onClick={() => setActiveConv({ conversation_id: mu.id, other_user: mu })}
              className={`w-full flex items-center gap-3 px-4 py-2.5 text-sm transition-colors ${activeConv?.conversation_id === mu.id ? 'bg-primary/10 text-primary font-semibold' : 'text-on-surface hover:bg-surface-container-low'}`}>
              <div className="relative">
                <div className="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center text-[11px] font-bold text-primary">{mu.name[0]}</div>
                <span className={`absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 rounded-full border-2 border-surface-container-lowest ${statusDot(mu.status)}`} />
              </div>
              <span className="truncate">{mu.name}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 bg-surface-container-lowest border border-outline-variant rounded-xl flex flex-col overflow-hidden">
        {activeConv ? (
          <>
            <div className="px-4 py-3 border-b border-outline-variant bg-surface-container-low flex items-center gap-3">
              <div className="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center text-[11px] font-bold text-primary">{activeConv.other_user.name[0]}</div>
              <div>
                <div className="text-sm font-semibold text-on-surface">{activeConv.other_user.name}</div>
                <div className="text-[10px] text-outline capitalize">{activeConv.other_user.status}</div>
              </div>
            </div>
            <div className="flex-1 overflow-y-auto p-4 space-y-3">
              {messages.length === 0 && <p className="text-sm text-outline text-center py-8">No messages yet. Say hello!</p>}
              {messages.map((msg) => {
                const isMe = msg.sender_name === (user?.username || 'Me')
                return (
                  <div key={msg.message_id} className={`flex ${isMe ? 'justify-end' : 'justify-start'}`}>
                    <div className={`max-w-[70%] ${isMe ? 'bg-primary/10 rounded-2xl rounded-br-md' : 'bg-surface-container-high rounded-2xl rounded-bl-md'} px-4 py-2.5`}>
                      <p className="text-sm text-on-surface">{msg.content}</p>
                      <div className={`text-[10px] text-outline mt-0.5 ${isMe ? 'text-right' : 'text-left'}`}>{new Date(msg.created_at).toLocaleTimeString()}</div>
                    </div>
                  </div>
                )
              })}
              <div ref={bottomRef} />
            </div>
            <div className="p-3 border-t border-outline-variant">
              <div className="flex gap-2">
                <input type="text" value={input} onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSend()} placeholder="Type a message..."
                  className="flex-1 px-3 py-2 bg-surface-bright border border-outline-variant rounded-lg text-sm text-on-surface focus:border-primary focus:ring-1 focus:ring-primary outline-none" />
                <button onClick={handleSend} className="px-3 py-2 bg-primary text-primary-foreground rounded-lg text-sm font-semibold hover:opacity-90">Send</button>
              </div>
            </div>
          </>
        ) : (
          <div className="flex items-center justify-center flex-1 text-outline text-sm">Select a person to start chatting</div>
        )}
      </div>
    </div>
  )
}
