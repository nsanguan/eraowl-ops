BEGIN;

-- ============================================================
-- PRIVILEGES
-- ============================================================

INSERT INTO admin.privileges (privilege_id, module, action, description) VALUES
(gen_random_uuid(), 'admin', 'view', 'View admin'),
(gen_random_uuid(), 'admin', 'manage_users', 'Manage users'),
(gen_random_uuid(), 'admin', 'manage_roles', 'Manage roles'),
(gen_random_uuid(), 'admin', 'assign_privileges', 'Assign privileges'),
(gen_random_uuid(), 'admin', 'view_audit_logs', 'View audit logs'),
(gen_random_uuid(), 'org_structure', 'view', 'View org structure'),
(gen_random_uuid(), 'org_structure', 'manage_corporate', 'Manage corporates'),
(gen_random_uuid(), 'org_structure', 'manage_company', 'Manage companies'),
(gen_random_uuid(), 'org_structure', 'manage_site', 'Manage sites'),
(gen_random_uuid(), 'org_structure', 'manage_warehouse', 'Manage warehouses'),
(gen_random_uuid(), 'org_structure', 'manage_locator', 'Manage locators'),
(gen_random_uuid(), 'party', 'view', 'View parties'),
(gen_random_uuid(), 'party', 'manage_supplier', 'Manage suppliers'),
(gen_random_uuid(), 'party', 'manage_customer', 'Manage customers'),
(gen_random_uuid(), 'party', 'manage_address', 'Manage addresses'),
(gen_random_uuid(), 'item', 'view', 'View items'),
(gen_random_uuid(), 'item', 'manage_item', 'Manage items'),
(gen_random_uuid(), 'item', 'manage_category', 'Manage categories'),
(gen_random_uuid(), 'item', 'manage_uom', 'Manage UOMs'),
(gen_random_uuid(), 'item', 'manage_item_organization', 'Manage item-org'),
(gen_random_uuid(), 'bom', 'view', 'View BOMs'),
(gen_random_uuid(), 'bom', 'create', 'Create BOMs'),
(gen_random_uuid(), 'bom', 'edit', 'Edit BOMs'),
(gen_random_uuid(), 'bom', 'approve', 'Approve BOMs');

-- ============================================================
-- ROLES
-- ============================================================

INSERT INTO admin.roles (role_id, role_name, description) VALUES
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0001', 'Administrator', 'Full system access'),
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0002', 'Manager', 'Manage transactions'),
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0003', 'Operator', 'Operational access');

-- Admin role gets ALL privileges
INSERT INTO admin.role_privileges (role_id, privilege_id)
SELECT 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0001', privilege_id FROM admin.privileges;

-- Manager role privileges
INSERT INTO admin.role_privileges (role_id, privilege_id)
SELECT 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0002', privilege_id FROM admin.privileges
WHERE (module, action) IN (
    ('admin', 'view'), ('admin', 'manage_users'),
    ('org_structure', 'view'), ('org_structure', 'manage_company'), ('org_structure', 'manage_site'), ('org_structure', 'manage_warehouse'),
    ('party', 'view'), ('party', 'manage_supplier'), ('party', 'manage_customer'),
    ('item', 'view'), ('item', 'manage_item'), ('item', 'manage_category'),
    ('bom', 'view'), ('bom', 'create'), ('bom', 'edit')
);

-- Operator role — view-only
INSERT INTO admin.role_privileges (role_id, privilege_id)
SELECT 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0003', privilege_id FROM admin.privileges
WHERE action = 'view';

-- ============================================================
-- USERS
-- ============================================================

INSERT INTO admin.users (user_id, username, email, hashed_password, permission_version, is_active) VALUES
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0001', 'admin',    'admin@eraowl.com',    '$2b$12$ndrafh6UTmbNm1MtU2qtk.xYHItDY48lDP8MJmzcdCqD6eTTOUg3q', 0, true),
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0002', 'manager',  'manager@eraowl.com',  '$2b$12$ndrafh6UTmbNm1MtU2qtk.xYHItDY48lDP8MJmzcdCqD6eTTOUg3q', 0, true),
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0003', 'operator', 'operator@eraowl.com', '$2b$12$os2o0SiIK8aVckAr/t0bxOW1whhH1syzDADmUiUEgyXFsxMXn8Z/.', 0, true);

INSERT INTO admin.user_roles (user_id, role_id) VALUES
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0001', 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0001'),
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0002', 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0002'),
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0003', 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaa0003');

-- ============================================================
-- ORG STRUCTURE
-- ============================================================

INSERT INTO mdm.corporates (corporate_id, corp_name, corp_code) VALUES
('cccccccc-cccc-cccc-cccc-cccccccc0001', 'EraOwl Group Co., Ltd.', 'ERAOWL');

INSERT INTO mdm.companies (company_id, corporate_id, legal_name, tax_id, company_code) VALUES
('dddddddd-dddd-dddd-dddd-dddddddd0001', 'cccccccc-cccc-cccc-cccc-cccccccc0001', 'EraOwl Manufacturing Co., Ltd.', '0105556000001', 'EOMFG');

INSERT INTO mdm.business_units (business_unit_id, company_id, bu_name, bu_code) VALUES
('eeeeeeee-eeee-eeee-eeee-eeeeeeee0001', 'dddddddd-dddd-dddd-dddd-dddddddd0001', 'Bangkok Operations', 'BKK-OPS'),
('eeeeeeee-eeee-eeee-eeee-eeeeeeee0002', 'dddddddd-dddd-dddd-dddd-dddddddd0001', 'Eastern Seaboard Operations', 'ESB-OPS');

-- Assign admin user to BU
INSERT INTO admin.user_business_units (user_id, business_unit_id) VALUES
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbb0001', 'eeeeeeee-eeee-eeee-eeee-eeeeeeee0001');

-- ============================================================
-- PARTY: Addresses
-- ============================================================

INSERT INTO mdm.addresses (address_id, address_line1, city, postal_code, country_code) VALUES
('11111111-1111-1111-1111-111111110001', '123 Ratchadaphisek Road', 'Bangkok', '10400', 'TH'),
('11111111-1111-1111-1111-111111110002', '789 Rama IV Road', 'Bangkok', '10500', 'TH'),
('11111111-1111-1111-1111-111111110003', '456 Sukhumvit Road', 'Bangkok', '10110', 'TH'),
('11111111-1111-1111-1111-111111110004', '321 Silom Road', 'Bangkok', '10500', 'TH');

-- ============================================================
-- ORG STRUCTURE (Sites, Warehouses, Locators — after addresses exist)
-- ============================================================

INSERT INTO mdm.sites (site_id, business_unit_id, site_name, site_code, address_id) VALUES
('ffffffff-ffff-ffff-ffff-ffffffff0001', 'eeeeeeee-eeee-eeee-eeee-eeeeeeee0001', 'Bangkok HQ', 'BKK-HQ', '11111111-1111-1111-1111-111111110001');

INSERT INTO mdm.warehouses (warehouse_id, site_id, warehouse_name, warehouse_code) VALUES
('99999999-9999-9999-9999-999999990001', 'ffffffff-ffff-ffff-ffff-ffffffff0001', 'Main Warehouse', 'WH-MAIN');

-- Warehouse Locators (Zone A-C, Aisle 01-02, Rack 01-02, Bin 01 = 12 locators)
INSERT INTO mdm.warehouse_locators (warehouse_locator_id, warehouse_id, zone, aisle, rack, bin, locator_code) VALUES
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'A', '01', '01', '01', 'ZA-A01-R01-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'A', '01', '02', '01', 'ZA-A01-R02-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'A', '02', '01', '01', 'ZA-A02-R01-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'A', '02', '02', '01', 'ZA-A02-R02-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'B', '01', '01', '01', 'ZB-A01-R01-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'B', '01', '02', '01', 'ZB-A01-R02-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'B', '02', '01', '01', 'ZB-A02-R01-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'B', '02', '02', '01', 'ZB-A02-R02-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'C', '01', '01', '01', 'ZC-A01-R01-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'C', '01', '02', '01', 'ZC-A01-R02-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'C', '02', '01', '01', 'ZC-A02-R01-B01'),
(gen_random_uuid(), '99999999-9999-9999-9999-999999990001', 'C', '02', '02', '01', 'ZC-A02-R02-B01');

-- ============================================================
-- PARTY: Suppliers & Customers
-- ============================================================

-- Supplier 1: Siam Steel
INSERT INTO mdm.parties (party_id, party_type, party_name, tax_id) VALUES
('22222222-2222-2222-2222-222222220001', 'ORGANIZATION', 'Siam Steel Co., Ltd.', '0105556000002');
INSERT INTO mdm.party_roles (party_role_id, party_id, role_type) VALUES
(gen_random_uuid(), '22222222-2222-2222-2222-222222220001', 'SUPPLIER');
INSERT INTO mdm.suppliers (supplier_id, party_id, supplier_code, payment_term_days, currency) VALUES
('33333333-3333-3333-3333-333333330001', '22222222-2222-2222-2222-222222220001', 'SUP-001', 30, 'THB');
INSERT INTO mdm.party_sites (party_site_id, party_id, address_id, site_name, is_primary) VALUES
(gen_random_uuid(), '22222222-2222-2222-2222-222222220001', '11111111-1111-1111-1111-111111110002', 'Headquarters', true);
INSERT INTO mdm.party_site_uses (party_site_use_id, party_site_id, use_type)
SELECT gen_random_uuid(), party_site_id, 'BILL_TO' FROM mdm.party_sites
WHERE party_id = '22222222-2222-2222-2222-222222220001' LIMIT 1;

-- Customer 1: Mega Retail
INSERT INTO mdm.parties (party_id, party_type, party_name, tax_id) VALUES
('22222222-2222-2222-2222-222222220002', 'ORGANIZATION', 'Mega Retail Co., Ltd.', '0105556000003');
INSERT INTO mdm.party_roles (party_role_id, party_id, role_type) VALUES
(gen_random_uuid(), '22222222-2222-2222-2222-222222220002', 'CUSTOMER');
INSERT INTO mdm.customers (customer_id, party_id, customer_code, credit_limit, payment_term_days) VALUES
('44444444-4444-4444-4444-444444440001', '22222222-2222-2222-2222-222222220002', 'CUST-001', 5000000, 60);
INSERT INTO mdm.party_sites (party_site_id, party_id, address_id, site_name, is_primary) VALUES
(gen_random_uuid(), '22222222-2222-2222-2222-222222220002', '11111111-1111-1111-1111-111111110003', 'Headquarters', true);
INSERT INTO mdm.party_site_uses (party_site_use_id, party_site_id, use_type)
SELECT gen_random_uuid(), party_site_id, 'SHIP_TO' FROM mdm.party_sites
WHERE party_id = '22222222-2222-2222-2222-222222220002' LIMIT 1;

-- Dual-role: Bangkok Industrial Trading (BOTH Supplier + Customer)
INSERT INTO mdm.parties (party_id, party_type, party_name, tax_id) VALUES
('22222222-2222-2222-2222-222222220003', 'ORGANIZATION', 'Bangkok Industrial Trading Co., Ltd.', '0105556000004');
INSERT INTO mdm.party_roles (party_role_id, party_id, role_type) VALUES
(gen_random_uuid(), '22222222-2222-2222-2222-222222220003', 'SUPPLIER'),
(gen_random_uuid(), '22222222-2222-2222-2222-222222220003', 'CUSTOMER');
INSERT INTO mdm.suppliers (supplier_id, party_id, supplier_code, payment_term_days, currency) VALUES
('33333333-3333-3333-3333-333333330002', '22222222-2222-2222-2222-222222220003', 'SUP-002', 45, 'THB');
INSERT INTO mdm.customers (customer_id, party_id, customer_code, credit_limit, payment_term_days) VALUES
('44444444-4444-4444-4444-444444440002', '22222222-2222-2222-2222-222222220003', 'CUST-002', 3000000, 30);
INSERT INTO mdm.party_sites (party_site_id, party_id, address_id, site_name, is_primary) VALUES
(gen_random_uuid(), '22222222-2222-2222-2222-222222220003', '11111111-1111-1111-1111-111111110004', 'Main Office', true);

-- ============================================================
-- ITEM: UOMs
-- ============================================================

INSERT INTO mdm.uoms (uom_id, uom_code, uom_name, uom_type) VALUES
('55555555-5555-5555-5555-555555550001', 'EA', 'Each', 'QUANTITY'),
('55555555-5555-5555-5555-555555550002', 'KG', 'Kilogram', 'WEIGHT'),
('55555555-5555-5555-5555-555555550003', 'M', 'Meter', 'LENGTH'),
('55555555-5555-5555-5555-555555550004', 'BOX', 'Box', 'QUANTITY'),
('55555555-5555-5555-5555-555555550005', 'L', 'Liter', 'VOLUME');

INSERT INTO mdm.uom_conversions (uom_conversion_id, from_uom_id, to_uom_id, conversion_factor) VALUES
(gen_random_uuid(), '55555555-5555-5555-5555-555555550004', '55555555-5555-5555-5555-555555550001', 12.0);

-- ============================================================
-- ITEM: Categories
-- ============================================================

INSERT INTO mdm.item_categories (item_category_id, category_set, category_code, category_name, parent_category_id) VALUES
('66666666-6666-6666-6666-666666660001', 'PURCHASING', 'PUR-ALL', 'All Purchasing', NULL),
('66666666-6666-6666-6666-666666660002', 'INVENTORY', 'INV-ALL', 'All Inventory', NULL),
('66666666-6666-6666-6666-666666660003', 'SALES', 'SAL-ALL', 'All Sales', NULL),
('66666666-6666-6666-6666-666666660004', 'INVENTORY', 'INV-RM', 'Raw Materials', '66666666-6666-6666-6666-666666660002'),
('66666666-6666-6666-6666-666666660005', 'INVENTORY', 'INV-FG', 'Finished Goods', '66666666-6666-6666-6666-666666660002');

-- ============================================================
-- ITEM: Items
-- ============================================================

INSERT INTO mdm.items (item_id, item_code, item_name, item_type, primary_uom_id, description) VALUES
('77777777-7777-7777-7777-777777770001', 'RM-001', 'Steel Sheet 2mm', 'RAW_MATERIAL', '55555555-5555-5555-5555-555555550002', 'Stainless steel sheet, grade 304, 2mm thickness'),
('77777777-7777-7777-7777-777777770002', 'SA-001', 'Motor Assembly Unit', 'SUB_ASSEMBLY', '55555555-5555-5555-5555-555555550001', 'Electric motor sub-assembly for pumps'),
('77777777-7777-7777-7777-777777770003', 'FG-001', 'Industrial Water Pump 5HP', 'FINISHED_GOOD', '55555555-5555-5555-5555-555555550001', '5HP centrifugal water pump, cast iron body'),
('77777777-7777-7777-7777-777777770004', 'SVC-001', 'Installation Service', 'SERVICE', '55555555-5555-5555-5555-555555550001', 'On-site pump installation and commissioning');

-- Category assignments
INSERT INTO mdm.item_category_assignments (item_category_assignment_id, item_id, item_category_id) VALUES
(gen_random_uuid(), '77777777-7777-7777-7777-777777770001', '66666666-6666-6666-6666-666666660004'),
(gen_random_uuid(), '77777777-7777-7777-7777-777777770003', '66666666-6666-6666-6666-666666660005'),
(gen_random_uuid(), '77777777-7777-7777-7777-777777770003', '66666666-6666-6666-6666-666666660003');

-- Item-Org assignments
INSERT INTO mdm.item_organizations (item_organization_id, item_id, warehouse_id, min_qty, max_qty, lead_time_days, standard_cost, is_enabled) VALUES
(gen_random_uuid(), '77777777-7777-7777-7777-777777770001', '99999999-9999-9999-9999-999999990001', 10, 1000, 7, 150.0, true),
(gen_random_uuid(), '77777777-7777-7777-7777-777777770002', '99999999-9999-9999-9999-999999990001', 5, 500, 14, 2500.0, true),
(gen_random_uuid(), '77777777-7777-7777-7777-777777770003', '99999999-9999-9999-9999-999999990001', 2, 200, 21, 15000.0, true);

-- Supplier Xref
INSERT INTO mdm.item_supplier_xref (item_supplier_xref_id, item_id, supplier_id, supplier_item_code, is_preferred) VALUES
(gen_random_uuid(), '77777777-7777-7777-7777-777777770001', '33333333-3333-3333-3333-333333330001', 'SIA-STL-2MM', true),
(gen_random_uuid(), '77777777-7777-7777-7777-777777770001', '33333333-3333-3333-3333-333333330002', 'BIT-STL-2MM', false);

-- ============================================================
-- BOM
-- ============================================================

-- BOM for FG-001 (Industrial Water Pump)
INSERT INTO mdm.bom_headers (bom_header_id, item_id, revision, status, effective_date_from) VALUES
('88888888-8888-8888-8888-888888880001', '77777777-7777-7777-7777-777777770003', 'A', 'ACTIVE', CURRENT_DATE);

INSERT INTO mdm.bom_lines (bom_line_id, bom_header_id, component_item_id, quantity_per, uom_id, operation_seq, effective_date_from) VALUES
(gen_random_uuid(), '88888888-8888-8888-8888-888888880001', '77777777-7777-7777-7777-777777770001', 25.0, '55555555-5555-5555-5555-555555550002', 10, CURRENT_DATE),
(gen_random_uuid(), '88888888-8888-8888-8888-888888880001', '77777777-7777-7777-7777-777777770002', 1.0, '55555555-5555-5555-5555-555555550001', 20, CURRENT_DATE);

-- BOM for SA-001 (Motor Assembly)
INSERT INTO mdm.bom_headers (bom_header_id, item_id, revision, status, effective_date_from) VALUES
('88888888-8888-8888-8888-888888880002', '77777777-7777-7777-7777-777777770002', 'A', 'ACTIVE', CURRENT_DATE);

INSERT INTO mdm.bom_lines (bom_line_id, bom_header_id, component_item_id, quantity_per, uom_id, operation_seq, effective_date_from) VALUES
(gen_random_uuid(), '88888888-8888-8888-8888-888888880002', '77777777-7777-7777-7777-777777770001', 5.0, '55555555-5555-5555-5555-555555550002', 10, CURRENT_DATE);

COMMIT;
