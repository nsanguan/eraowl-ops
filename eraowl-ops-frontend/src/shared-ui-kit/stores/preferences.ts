import { create } from 'zustand';

export interface Warehouse {
  id: string;
  code: string;
  name: string;
}

export interface AIProvider {
  id: 'openai' | 'ollama' | 'open-webui' | 'none';
  name: string;
  apiUrl: string;
  apiKey: string;
  model: string;
}

export interface PreferencesState {
  warehouses: Warehouse[];
  selectedWarehouseIds: string[];
  aiProvider: AIProvider;
  setSelectedWarehouses: (ids: string[]) => void;
  toggleWarehouse: (id: string) => void;
  selectAllWarehouses: () => void;
  clearWarehouses: () => void;
  setAIProvider: (provider: Partial<AIProvider>) => void;
  isWarehouseSelected: (id: string) => boolean;
  getSelectedWarehouseCodes: () => string[];
}

const STORAGE_KEY = 'axonos-preferences';

function loadFromStorage(): Partial<PreferencesState> {
  if (typeof localStorage === 'undefined') return {};
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

function saveToStorage(state: { selectedWarehouseIds: string[]; aiProvider: AIProvider }) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      selectedWarehouseIds: state.selectedWarehouseIds,
      aiProvider: state.aiProvider,
    }));
  } catch {
    // ignore
  }
}

const stored = loadFromStorage();

export const usePreferencesStore = create<PreferencesState>((set: (partial: Partial<PreferencesState> | ((state: PreferencesState) => Partial<PreferencesState>)) => void, get: () => PreferencesState) => ({
  warehouses: [],
  selectedWarehouseIds: stored.selectedWarehouseIds ?? [],
  aiProvider: stored.aiProvider ?? {
    id: 'open-webui',
    name: 'Open WebUI',
    apiUrl: 'http://localhost:3000',
    apiKey: '',
    model: '',
  },

  setSelectedWarehouses: (ids: string[]) => {
    set({ selectedWarehouseIds: ids });
    saveToStorage({ selectedWarehouseIds: ids, aiProvider: get().aiProvider });
  },

  toggleWarehouse: (id: string) => {
    const current = get().selectedWarehouseIds;
    const next = current.includes(id)
      ? current.filter((w) => w !== id)
      : [...current, id];
    set({ selectedWarehouseIds: next });
    saveToStorage({ selectedWarehouseIds: next, aiProvider: get().aiProvider });
  },

  selectAllWarehouses: () => {
    const allIds = get().warehouses.map((w) => w.id);
    set({ selectedWarehouseIds: allIds });
    saveToStorage({ selectedWarehouseIds: allIds, aiProvider: get().aiProvider });
  },

  clearWarehouses: () => {
    set({ selectedWarehouseIds: [] });
    saveToStorage({ selectedWarehouseIds: [], aiProvider: get().aiProvider });
  },

  setAIProvider: (provider) => {
    const next = { ...get().aiProvider, ...provider };
    set({ aiProvider: next });
    saveToStorage({ selectedWarehouseIds: get().selectedWarehouseIds, aiProvider: next });
  },

  isWarehouseSelected: (id) => get().selectedWarehouseIds.includes(id),

  getSelectedWarehouseCodes: () => {
    const state = get();
    return state.warehouses
      .filter((w) => state.selectedWarehouseIds.includes(w.id))
      .map((w) => w.code);
  },
}));