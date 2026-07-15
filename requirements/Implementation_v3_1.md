# Project Plan: EraOwl-OPS - Admin & Identity Management Module (v3.1)

## 🎯 Project Goal
สร้างระบบ ERP แบบ Modular Monolith (Backend) และ Decoupled Architecture (Frontend) ครอบคลุม IAM, Master Data Management (Org Structure, Party, Item), Bill of Materials, และ Purchase Orders
โดยใช้สถาปัตยกรรมที่รองรับการเพิ่มโมดูลธุรกิจในอนาคต (GL, OM, Inventory, Manufacturing)

> **หมายเหตุจากการรีวิว:** เอกสารฉบับนี้เพิ่ม (1) ตารางที่ขาดหายไปสำหรับ production, (2) กลยุทธ์ JWT ที่ revoke สิทธิ์ได้จริง, (3) Phase สำหรับ migration/testing/deployment, (4) โครงสร้างรองรับหลายโมดูลธุรกิจในอนาคต (PO/GL/OM), (5) Master Data module (Org Structure, Party แบบ TCA-lite, Item Master) และ (6) BOM module พร้อม validation สำหรับ circular reference และ multi-level explode

---

## 🛠️ Tech Stack Specification
- **Backend:** Python 3.12+, FastAPI, Asyncpg, Pydantic v2, SQLAlchemy/SQLModel (Async Mode), **Alembic** (migrations)
- **Database:** PostgreSQL (รองรับความสัมพันธ์แบบ RBAC)
- **Cache/Session support:** Redis (สำหรับ permission versioning และ token blacklist — ดูหัวข้อ Auth Strategy)
- **Frontend:** React.js (Vite), Tailwind CSS, UI Library (shadcn/ui หรือ Ant Design)
- **Authentication:** JWT แบบ Access + Refresh Token (ไม่ใช่ stateless ล้วน — ดูเหตุผลด้านล่าง)
- **Testing:** pytest, pytest-asyncio, httpx AsyncClient, testcontainers-postgres
- **DevOps:** Docker Compose (local, network `eraowlops-global-network`), GitHub Actions (CI)

## 🔌 External Database Connection

- **Host:** `202.71.1.13`
- **Port:** `5435`
- **Database:** `eraowlops`
- **User:** `eraowlopsadmin`
- **Connection string:** `postgres://eraowlopsadmin:{password}@202.71.1.13:5435/eraowlops`
- ค่า connection อ่านจากไฟล์ `.env` (template ใน `.env.sample`) ห้าม hardcode credentials ในโค้ด หรือ commit `.env` เข้า repo
- ก่อนเริ่มพัฒนาต้อง verify การเชื่อมต่อก่อน:
  ```bash
  psql -h 202.71.1.13 -p 5435 -U eraowlopsadmin -d eraowlops -c "SELECT version();"
  ```

---

## 🏗️ Folder Structure Blueprint (Multi-Module Ready)

> โครงสร้างนี้ปรับให้รองรับการเพิ่มโมดูลธุรกิจในอนาคต (Purchase Order, GL, Order Management ฯลฯ) โดยที่แต่ละโมดูลไม่ต้องแตะโค้ดของโมดูลอื่น — ดูหลักการเพิ่มเติมที่หัวข้อ "Module Scaffolding Convention" ด้านล่าง

```text
eraowl-ops/
├── eraowl-ops-backend/
│   ├── app/
│   │   ├── core/                    # Framework-level utilities ทุกโมดูลใช้ร่วม
│   │   │   ├── config.py            # Pydantic Settings (DB, Redis, JWT, CORS)
│   │   │   ├── database.py          # AsyncSession factory (asyncpg, pool_size=20)
│   │   │   ├── security.py          # bcrypt hash/verify, JWT create/decode
│   │   │   ├── dependencies.py      # get_current_user(), check_privilege()
│   │   │   ├── middleware.py        # RequestLoggingMiddleware
│   │   │   ├── exceptions.py        # AppError, UnauthorizedError, ForbiddenError ฯลฯ
│   │   │   └── module_registry.py   # auto-discover และ mount router ของทุกโมดูล
│   │   ├── shared/                  # Domain-level utilities
│   │   │   ├── base_model.py        # TimestampMixin, SoftDeleteMixin, UUID PK base
│   │   │   ├── das_filters.py       # Dynamic filtering utilities
│   │   │   ├── events.py            # In-process pub/sub event bus
│   │   │   ├── module_base/
│   │   │   │   ├── crud.py          # BaseCRUDService<T> generic CRUD
│   │   │   │   ├── generic.py       # BaseGenericService dynamic table CRUD
│   │   │   │   └── mixins.py        # UUIDPKMixin, AuditMixin, SoftDeleteMixin
│   │   │   └── pagination.py        # PaginatedResponse<T>, PaginationParams
│   │   ├── module_template/         # Scaffold สำหรับสร้างโมดูลใหม่
│   │   │   ├── components/
│   │   │   ├── exceptions.py
│   │   │   ├── models.py
│   │   │   ├── permissions.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── services/
│   │   │   └── README.md
│   │   ├── modules/
│   │   │   ├── mdm/                         # Master Data Management
│   │   │   │   ├── org_structure/           # Corporate, Company, BU, Site, Warehouse, Locator
│   │   │   │   │   ├── router.py, schemas.py, models.py, services.py, permissions.py, exceptions.py
│   │   │   │   ├── party/                   # Address, Party, Supplier, Customer (TCA-lite)
│   │   │   │   │   ├── router.py, schemas.py, models.py, services.py, permissions.py, exceptions.py
│   │   │   │   └── item/                    # Item Master, UOM, Category, Item-Org
│   │   │   │       ├── router.py, schemas.py, models.py, services.py, permissions.py, exceptions.py
│   │   │   ├── admin/                       # IAM — Identity & Access Management
│   │   │   │   ├── models.py                # User, Role, Privilege, UserRole, RolePrivilege, UserBusinessUnit, AuditLog, RefreshToken
│   │   │   │   ├── schemas.py               # Pydantic request/response schemas
│   │   │   │   ├── router.py                # 30+ endpoints (login, refresh, logout, users CRUD, roles CRUD, privileges, audit-logs, generic CRUD)
│   │   │   │   ├── permissions.py           # Declarative privilege definitions
│   │   │   │   └── services/
│   │   │   │       ├── crud.py              # AdminService
│   │   │   │       └── generic.py           # AdminGenericService (dynamic CRUD)
│   │   │   ├── bom/                         # Bill of Materials
│   │   │   │   ├── models.py                # BomHeader, BomLine
│   │   │   │   ├── schemas.py
│   │   │   │   ├── router.py                # 12 endpoints (CRUD + approve + explode)
│   │   │   │   ├── services.py              # explode_bom(), validate_no_circular_ref()
│   │   │   │   ├── permissions.py
│   │   │   │   └── exceptions.py
│   │   │   ├── po/                          # Purchase Orders (fully implemented)
│   │   │   │   ├── models.py                # PoHeader, PoLine, PoShipment, PoDistribution, PoRelease, PoAmendment, PoApproval
│   │   │   │   ├── dto/schemas.py           # Composite request/response types
│   │   │   │   ├── router.py                # Full CRUD + composite endpoints
│   │   │   │   ├── permissions.py
│   │   │   │   ├── exceptions.py
│   │   │   │   └── services/
│   │   │   │       ├── composite.py         # PoCompositeService
│   │   │   │       ├── crud.py              # Individual CRUD services
│   │   │   │       └── generic.py           # GenericPoService
│   │   │   ├── gl/                          # General Ledger (placeholder)
│   │   │   │   └── __init__.py
│   │   │   └── om/                          # Order Management (placeholder)
│   │   └── main.py                          # FastAPI entrypoint, auto-discovers modules via module_registry
│   ├── alembic/
│   │   ├── env.py                           # Async Alembic config, imports all models
│   │   └── versions/
│   │       └── 001_initial_schema.py        # Complete schema: 5 PG schemas, 25+ tables
│   ├── scripts/
│   │   ├── 001_schema.sql
│   │   ├── 002_seed_data.sql
│   │   ├── 003_po_schema.sql
│   │   ├── 004_objects_schema.sql
│   │   ├── scan_objects.py
│   │   ├── seed_data.py
│   │   └── seed.py
│   ├── tests/
│   ├── .env
│   ├── .env.example
│   ├── Dockerfile                           # Multi-stage Python 3.12-slim
│   └── pyproject.toml
└── eraowl-ops-frontend/
    ├── src/
    │   ├── main.jsx                         # React root mount
    │   ├── App.jsx                          # BrowserRouter, aggregates routes from all modules
    │   ├── index.css                        # Dark/light tokens, Tailwind v4, Inter font
    │   ├── api/
    │   │   └── client.js                    # Axios instance with auto-refresh on 401
    │   ├── store/
    │   │   └── authStore.js                 # Zustand: login, logout, checkAuth, token management
    │   ├── components/
    │   │   ├── Header.jsx                   # Top bar: theme toggle, notifications, help, logout
    │   │   ├── Layout.jsx                   # Sidebar navigation, breadcrumbs, Outlet
    │   │   └── ProtectedRoute.jsx           # Auth guard, redirect to /login
    │   ├── modules/
    │   │   ├── admin/pages/
    │   │   │   ├── Login.jsx                # Username/password login form
    │   │   │   ├── UserManagement.jsx       # User CRUD with role assignment, CSV export
    │   │   │   └── RoleManagement.jsx       # Role CRUD with permission matrix grid
    │   │   ├── bom/pages/
    │   │   │   └── BomPage.jsx              # BOM Headers & Lines management with tabs
    │   │   ├── mdm/
    │   │   │   ├── item/pages/ItemPage.jsx  # Items, Categories, UOMs management
    │   │   │   ├── org_structure/pages/OrgStructurePage.jsx  # Corporate/Company/BU/Site/Warehouse/Locator
    │   │   │   └── party/pages/PartyPage.jsx  # Addresses, Parties, Suppliers, Customers
    │   │   ├── gl/                          # (placeholder)
    │   │   ├── om/                          # (placeholder)
    │   │   └── po/                          # (placeholder — backend implemented, frontend pending)
    │   ├── shared-ui-kit/                   # Reusable UI component library
    │   │   ├── index.ts
    │   │   ├── components/
    │   │   │   ├── auth/AuthGate.tsx
    │   │   │   ├── layout/AppShell.tsx, Header.tsx, Sidebar.tsx, MenuTree.tsx, ErrorBoundary.tsx
    │   │   │   ├── theme/ThemeRoller.tsx
    │   │   │   └── ui/ (33 components: InteractiveGrid, PageHeader, StatCard, StatusChip, ฯลฯ)
    │   │   ├── hooks/
    │   │   ├── stores/ (auth.ts, preferences.ts)
    │   │   ├── providers/ThemeProvider.tsx
    │   │   ├── styles/
    │   │   └── lib/gateway.ts, utils.ts
    │   └── module_template/
    │       └── README.md                    # Frontend module scaffold guide
    ├── nginx.conf
    ├── Dockerfile
    ├── package.json                         # React 19, Vite 6, Tailwind CSS 4, Zustand 5
    └── vite.config.js                       # Dev server:5173, proxy /api -> :8000
```

---

## 📊 Database Schema Design (RBAC Model — Revised)

**ตารางหลัก:**
- `users`: id (PK UUID), username (Unique), email (Unique), hashed_password, is_active (Boolean), created_at, updated_at, last_login_at, is_deleted (soft delete)
- `roles`: id (PK UUID), role_name (Unique), description, created_at, updated_at
- `privileges`: id (PK UUID), module, action, description

**ตารางเชื่อม (Many-to-Many):**
- `user_roles`: user_id, role_id
- `role_privileges`: role_id, privilege_id
- `user_business_units`: user_id, bu_id — **ตารางใหม่** แทนที่ `allowed_bu_id` เดิม เพื่อรองรับ user ที่ดูแลได้หลาย BU
  - ⚠️ **ปรับจากฉบับก่อนหน้า:** `bu_id` ตอนนี้ FK ไปที่ `master_data.org_structure.business_units` แทนที่จะเป็นตาราง `business_units` ของ Admin เอง — เพราะ Business Unit ไม่ใช่ concept ของ IAM แต่เป็น Master Data ที่ PO/GL/OM ก็ต้องใช้ร่วมกัน ถ้าให้ Admin เป็นเจ้าของตารางนี้ โมดูลอื่นจะต้อง import ข้าม module ผิดหลักการที่วางไว้

**ตารางเสริมสำหรับ production (ขาดในฉบับเดิม):**
- `audit_logs`: id (PK), user_id, action, target_entity, target_id, old_value (JSONB), new_value (JSONB), created_at — บันทึกการเปลี่ยน role/privilege/user ทุกครั้ง จำเป็นมากเพราะระบบนี้คุมสิทธิ์ระดับปุ่ม ถ้าไม่มี audit trail จะตรวจสอบย้อนหลังไม่ได้เมื่อเกิดปัญหา (เช่น ใครไปเปิดสิทธิ์ edit_price ให้ใคร)
- `refresh_tokens`: id (PK), user_id, token_hash, expires_at, revoked_at (nullable), created_at — จำเป็นสำหรับ revoke session ได้จริงเมื่อ logout หรือพนักงานลาออก

### PostgreSQL Schema Strategy

เนื่องจากทุกโมดูล (admin, master_data/org_structure, master_data/party, master_data/item, bom, และโมดูลธุรกิจในอนาคต) ใช้ PostgreSQL instance เดียว ควรใช้ **PostgreSQL Schema** เป็น container แยก namespace:

```sql
CREATE SCHEMA IF NOT EXISTS admin;
CREATE SCHEMA IF NOT EXISTS org_structure;
CREATE SCHEMA IF NOT EXISTS party;
CREATE SCHEMA IF NOT EXISTS item;
CREATE SCHEMA IF NOT EXISTS bom;
-- future: CREATE SCHEMA IF NOT EXISTS po;
```

**ตารางจะกลายเป็น:**
- `admin.users`, `admin.roles`, `admin.privileges`, `admin.user_roles`, `admin.role_privileges`, `admin.user_business_units`, `admin.audit_logs`, `admin.refresh_tokens`
- `org_structure.corporates`, `org_structure.companies`, `org_structure.business_units`, `org_structure.sites`, `org_structure.warehouses`, `org_structure.warehouse_locators`
- `party.addresses`, `party.parties`, `party.party_sites`, `party.party_site_uses`, `party.party_roles`, `party.suppliers`, `party.customers`
- `item.uoms`, `item.uom_conversions`, `item.item_categories`, `item.items`, `item.item_category_assignments`, `item.item_organizations`, `item.item_supplier_xref`
- `bom.bom_headers`, `bom.bom_lines`

เห็นผลดี:
- แต่ละโมดูลมี namespace ของตัวเอง — ชื่อตารางชัดเจนว่าใครเป็นเจ้าของ, ลดความเสี่ยงชื่อชนโดยบังเอิญ (เช่น `admin.users` vs `item.items` ไม่ชนกันแน่นอน)
- `search_path` ตั้งค่าใน SQLAlchemy session: `SET search_path = admin, org_structure, party, item, bom, public;` 
- FK ยัง reference ข้าม schema ได้: `admin.user_business_units.bu_id → org_structure.business_units.id`

### Docker Network Configuration

ทุก container ในโปรเจกต์นี้ใช้ Docker network `eraowlops-global-network` ร่วมกัน:

```yaml
# docker-compose.yml
networks:
  eraowlops-global-network:
    name: eraowlops-global-network
    driver: bridge

services:
  backend:
    networks:
      - eraowlops-global-network
  frontend:
    networks:
      - eraowlops-global-network
  redis:
    networks:
      - eraowlops-global-network
```

PostgreSQL เป็น external database (202.71.1.13:5435) — จึงไม่รวมอยู่ใน docker-compose ของโปรเจกต์นี้

---

## 🔐 Auth Strategy — จุดที่แก้ไขจากฉบับเดิม

ฉบับเดิมระบุว่า "แพ็ก Roles และ Privileges ทั้งหมดลงใน JWT payload" ซึ่งมี 2 ปัญหา:

1. **Token บวม** — ถ้า user มีหลาย role/privileges เยอะ ขนาด JWT อาจเกิน HTTP header limit ของบาง proxy/gateway
2. **Revoke ไม่ได้ทันที** — JWT ที่ sign แล้วจะ valid จนกว่าจะหมดอายุ ถ้า admin ไปแก้สิทธิ์ user คนหนึ่ง (เช่น ปิดสิทธิ์ edit_price) แต่ user คนนั้นยัง login ค้างอยู่ ระบบจะยังคุมสิทธิ์เดิมจน token หมดอายุ

**แนวทางที่แนะนำ:**
- JWT payload เก็บแค่ `user_id`, `role_ids`, และ `permission_version` (int)
- Backend เก็บ permission_version ปัจจุบันของแต่ละ user ไว้ (DB หรือ Redis) — ทุกครั้งที่ role/privilege ของ user เปลี่ยน ให้ increment version
- Middleware ตรวจสอบว่า version ใน token ตรงกับ version ปัจจุบันหรือไม่ ถ้าไม่ตรง → บังคับ re-login
- ใช้ Access Token อายุสั้น (15 นาที) + Refresh Token อายุยาว (7 วัน) เก็บใน httpOnly Secure Cookie แทนการเก็บใน LocalStorage ทั้งคู่ (ป้องกัน XSS)

---

## 🧩 Module Scaffolding Convention (สำหรับเพิ่ม PO / GL / OM ในอนาคต)

โครง Folder อย่างเดียวไม่พอ — ถ้าไม่มีกติกาชัดเจน พอโมดูลเพิ่มขึ้นเรื่อยๆ (PO, GL, OM, Inventory ฯลฯ) โค้ดจะเริ่มอ้างอิงข้ามโมดูลกันมั่วจนกลายเป็น "Big Ball of Mud" ทั้งที่ตั้งใจทำ Modular Monolith แต่แรก กติกาที่ควรตรึงไว้:

**1. ทุกโมดูลต้องมีหน้าตาเหมือนกันทุกไฟล์** (`router.py`, `schemas.py`, `models.py`, `services.py`, `permissions.py`, `exceptions.py`) — ทำให้ AI coding tool หรือ dev คนใหม่เดาโครงสร้างโมดูลใหม่ได้จาก pattern เดิมโดยไม่ต้องอ่าน spec ใหม่ทุกครั้ง

**2. `permissions.py` ของแต่ละโมดูล ประกาศ privilege ของตัวเองแบบ declarative** เช่น
```python
# modules/po/permissions.py
MODULE_NAME = "po"
PRIVILEGES = [
    {"action": "view", "description": "ดู PO"},
    {"action": "create", "description": "สร้าง PO"},
    {"action": "approve", "description": "อนุมัติ PO"},
]
```
แล้วให้ script ตอน seed/migration ไล่อ่านทุกโมดูลมา insert ลงตาราง `privileges` อัตโนมัติ — Admin module (RoleManagement.jsx) จะเห็น privilege ของ PO/GL/OM ขึ้นเองโดยไม่ต้องไปแก้โค้ด Admin ทุกครั้งที่เพิ่มโมดูลใหม่

**3. ห้าม import ข้าม `models.py` ของโมดูลอื่นโดยตรง (no direct cross-module DB joins)** — ถ้า PO ต้องรู้ข้อมูล GL account ให้เรียกผ่าน `services.py` ของ GL เท่านั้น (function call ภายในโมดูล monolith เดียวกันก็จริง แต่รักษาขอบเขตไว้) เหตุผล: วันหน้าถ้าต้องแยก GL ออกเป็น microservice จริง จะทำได้โดยแก้แค่ implementation ของ service layer ไม่ต้องรื้อทั้งระบบ
   - ถ้าต้องการความหลวมกว่านั้น (เช่น PO อนุมัติเสร็จแล้วต้องให้ GL สร้าง journal entry) ใช้ `shared/events.py` เป็น internal event bus แทนการเรียก service ตรงๆ — PO publish event `po.approved`, GL subscribe แล้วทำงานของตัวเอง

**4. `module_registry.py` เป็นจุดเดียวที่ `main.py` ต้อง import** — เพิ่มโมดูลใหม่แค่ให้ registry เดินหาโฟลเดอร์ใน `modules/` ที่มี `router.py` แล้ว mount อัตโนมัติ (prefix `/api/v1/{module_name}`) ไม่ต้องแก้ `main.py` ทุกครั้งที่เพิ่มโมดูล

**5. Frontend mirror หลักการเดียวกัน** — แต่ละโมดูลมี `routes.jsx` export ของตัวเอง, `App.jsx` แค่ import และ spread routes จากทุกโมดูล, เมนู sidebar อ่านจาก privilege ที่ user มี (field `module` ใน token/permission cache) เพื่อซ่อน/โชว์เมนูอัตโนมัติโดยไม่ต้อง hardcode ว่า user คนไหนเห็นเมนู PO/GL/OM

**6. Migration เดียวกันทั้งระบบ** — เพราะเป็น Modular Monolith ใช้ DB เดียว, Alembic migration history จึงรวมทุกโมดูลไว้ chain เดียว ไม่แยกเป็นคนละ migration history ต่อโมดูล (ต่างจาก microservice ที่แยก DB ต่อ service)

---

## 🏢 Master Data Structure — Corporate / Company / Site / BU / Warehouse / Supplier / Customer

Master data พวกนี้ (Corporate, Company, Site, Business Unit, Warehouse, Warehouse Locator, Address, Supplier, Customer) **ไม่ควรอยู่ใต้ Admin และไม่ควรอยู่ใต้โมดูลธุรกิจไหนโมดูลหนึ่ง** (เช่น PO) เพราะทุกโมดูล (PO ใช้ Supplier+Warehouse, GL ใช้ Company+BU, OM ใช้ Customer+Warehouse) ต้องอ้างอิงข้อมูลชุดนี้ร่วมกัน ถ้าไปฝากไว้ใต้โมดูลใดโมดูลหนึ่งจะเกิดปัญหา circular dependency ทันที จึงแยกเป็นโมดูลรากฐานของตัวเอง `master_data/` แบ่งเป็น 2 กลุ่มย่อยเพราะสิทธิ์การจัดการต่างกันชัดเจน (ผู้ดูแลโครงสร้างองค์กรกับผู้ดูแล Supplier/Customer มักเป็นทีมคนละทีม):

### 1. `org_structure` — โครงสร้างองค์กร (Enterprise Hierarchy)

ลำดับชั้น: **Corporate → Company → Business Unit → Site → Warehouse → Warehouse Locator**

- `corporates`: id (PK UUID), corp_name, corp_code (Unique)
- `companies`: id (PK UUID), corporate_id (FK), legal_name, tax_id, company_code (Unique)
- `business_units`: id (PK UUID), company_id (FK), bu_name, bu_code (Unique) — ย้ายมาจาก Admin module ตามที่อธิบายด้านบน
- `sites`: id (PK UUID), business_unit_id (FK), site_name, site_code, address_id (FK → `party.addresses`)
- `warehouses`: id (PK UUID), site_id (FK), warehouse_name, warehouse_code
- `warehouse_locators`: id (PK UUID), warehouse_id (FK), zone, aisle, rack, bin, locator_code (Unique ต่อ warehouse)

ทุกตารางมี `created_at`, `updated_at`, `is_active`, `is_deleted` (soft delete) ตาม convention กลาง

### 2. `party` — TCA-lite Party Model (ดีกว่าการแยกตาราง Supplier/Customer โดด ๆ)

คำถามที่ถามว่า "TCA หรือดีกว่า" — คำตอบคือใช้แนวคิดหลักของ TCA (Party ผูกกับ Role แทนการแยกตาราง Supplier/Customer เต็มรูปแบบตั้งแต่ต้น) แต่ตัด complexity ส่วนที่ Oracle TCA เต็มรูปแบบมีเยอะเกินความจำเป็น (เช่น Party Relationships หลายชั้น, Classification hierarchy) ออกไปก่อน เพิ่มทีหลังได้ถ้าจำเป็นจริง

**ปัญหาของการแยกตาราง `suppliers` และ `customers` ตรง ๆ (แบบที่ระบบเก่ามักทำ):**
- คู่ค้าเดียวกันที่เป็นทั้ง Supplier และ Customer (พบบ่อยในธุรกิจ B2B) ต้องกรอกข้อมูลที่อยู่/ข้อมูลบริษัทซ้ำ 2 รอบ ข้อมูลไม่ sync กัน
- เพิ่ม role ใหม่ในอนาคต (เช่น Carrier, Broker, Sub-contractor) ต้องสร้างตารางใหม่ทุกครั้งพร้อม address logic ซ้ำเดิม

**โครงสร้างที่แนะนำ:**
- `addresses`: id (PK UUID), address_line1, address_line2, city, state_province, postal_code, country_code, latitude, longitude — ตารางที่อยู่กลาง ใช้ร่วมกันทั้ง Site และ Party
- `parties`: id (PK UUID), party_type (`PERSON` / `ORGANIZATION`), party_name, tax_id, is_active — entity กลาง 1 แถวต่อ 1 นิติบุคคล/บุคคลจริง ไม่ว่าจะเล่นบทบาทไหน
- `party_sites`: id (PK UUID), party_id (FK), address_id (FK), site_name, is_primary — 1 party มีได้หลายที่อยู่ (สำนักงานใหญ่, โกดัง, จุดส่งของ)
- `party_site_uses`: id (PK UUID), party_site_id (FK), use_type (`BILL_TO` / `SHIP_TO` / `REMIT_TO` / `GENERAL`) — 1 ที่อยู่ใช้ได้หลายวัตถุประสงค์ เช่น ที่อยู่เดียวกันเป็นทั้ง Ship-to และ Bill-to
- `party_roles`: id (PK UUID), party_id (FK), role_type (`SUPPLIER` / `CUSTOMER` / `CARRIER` / ...), unique(party_id, role_type) — บอกว่า party นี้เล่นบทบาทอะไรบ้าง เพิ่ม role ใหม่ในอนาคตแค่เพิ่มค่าใน enum ไม่ต้องสร้างตารางใหม่
- `suppliers`: id (PK UUID), party_id (FK Unique), supplier_code (Unique), payment_term_days, currency — attribute เฉพาะฝั่ง Supplier เท่านั้น
- `customers`: id (PK UUID), party_id (FK Unique), customer_code (Unique), credit_limit, payment_term_days — attribute เฉพาะฝั่ง Customer เท่านั้น

**ผลลัพธ์:** คู่ค้าที่เป็นทั้ง Supplier และ Customer = 1 แถวใน `parties` + 1 แถวใน `party_sites` (ที่อยู่เดียว ใช้ร่วมกัน) + 2 แถวใน `party_roles` (SUPPLIER, CUSTOMER) — ไม่ต้องกรอกซ้ำ ไม่ต้อง sync ข้อมูลข้าม 2 ตาราง

### 3. Coupling ระหว่าง `org_structure` และ `party`

สองโมดูลย่อยนี้เป็น Master Data ด้วยกัน อัตราการเปลี่ยนแปลง schema ต่ำและเสถียรกว่าโมดูลธุรกิจ จึงอนุญาตให้ FK ข้ามกันได้โดยตรง (เช่น `sites.address_id` → `party.addresses.id`) ต่างจากกติกาเข้มงวดที่ใช้กับโมดูลธุรกิจ (PO/GL/OM/Admin) ซึ่ง**ต้องเรียกผ่าน `services.py` ของ `master_data` เท่านั้น ห้าม import model ตรง** — เช่น PO ต้องการ default warehouse ของ supplier ให้เรียก `master_data.party.services.get_supplier_default_warehouse()` ไม่ใช่ query ตาราง `suppliers`/`warehouses` เอง

### 4. Privilege Design สำหรับ Master Data

แยก privilege module string เป็น `org_structure` และ `party` (ไม่รวมเป็น `master_data` เดียว) เพราะทีมที่ดูแลต่างกันจริงในองค์กรส่วนใหญ่:
- `org_structure`: actions `view`, `manage_corporate`, `manage_company`, `manage_site`, `manage_warehouse`, `manage_locator` — ปกติทีม IT/Finance เป็นคนคุม
- `party`: actions `view`, `manage_supplier`, `manage_customer`, `manage_address` — ปกติทีม Purchasing คุม Supplier, ทีม Sales คุม Customer แยกกัน (อาจแตกเป็น `view_supplier`/`manage_supplier` กับ `view_customer`/`manage_customer` แยกกันเลยถ้าต้องการละเอียดกว่านี้)

---

## 📦 Item Master & BOM — Enterprise-Grade Design

### 1. Item Master → อยู่ใต้ `master_data/item` (ไม่ใช่ `bom`, ไม่ใช่ `po`)

Item Master เป็น master data เหมือน org_structure/party — PO ใช้ซื้อ item, OM ใช้ขาย item, Warehouse ใช้เก็บ item, GL ใช้ผูก item กับบัญชีต้นทุน, BOM ใช้ item เป็น component จึงต้องอยู่ใต้ `master_data` เป็นรากฐานเดียวกัน หลักการออกแบบที่ enterprise ระดับ Oracle/SAP ใช้ (แยก **Item Definition** ออกจาก **Item-Organization Attribute**) ควรนำมาใช้ตั้งแต่ต้น เพราะแก้ทีหลังจะกระทบข้อมูล transaction จำนวนมาก:

- `uoms`: id (PK UUID), uom_code (Unique), uom_name, uom_type (`QUANTITY`/`WEIGHT`/`VOLUME`/`LENGTH`)
- `uom_conversions`: id (PK UUID), from_uom_id (FK), to_uom_id (FK), item_id (FK, nullable) — nullable เพื่อรองรับทั้ง conversion กลาง (เช่น 1 กล่อง = 12 ชิ้น ใช้ได้ทุก item) และ conversion เฉพาะ item (เช่น item นี้ 1 ม้วน = 50 เมตร)
- `item_categories`: id (PK UUID), category_set (`PURCHASING`/`SALES`/`INVENTORY`/`COSTING`), category_code, category_name, parent_category_id (self-FK, รองรับ hierarchy) — enterprise จริงต้องมีหลาย category set ต่อ item พร้อมกัน ไม่ใช่ category เดียว
- `items`: id (PK UUID), item_code (Unique), item_name, item_type (`FINISHED_GOOD`/`RAW_MATERIAL`/`SUB_ASSEMBLY`/`SERVICE`), primary_uom_id (FK), status (`ACTIVE`/`PENDING`/`OBSOLETE`), description — **นี่คือ Item Definition ระดับองค์กร ไม่ผูกกับ warehouse ใดๆ**
- `item_category_assignments`: item_id (FK), category_id (FK) — M2M เพราะ item เดียวอยู่ได้หลาย category set พร้อมกัน
- `item_organizations`: id (PK UUID), item_id (FK), warehouse_id (FK → `org_structure.warehouses`), min_qty, max_qty, lead_time_days, costing_method, standard_cost, is_enabled — **นี่คือ Item-Organization Attribute** ข้อมูลเดียวกันแต่ค่า min/max/cost ต่างกันได้ต่อคลัง (Item นี้ enable ที่คลัง A แต่ไม่ enable ที่คลัง B ก็ได้)
- `item_supplier_xref`: id (PK UUID), item_id (FK), supplier_id (FK → `party.suppliers`), supplier_item_code, is_preferred — Approved Supplier List เบื้องต้น สำหรับ PO ใช้ตอนดึงราคา/lead time จาก supplier ที่ผูกไว้

**ทำไมต้องแยก Item Definition ออกจาก Item-Organization:** ถ้ารวมกันเป็นตารางเดียว (item + คลังในแถวเดียว) พอ item ตัวเดียวเปิดใช้ใน 5 คลัง ข้อมูล item_name/item_code จะซ้ำ 5 แถว แก้ชื่อ item ต้องแก้ 5 ที่ และเสี่ยงข้อมูลไม่ตรงกัน

### 2. BOM → แยกเป็นโมดูลของตัวเอง `modules/bom` (ไม่ใช่ `master_data/bom`)

จุดนี้ต่างจาก Item Master — BOM ไม่ใช่ static reference data เหมือน address/site แต่มี **lifecycle การอนุมัติ (revision, effective date, approval workflow)** คล้ายเอกสารธุรกิจมากกว่า master data นิ่งๆ จึงควรแยกเป็นโมดูลธุรกิจของตัวเอง (ตาม pattern เดียวกับ PO/GL/OM) ไม่ใช่ยัดใต้ `master_data`

- `bom_headers`: id (PK UUID), item_id (FK → `master_data.item.items`, คือ item ที่เป็น "ตัวประกอบ/Assembly"), alternate_bom_code (nullable, รองรับหลายสูตรของ item เดียวกัน), revision, status (`ACTIVE`/`PENDING_APPROVAL`/`OBSOLETE`), effective_date_from, effective_date_to
- `bom_lines`: id (PK UUID), bom_header_id (FK), component_item_id (FK → `master_data.item.items`), quantity_per, uom_id (FK), operation_seq (nullable, เผื่อเชื่อม Routing ในอนาคต), effective_date_from, effective_date_to

**กติกาที่ service layer ต้องมี (สำคัญมากสำหรับ BOM โดยเฉพาะ):**
- **Validate circular reference** — component_item_id ห้ามย้อนกลับไปเป็น ancestor ของตัวเองในต้นไม้ BOM (เช่น A ใช้ B เป็นส่วนประกอบ, B ห้ามใช้ A เป็นส่วนประกอบอีกที ไม่ว่าจะกี่ level) ต้อง validate ตอน insert/update ทุกครั้ง ไม่งั้น multi-level explode จะ infinite loop
- **Multi-level BOM explode** — เขียนฟังก์ชัน recursive `explode_bom(item_id, quantity)` ใน services.py คืนค่ารายการ component ทุก level พร้อมปริมาณที่คูณทบกันแล้ว (ใช้สำหรับ MRP/costing ในอนาคต)
- **Effective dating** — รองรับ BOM หลายเวอร์ชันของ item เดียวกันคาบเกี่ยวช่วงเวลากันได้ (สำหรับ Engineering Change) โดย query ต้อง filter ตามวันที่ใช้งานจริงเสมอ ไม่ใช่ดึง revision ล่าสุดตรงๆ

**Roadmap ที่ยังไม่ต้องสร้างตอนนี้ แต่ออกแบบเผื่อไว้:** `routings` / `routing_operations` / `work_centers` (สำหรับ Manufacturing Order ในอนาคต) และ `engineering_change_orders` (ECO) — field `operation_seq` ใน `bom_lines` กันที่ไว้แล้วเพื่อไม่ต้อง migrate schema ใหญ่ตอนขยาย

### 3. Privilege เพิ่มเติม

- `item`: actions `view`, `manage_item`, `manage_category`, `manage_uom`, `manage_item_organization` — ปกติทีม Product/Supply Chain คุม
- `bom`: actions `view`, `create`, `edit`, `approve` — แยก `approve` ออกจาก `edit` ชัดเจน เพราะ BOM มี workflow อนุมัติก่อนใช้งานจริง (คนสร้าง BOM กับคนอนุมัติมักเป็นคนละคน ตรงกับ pattern "ดูได้แต่แก้ไม่ได้" ที่โปรเจกต์นี้ต้องการอยู่แล้ว)

---

## 📋 Implementation Status (Actual vs. Plan)

### ✅ Completed (Phases 1-6 fully implemented)

| Phase | Description | Status | Notes |
|-------|-------------|--------|-------|
| 1 | Backend Core Setup | ✅ Complete | `core/config.py`, `database.py`, `security.py`, `dependencies.py`, `middleware.py`, `exceptions.py`, `module_registry.py` — all implemented |
| 2 | Master Data Foundation | ✅ Complete | Under `mdm/` (not `master_data/` as planned). All 3 sub-modules: `org_structure`, `party`, `item` with full CRUD, services, permissions |
| 2.5 | Bill of Materials | ✅ Complete | `bom/` module with `explode_bom()`, `validate_no_circular_ref()`, approve workflow |
| 3 | Admin Module IAM | ✅ Complete | Users, Roles, Privileges, User-Role mapping, Business Unit assignment, Audit Logs, Refresh Tokens, generic CRUD |
| 4 | Authentication & Authorization | ✅ Complete | JWT with Access+Refresh tokens, `check_privilege()`, permission versioning, httpOnly cookies |
| 4.5 | Database Migrations | ✅ Complete | Single Alembic migration (`001_initial_schema.py`) covering all schemas: `org_structure`, `party`, `item`, `admin`, `bom`, `po` |
| 5 | Frontend Auth & Routing | ✅ Complete | Zustand authStore, axios interceptor with auto-refresh, ProtectedRoute, Layout with sidebar |
| 6 | Admin Management Screens | ✅ Complete | Login, UserManagement (with search/pagination/CSV export), RoleManagement (with permission matrix grid) |

### ➕ Beyond Original Plan

| Feature | Description |
|---------|-------------|
| **PO Module** | Fully implemented backend (not just a placeholder). 12+ entities: PoHeader, PoLine, PoShipment, PoDistribution, PoRelease, PoAmendment, PoApproval with composite CRUD services |
| **shared-ui-kit/** | 33 reusable React components (InteractiveGrid, Sidebar, AppShell, Wizard, TreeGrid, ShuttleControl, ฯลฯ) built as an internal UI library |
| **module_template/** | Scaffold for backend modules with README guide — lets AI/devs clone a new module in minutes |
| **scripts/** | SQL scripts (schema, seed data) and Python seed scripts for database initialization |
| **Design System** | EraOwl Design System (EODS v1.0.0) in `design/eraowl-ds/` — 12 CSS files, 1496-line JS utility library, 33-component shared UI kit |
| **Base Generic Service** | `BaseGenericService` for dynamic table CRUD — allows API CRUD on any table without writing module-specific code |
| **Docker Compose** | 3 services: backend (:8000), frontend (:3001), redis (:6379) on shared `eraowlops-global-network` |

### 📝 Plan Deviations

| Item | Planned | Actual |
|------|---------|--------|
| Master Data location | `modules/master_data/` | `modules/mdm/` |
| Frontend BOM pages | `modules/bom/` pages | `modules/bom/pages/BomPage.jsx` |
| PO module | Placeholder only | Fully implemented backend + services |
| Item number of tables | `items` + `item_organizations` | As planned, with additional `item_supplier_xref` and `item_category_assignments` |
| Frontend `master_data/` pages | `modules/master_data/` | `modules/mdm/` with 3 sub-modules mirroring backend |
| Shared UI Kit | Not planned | 33-component library under `shared-ui-kit/` |
| Backend module template | Not planned | `module_template/` with README scaffold guide |

### 🔜 Not Yet Started

| Item | Phase | Priority |
|------|-------|----------|
| GL module frontend & backend | Placeholder only | Medium |
| OM module frontend & backend | Placeholder only | Medium |
| PO module frontend pages | Backend done, frontend pending | Medium |
| Test suite (pytest) | Phase 7 | High |
| CI/CD (GitHub Actions) | Phase 8 | High |
| BOM multi-level tree view on frontend | Enhancement | Low |

---

## 🔍 Definition of Done (DoD) — Revised

- ยูสเซอร์ login ผ่านหน้าบ้าน ได้รับ Access Token + Refresh Token (httpOnly cookie) และเก็บสิทธิ์ลง Store สำเร็จ
- โครงสร้างสิทธิ์ระดับละเอียด `{"module": "order_entry", "action": "edit_price"}` ตรวจสอบจาก DB/cache จริง ไม่ใช่เชื่อ token อย่างเดียว
- แก้สิทธิ์ role แล้ว user ที่ login ค้างอยู่ถูก invalidate ภายใน request ถัดไป (ผ่าน permission_version)
- ระบบบล็อก/เปิดปุ่มบน Frontend ตามสิทธิ์จริง
- Backend ทั้งหมด async, มี migration history ผ่าน Alembic, มี test coverage สำหรับ auth/RBAC logic
- ทุกการเปลี่ยนแปลง role/privilege ถูกบันทึกใน audit_logs
- Item Master แยก Item Definition กับ Item-Organization Attribute ชัดเจน (item เดียวเปิดใช้หลายคลังได้โดยไม่ต้องซ้ำข้อมูล)
- BOM ป้องกัน circular reference ได้ที่ระดับ service layer และ `explode_bom()` คืนค่าถูกต้องสำหรับ BOM หลายระดับ
