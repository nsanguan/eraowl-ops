# EraOwl-OPS Frontend

React-based frontend for the EraOwl-OPS ERP platform. Decoupled from backend, communicates via REST API.

## Tech Stack

- **React 19** — UI framework
- **Vite 6** — Build tool & dev server
- **react-router-dom 7** — Client-side routing
- **Tailwind CSS 4** — Utility-first CSS
- **Zustand 5** — State management
- **Axios** — HTTP client with interceptor-based auth
- **lucide-react** — Icon library

## Pages & Routes

| Path | Page | Module |
|------|------|--------|
| `/login` | Login form | admin |
| `/` | Dashboard (welcome) | — |
| `/admin/users` | User Management (CRUD, roles, CSV export) | admin |
| `/admin/roles` | Role Management (permission matrix grid) | admin |
| `/org-structure` | Org Structure (6-tab) | mdm/org_structure |
| `/party` | Party Management (4-tab) | mdm/party |
| `/items` | Item Management (3-tab) | mdm/item |
| `/bom` | BOM Management (2-tab) | bom |

## Project Structure

```
src/
├── main.jsx                  # React root mount
├── App.jsx                   # BrowserRouter with route definitions
├── index.css                 # Dark/light tokens, Tailwind v4, Inter font
├── api/
│   └── client.js             # Axios instance with auto-refresh on 401
├── store/
│   └── authStore.js          # Zustand: login, logout, checkAuth, token
├── components/
│   ├── Header.jsx            # Top bar (theme toggle, notifications, logout)
│   ├── Layout.jsx            # Sidebar + breadcrumbs + Outlet
│   └── ProtectedRoute.jsx    # Auth guard, redirect to /login
├── modules/                  # Page components per module
│   ├── admin/pages/
│   │   ├── Login.jsx
│   │   ├── UserManagement.jsx
│   │   └── RoleManagement.jsx
│   ├── bom/pages/BomPage.jsx
│   ├── mdm/
│   │   ├── item/pages/ItemPage.jsx
│   │   ├── org_structure/pages/OrgStructurePage.jsx
│   │   └── party/pages/PartyPage.jsx
│   ├── gl/                   # Placeholder
│   ├── om/                   # Placeholder
│   └── po/                   # Placeholder
├── shared-ui-kit/            # Reusable component library (33 components)
│   ├── components/
│   │   ├── ui/InteractiveGrid.tsx, StatCard.tsx, StatusChip.tsx, etc.
│   │   ├── layout/AppShell.tsx, Sidebar.tsx, Header.tsx, etc.
│   │   └── auth/AuthGate.tsx
│   ├── hooks/                # Custom React hooks
│   ├── stores/               # Zustand stores (auth, preferences)
│   ├── providers/ThemeProvider.tsx
│   ├── styles/globals.css
│   └── lib/gateway.ts, utils.ts
└── module_template/README.md # Guide for creating new frontend modules
```

## Auth Flow

1. User submits credentials via Login form
2. Backend returns Access Token (in memory/state) + Refresh Token (httpOnly cookie)
3. Axios interceptor attaches `Authorization: Bearer <access_token>` to every request
4. On 401 response, interceptor calls `/api/v1/admin/refresh` to rotate tokens
5. If refresh fails, user is redirected to `/login`

## Development

```bash
# Install dependencies
npm install

# Start dev server (port 5173, proxies /api to localhost:8000)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

The dev server proxies `/api` requests to `http://localhost:8000` (configured in `vite.config.js`).

## Shared UI Kit

The `shared-ui-kit/` directory contains 33 reusable React components used across all module pages:

- **InteractiveGrid** — Primary data table with search, pagination, CRUD, custom column rendering
- **PageHeader**, **StatCard**, **StatusChip** — Layout and display components
- **AppShell**, **Sidebar**, **Header**, **MenuTree** — Application shell components
- **Wizard**, **TreeGrid**, **ShuttleControl**, **SegmentedControl** — Advanced interaction components

Each module page imports these components from `shared-ui-kit/` rather than reimplementing common patterns.

## Docker

```bash
# Production build
docker build -t eraowl-ops-frontend .
docker run -p 3001:80 eraowl-ops-frontend
```

Nginx serves the built assets and proxies `/api` to the backend.
