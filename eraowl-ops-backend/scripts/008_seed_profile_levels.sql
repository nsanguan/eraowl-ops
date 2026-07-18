-- ============================================================================
-- Seed: User Profile Levels (EBS FND_PROFILE_LEVELS)
-- Idempotent: inserts only when the level_code is absent.
-- ============================================================================

INSERT INTO admin.profile_levels (profile_level_id, level_code, name, description, precedence)
SELECT 10001, 'site',        'Site',        'Entire instance (lowest specificity)',        4
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_levels WHERE level_code = 'site');

INSERT INTO admin.profile_levels (profile_level_id, level_code, name, description, precedence)
SELECT 10002, 'application',  'Application', 'A specific functional module (mdm, bom, ...)', 3
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_levels WHERE level_code = 'application');

INSERT INTO admin.profile_levels (profile_level_id, level_code, name, description, precedence)
SELECT 10003, 'role',         'Role',        'A security role (maps EBS Responsibility)',     2
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_levels WHERE level_code = 'role');

INSERT INTO admin.profile_levels (profile_level_id, level_code, name, description, precedence)
SELECT 10004, 'user',         'User',        'A specific user (highest specificity)',       1
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_levels WHERE level_code = 'user');

-- ----------------------------------------------------------------------------
-- Example profile options (illustrative; mirrors common EBS profile options)
-- ----------------------------------------------------------------------------

INSERT INTO admin.profile_options
  (profile_option_id, profile_option_name, user_profile_option_name, description, value_type, site_enabled, application_enabled, role_enabled, user_enabled, is_system)
SELECT
  'd1d1d1d1-d1d1-d1d1-d1d1-d1d1d1d10001', 'GL_DEFAULT_SET_OF_BOOKS', 'Default Set of Books',
  'Default ledger/set of books for the session', 'text',
  true, true, true, true, true
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_options WHERE profile_option_name = 'GL_DEFAULT_SET_OF_BOOKS');

INSERT INTO admin.profile_options
  (profile_option_id, profile_option_name, user_profile_option_name, description, value_type, site_enabled, application_enabled, role_enabled, user_enabled, is_system)
SELECT
  'd1d1d1d1-d1d1-d1d1-d1d1-d1d1d1d10002', 'ORG_ID', 'Default Operating Unit',
  'Default operating unit (MOAC)', 'text',
  true, true, true, true, true
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_options WHERE profile_option_name = 'ORG_ID');

INSERT INTO admin.profile_options
  (profile_option_id, profile_option_name, user_profile_option_name, description, value_type, site_enabled, application_enabled, role_enabled, user_enabled, is_system)
SELECT
  'd1d1d1d1-d1d1-d1d1-d1d1-d1d1d1d10003', 'UI_ITEMS_PER_PAGE', 'Items Per Page',
  'Default page size for list/grid views', 'number',
  true, false, true, true, false
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_options WHERE profile_option_name = 'UI_ITEMS_PER_PAGE');

INSERT INTO admin.profile_options
  (profile_option_id, profile_option_name, user_profile_option_name, description, value_type, site_enabled, application_enabled, role_enabled, user_enabled, is_system)
SELECT
  'd1d1d1d1-d1d1-d1d1-d1d1-d1d1d1d10004', 'APP_THEME', 'Application Theme',
  'Light / Dark / System UI theme', 'text',
  true, false, true, true, false
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_options WHERE profile_option_name = 'APP_THEME');

INSERT INTO admin.profile_options
  (profile_option_id, profile_option_name, user_profile_option_name, description, value_type, site_enabled, application_enabled, role_enabled, user_enabled, is_system)
SELECT
  'd1d1d1d1-d1d1-d1d1-d1d1-d1d1d1d10005', 'ENABLE_AUDIT_TRAIL', 'Enable Audit Trail',
  'Master switch for UI audit trail logging', 'checkbox',
  true, false, true, false, true
WHERE NOT EXISTS (SELECT 1 FROM admin.profile_options WHERE profile_option_name = 'ENABLE_AUDIT_TRAIL');
