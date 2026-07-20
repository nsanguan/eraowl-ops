#!/usr/bin/env python3
"""
Codegen: AxonOS schema CSVs -> EraOwl-OPS module files.

Reads:
  requirements/axonos/schema/{columns.csv,foreign_keys.csv,tables.csv}
Emits for each target schema:
  app/modules/{module}/models.py | schemas.py | services.py | router.py

Conventions mirrored from the pilot modules (sup/exp/wms) and po/mdm:
  - SQLModel table=True, __table_args__={"schema": "<pg_schema>"}
  - UUID PK: Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
  - audit: created_at/updated_at (DateTime tz, server_default/onupdate func.now()), update_by (uuid)
  - is_active / is_deleted booleans when present
  - FKs: Field(foreign_key="<schema>.<table>.<col>")
  - BaseCRUDService per entity; paginated router w/ check_privilege guard
"""
from __future__ import annotations

import csv
import os
import re
import sys
from collections import defaultdict

ROOT = "/u01/eraowl-ops"
SCHEMA_DIR = os.path.join(ROOT, "requirements/axonos/schema")
MODULES_DIR = os.path.join(ROOT, "eraowl-ops-backend/app/modules")

# schema renames (AxonOS -> EraOwl module folder / db schema)
RENAMES = {"log": "tms", "prod": "prd"}
# 'log' -> module 'tms' (DB schema stays 'log'); 'prod' -> module 'prd' (DB schema stays 'prod').

# Target schemas to generate (exclude already-done / removed modules)
TARGET_SCHEMAS = ["ap", "ar", "eam", "fa", "gl", "inv", "log", "mes", "om", "prod", "qc", "scm", "tax"]

# PG type -> (python type, sa type, extra kw)
# Order matters: more specific first.
TYPE_MAP = [
    (r"^uuid$", ("uuid.UUID", "PG_UUID(as_uuid=True)", None)),
    (r"^character varying\((\d+)\)$", ("str", "String(\\1)", None)),
    (r"^character varying$", ("str", "String", None)),
    (r"^varchar\((\d+)\)$", ("str", "String(\\1)", None)),
    (r"^text$", ("str", "Text", None)),
    (r"^character\((\d+)\)$", ("str", "String(\\1)", None)),
    (r"^character$", ("str", "String(1)", None)),
    (r"^integer$", ("int", "Integer", None)),
    (r"^int$", ("int", "Integer", None)),
    (r"^bigint$", ("int", "BigInteger", None)),
    (r"^smallint$", ("int", "SmallInteger", None)),
    (r"^numeric\((\d+),(\d+)\)$", ("float", "Numeric(\\1, \\2)", None)),
    (r"^numeric$", ("float", "Numeric", None)),
    (r"^decimal\((\d+),(\d+)\)$", ("float", "Numeric(\\1, \\2)", None)),
    (r"^real$", ("float", "Float", None)),
    (r"^double precision$", ("float", "Float", None)),
    (r"^money$", ("float", "Numeric(19,4)", None)),
    (r"^boolean$", ("bool", "Boolean", None)),
    (r"^timestamp with time zone$", ("datetime", "DateTime(timezone=True)", "tz")),
    (r"^timestamp without time zone$", ("datetime", "DateTime", None)),
    (r"^timestamp$", ("datetime", "DateTime", None)),
    (r"^date$", ("date", "Date", None)),
    (r"^time with time zone$", ("str", "Time(timezone=True)", None)),
    (r"^time without time zone$", ("str", "Time", None)),
    (r"^jsonb$", ("dict", "JSONB", None)),
    (r"^json$", ("dict", "JSON", None)),
    (r"^bytea$", ("bytes", "LargeBinary", None)),
    (r"^interval$", ("str", "Interval", None)),
    # arrays
    (r"^_int4$", ("list[int]", "ARRAY(Integer)", None)),
    (r"^_int8$", ("list[int]", "ARRAY(BigInteger)", None)),
    (r"^_numeric$", ("list[float]", "ARRAY(Numeric)", None)),
    (r"^_text$", ("list[str]", "ARRAY(Text)", None)),
    (r"^_varchar$", ("list[str]", "ARRAY(String)", None)),
    (r"^_uuid$", ("list[uuid.UUID]", "ARRAY(PG_UUID(as_uuid=True))", None)),
    (r"^character varying\(\d+\)\[\]$", ("list[str]", "ARRAY(String)", None)),
]


def map_type(pg_type: str):
    for pat, mapped in TYPE_MAP:
        m = re.match(pat, pg_type)
        if m:
            py, sa, flag = mapped
            sa = m.expand(sa)
            return py, sa, flag
    # fallback
    return "str", "String", None


def camel_to_snake(name: str) -> str:
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def snake_to_pascal(name: str) -> str:
    return "".join(p.capitalize() for p in name.split("_"))


def clean_ident(name: str) -> str:
    # SQLModel/pydantic reserved-word safe
    return name


def is_reserved(word: str) -> bool:
    return word in {
        "from", "import", "class", "def", "return", "lambda", "pass", "global", "nonlocal",
        "assert", "async", "await", "yield", "with", "as", "in", "is", "not", "and", "or",
        "if", "else", "elif", "for", "while", "break", "continue", "try", "except", "finally",
        "raise", "del", "type", "id",
    }


# ---------------------------------------------------------------------------

def load_columns():
    cols = defaultdict(list)  # (schema, table) -> [dict]
    with open(os.path.join(SCHEMA_DIR, "columns.csv")) as f:
        for row in csv.reader(f, delimiter="|"):
            if len(row) < 8:
                continue
            schema, table, col, ptype, null, default, pk, fk = row[:8]
            cols[(schema, table)].append({
                "name": col, "type": ptype, "null": null,
                "default": default, "pk": pk, "fk": fk,
            })
    return cols


# Shared-dimension tables that live in the eraowl-ops `mdm` schema.
# In AXONDB these are spread across `mdm`/`core`; the FK CSV omits the
# referenced schema, so cross-schema FKs to these names are remapped to mdm.
# Shared-dimension tables that live in the eraowl-ops `mdm` schema.
# In AXONDB these are spread across `mdm`/`core`; the FK CSV omits the
# referenced schema, so cross-schema FKs to these names are remapped to mdm.
SHARED_DIMS = {
    "companies", "corporates", "sites", "business_units", "items",
    "suppliers", "customers", "parties", "party_sites", "partner_sites",
    "partners", "warehouses", "warehouse_locators", "uoms",
    "uom_conversions", "addresses", "item_categories",
    "item_category_assignments",
}

# AXONDB PostgreSQL schema -> eraowl-ops PostgreSQL schema (when renamed).
SCHEMA_RENAME = {"log": "tms", "prod": "prd"}

# AXONDB/Core table name -> eraowl-ops mdm table name (when they differ).
DIM_RENAME = {
    "partners": "parties",
    "partner_sites": "party_sites",
}

# Referenced (table, column) -> (new_table, new_column) when eraowl-ops
# renames the PK column (e.g. partner_id -> party_id).
DIM_COL_RENAME = {
    ("partners", "partner_id"): ("parties", "party_id"),
    ("partner_sites", "partner_site_id"): ("party_sites", "party_site_id"),
}


def load_fks():
    fks = defaultdict(list)  # (schema, table) -> list of (col, target)
    with open(os.path.join(SCHEMA_DIR, "foreign_keys.csv")) as f:
        for row in csv.reader(f, delimiter="|"):
            if len(row) < 6:
                continue
            schema, table, conname, cols, reftable, refcols = row[:6]
            for c, rc in zip(cols.split(","), refcols.split(",")):
                c = c.strip()
                rc = rc.strip()
                # Determine referenced schema + optional table/column rename
                if reftable in SHARED_DIMS:
                    new_table = DIM_RENAME.get(reftable, reftable)
                    new_col = rc
                    if (reftable, rc) in DIM_COL_RENAME:
                        new_table, new_col = DIM_COL_RENAME[(reftable, rc)]
                    fks[(schema, table)].append((c, f"mdm.{new_table}.{new_col}"))
                else:
                    ref_schema = SCHEMA_RENAME.get(schema, schema)
                    fks[(schema, table)].append((c, f"{ref_schema}.{reftable}.{rc}"))
    return fks


def load_tables():
    tabs = defaultdict(list)
    with open(os.path.join(SCHEMA_DIR, "tables.csv")) as f:
        for row in csv.reader(f, delimiter="|"):
            if len(row) < 4:
                continue
            schema, table, kind, size = row[:4]
            if kind == "table":
                tabs[schema].append(table)
    return tabs


AUDIT_FIELDS = {"created_at", "updated_at", "update_by", "is_active", "is_deleted", "object_version_number"}


def gen_models(schema, tables, cols, fks):
    lines = []
    lines.append("import uuid")
    lines.append("from datetime import date, datetime, time")
    lines.append("from typing import Optional, List, Dict, Any")
    lines.append("from sqlalchemy import (")
    lines.append("    BigInteger, Boolean, Column, Date, DateTime, Float, Integer,")
    lines.append("    SmallInteger, String, Text, Time, Interval, LargeBinary,")
    lines.append("    Numeric, ARRAY, func,")
    lines.append(")")
    lines.append("from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB, JSON")
    lines.append("from sqlalchemy import ForeignKey")
    lines.append("from sqlmodel import Field, SQLModel")
    lines.append("")
    lines.append("")
    out = []
    out.extend(lines)
    class_defs = []
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        fields = cols.get((schema, table), [])
        if not fields:
            continue
        cls = snake_to_pascal(table)
        out.append(f"class {cls}(SQLModel, table=True):")
        out.append(f'    __tablename__ = "{table}"')
        out.append(f'    __table_args__ = {{"schema": "{SCHEMA_RENAME.get(schema, schema)}"}}')
        out.append("")
        for fdict in fields:
            col = fdict["name"]
            col_py = "meta_data" if col == "metadata" else col
            ptype = fdict["type"]
            is_pk = fdict["pk"] == "PK"
            nullable = fdict["null"] != "NOT NULL"
            fk = fdict["fk"]
            # find fk target from fks list
            fk_target = None
            for (c, tgt) in fks.get((schema, table), []):
                if c == col:
                    fk_target = tgt
                    break
            py, sa, flag = map_type(ptype)
            col_safe = col
            # audit/standard fields
            if is_pk:
                if py == "uuid.UUID":
                    out.append(f"    {col_py}: uuid.UUID = Field(")
                    out.append(f"        default_factory=uuid.uuid4,")
                    out.append(f"        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),")
                    out.append(f"    )")
                else:
                    out.append(f"    {col_py}: {py} = Field(sa_column=Column({sa}, primary_key=True))")
            elif col == "created_at":
                out.append(f"    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))")
            elif col == "updated_at":
                out.append(f"    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))")
            elif col == "update_by":
                out.append(f"    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))")
            elif col == "is_active":
                out.append(f"    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))")
            elif col == "is_deleted":
                out.append(f"    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))")
            elif col == "object_version_number":
                out.append(f"    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))")
            elif col == "metadata":
                # 'metadata' is reserved by SQLModel; alias to meta_data
                opt = "Optional[" if nullable else ""
                close = "]" if nullable else ""
                fk_kw = f', ForeignKey("{fk_target}")' if fk_target else ""
                nul_kw = "True" if nullable else "False"
                out.append(f"    meta_data: {opt}dict{close} = Field(default=None, sa_column=Column(JSONB{fk_kw}, nullable={nul_kw}))")
            else:
                opt = "Optional[" if nullable else ""
                close = "]" if nullable else ""
                fk_kw = f', ForeignKey("{fk_target}")' if fk_target else ""
                nul_kw = "True" if nullable else "False"
                if py.startswith("list[") or py.startswith("dict"):
                    out.append(f"    {col_py}: {opt}{py}{close} = Field(default=None, sa_column=Column({sa}{fk_kw}, nullable={nul_kw}))")
                elif py == "uuid.UUID":
                    out.append(f"    {col_py}: {opt}uuid.UUID{close} = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True){fk_kw}, nullable={nul_kw}))")
                else:
                    out.append(f"    {col_py}: {opt}{py}{close} = Field(default=None, sa_column=Column({sa}{fk_kw}, nullable={nul_kw}))")
            out.append("")
        out.append("")
    return "\n".join(out)


def gen_schemas(schema, tables, cols, fks):
    classes = []
    block = ["import uuid", "from datetime import date, datetime, time", "from typing import Optional, List, Dict, Any", "from pydantic import BaseModel", "", ""]
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        fields = cols.get((schema, table), [])
        if not fields:
            continue
        cls = snake_to_pascal(table)
        create_fields, update_fields, out_fields = [], [], []
        for fdict in fields:
            col = fdict["name"]
            col_py = "meta_data" if col == "metadata" else col
            ptype = fdict["type"]
            is_pk = fdict["pk"] == "PK"
            nullable = fdict["null"] != "NOT NULL"
            py, sa, flag = map_type(ptype)
            # map types for pydantic
            py_p = py
            if py == "uuid.UUID":
                py_p = "uuid.UUID"
            if py.startswith("list["):
                py_p = "list"
            if py == "dict":
                py_p = "dict"
            col_typed = f"{col_py}: {py_p}"
            if is_pk:
                # present in Out and Create (required PK) but update optional
                create_fields.append(f"    {col_py}: {py_p}")
                update_fields.append(f"    {col_py}: Optional[{py_p}] = None")
                out_fields.append(f"    {col_py}: {py_p}")
            elif col in ("created_at", "updated_at", "update_by"):
                # audit: out only
                out_fields.append(f"    {col_py}: Optional[{py_p}] = None")
            elif col in ("is_active", "is_deleted", "object_version_number"):
                pyt = "bool" if col != "object_version_number" else "int"
                if col == "is_active":
                    dflt = "True"
                elif col == "is_deleted":
                    dflt = "False"
                else:
                    dflt = "1"
                create_fields.append(f"    {col_py}: {pyt} = {dflt}")
                update_fields.append(f"    {col_py}: Optional[{pyt}] = None")
                out_fields.append(f"    {col_py}: {pyt}")
            else:
                if nullable:
                    create_fields.append(f"    {col_py}: Optional[{py_p}] = None")
                    update_fields.append(f"    {col_py}: Optional[{py_p}] = None")
                    out_fields.append(f"    {col_py}: Optional[{py_p}] = None")
                else:
                    create_fields.append(f"    {col_py}: {py_p}")
                    update_fields.append(f"    {col_py}: Optional[{py_p}] = None")
                    out_fields.append(f"    {col_py}: {py_p}")
        classes.append((cls, create_fields, update_fields, out_fields))
    out = list(block)
    for cls, cf, uf, of in classes:
        out.append(f"class {cls}Create(BaseModel):")
        out.extend(cf if cf else ["    pass"])
        out.append("")
        out.append(f"class {cls}Update(BaseModel):")
        out.extend(uf if uf else ["    pass"])
        out.append("")
        out.append(f"class {cls}Out(BaseModel):")
        out.extend(of if of else ["    pass"])
        out.append('    model_config = {"from_attributes": True}')
        out.append("")
    return "\n".join(out), classes


def gen_services(mod, tables):
    out = ["from sqlalchemy.ext.asyncio import AsyncSession", "",
           "from app.shared.module_base.crud import BaseCRUDService", ""]
    imports = []
    body = []
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        cls = snake_to_pascal(table)
        svc = f"{cls}Service"
        imports.append(f"from app.modules.{mod}.models import {cls}")
        body.append(f"class {svc}(BaseCRUDService[{cls}]):")
        body.append(f"    def __init__(self, db: AsyncSession):")
        body.append(f"        super().__init__(db, {cls})")
        body.append("")
    out.extend(imports)
    out.append("")
    out.extend(body)
    return "\n".join(out)


def gen_router(mod, tables, schema_classes):
    """schema_classes: list of (table, cls, has_status, search_cols)."""
    out = []
    out.append("import uuid")
    out.append("from typing import Optional")
    out.append("")
    out.append("from fastapi import APIRouter, Depends, Query, status")
    out.append("from sqlalchemy.ext.asyncio import AsyncSession")
    out.append("")
    out.append("from app.core.database import get_db")
    out.append("from app.core.dependencies import check_privilege, get_current_user")
    out.append("from app.shared.pagination import PaginatedResponse")
    out.append(f"from app.modules.{mod}.services import (")
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        out.append(f"    {snake_to_pascal(table)}Service,")
    out.append(")")
    out.append(f"from app.modules.{mod}.schemas import (")
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        cls = snake_to_pascal(table)
        out.append(f"    {cls}Create,")
        out.append(f"    {cls}Update,")
        out.append(f"    {cls}Out,")
    out.append(")")
    out.append("")
    out.append('router = APIRouter(dependencies=[Depends(get_current_user)])')
    out.append("")
    out.append("")
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        cls = snake_to_pascal(table)
        svc = f"{cls}Service"
        endpoint = table  # use raw table name as endpoint
        route = camel_to_snake(table)
        # detect status / search columns from class info
        has_status = False
        search_cols = []
        for (t2, c2, hs, sc) in schema_classes:
            if t2 == table:
                has_status = hs
                search_cols = sc
                break
        # list
        qparams = "page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),"
        extra = ""
        if has_status:
            qparams += " status_filter: Optional[str] = Query(None, alias=\"status\"),"
        if search_cols:
            qparams += " search: Optional[str] = Query(None),"
        out.append(f"@router.get(\"/{endpoint}\", response_model=PaginatedResponse[{cls}Out])")
        out.append(f"async def list_{route}(")
        out.append(f"    {qparams}")
        out.append(f"    db: AsyncSession = Depends(get_db),")
        out.append(f'    _priv=check_privilege("{mod}", "view"),')
        out.append(f"):")
        out.append(f"    svc = {svc}(db)")
        filter_line = ""
        if has_status:
            filter_line = '    filters = {"status": status_filter} if status_filter else None'
            out.append(filter_line)
            flt_arg = "filters"
        else:
            flt_arg = "None"
        if search_cols:
            sc_str = "[" + ", ".join(f'"{c}"' for c in search_cols) + "]"
            out.append(f"    result = await svc.list(page, page_size, filters={flt_arg}, search_cols={sc_str}, search_term=search)")
        else:
            out.append(f"    result = await svc.list(page, page_size, filters={flt_arg})")
        out.append(f"    return PaginatedResponse(**result.model_dump())")
        out.append("")
        # get
        out.append(f"@router.get(\"/{endpoint}/{{entity_id}}\", response_model={cls}Out)")
        out.append(f"async def get_{route}(")
        out.append(f"    entity_id: uuid.UUID,")
        out.append(f"    db: AsyncSession = Depends(get_db),")
        out.append(f'    _priv=check_privilege("{mod}", "view"),')
        out.append(f"):")
        out.append(f"    return await {svc}(db).get(entity_id)")
        out.append("")
        # create
        out.append(f"@router.post(\"/{endpoint}\", response_model={cls}Out, status_code=status.HTTP_201_CREATED)")
        out.append(f"async def create_{route}(")
        out.append(f"    data: {cls}Create,")
        out.append(f"    db: AsyncSession = Depends(get_db),")
        out.append(f'    _priv=check_privilege("{mod}", "manage"),')
        out.append(f"):")
        out.append(f"    return await {svc}(db).create(data)")
        out.append("")
        # update
        out.append(f"@router.put(\"/{endpoint}/{{entity_id}}\", response_model={cls}Out)")
        out.append(f"async def update_{route}(")
        out.append(f"    entity_id: uuid.UUID,")
        out.append(f"    data: {cls}Update,")
        out.append(f"    db: AsyncSession = Depends(get_db),")
        out.append(f'    _priv=check_privilege("{mod}", "manage"),')
        out.append(f"):")
        out.append(f"    return await {svc}(db).update(entity_id, data)")
        out.append("")
        # delete
        out.append(f"@router.delete(\"/{endpoint}/{{entity_id}}\", status_code=status.HTTP_204_NO_CONTENT)")
        out.append(f"async def delete_{route}(")
        out.append(f"    entity_id: uuid.UUID,")
        out.append(f"    db: AsyncSession = Depends(get_db),")
        out.append(f'    _priv=check_privilege("{mod}", "manage"),')
        out.append(f"):")
        out.append(f"    await {svc}(db).delete(entity_id)")
        out.append("")
    return "\n".join(out)


def detect_class_info(schema, tables, cols):
    info = []
    for table in sorted(tables):
        if table == "__drizzle_migrations":
            continue
        fields = cols.get((schema, table), [])
        has_status = any(f["name"] == "status" for f in fields)
        # searchable: name/code/number-like string cols
        search_cols = []
        for f in fields:
            if f["name"] in ("created_at", "updated_at"):
                continue
            if re.match(r"^(character varying|character|text|varchar)", f["type"]) and f["type"] not in ("text",):
                if re.search(r"(code|name|number|description|title|label|email)", f["name"]):
                    search_cols.append(f["name"])
        search_cols = search_cols[:3]
        info.append((table, snake_to_pascal(table), has_status, search_cols))
    return info


def main():
    cols = load_columns()
    fks = load_fks()
    tables = load_tables()
    total = 0
    for schema in TARGET_SCHEMAS:
        if schema not in tables:
            print(f"WARN: schema {schema} has no tables, skipping")
            continue
        mod = RENAMES.get(schema, schema)
        mod_dir = os.path.join(MODULES_DIR, mod)
        os.makedirs(mod_dir, exist_ok=True)
        ts = tables[schema]
        # models
        with open(os.path.join(mod_dir, "models.py"), "w") as f:
            f.write(gen_models(schema, ts, cols, fks))
        # schemas
        schema_text, classes = gen_schemas(schema, ts, cols, fks)
        with open(os.path.join(mod_dir, "schemas.py"), "w") as f:
            f.write(schema_text)
        # services
        with open(os.path.join(mod_dir, "services.py"), "w") as f:
            f.write(gen_services(mod, ts))
        # router
        info = detect_class_info(schema, ts, cols)
        with open(os.path.join(mod_dir, "router.py"), "w") as f:
            f.write(gen_router(mod, ts, info))
        n = len([t for t in ts if t != "__drizzle_migrations"])
        total += n
        print(f"  generated module '{mod}' (schema {schema}): {n} tables")
    print(f"TOTAL tables generated: {total}")


if __name__ == "__main__":
    main()
