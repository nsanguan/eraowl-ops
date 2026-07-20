# AXONDB Schema Dump (EraOwl-OPS → AXONDB migration source)

Source database connection used for this extraction:

| Property | Value |
|----------|-------|
| Connection name | AXONDB |
| Host | 202.71.1.13 |
| Port | 5435 |
| Database | axonosdb |
| User | axonos |
| Password | EraOwl2026 |
| Extracted | 2026-07-20 |

## Statistics
- Schemas: 24 application schemas (excluding pg_catalog, information_schema, cron, public-system)
- Total tables (relkind=r/p): 1129
- Total views/materialized views: 152
- Total columns catalogued: 21659
- Indexes (non-PK): 2482
- Foreign keys: 1239
- Custom enums: 0

## Files
| File | Description |
|------|-------------|
| full_schema.sql | Complete DDL (schema-only, no data, no owner/privs/comments), 100k+ lines. Load with `psql ... -f full_schema.sql` |
| tables.csv | schema|table|kind|size_bytes for all 1281 relations |
| columns.csv | schema|table|column|type|nullability|default|PK|FK-target |
| indexes.csv | schema|table|index|definition|unique |
| foreign_keys.csv | schema|table|constraint|columns|ref_table|ref_columns |
| enums.csv | (empty — no custom enums in source) |
| schema_summary.csv | schema|tables|views per schema |

## Per-schema table/view counts
```
admin          12 tables    0 views
ap             36 tables   10 views
ar             34 tables    3 views
collab          8 tables    0 views
core           27 tables    5 views
eam            92 tables   18 views
exp             4 tables    2 views
fa             77 tables   13 views
gl             23 tables    3 views
inv            35 tables    9 views
log           116 tables   16 views
mdm            94 tables   14 views
mes           123 tables    5 views
om             18 tables    5 views
po             33 tables    8 views
prod           21 tables    2 views
public         23 tables    0 views
qc             83 tables   10 views
reporting       0 tables    4 views
scm           168 tables   11 views
sup             4 tables    2 views
tax            90 tables    8 views
wms             8 tables    4 views
```

## Notes for migration
- Source uses `uuidv7()` default for UUID PKs (admin.audit_logs etc.) — confirm eraowl-ops schema uses the same generator or uuid4.
- 24 schemas; eraowl-ops uses 5 schemas (admin, mdm, bom, po, collab). A future migration step must map AXONDB schemas into the eraowl-ops module/namespace layout.
- Connection string (SQLAlchemy async): postgresql+asyncpg://axonos:EraOwl2026@202.71.1.13:5435/axonosdb
