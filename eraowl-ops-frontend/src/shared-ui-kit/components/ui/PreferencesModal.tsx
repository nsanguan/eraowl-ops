import { useState } from 'react';
import { usePreferencesStore, type Warehouse, type AIProvider } from '../../stores/preferences';

interface PreferencesModalProps {
  open: boolean;
  onClose: () => void;
  warehouses: Warehouse[];
}

type Tab = 'warehouses' | 'ai';

export function PreferencesModal({ open, onClose, warehouses }: PreferencesModalProps) {
  const [activeTab, setActiveTab] = useState<Tab>('warehouses');
  const {
    selectedWarehouseIds,
    toggleWarehouse,
    selectAllWarehouses,
    clearWarehouses,
    setSelectedWarehouses,
    aiProvider,
    setAIProvider,
  } = usePreferencesStore();

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-[100] flex items-center justify-center bg-black/40 backdrop-blur-sm"
      onClick={onClose}
    >
      <div
        className="w-full max-w-lg mx-4 rounded-2xl bg-background neo-raised overflow-hidden border border-border/30 shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-border/20">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-primary/10 flex items-center justify-center text-primary">
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <div>
              <h3 className="text-base font-bold text-foreground">Preferences Setup</h3>
              <p className="text-[11px] text-muted-foreground">Configure warehouse filter & AI provider</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-lg bg-background neo-inset flex items-center justify-center text-muted-foreground hover:text-foreground transition-colors"
          >
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Tabs */}
        <div className="flex border-b border-border/20">
          <button
            onClick={() => setActiveTab('warehouses')}
            className={`flex-1 flex items-center justify-center gap-2 px-4 py-3 text-xs font-bold uppercase tracking-wider transition-colors ${
              activeTab === 'warehouses'
                ? 'text-primary border-b-2 border-primary bg-primary/5'
                : 'text-muted-foreground hover:text-foreground'
            }`}
          >
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2-2z M3 7a2 2 0 002 2h12 M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2" />
            </svg>
            Warehouses
          </button>
          <button
            onClick={() => setActiveTab('ai')}
            className={`flex-1 flex items-center justify-center gap-2 px-4 py-3 text-xs font-bold uppercase tracking-wider transition-colors ${
              activeTab === 'ai'
                ? 'text-primary border-b-2 border-primary bg-primary/5'
                : 'text-muted-foreground hover:text-foreground'
            }`}
          >
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
            AI Provider
          </button>
        </div>

        {/* Tab Content */}
        <div className="p-6 max-h-[400px] overflow-y-auto">
          {activeTab === 'warehouses' && (
            <div>
              {/* Info banner */}
              <div className="mb-4 p-3 rounded-xl bg-primary/5 border border-primary/20">
                <p className="text-xs text-muted-foreground">
                  Select warehouses to filter data across all modules. Only data from selected warehouses will be displayed (similar to Oracle EBS organization selection).
                </p>
              </div>

              {/* Select all / clear */}
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-semibold text-muted-foreground">
                  {selectedWarehouseIds.length} of {warehouses.length} selected
                </span>
                <div className="flex gap-2">
                  <button
                    onClick={selectAllWarehouses}
                    className="text-[11px] font-semibold px-3 py-1.5 rounded-lg bg-primary/10 text-primary hover:bg-primary/20 transition-colors"
                  >
                    Select All
                  </button>
                  <button
                    onClick={clearWarehouses}
                    className="text-[11px] font-semibold px-3 py-1.5 rounded-lg bg-muted text-muted-foreground hover:bg-destructive/10 hover:text-destructive transition-colors"
                  >
                    Clear
                  </button>
                </div>
              </div>

              {/* Warehouse list */}
              {warehouses.length === 0 ? (
                <div className="text-center py-8 text-sm text-muted-foreground">
                  No warehouses available. Configure warehouses in the system settings.
                </div>
              ) : (
                <div className="space-y-2">
                  {warehouses.map((wh) => {
                    const isSelected = selectedWarehouseIds.includes(wh.id);
                    return (
                      <button
                        key={wh.id}
                        onClick={() => toggleWarehouse(wh.id)}
                        className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl border transition-all text-left ${
                          isSelected
                            ? 'border-primary/40 bg-primary/10'
                            : 'border-border/20 bg-background hover:bg-accent/50'
                        }`}
                      >
                        <div
                          className={`w-5 h-5 rounded-md border-2 flex items-center justify-center transition-colors ${
                            isSelected ? 'border-primary bg-primary' : 'border-muted-foreground/40'
                          }`}
                        >
                          {isSelected && (
                            <svg className="w-3 h-3 text-primary-foreground" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
                              <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                            </svg>
                          )}
                        </div>
                        <div className="flex-1">
                          <div className="flex items-center gap-2">
                            <span className="font-mono text-[11px] font-bold px-1.5 py-0.5 rounded bg-muted text-muted-foreground uppercase tracking-wider">
                              {wh.code}
                            </span>
                            <span className="text-sm font-medium text-foreground">{wh.name}</span>
                          </div>
                        </div>
                      </button>
                    );
                  })}
                </div>
              )}
            </div>
          )}

          {activeTab === 'ai' && (
            <AITabContent provider={aiProvider} onChange={setAIProvider} />
          )}
        </div>

        {/* Footer */}
        <div className="flex items-center justify-end gap-3 px-6 py-4 border-t border-border/20 bg-accent/20">
          <button
            onClick={onClose}
            className="neo-button px-4 py-2 text-sm text-muted-foreground hover:text-foreground"
          >
            Close
          </button>
          <button
            onClick={() => {
              setSelectedWarehouses(selectedWarehouseIds);
              onClose();
            }}
            className="bg-primary text-primary-foreground rounded-xl px-5 py-2 text-sm font-semibold hover:opacity-90 transition-opacity"
          >
            Save & Apply
          </button>
        </div>
      </div>
    </div>
  );
}

function AITabContent({ provider, onChange }: { provider: AIProvider; onChange: (p: Partial<AIProvider>) => void }) {
  const providers: { id: AIProvider['id']; label: string; desc: string; defaultUrl: string }[] = [
    { id: 'open-webui', label: 'Open WebUI', desc: 'Self-hosted AI portal (port 3000)', defaultUrl: 'http://localhost:3000' },
    { id: 'ollama', label: 'Ollama (Local)', desc: 'Local LLM via Ollama', defaultUrl: 'http://localhost:11434' },
    { id: 'openai', label: 'OpenAI API', desc: 'Cloud GPT models', defaultUrl: 'https://api.openai.com/v1' },
    { id: 'none', label: 'Disabled', desc: 'No AI integration', defaultUrl: '' },
  ];

  return (
    <div>
      <div className="mb-4 p-3 rounded-xl bg-primary/5 border border-primary/20">
        <p className="text-xs text-muted-foreground">
          Configure the AI provider used for intelligent features across modules. The gateway will proxy requests to the selected provider.
        </p>
      </div>

      {/* Provider selection */}
      <div className="space-y-2 mb-5">
        {providers.map((p) => {
          const isSelected = provider.id === p.id;
          return (
            <button
              key={p.id}
              onClick={() =>
                onChange({ id: p.id, name: p.label, apiUrl: p.defaultUrl })
              }
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl border transition-all text-left ${
                isSelected
                  ? 'border-primary/40 bg-primary/10'
                  : 'border-border/20 bg-background hover:bg-accent/50'
              }`}
            >
              <div
                className={`w-5 h-5 rounded-full border-2 flex items-center justify-center transition-colors ${
                  isSelected ? 'border-primary bg-primary' : 'border-muted-foreground/40'
                }`}
              >
                {isSelected && <div className="w-2 h-2 rounded-full bg-primary-foreground" />}
              </div>
              <div className="flex-1">
                <div className="text-sm font-medium text-foreground">{p.label}</div>
                <div className="text-[11px] text-muted-foreground">{p.desc}</div>
              </div>
            </button>
          );
        })}
      </div>

      {/* API URL */}
      {provider.id !== 'none' && (
        <div className="space-y-4">
          <div>
            <label className="block text-[11px] font-semibold uppercase tracking-wider text-muted-foreground mb-1.5">
              API URL
            </label>
            <input
              type="text"
              value={provider.apiUrl}
              onChange={(e) => onChange({ apiUrl: e.target.value })}
              placeholder="http://localhost:11434"
              className="w-full bg-background neo-inset border-none rounded-xl px-4 py-2.5 text-sm font-mono text-foreground placeholder:text-muted-foreground/50 outline-none focus:ring-2 focus:ring-primary/20"
            />
          </div>

          {/* API Key */}
          <div>
            <label className="block text-[11px] font-semibold uppercase tracking-wider text-muted-foreground mb-1.5">
              API Key <span className="text-muted-foreground/50 normal-case font-normal">(optional)</span>
            </label>
            <input
              type="password"
              value={provider.apiKey}
              onChange={(e) => onChange({ apiKey: e.target.value })}
              placeholder="sk-..."
              className="w-full bg-background neo-inset border-none rounded-xl px-4 py-2.5 text-sm font-mono text-foreground placeholder:text-muted-foreground/50 outline-none focus:ring-2 focus:ring-primary/20"
            />
          </div>

          {/* Model */}
          <div>
            <label className="block text-[11px] font-semibold uppercase tracking-wider text-muted-foreground mb-1.5">
              Model <span className="text-muted-foreground/50 normal-case font-normal">(optional)</span>
            </label>
            <input
              type="text"
              value={provider.model}
              onChange={(e) => onChange({ model: e.target.value })}
              placeholder="llama3.1 / gpt-4o / ..."
              className="w-full bg-background neo-inset border-none rounded-xl px-4 py-2.5 text-sm font-mono text-foreground placeholder:text-muted-foreground/50 outline-none focus:ring-2 focus:ring-primary/20"
            />
          </div>
        </div>
      )}

      {provider.id === 'none' && (
        <div className="text-center py-8 text-sm text-muted-foreground">
          AI features will be disabled.
        </div>
      )}
    </div>
  );
}