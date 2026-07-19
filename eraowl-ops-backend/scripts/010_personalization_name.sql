-- ============================================================================
-- Add a human-readable 'name' to saved personalizations and themes so each
-- saved change can be labelled (Personalize Name). Applied after 009_ui_theme.sql.
-- ============================================================================

ALTER TABLE admin.user_ui_personalizations
    ADD COLUMN IF NOT EXISTS name VARCHAR(255);

ALTER TABLE admin.ui_themes
    ADD COLUMN IF NOT EXISTS name VARCHAR(255);
