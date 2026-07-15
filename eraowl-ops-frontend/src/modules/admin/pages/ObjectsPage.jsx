import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { InteractiveGrid } from '../../../shared-ui-kit/components/ui/InteractiveGrid'

const COLUMNS = [
  { key: 'object_type', header: 'Type', width: '120px' },
  { key: 'object_name', header: 'Name', width: '300px' },
  { key: 'module_name', header: 'Module', width: '150px' },
  { key: 'created_at', header: 'Created', width: '160px',
    render: (r) => r.created_at ? new Date(r.created_at).toLocaleString() : '—' },
]

export default function ObjectsPage() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [total, setTotal] = useState(0)

  const fetchObjects = useCallback(async () => {
    setLoading(true)
    try {
      const { data } = await api.get('/admin/objects', { params: { page: 1, page_size: 500 } })
      setItems(data.items || [])
      setTotal(data.total || 0)
    } catch (err) {
      console.error('Failed to load objects:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => { fetchObjects() }, [fetchObjects])

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-on-surface">Code Objects</h1>
        <p className="text-sm text-outline mt-1">
          Catalog of {total} code-level objects (tables, endpoints, permissions, pages, components) discovered across the system.
        </p>
      </div>

      <InteractiveGrid
        columns={COLUMNS}
        data={items}
        loading={loading}
        idKey="object_id"
        searchable
        tableHeight="calc(100vh - 240px)"
      />
    </div>
  )
}
