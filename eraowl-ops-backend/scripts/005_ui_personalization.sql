-- ============================================================================
-- EraOwl-OPS UI Personalization Schema
-- Matches alembic revision 002 (admin.ui_standard_templates,
-- admin.user_ui_personalizations). Apply after 001_schema.sql.
-- ============================================================================

CREATE TABLE IF NOT EXISTS admin.ui_standard_templates (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    page_key          VARCHAR(255) NOT NULL,
    schema_version    VARCHAR(50)  NOT NULL,
    base_layout_json  JSONB        NOT NULL DEFAULT '{}'::jsonb,
    created_at        TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at        TIMESTAMPTZ  NOT NULL DEFAULT now(),
    CONSTRAINT uq_ui_standard_templates_page_key UNIQUE (page_key)
);

CREATE INDEX IF NOT EXISTS ix_ui_standard_templates_page_key
    ON admin.ui_standard_templates (page_key);

CREATE TABLE IF NOT EXISTS admin.user_ui_personalizations (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    page_key       VARCHAR(255) NOT NULL,
    user_id        UUID REFERENCES admin.users (user_id) ON DELETE CASCADE,
    role_id        UUID REFERENCES admin.roles (role_id) ON DELETE CASCADE,
    override_json  JSONB        NOT NULL DEFAULT '{}'::jsonb,
    created_at     TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at     TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS ix_user_ui_personalizations_page_key
    ON admin.user_ui_personalizations (page_key);
