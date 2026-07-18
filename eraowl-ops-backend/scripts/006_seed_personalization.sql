-- ============================================================================
-- EraOwl-OPS UI Personalization — Base Templates Seed
-- Matches alembic revision 002 (admin.ui_standard_templates).
-- Run after 005_ui_personalization.sql / `alembic upgrade head`.
--
-- page_key        = frontend route (the value PagesPage passes to loadPersonalization)
-- base_layout_json = tree of { id, styles } nodes, one per real UI
--                   component on the page (header, tab strip, InteractiveGrid,
--                   StatCard region). Node ids are keyed by route/endpoint
--                   segment so they stay stable if UI copy changes.
--                   PersonalizeWrapper registers componentId == node id.
--
-- Grounded in current frontend code (App.jsx routes + each page's JSX):
--   /admin/users          -> UserManagement.jsx     (h1 "Users", InteractiveGrid)
--   /admin/roles         -> RoleManagement.jsx    (h1 "Roles", InteractiveGrid)
--   /admin/objects       -> ObjectsPage.jsx        (header:code-objects, grid:code-objects)
--   /org-structure        -> OrgStructurePage.jsx    (6 tabs + 6 grids)
--   /party               -> PartyPage.jsx           (4 tabs + 4 grids)
--   /items               -> ItemPage.jsx            (3 tabs + 3 grids)
--   /bom                 -> BomPage.jsx              (2 tabs + 2 grids)
--   /collaboration/todo  -> TodoPage.jsx            (h1 "To-Do")
--   /collaboration/calendar -> CalendarPage.jsx      (h1 "Calendar")
--   /collaboration/activities -> ActivitiesPage.jsx   (h1 "Activities")
--   /                    -> DashboardHome.jsx         (h1 "EraOwl-OPS")
--
-- Idempotent: each row is inserted only when its page_key is absent,
-- so the script is safe to re-run.
-- ============================================================================

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10001', 'admin.users', '1.0.0',
       '{"id":"admin.users","children":[{"id":"header:users","styles":{}},{"id":"grid:users","styles":{}},{"id":"form:user","styles":{},"children":[{"id":"field:user.username","meta":{"label":"Username","required":true}},{"id":"field:user.email","meta":{"label":"Email"}},{"id":"field:user.password","meta":{"label":"Password"}},{"id":"field:user.is_active","meta":{"label":"Active"}},{"id":"field:user.roles","meta":{"label":"Roles"}}]}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'admin.users');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10002', 'admin.roles', '1.0.0',
       '{"id":"admin.roles","children":[{"id":"header:roles","styles":{}},{"id":"grid:roles","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'admin.roles');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10003', 'admin.objects', '1.0.0',
       '{"id":"admin.objects","children":[{"id":"header:code-objects","styles":{}},{"id":"grid:code-objects","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'admin.objects');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10004', 'mdm.org_structure', '1.0.0',
       '{"id":"mdm.org_structure","children":[{"id":"header:org-structure","styles":{}},{"id":"tabs:org-structure","styles":{}},{"id":"grid:corporates","styles":{}},{"id":"grid:companies","styles":{}},{"id":"grid:businessUnits","styles":{}},{"id":"grid:sites","styles":{}},{"id":"grid:warehouses","styles":{}},{"id":"grid:locators","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'mdm.org_structure');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10005', 'mdm.party', '1.0.0',
       '{"id":"mdm.party","children":[{"id":"header:party","styles":{}},{"id":"tabs:party","styles":{}},{"id":"grid:addresses","styles":{}},{"id":"grid:parties","styles":{}},{"id":"grid:suppliers","styles":{}},{"id":"grid:customers","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'mdm.party');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10006', 'mdm.item', '1.0.0',
       '{"id":"mdm.item","children":[{"id":"header:item-master","styles":{}},{"id":"tabs:items","styles":{}},{"id":"grid:items","styles":{}},{"id":"grid:item-categories","styles":{}},{"id":"grid:uoms","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'mdm.item');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10007', 'bom.bom', '1.0.0',
       '{"id":"bom.bom","children":[{"id":"header:bom","styles":{}},{"id":"tabs:bom","styles":{}},{"id":"grid:bom-headers","styles":{}},{"id":"grid:bom-lines","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'bom.bom');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10008', 'collaboration.todo', '1.0.0',
       '{"id":"collaboration.todo","children":[{"id":"header:todo","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'collaboration.todo');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10009', 'collaboration.calendar', '1.0.0',
       '{"id":"collaboration.calendar","children":[{"id":"header:calendar","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'collaboration.calendar');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10010', 'collaboration.activities', '1.0.0',
       '{"id":"collaboration.activities","children":[{"id":"header:activities","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'collaboration.activities');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10011', 'dashboard.home', '1.0.0',
       '{"id":"dashboard.home","children":[{"id":"header:dashboard","styles":{}}]}'
 WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'dashboard.home');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10012', 'admin.home', '1.0.0',
       '{"id":"admin.home","children":[{"id":"header:admin-home","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'admin.home');

INSERT INTO admin.ui_standard_templates (id, page_key, schema_version, base_layout_json)
SELECT 'c1c1c1c1-c1c1-c1c1-c1c1-c1c1c1c10013', 'admin.user_profiles', '1.0.0',
       '{"id":"admin.user_profiles","children":[{"id":"header:user-profiles","styles":{}},{"id":"grid:user-profiles","styles":{}},{"id":"panel:user-profiles-detail","styles":{}}]}'
WHERE NOT EXISTS (SELECT 1 FROM admin.ui_standard_templates WHERE page_key = 'admin.user_profiles');
