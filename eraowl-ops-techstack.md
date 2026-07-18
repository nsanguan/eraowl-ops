# EraOwl-OPS Tech Stack

## Backend

| Category | Technology | Version |
|----------|-----------|---------|
| **Language** | Python | >= 3.12 |
| **Framework** | FastAPI | >= 0.115.0 |
| **ASGI Server** | Uvicorn (with standard extras) | >= 0.32.0 |
| **ORM** | SQLAlchemy (async) | >= 2.0.36 |
| **ORM + Pydantic** | SQLModel | >= 0.0.22 |
| **DB Driver** | asyncpg (async) | >= 0.30.0 |
| | psycopg2-binary (sync, Alembic) | >= 2.9.10 |
| **Migrations** | Alembic | >= 1.14.0 |
| **Validation** | Pydantic | >= 2.10.0 |
| **Settings** | pydantic-settings | >= 2.7.0 |
| **Auth (JWT)** | python-jose + cryptography | >= 3.3.0 |
| **Password Hashing** | passlib[bcrypt] | >= 1.7.4 |
| | bcrypt | >= 4.1.0 |
| **File Uploads** | python-multipart | >= 0.0.18 |
| **Cache / Token Store** | Redis (redis-py) | >= 5.2.0 |
| **Rate Limiting** | slowapi | >= 0.1.9 |
| **HTTP Client** | httpx | >= 0.28.0 |
| **Data Analysis** | pandas | >= 2.2.0 |
| **Build System** | setuptools | >= 75.0 |
| **CI DB Service** | PostgreSQL (Docker) | 17 |

### Dev / Testing

| Technology | Version |
|-----------|---------|
| pytest | >= 8.3.0 |
| pytest-asyncio | >= 0.24.0 |
| testcontainers[postgres] | >= 4.9.0 |

---

## Frontend

| Category | Technology | Version |
|----------|-----------|---------|
| **Language** | JavaScript (ES modules, JSX) | — |
| **Runtime** | Node.js | 22 |
| **UI Framework** | React | ^19.0.0 |
| **DOM Rendering** | react-dom | ^19.0.0 |
| **Routing** | react-router-dom | ^7.0.0 |
| **State Management** | Zustand | ^5.0.0 |
| **HTTP Client** | axios | ^1.7.0 |
| **Build Tool** | Vite | ^6.0.0 |
| **Vite Plugin - React** | @vitejs/plugin-react | ^4.3.0 |
| **CSS Framework** | Tailwind CSS | ^4.0.0 |
| **Tailwind Vite Plugin** | @tailwindcss/vite | ^4.0.0 |
| **Icons** | lucide-react | ^0.460.0 |
| **Class Utilities** | clsx | ^2.1.1 |
| **Class Merge** | tailwind-merge | ^3.6.0 |
| **Production Server** | nginx (Docker) | alpine |

---

## Database

| Technology | Version |
|-----------|---------|
| PostgreSQL | 15+ |
| Schema Isolation | 6 schemas: `admin`, `org_structure`, `party`, `item`, `bom`, `po` |
| Async Driver | asyncpg |
| Sync Driver | psycopg2-binary |

---

## Cache / Middleware

| Technology | Version | Purpose |
|-----------|---------|---------|
| Redis | 7 (alpine) | Token blacklist, permission versioning |

---

## Infrastructure

| Component | Technology |
|-----------|-----------|
| **Orchestration** | Docker Compose |
| **Backend Container** | python:3.12-slim (multi-stage) |
| **Frontend Container** | node:22-alpine build → nginx:alpine serve |
| **CI/CD** | GitHub Actions |
| **Network** | Docker bridge network (`eraowlops-global-network`) |

---

## Architecture Patterns

- **Modular Monolith**: Auto-discovered modules under `app/modules/{name}/` mounted at `/api/v1/{name}`
- **Generic CRUD**: `BaseCRUDService<T>` with soft-delete, pagination, search, filters
- **Auth**: JWT (access + refresh tokens via httpOnly cookies), bcrypt hashing, permission versioning, Redis token blacklist
- **Rate Limiting**: slowapi on auth endpoints (login 10/min, refresh 20/min)
- **API Style**: RESTful with `/{entity_id}` path params, pagination via query params
- **RBAC**: Per-module privilege enforcement via `check_privilege(module, action)` dependency
- **Frontend Pattern**: Tabbed pages with `InteractiveGrid` for CRUD, Zustand stores, axios interceptors for token refresh

---

## Design System

| Component | Details |
|-----------|---------|
| **EraOwl Design System (EODS)** | Located in `design/eraowl-ds/` |
| **CSS** | 350+ custom properties, OKLCH color space, `.eods-*` class prefix |
| **JS Utilities** | 1496-line vanilla JS utility library |
| **Fonts** | Inter (body), JetBrains Mono (code) |
| **Themes** | Light / Dark mode support |
