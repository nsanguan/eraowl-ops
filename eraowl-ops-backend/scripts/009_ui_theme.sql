-- ============================================================================
-- 009_ui_theme.sql — Global Theme Roller tokens (APEX-style Theme Style)
-- Mirrors app/modules/admin/models.py:UiTheme (schema admin.ui_themes).
-- Idempotent: skips if the table already exists.
-- ============================================================================

CREATE TABLE IF NOT EXISTS admin.ui_themes (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id      UUID REFERENCES admin.users(user_id) ON DELETE CASCADE,
    role_id      UUID REFERENCES admin.roles(role_id) ON DELETE CASCADE,
    tokens       JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS ix_ui_themes_user ON admin.ui_themes (user_id);
CREATE INDEX IF NOT EXISTS ix_ui_themes_role ON admin.ui_themes (role_id);
