# AxonOS → EraOwl-OPS Migration Implementation Plan

**Plan ID:** `axonos_migration_plan`
**Date:** 2026-07-20
**Author:** AI Agent (opencode)
**Status:** Draft for execution in future step

---

## 1. Objective

Migrate the AxonOS ERP database (`AXONDB` — `axonosdb` @ `202.71.1.13:5435`) into the **EraOwl-OPS** Modular Monolith so that the 17 AxonOS application schemas become first-class, auto-discovered FastAPI backend modules and corresponding React frontend pages, following the existing EraOwl-OPS architecture (SQLModel + `BaseCRUDService` + `module_registry` auto-mount + single Alembic chain + EODS frontend kit).

The full AXONDB schema has already been extracted and saved to `/requirements/axonos/schema/` (see `README.md` there):
`full_schema.sql` (DDL), `tables.csv`, `columns.csv` (21,659 cols), `indexes.csv` (2,482), `foreign_keys.csv` (1,239), `schema_summary.csv`.

---

## 2. Source Inventory (from extracted schema)

| AxonOS Schema | Renamed Module | Tables | Views | Columns (approx) | EraOwl Domain |
|---------------|----------------|-------:|------:|-----------------:|---------------|
| `ap`  | `ap`   | 36 | 10 | 741  | Accounts Payable |
| `ar`  | `ar`   | 34 | 3  | 705  | Accounts Receivable |
| `eam` | `eam`  | 92 | 18 | 2386 | Enterprise Asset Mgmt |
| `exp` | `exp`  | 4  | 2  | ~60  | Expenses |
| `fa`  | `fa`   | 77 | 13 | ~1200| Fixed Assets |
| `gl`  | `gl`   | 23 | 3  | 311  | General Ledger |
| `inv` | `inv`  | 35 | 9  | ~600 | Inventory |
| `log` | **`tms`** | 116 | 16 | 2381 | Transportation Mgmt (rename) |
| `mes` | `mes`  | 123 | 5  | ~2100| Manufacturing Exec. |
| `om`  | `om`   | 18 | 5  | ~300 | Order Management |
| `po`  | `po`   | 33 | 8  | (exists) | Purchase Orders (exists, align) |
| `prod`| **`prd`** | 21 | 2  | 303  | Production (rename) |
| `qc`  | `qc`   | 83 | 10 | 2377 | Quality Control |
| `scm` | `scm`  | 168 | 11 | 2850 | Supply Chain Mgmt |
| `sup` | `sup`  | 4  | 2  | ~60  | Suppliers |
| `tax` | `tax`  | 90 | 8  | 1319 | Tax |
| `wms` | `wms`  | 8  | 4  | 131  | Warehouse Mgmt |
| `cron`| `cron` | 2  | 0  | — | Scheduled jobs (owned by postgres) |

**Total:** ~1,188 tables, ~93 views, ~21,659 columns, 1,239 FKs.

### Special cases
- **`log` → `tms`** and **`prod` → `prd`**: rename at module, router prefix, schema folder, and DB schema level. The DB schema name itself should be renamed (or an alias schema created) so `__table_args__={"schema": "tms"}` matches.
- **`cron`**: owned by `postgres`, only 2 tables — create a `cron` module but treat as a low-priority/utility module (job schedules). Keep separate from business modules.
- **`public` schema (23 tables in AXONDB)**: this is *legacy AxonOS public*, NOT the eraowl-ops `core.*` tables (those live in eraowl-ops' own `public`). **Decision: exclude AXONDB `public` from migration** — it overlaps with eraowl-ops' existing `mdm`/`admin`/`bom`/`po` data model. Flag for manual review.
- **`mdm`, `core`, `admin`, `collab`, `bom`, `reporting`, `app`, `ar` shared types**: eraowl-ops already has `mdm`, `admin`, `bom`, `po`, `collab`. AXONDB `mdm` (94 tbl) is the canonical master data source — it is the FK hub (sites/companies/corporates/items referenced by 16+ schemas). **Migrate `mdm` first** as the shared-dimension backbone.

### Cross-schema dependency insight (from `foreign_keys.csv`)
Heavy FK fan-in to `mdm` (items, sites, companies, corporates) and to intra-schema self-references. Migration/implementation **ordering must be**: `mdm` (shared dims) → dependent operational modules → `gl`/`fa`/`tax` (financial, often depend on everything).

---

## 3. Target Architecture Mapping

Each AxonOS schema → one EraOwl-OPS backend module folder:

```
eraowl-ops-backend/app/modules/
├── tms/          (from log)      ├── models.py | schemas.py | router.py | services.py | permissions.py | exceptions.py
├── prd/          (from prod)
├── ap/  ar/  eam/ exp/ fa/  gl/  inv/ mes/ om/  po/  qc/  scm/ sup/ tax/ wms/ cron/
```

Frontend:
```
eraowl-ops-frontend/src/modules/
├── tms/  prd/  ap/  ar/  ...   each: pages/ components/ api/ routes.jsx
```

Naming rules:
- Module folder = target module name (`tms`, `prd`, etc.).
- API prefix auto-derived by `module_registry` = `/api/v1/{folder}` → so `log` folder must be named `tms` to get `/api/v1/tms`.
- DB schema in `models.py` `__table_args__` = the **actual PostgreSQL schema name**. Two options:
  - **(A) Rename DB schema** `ALTER SCHEMA log RENAME TO tms;` and `prod`→`prd` (cleanest; do once in a migration).
  - **(B) Keep DB schema `log`/`prod`, set `{"schema": "log"}` in models but mount router at `tms`.** Not recommended (confusing).
  - **Plan uses (A).**

---

## 4. Implementation Phases

### Phase 0 — Prerequisites & Decisions
- [ ] Confirm EXCLUDE of AXONDB `public` schema (legacy overlap).
- [ ] Decide schema rename strategy (A: `ALTER SCHEMA`). Create Alembic migration `000X_rename_log_prod_schemas.py`.
- [ ] Confirm `cron` inclusion scope (utility jobs only).
- [ ] Add `AXONDB` source connection to `.env` (read-only extract) for any differential sync scripts.

### Phase 1 — Shared Dimension Backbone (`mdm`)
- [ ] Migrate AXONDB `mdm` (94 tbl) — already partially mirrored by eraowl-ops `mdm` (org_structure/party/item). **Reconcile**: add missing AXONDB `mdm` tables (e.g., sites, companies, corporates, items, suppliers, customers) not yet present.
- [ ] Ensure `sites`, `companies`, `corporates`, `items` exist as shared FK targets for all downstream modules.
- [ ] Establish `core`-style shared enums/lookups if any AXONDB `core` tables are needed (27 tbl, 5 views) — migrate only the lookup/dimension tables that downstream modules reference.

### Phase 2 — Module Scaffolding Generator
Build a codegen script `scripts/gen_module_from_schema.py` that reads `columns.csv` + `foreign_keys.csv` + `indexes.csv` for a given schema and emits:
- `models.py`: one SQLModel class per table with correct `schema=`, UUID/serial PK, types mapped (see §5), `is_active`/`is_deleted`/`created_at`/`updated_at`/`object_version_number` audit mixin, FKs as relationships.
- `schemas.py`: Pydantic v2 `XxxCreate` / `XxxUpdate` / `XxxOut` (exclude unset; `from_attributes=True`).
- `router.py`: standard endpoints (list/get/create/update/delete) per entity + `check_privilege` guard.
- `services.py`: `class XxxService(BaseCRUDService[XxxModel])`.
- `permissions.py`: declarative privileges (view / create / update / delete / approve / export).
- `exceptions.py`: module-specific exceptions.

This replaces the current **commented-out stub files** in all 17 module folders.

### Phase 3 — Per-Module Implementation (in dependency order)
Order (least dependent → most dependent):
1. `sup` (4), `exp` (4) — small, leaf-ish
2. `wms` (8), `om` (18), `prd`(prod, 21), `gl` (23)
3. `ap` (36), `ar` (34), `inv` (35), `fa` (77)
4. `qc` (83), `tax` (90), `eam` (92)
5. `mes` (123), `tms`(log, 116)
6. `scm` (168) — largest, depends on many
7. `cron` (2) — utility
- `po` already exists → **align/extend** to AXONDB `po` (33 tbl) rather than regenerate.

For each module:
- [ ] Generate models/schemas/router/services/permissions/exceptions.
- [ ] Register models in `alembic/env.py` import block.
- [ ] Write Alembic migration (autogenerate against AXONDB-connected DB or hand-written from `full_schema.sql`).
- [ ] Run `ruff check` + `mypy` + unit smoke test (list endpoint returns 200).
- [ ] (Optional) generate frontend page with `InteractiveGrid` tabs.

### Phase 4 — Database Migration (Alembic)
- [ ] Single migration chain. Since AXONDB already has the tables, the migration should be **idempotent schema-sync** (create tables if not exist) OR point eraowl-ops `DATABASE_URL` at AXONDB and run `alembic revision --autogenerate` to capture diff.
- [ ] Rename `log`→`tms`, `prod`→`prd` schemas (Phase 0 migration).
- [ ] Indexes & FKs from `indexes.csv` / `foreign_keys.csv` reproduced.
- [ ] `alembic upgrade head` verified.

### Phase 5 — Frontend Pages
- [ ] For each module, create `src/modules/{mod}/` with tabbed `InteractiveGrid` pages (mirror existing `mdm`/`po` patterns).
- [ ] Add routes in `App.jsx` (e.g., `/tms`, `/prd`, `/ap`, `/ar`, ...).
- [ ] Wire `api/client.js` calls; reuse `authStore`.
- [ ] `npm run build` passes.

### Phase 6 — Verification & Cutover
- [ ] Backend: `ruff check .` and `mypy .` clean.
- [ ] Frontend: `npm run build` succeeds.
- [ ] DB: `alembic upgrade head` applied; spot-check 5 endpoints per module return data.
- [ ] Auth/RBAC: `check_privilege` enforced; seed default roles/privileges for new modules.
- [ ] `docker compose up -d` end-to-end smoke test.

---

## 5. Type Mapping (AXONDB → SQLModel/SQLAlchemy)

| PG Type | SQLModel/SA |
|---------|-------------|
| `uuid` (+ `uuidv7()` default) | `UUID(as_uuid=True)` PK, default `uuid.uuid4`* |
| `character varying(n)` | `String(n)` |
| `text` | `String` / `Text` |
| `integer` / `bigint` / `smallint` | `int` / `BigInt` / `SmallInteger` |
| `numeric(p,s)` | `Numeric(p, s)` |
| `boolean` | `Boolean` |
| `timestamp with/without tz` | `DateTime` (+ `server_default=func.now()`) |
| `date` | `Date` |
| `json` / `jsonb` | `JSON` / `JSONB` |
| `double precision` | `Float` |
| arrays (`_int4` etc.) | `ARRAY(...)` |

> *AXONDB uses `uuidv7()`. EraOwl-OPS uses `uuid4`. **Decision needed**: install `pguuid`/`uuidv7()` in eraowl-ops DB OR map default to `uuid4` (divergence in ID sortability). Recommended: keep `uuid4` for new rows, accept existing `uuidv7` rows as-is (they're still valid UUIDs).

---

## 6. Effort & Risk

| Risk | Mitigation |
|------|------------|
| 21,659 columns across 1,188 tables → huge generated code | Codegen script (Phase 2) + review samples; prioritize high-value modules |
| `mdm` is FK hub; wrong order breaks FKs | Phase 1 + dependency ordering in §4 |
| AXONDB `public` collides with eraowl-ops `public`/`core` | Exclude; manual reconciliation only |
| `uuidv7` vs `uuid4` | Keep `uuid4` default; legacy rows unaffected |
| Schema renames (`log`/`prod`) | `ALTER SCHEMA` in dedicated migration; update folder + router prefix |
| Performance of 17 new modules at startup | `module_registry` already lazy-imports; OK |
| Financial modules (`gl`/`fa`/`tax`) complexity | Implement after operational modules; reuse `BaseCRUDService` |

---

## 7. Deliverables Checklist

- [ ] 17 backend modules fully implemented (models/schemas/router/services/permissions/exceptions), `po` extended.
- [ ] `tms` and `prd` modules reflect renamed schemas.
- [ ] `cron` utility module.
- [ ] `mdm` reconciled as shared dimension hub.
- [ ] Alembic migrations (incl. schema renames) — `upgrade head` verified.
- [ ] `alembic/env.py` imports all new models.
- [ ] Frontend pages + routes for each module; `npm run build` green.
- [ ] Lint/typecheck green on backend.
- [ ] Smoke tests passing.
- [ ] `AXONDB` connection documented in `/requirements/axonos/schema/README.md` (done).

---

## 8. Open Questions (need user input)
1. **Exclude AXONDB `public`?** (Recommended: yes.)
2. **Schema rename vs alias?** (Recommended: `ALTER SCHEMA`.)
3. **`uuidv7` retention?** (Recommended: `uuid4` for new.)
4. **Full codegen now, or pilot 2–3 modules first?** (Recommended: pilot `sup`+`exp`+`wms`, then bulk.)
5. **Frontend pages in same pass or separate?** (Recommended: backend-first, frontend second.)
