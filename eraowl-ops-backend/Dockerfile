FROM python:3.12-slim AS builder

WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir --break-system-packages \
    fastapi>=0.115.0 \
    "uvicorn[standard]>=0.32.0" \
    "sqlalchemy[asyncio]>=2.0.36" \
    sqlmodel>=0.0.22 \
    asyncpg>=0.30.0 \
    psycopg2-binary>=2.9.10 \
    alembic>=1.14.0 \
    pydantic>=2.10.0 \
    pydantic-settings>=2.7.0 \
    "python-jose[cryptography]>=3.3.0" \
    python-multipart>=0.0.18 \
    redis>=5.2.0 \
    slowapi>=0.1.9 \
    httpx>=0.28.0 \
    pandas>=2.2.0 \
    bcrypt>=4.1.0

FROM python:3.12-slim AS runner

WORKDIR /app
RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini .

USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
