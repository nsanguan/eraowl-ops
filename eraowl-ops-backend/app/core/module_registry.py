import importlib
import os
from fastapi import APIRouter, FastAPI


def discover_and_mount_modules(app: FastAPI) -> None:
    modules_dir = os.path.join(os.path.dirname(__file__), "..", "modules")
    if not os.path.isdir(modules_dir):
        return

    for entry in sorted(os.listdir(modules_dir)):
        module_path = os.path.join(modules_dir, entry)
        if not os.path.isdir(module_path):
            continue

        module_name = entry
        router_file = os.path.join(module_path, "router.py")

        if not os.path.isfile(router_file):
            _discover_submodules(app, module_name, module_path)
            continue

        try:
            mod = importlib.import_module(f"app.modules.{module_name}.router")
            router: APIRouter = getattr(mod, "router", None)
            if router:
                prefix = f"/api/v1/{module_name}"
                app.include_router(router, prefix=prefix, tags=[module_name])
        except Exception as e:
            import logging
            logging.getLogger("eraowl-ops").warning("Failed to mount module %s: %s", module_name, e)


def _discover_submodules(app: FastAPI, parent_name: str, parent_path: str) -> None:
    for entry in sorted(os.listdir(parent_path)):
        sub_path = os.path.join(parent_path, entry)
        if not os.path.isdir(sub_path):
            continue
        router_file = os.path.join(sub_path, "router.py")
        if not os.path.isfile(router_file):
            continue
        try:
            mod = importlib.import_module(f"app.modules.{parent_name}.{entry}.router")
            router: APIRouter = getattr(mod, "router", None)
            if router:
                prefix = f"/api/v1/{entry}"
                app.include_router(router, prefix=prefix, tags=[entry])
        except Exception as e:
            import logging
            logging.getLogger("eraowl-ops").warning("Failed to mount submodule %s.%s: %s", parent_name, entry, e)
