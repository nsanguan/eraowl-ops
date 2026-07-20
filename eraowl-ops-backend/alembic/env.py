import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlmodel import SQLModel

from app.core.config import settings

config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import all models so SQLModel.metadata knows about them
from app.modules.mdm.org_structure import models as _org  # noqa: F401
from app.modules.mdm.party import models as _party  # noqa: F401
from app.modules.mdm.item import models as _item  # noqa: F401
from app.modules.bom import models as _bom  # noqa: F401
from app.modules.po import models as _po  # noqa: F401
from app.modules.admin import models as _admin  # noqa: F401
from app.modules.collaboration import models as _collab  # noqa: F401
from app.modules.sup import models as _sup  # noqa: F401
from app.modules.exp import models as _exp  # noqa: F401
from app.modules.wms import models as _wms  # noqa: F401
from app.modules.ap import models as _ap  # noqa: F401
from app.modules.ar import models as _ar  # noqa: F401
from app.modules.eam import models as _eam  # noqa: F401
from app.modules.fa import models as _fa  # noqa: F401
from app.modules.gl import models as _gl  # noqa: F401
from app.modules.inv import models as _inv  # noqa: F401
from app.modules.mes import models as _mes  # noqa: F401
from app.modules.om import models as _om  # noqa: F401
from app.modules.qc import models as _qc  # noqa: F401
from app.modules.scm import models as _scm  # noqa: F401
from app.modules.tax import models as _tax  # noqa: F401
from app.modules.tms import models as _tms  # noqa: F401
from app.modules.prd import models as _prd  # noqa: F401

target_metadata = SQLModel.metadata


# Schemas already deployed by migrations 001-003; skip them during
# autogenerate so we only emit DDL for the new AxonOS modules.
_DEPLOYED_SCHEMAS = {"admin", "mdm", "bom", "po", "collab"}


def include_object(obj, name, type_, reflected, compare_to):
    if type_ == "table" and name == "alembic_version":
        return False
    schema = getattr(obj, "schema", None)
    if schema is None and hasattr(obj, "table"):
        schema = getattr(obj.table, "schema", None)
    if schema in _DEPLOYED_SCHEMAS:
        return False
    return True


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        include_schemas=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_object=include_object,
        include_schemas=True,
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
