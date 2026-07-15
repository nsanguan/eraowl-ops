import { useState, useMemo } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { AppShell } from '../layout/AppShell';
import { mcpCall } from '../../lib/gateway';
import { InteractiveGrid, type GridColumn } from './InteractiveGrid';

export interface EntityField {
  key: string;
  label: string;
  type?: 'text' | 'number' | 'select' | 'boolean';
  options?: { label: string; value: string }[];
  width?: string;
  required?: boolean;
  render?: (val: unknown, row: Record<string, unknown>) => React.ReactNode;
}

export interface EntityPageProps {
  /** MCP table name (e.g. 'corporates', 'business_units') */
  table: string;
  /** Display title */
  title: string;
  /** Primary key column name */
  pk?: string;
  /** Field definitions for columns and form */
  fields: EntityField[];
  /** Module label for AppShell */
  moduleLabel?: string;
  /** Module initials for AppShell */
  moduleInitials?: string;
  /** Current path for AppShell */
  currentPath?: string;
  /** Home path for AppShell */
  homePath?: string;
  /** Whether to hide the is_active toggle */
  hideStatus?: boolean;
}

function snakeToLabel(s: string): string {
  return s.split('_').map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

export function EntityPage({
  table, title, pk, fields, moduleLabel = 'Core', moduleInitials = 'CR',
  currentPath, homePath = '/core/dashboard', hideStatus = false,
}: EntityPageProps) {
  const portalUrl = `http://${window.location.hostname}:3300/`;
  const queryClient = useQueryClient();
  const [editId, setEditId] = useState<string | null>(null);
  const [form, setForm] = useState<Record<string, string>>({});
  const [formActive, setFormActive] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [searchTerms, setSearchTerms] = useState<string[]>([]);

  const { data, isLoading } = useQuery<Record<string, unknown>[]>({
    queryKey: [table],
    queryFn: () => mcpCall(`${table}.list`),
  });

  const records = data ?? [];

  const filteredRecords = useMemo(() => {
    if (searchTerms.length === 0) return records;
    const q = searchTerms.join(' ').toLowerCase();
    return records.filter((item) =>
      Object.values(item).some((val) => String(val ?? '').toLowerCase().includes(q))
    );
  }, [records, searchTerms]);

  const autoPk = useMemo(() => {
    if (pk) return pk;
    const keys = records.length > 0 ? Object.keys(records[0]) : [];
    return keys.find((k) => k.endsWith('_id') && k !== 'update_by') || 'id';
  }, [records, pk]);

  const editableFields = useMemo(() => {
    return fields.filter((f) => f.key !== autoPk && f.key !== 'is_active' && !f.key.endsWith('_id'));
  }, [fields, autoPk]);

  const saveMutation = useMutation({
    mutationFn: async () => {
      const payload = { ...form, is_active: formActive };
      if (editId) {
        await mcpCall(`${table}.update`, { id: editId, ...payload });
      } else {
        await mcpCall(`${table}.create`, payload);
      }
    },
    onSuccess: () => { queryClient.invalidateQueries({ queryKey: [table] }); resetForm(); },
  });

  const deleteMutation = useMutation({
    mutationFn: async (id: string) => { await mcpCall(`${table}.delete`, { id }); },
    onSuccess: () => queryClient.invalidateQueries({ queryKey: [table] }),
  });

  const resetForm = () => { setEditId(null); setForm({}); setFormActive(true); setShowForm(false); };
  const openAddForm = () => { resetForm(); setShowForm(true); };

  const startEdit = (entry: Record<string, unknown>) => {
    setEditId(entry[autoPk] as string);
    const f: Record<string, string> = {};
    for (const field of editableFields) {
      f[field.key] = String(entry[field.key] ?? '');
    }
    setForm(f);
    setFormActive(entry.is_active !== false);
    setShowForm(true);
  };

  const hasActive = !hideStatus && records.length > 0 && 'is_active' in records[0];

  const gridColumns: GridColumn<Record<string, unknown>>[] = [
    ...fields.map((f) => ({
      key: f.key,
      header: f.label || snakeToLabel(f.key),
      width: f.width,
      render: (row: Record<string, unknown>) => {
        if (f.render) return f.render(row[f.key], row);
        const val = row[f.key];
        if (typeof val === 'boolean') {
          return <span className="text-[12px] text-on-surface">{val ? 'Yes' : 'No'}</span>;
        }
        return <span className="text-[12px] text-on-surface truncate block max-w-[240px]">{val === null || val === undefined ? '\u2014' : String(val)}</span>;
      },
    } as GridColumn<Record<string, unknown>>)),
    ...(hasActive ? [{
      key: 'is_active',
      header: 'Status',
      width: '100px',
      render: (row: Record<string, unknown>) => {
        const active = row.is_active as boolean;
        return (
          <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wide ${
            active ? 'bg-green-500/10 text-green-400' : 'bg-outline-variant/30 text-outline'
          }`}>
            <span className={`w-1.5 h-1.5 rounded-full ${active ? 'bg-green-500' : 'bg-outline'}`} />
            {active ? 'Active' : 'Inactive'}
          </span>
        );
      },
    } as GridColumn<Record<string, unknown>>] : []),
  ];

  const set = (k: string, v: string) => setForm({ ...form, [k]: v });

  return (
    <AppShell
      onNavigate={(path) => { window.location.href = path; }}
      currentPath={currentPath ?? `/${moduleLabel.toLowerCase()}/data/${table}`}
      homePath={homePath}
      homeLabel="Home"
      moduleLabel={moduleLabel}
      moduleInitials={moduleInitials}
      helpUrl={portalUrl}
      homeUrl={portalUrl}
      userLabel={`${moduleLabel} Admin`}
      userInitials={moduleInitials}
    >
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 style={{ fontSize: '32px', lineHeight: '40px', letterSpacing: '-0.01em', fontWeight: 600 }} className="text-slate-900! dark:text-white!">{title}</h1>
          <p style={{ fontSize: '14px', lineHeight: '20px' }} className="text-slate-500! dark:text-slate-300! mt-1">
            {isLoading ? 'Loading...' : `${filteredRecords.length} ${title.toLowerCase()} record${filteredRecords.length !== 1 ? 's' : ''}`}
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button onClick={openAddForm}
            className="px-4 py-2 bg-primary text-primary-foreground text-[11px] font-semibold rounded-lg hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20 flex items-center gap-1.5">
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" d="M12 4.5v15m7.5-7.5h-15" /></svg> Add {title}
          </button>
          <span className="flex items-center gap-2 text-[12px] text-outline">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" /> Connected
          </span>
        </div>
      </div>

      <InteractiveGrid<Record<string, unknown>>
        title="" columns={gridColumns} data={filteredRecords} idKey={autoPk}
        searchable onSearch={(q) => setSearchTerms(q.split(/\s+/).filter(Boolean))}
        loading={isLoading}
        onEdit={(r) => startEdit(r)}
        onDelete={(r) => { if (confirm('Delete this record?')) deleteMutation.mutate(r[autoPk] as string); }}
        onAddRow={openAddForm} addLabel={`Add ${title}`}
      />

      {showForm && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-50" onClick={resetForm}>
          <div className="bg-background rounded-2xl border border-outline-variant shadow-2xl w-full max-w-lg mx-4" onClick={(e) => e.stopPropagation()}>
            <div className="p-6 border-b border-outline-variant/30">
              <h2 className="text-sm font-semibold text-on-surface">{editId ? `Edit ${title}` : `New ${title}`}</h2>
            </div>
            <div className="p-6 space-y-4 max-h-[60vh] overflow-y-auto">
              {editableFields.map((field) => (
                <div key={field.key}>
                  <label className="text-[9px] font-semibold uppercase tracking-wider text-outline block mb-1.5">
                    {field.label || snakeToLabel(field.key)}
                    {field.required && <span className="text-error ml-0.5">*</span>}
                  </label>
                  {field.type === 'select' ? (
                    <select value={form[field.key] ?? ''} onChange={(e) => set(field.key, e.target.value)}
                      className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-4 py-3 text-sm text-on-surface font-semibold focus:ring-2 focus:ring-primary outline-none transition-all appearance-none">
                      <option value="">Select...</option>
                      {(field.options ?? []).map((o) => (
                        <option key={o.value} value={o.value}>{o.label}</option>
                      ))}
                    </select>
                  ) : field.type === 'number' ? (
                    <input type="number" value={form[field.key] ?? ''} onChange={(e) => set(field.key, e.target.value)}
                      className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-4 py-3 text-sm text-on-surface font-semibold focus:ring-2 focus:ring-primary outline-none transition-all"
                      placeholder={field.label || snakeToLabel(field.key)} />
                  ) : (
                    <input type="text" value={form[field.key] ?? ''} onChange={(e) => set(field.key, e.target.value)}
                      className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-4 py-3 text-sm text-on-surface font-semibold focus:ring-2 focus:ring-primary outline-none transition-all"
                      placeholder={field.label || snakeToLabel(field.key)} />
                  )}
                </div>
              ))}
              {hasActive && (
                <div className="flex items-center justify-between py-2">
                  <label className="text-[9px] font-semibold uppercase tracking-wider text-outline">Active Status</label>
                  <button type="button" onClick={() => setFormActive(!formActive)}
                    className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors duration-200 ${formActive ? 'bg-green-500' : 'bg-outline-variant'}`}>
                    <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform duration-200 shadow-sm ${formActive ? 'translate-x-6' : 'translate-x-1'}`} />
                  </button>
                </div>
              )}
            </div>
            <div className="flex justify-end gap-2 p-6 border-t border-outline-variant/30">
              <button onClick={resetForm}
                className="px-6 py-2.5 text-[11px] font-semibold rounded-lg border border-outline-variant text-on-surface-variant hover:bg-surface-container-high transition-all">Cancel</button>
              <button onClick={() => saveMutation.mutate()} disabled={saveMutation.isPending}
                className="px-8 py-2.5 bg-primary text-primary-foreground text-[11px] font-semibold rounded-lg hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20 disabled:opacity-50">
                {saveMutation.isPending ? 'Saving...' : editId ? 'Update' : 'Create'}
              </button>
            </div>
          </div>
        </div>
      )}
    </AppShell>
  );
}
