import { create } from 'zustand'
import api from '../api/client'

let accessToken = null

const useAuthStore = create((set, get) => ({
  user: null,
  isAuthenticated: false,
  isLoading: true,

  login: async (username, password) => {
    const { data } = await api.post('/admin/login', { username, password })
    accessToken = data.access_token
    localStorage.setItem('refresh_token', data.refresh_token)
    localStorage.setItem('access_token', data.access_token)
    set({ user: data.user, isAuthenticated: true })
    return data
  },

  logout: async () => {
    const refreshToken = localStorage.getItem('refresh_token')
    if (refreshToken) {
      try { await api.post('/admin/logout', { refresh_token: refreshToken }) } catch {}
    }
    accessToken = null
    localStorage.clear()
    set({ user: null, isAuthenticated: false })
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
      set({ user: data, isAuthenticated: true, isLoading: false })
    } catch {
      accessToken = null
      localStorage.clear()
      set({ user: null, isAuthenticated: false, isLoading: false })
    }
  },

  getAccessToken: () => accessToken,
}))

export default useAuthStore
