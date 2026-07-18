import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.engine import make_url
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import SQLModel

from app.core.config import settings


# Swap only the database *name* — a naive str.replace would also rewrite the
# username ("eraowlopsadmin" contains "eraowlops").
TEST_DATABASE_URL = make_url(settings.DATABASE_URL).set(database="eraowlops_test").render_as_string(hide_password=False)


@pytest_asyncio.fixture()
async def test_engine():
    # Function-scoped: each test gets its own engine whose connections are
    # bound to that test's event loop (pytest-asyncio uses one loop per test).
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture()
async def db_session(test_engine):
    # Importing the app registers every module's models on SQLModel.metadata
    import app.main  # noqa: F401
    from sqlalchemy import text

    async with test_engine.begin() as conn:
        # create_all does not create PostgreSQL schemas — do it explicitly
        schemas = sorted({t.schema for t in SQLModel.metadata.tables.values() if t.schema})
        for schema in schemas:
            await conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))
        await conn.run_sync(SQLModel.metadata.create_all)
    # autoflush=False matches the production session factory (app/core/database.py);
    # with autoflush on, an ORM UPDATE expires server-onupdate attributes and
    # later sync attribute access raises MissingGreenlet under asyncpg.
    session_factory = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)
    async with session_factory() as session:
        yield session
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)


@pytest_asyncio.fixture()
async def client(db_session):
    from app.main import app
    from app.core.database import get_db

    # Routers depend on get_db — override it so requests use the test session
    app.dependency_overrides[get_db] = lambda: db_session
    # Rate limiting (slowapi) keys on client IP — disable for deterministic tests
    app.state.limiter.enabled = False

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.state.limiter.enabled = True
    app.dependency_overrides.clear()
