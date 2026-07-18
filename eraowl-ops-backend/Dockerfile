FROM python:3.12-slim AS builder

WORKDIR /app
# Install from pyproject.toml — the single source of truth for dependencies
COPY pyproject.toml .
COPY app/ ./app/
RUN pip install --no-cache-dir --break-system-packages .

FROM python:3.12-slim AS runner

WORKDIR /app
RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY alembic/ ./alembic/
COPY alembic.ini .

USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
