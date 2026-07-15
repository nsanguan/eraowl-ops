#!/usr/bin/env python3
"""
Project Object Scanner — scans backend + frontend code and populates admin.objects.
"""

import ast
import json
import os
import re
import uuid
from datetime import date
from pathlib import Path

import asyncpg

DATABASE_URL = "postgres://eraowlopsadmin:EraOwl2026@202.71.1.13:5435/eraowlops"
# Paths — relative to the container or host
HOST_ROOT = os.environ.get("HOST_ROOT", "/u01/eraowl-ops")
CONTAINER_ROOT = os.environ.get("CONTAINER_ROOT", "/u01/eraowl-ops")
ROOT = Path(CONTAINER_ROOT)

BACKEND_MODULES = ROOT / "eraowl-ops-backend/app/modules"
FRONTEND_PAGES = ROOT / "eraowl-ops-frontend/src/modules"
FRONTEND_COMPONENTS = ROOT / "eraowl-ops-frontend/src/components"
SHARED_UI_KIT = ROOT / "eraowl-ops-frontend/src/shared-ui-kit/components/ui"
SHARED_KIT_LAYOUT = ROOT / "eraowl-ops-frontend/src/shared-ui-kit/components/layout"

# ── Module metadata (name → label)
MODULE_LABELS = {
    "admin": "Identity & Access Management",
    "mdm": "Master Data Management",
    "org_structure": "Organization Structure",
    "party": "Party Management (TCA-lite)",
    "item": "Item Master",
    "bom": "Bill of Materials",
    "po": "Purchase Order",
    "gl": "General Ledger",
    "om": "Order Management",
}


def parse_models(filepath: Path) -> list[dict]:
    """Parse SQLModel models and extract tables + columns."""
    objects = []
    try:
        tree = ast.parse(filepath.read_text())
    except Exception:
        return objects

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and any(
            isinstance(base, ast.Call) and getattr(base.func, "attr", None) == "table"
            or isinstance(base, ast.Name) and base.id == "SQLModel"
            for base in node.bases
        ):
            schema = "public"
            table_name = node.name
            for deco in node.decorator_list:
                if isinstance(deco, ast.Call) and hasattr(deco.func, "attr"):
                    if deco.func.attr == "table_args":
                        for kw in deco.keywords:
                            if kw.arg == "schema" and isinstance(kw.value, ast.Constant):
                                schema = kw.value.value
            # Also check __table_args__ class body
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name) and target.id == "__table_args__":
                            if isinstance(item.value, ast.Dict):
                                for k, v in zip(item.value.keys, item.value.values):
                                    if isinstance(k, ast.Constant) and k.value == "schema" and isinstance(v, ast.Constant):
                                        schema = v.value
                            elif isinstance(item.value, ast.Tuple):
                                for elt in item.value.elts:
                                    if isinstance(elt, ast.Dict):
                                        for k, v in zip(elt.keys, elt.values):
                                            if isinstance(k, ast.Constant) and k.value == "schema" and isinstance(v, ast.Constant):
                                                schema = v.value

            tid = str(uuid.uuid4())
            objects.append({
                "id": tid,
                "type": "TABLE",
                "name": f"{schema}.{table_name}",
                "parent": None,
                "meta": json.dumps({"schema": schema, "class": node.name}),
            })

            for item in node.body:
                if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                    col_name = item.target.id
                    col_type = ast.dump(item.annotation) if item.annotation else "unknown"
                    objects.append({
                        "id": str(uuid.uuid4()),
                        "type": "COLUMN",
                        "name": f"{schema}.{table_name}.{col_name}",
                        "parent": tid,
                        "meta": json.dumps({"type": col_type, "class": node.name}),
                    })
    return objects


def parse_endpoints(filepath: Path, module_name: str) -> list[dict]:
    """Parse router.py to extract API endpoints."""
    objects = []
    try:
        src = filepath.read_text()
    except Exception:
        return objects

    for match in re.finditer(
        r'@router\.(get|post|put|delete|patch)\s*\(\s*["\']([^"\']+)["\']',
        src,
    ):
        method = match.group(1)
        path = match.group(2)
        full_path = f"/api/v1/{module_name}{path}"
        desc = ""
        # Try to find the docstring/comment
        lines = src[: match.start()].split("\n")
        for line in reversed(lines[-10:]):
            m = re.search(r'description\s*=\s*["\']([^"\']+)["\']', line)
            if m:
                desc = m.group(1)
                break
            m = re.search(r'#\s*(.+)$', line)
            if m:
                desc = m.group(1).strip()
                break
        objects.append({
            "id": str(uuid.uuid4()),
            "type": "ENDPOINT",
            "name": f"{method.upper()} {full_path}",
            "parent": None,
            "meta": json.dumps({"method": method.upper(), "path": full_path, "module": module_name}),
        })
    return objects


def parse_permissions(filepath: Path, module_name: str) -> list[dict]:
    """Extract permission/privilege definitions."""
    objects = []
    try:
        tree = ast.parse(filepath.read_text())
    except Exception:
        return objects

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "PRIVILEGES":
                    if isinstance(node.value, ast.List):
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Dict):
                                action = None
                                desc = None
                                for k, v in zip(elt.keys, elt.values):
                                    if isinstance(k, ast.Constant):
                                        if k.value == "action" and isinstance(v, ast.Constant):
                                            action = v.value
                                        if k.value == "description" and isinstance(v, ast.Constant):
                                            desc = v.value
                                if action:
                                    objects.append({
                                        "id": str(uuid.uuid4()),
                                        "type": "PERMISSION",
                                        "name": f"{module_name}.{action}",
                                        "parent": None,
                                        "meta": json.dumps({"module": module_name, "action": action, "description": desc}),
                                    })
    return objects


def parse_frontend_pages(base_dir: Path, parent_name: str = "") -> list[dict]:
    """Scan frontend module directories for page components."""
    objects = []
    if not base_dir.exists():
        return objects

    for entry in sorted(base_dir.iterdir()):
        if entry.is_dir():
            pages_dir = entry / "pages"
            mod_name = f"{parent_name}.{entry.name}" if parent_name else entry.name
            if pages_dir.exists():
                for page_file in sorted(pages_dir.iterdir()):
                    if page_file.suffix in (".jsx", ".tsx", ".js", ".ts"):
                        objects.append({
                            "id": str(uuid.uuid4()),
                            "type": "PAGE",
                            "name": f"{mod_name}/{page_file.stem}",
                            "parent": None,
                            "meta": json.dumps({"module": mod_name, "file": str(page_file)}),
                        })
            # Recurse for submodules
            objects += parse_frontend_pages(entry, mod_name)

    return objects


def parse_frontend_components(base_dir: Path, prefix: str = "") -> list[dict]:
    """Scan frontend component directories."""
    objects = []
    if not base_dir.exists():
        return objects
    for f in sorted(base_dir.iterdir()):
        if f.suffix in (".jsx", ".tsx", ".js", ".ts") and not f.name.startswith("_"):
            objects.append({
                "id": str(uuid.uuid4()),
                "type": "COMPONENT",
                "name": f"{prefix}/{f.stem}" if prefix else f.stem,
                "parent": None,
                "meta": json.dumps({"file": str(f)}),
            })
    return objects


async def main():
    conn = await asyncpg.connect(DATABASE_URL)

    # Clear existing
    await conn.execute("DELETE FROM admin.objects")
    print("Cleared admin.objects")

    all_objects = []
    seen = set()

    for module_dir in sorted(BACKEND_MODULES.iterdir()):
        if not module_dir.is_dir() or module_dir.name.startswith("_"):
            continue
        module_name = module_dir.name
        label = MODULE_LABELS.get(module_name, module_name.title())

        module_id = str(uuid.uuid4())
        all_objects.append({
            "id": module_id,
            "type": "MODULE",
            "name": module_name,
            "parent": None,
            "meta": json.dumps({"label": label, "path": str(module_dir)}),
        })

        # Scan submodules (e.g., master_data/org_structure)
        submodules = [module_dir]
        for sub in module_dir.iterdir():
            if sub.is_dir() and (sub / "models.py").exists() and sub.name not in ("dto", "services", "domain", "presentation"):
                submodules.append(sub)

        for sm in submodules:
            sm_name = sm.relative_to(BACKEND_MODULES).as_posix()

            # Models
            models_file = sm / "models.py"
            if models_file.exists():
                for obj in parse_models(models_file):
                    obj["parent"] = module_id
                    key = (obj["type"], obj["name"])
                    if key not in seen:
                        seen.add(key)
                        all_objects.append(obj)

            # Endpoints
            router_file = sm / "router.py"
            if router_file.exists():
                for obj in parse_endpoints(router_file, sm_name):
                    if "generic" not in obj["name"]:
                        obj["parent"] = module_id
                        key = (obj["type"], obj["name"])
                        if key not in seen:
                            seen.add(key)
                            all_objects.append(obj)

            # Permissions
            perm_file = sm / "permissions.py"
            if perm_file.exists():
                for obj in parse_permissions(perm_file, module_name):
                    obj["parent"] = module_id
                    key = (obj["type"], obj["name"])
                    if key not in seen:
                        seen.add(key)
                        all_objects.append(obj)

    # Frontend pages
    for obj in parse_frontend_pages(FRONTEND_PAGES):
        key = (obj["type"], obj["name"])
        if key not in seen:
            seen.add(key)
            all_objects.append(obj)

    # Frontend components
    for obj in parse_frontend_components(FRONTEND_COMPONENTS, "components"):
        key = (obj["type"], obj["name"])
        if key not in seen:
            seen.add(key)
            all_objects.append(obj)

    # Shared UI Kit components
    for obj in parse_frontend_components(SHARED_UI_KIT, "shared-ui"):
        key = (obj["type"], obj["name"])
        if key not in seen:
            seen.add(key)
            all_objects.append(obj)

    for obj in parse_frontend_components(SHARED_KIT_LAYOUT, "shared-ui/layout"):
        key = (obj["type"], obj["name"])
        if key not in seen:
            seen.add(key)
            all_objects.append(obj)

    # Insert
    for obj in all_objects:
        await conn.execute(
            "INSERT INTO admin.objects (object_id, object_type, module_name, object_name, parent_object_id, metadata) "
            "VALUES ($1, $2, $3, $4, $5, $6::jsonb)",
            uuid.UUID(obj["id"]),
            obj["type"],
            obj["name"] if obj["type"] in ("MODULE", "TABLE", "COLUMN") else (
                obj["meta"] and json.loads(obj["meta"]).get("module") or obj["name"]
            ),
            obj["name"],
            uuid.UUID(obj["parent"]) if obj["parent"] else None,
            obj["meta"],
        )

    # Stats
    counts = {}
    for obj in all_objects:
        t = obj["type"]
        counts[t] = counts.get(t, 0) + 1

    print(f"\nSeeded {len(all_objects)} objects:")
    for t, c in sorted(counts.items()):
        print(f"  {t:12s} {c}")

    await conn.close()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
