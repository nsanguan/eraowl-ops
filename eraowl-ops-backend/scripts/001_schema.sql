DROP SCHEMA IF EXISTS org_structure, party, item, mdm, admin, bom CASCADE;

CREATE SCHEMA IF NOT EXISTS mdm;
CREATE SCHEMA IF NOT EXISTS admin;

-- ============================================================

-- ============================================================
-- org_structure
-- ============================================================

CREATE TABLE mdm.corporates (
    corporate_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    corp_name VARCHAR(255) NOT NULL,
    corp_code VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.companies (
    company_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    corporate_id UUID NOT NULL REFERENCES mdm.corporates(corporate_id),
    legal_name VARCHAR(255) NOT NULL,
    tax_id VARCHAR(50) NOT NULL,
    company_code VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.business_units (
    business_unit_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    company_id UUID NOT NULL REFERENCES mdm.companies(company_id),
    bu_name VARCHAR(255) NOT NULL,
    bu_code VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.addresses (
    address_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    state_province VARCHAR(100),
    postal_code VARCHAR(20),
    country_code VARCHAR(10),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.parties (
    party_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    party_type VARCHAR(20) NOT NULL CHECK (party_type IN ('PERSON','ORGANIZATION')),
    party_name VARCHAR(255) NOT NULL,
    tax_id VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.party_sites (
    party_site_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    party_id UUID NOT NULL REFERENCES mdm.parties(party_id),
    address_id UUID NOT NULL REFERENCES mdm.addresses(address_id),
    site_name VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.party_site_uses (
    party_site_use_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    party_site_id UUID NOT NULL REFERENCES mdm.party_sites(party_site_id),
    use_type VARCHAR(20) NOT NULL CHECK (use_type IN ('BILL_TO','SHIP_TO','REMIT_TO','GENERAL')),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.party_roles (
    party_role_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    party_id UUID NOT NULL REFERENCES mdm.parties(party_id),
    role_type VARCHAR(20) NOT NULL CHECK (role_type IN ('SUPPLIER','CUSTOMER','CARRIER')),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    UNIQUE(party_id, role_type)
);

CREATE TABLE mdm.suppliers (
    supplier_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    party_id UUID NOT NULL UNIQUE REFERENCES mdm.parties(party_id),
    supplier_code VARCHAR(50) NOT NULL UNIQUE,
    payment_term_days INTEGER DEFAULT 30,
    currency VARCHAR(10) DEFAULT 'THB',
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.customers (
    customer_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    party_id UUID NOT NULL UNIQUE REFERENCES mdm.parties(party_id),
    customer_code VARCHAR(50) NOT NULL UNIQUE,
    credit_limit DOUBLE PRECISION,
    payment_term_days INTEGER DEFAULT 30,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.sites (
    site_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    business_unit_id UUID NOT NULL REFERENCES mdm.business_units(business_unit_id),
    site_name VARCHAR(255) NOT NULL,
    site_code VARCHAR(50) NOT NULL,
    address_id UUID REFERENCES mdm.addresses(address_id),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.warehouses (
    warehouse_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    site_id UUID NOT NULL REFERENCES mdm.sites(site_id),
    warehouse_name VARCHAR(255) NOT NULL,
    warehouse_code VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.warehouse_locators (
    warehouse_locator_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    warehouse_id UUID NOT NULL REFERENCES mdm.warehouses(warehouse_id),
    zone VARCHAR(50) NOT NULL,
    aisle VARCHAR(50) NOT NULL,
    rack VARCHAR(50) NOT NULL,
    bin VARCHAR(50) NOT NULL,
    locator_code VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.uoms (
    uom_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    uom_code VARCHAR(50) NOT NULL UNIQUE,
    uom_name VARCHAR(100) NOT NULL,
    uom_type VARCHAR(20) NOT NULL CHECK (uom_type IN ('QUANTITY','WEIGHT','VOLUME','LENGTH')),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.item_categories (
    item_category_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    category_set VARCHAR(20) NOT NULL CHECK (category_set IN ('PURCHASING','SALES','INVENTORY','COSTING')),
    category_code VARCHAR(50) NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    parent_category_id UUID REFERENCES mdm.item_categories(item_category_id),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.items (
    item_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    item_code VARCHAR(50) NOT NULL UNIQUE,
    item_name VARCHAR(255) NOT NULL,
    item_type VARCHAR(30) NOT NULL CHECK (item_type IN ('FINISHED_GOOD','RAW_MATERIAL','SUB_ASSEMBLY','SERVICE')),
    primary_uom_id UUID NOT NULL REFERENCES mdm.uoms(uom_id),
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE','PENDING','OBSOLETE')),
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.uom_conversions (
    uom_conversion_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    from_uom_id UUID NOT NULL REFERENCES mdm.uoms(uom_id),
    to_uom_id UUID NOT NULL REFERENCES mdm.uoms(uom_id),
    item_id UUID REFERENCES mdm.items(item_id),
    conversion_factor DOUBLE PRECISION NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.item_category_assignments (
    item_category_assignment_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    item_id UUID NOT NULL REFERENCES mdm.items(item_id),
    item_category_id UUID NOT NULL REFERENCES mdm.item_categories(item_category_id),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    UNIQUE(item_id, item_category_id)
);

CREATE TABLE mdm.item_organizations (
    item_organization_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    item_id UUID NOT NULL REFERENCES mdm.items(item_id),
    warehouse_id UUID NOT NULL REFERENCES mdm.warehouses(warehouse_id),
    min_qty DOUBLE PRECISION DEFAULT 0,
    max_qty DOUBLE PRECISION,
    lead_time_days INTEGER DEFAULT 0,
    costing_method VARCHAR(20) DEFAULT 'STANDARD',
    standard_cost DOUBLE PRECISION,
    is_enabled BOOLEAN DEFAULT TRUE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.item_supplier_xref (
    item_supplier_xref_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    item_id UUID NOT NULL REFERENCES mdm.items(item_id),
    supplier_id UUID NOT NULL REFERENCES mdm.suppliers(supplier_id),
    supplier_item_code VARCHAR(100),
    is_preferred BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE admin.users (
    user_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    permission_version INTEGER DEFAULT 0 NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    last_login_at TIMESTAMPTZ,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE admin.roles (
    role_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    role_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE admin.privileges (
    privilege_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    module VARCHAR(100) NOT NULL,
    action VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE admin.user_roles (
    user_id UUID NOT NULL REFERENCES admin.users(user_id) ON DELETE CASCADE,
    role_id UUID NOT NULL REFERENCES admin.roles(role_id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE admin.role_privileges (
    role_id UUID NOT NULL REFERENCES admin.roles(role_id) ON DELETE CASCADE,
    privilege_id UUID NOT NULL REFERENCES admin.privileges(privilege_id) ON DELETE CASCADE,
    PRIMARY KEY (role_id, privilege_id)
);

CREATE TABLE admin.user_business_units (
    user_id UUID NOT NULL REFERENCES admin.users(user_id) ON DELETE CASCADE,
    business_unit_id UUID NOT NULL REFERENCES mdm.business_units(business_unit_id),
    PRIMARY KEY (user_id, business_unit_id)
);

CREATE TABLE admin.audit_logs (
    audit_log_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    user_id UUID REFERENCES admin.users(user_id),
    action VARCHAR(255) NOT NULL,
    target_entity VARCHAR(100) NOT NULL,
    target_id UUID,
    old_value JSONB,
    new_value JSONB,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE admin.refresh_tokens (
    refresh_token_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES admin.users(user_id) ON DELETE CASCADE,
    token_hash VARCHAR(512) NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    revoked_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.bom_headers (
    bom_header_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    item_id UUID NOT NULL REFERENCES mdm.items(item_id),
    alternate_bom_code VARCHAR(50),
    revision VARCHAR(50) NOT NULL,
    status VARCHAR(30) DEFAULT 'PENDING_APPROVAL' CHECK (status IN ('ACTIVE','PENDING_APPROVAL','OBSOLETE')),
    effective_date_from DATE NOT NULL,
    effective_date_to DATE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE mdm.bom_lines (
    bom_line_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    bom_header_id UUID NOT NULL REFERENCES mdm.bom_headers(bom_header_id) ON DELETE CASCADE,
    component_item_id UUID NOT NULL REFERENCES mdm.items(item_id),
    quantity_per DOUBLE PRECISION NOT NULL,
    uom_id UUID NOT NULL REFERENCES mdm.uoms(uom_id),
    operation_seq INTEGER,
    effective_date_from DATE NOT NULL,
    effective_date_to DATE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE INDEX ix_users_username ON admin.users(username);
CREATE INDEX ix_users_email ON admin.users(email);
CREATE INDEX ix_refresh_tokens_token_hash ON admin.refresh_tokens(token_hash);
CREATE INDEX ix_refresh_tokens_user_id ON admin.refresh_tokens(user_id);
CREATE INDEX ix_items_item_code ON mdm.items(item_code);
CREATE INDEX ix_privileges_module_action ON admin.privileges(module, action);
CREATE INDEX ix_audit_logs_user_id ON admin.audit_logs(user_id);
CREATE INDEX ix_audit_logs_target ON admin.audit_logs(target_entity, target_id);
