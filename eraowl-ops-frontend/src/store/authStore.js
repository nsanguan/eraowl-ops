import { create } from 'zustand'
import api from '../api/client'

let accessToken = null

const useAuthStore = create((set, get) => ({
  user: null,
  isAuthenticated: false,
  isLoading: true,
  roles: [],
  privileges: [],

  login: async (username, password) => {
    const { data } = await api.post('/admin/login', { username, password })
    accessToken = data.access_token
    localStorage.setItem('refresh_token', data.refresh_token)
    localStorage.setItem('access_token', data.access_token)
    set({ user: data.user, isAuthenticated: true })
    await get().fetchPrivileges()
    return data
  },

  logout: async () => {
    const refreshToken = localStorage.getItem('refresh_token')
    if (refreshToken) {
      try { await api.post('/admin/logout', { refresh_token: refreshToken }) } catch {}
    }
    accessToken = null
    localStorage.clear()
    set({ user: null, isAuthenticated: false, roles: [], privileges: [] })
  },

  checkAuth: async () => {
    const token = localStorage.getItem('access_token')
    if (!token) {
      set({ isLoading: false, isAuthenticated: false })
      return
    }
    accessToken = token
    try {
      const { data } = await api.get('/admin/users/me')
      set({
        user: data,
        isAuthenticated: true,
        isLoading: false,
        roles: data.roles || [],
        privileges: data.privileges || [],
      })
    } catch {
      accessToken = null
      localStorage.clear()
      set({ user: null, isAuthenticated: false, isLoading: false, roles: [], privileges: [] })
    }
  },

  fetchPrivileges: async () => {
    try {
      const { data } = await api.get('/admin/users/me/privileges')
      set({ privileges: data })
    } catch {
      set({ privileges: [] })
    }
  },

  hasPrivilege: (module, action) => {
    const { privileges } = get()
    return privileges.some(
      (p) => p.module === module && (p.action === action || p.action === 'manage')
    )
  },

  getAccessibleModules: () => {
    const { privileges } = get()
    const moduleSet = new Set(privileges.map((p) => p.module))
    return Array.from(moduleSet)
  },

  getAccessToken: () => accessToken,
}))

export default useAuthStore
