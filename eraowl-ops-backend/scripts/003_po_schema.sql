CREATE SCHEMA IF NOT EXISTS po;

-- ============================================================
-- po_headers
-- ============================================================
CREATE TABLE po.po_headers (
    po_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_number VARCHAR(50) NOT NULL UNIQUE,
    status VARCHAR(20) NOT NULL DEFAULT 'DRAFT' CHECK (status IN ('DRAFT','PENDING_APPROVAL','APPROVED','REJECTED','CLOSED','CANCELLED')),
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    supplier_id UUID REFERENCES mdm.suppliers(supplier_id),
    supplier_site_id UUID REFERENCES mdm.party_sites(party_site_id),
    currency_code VARCHAR(10) DEFAULT 'THB',
    exchange_rate DOUBLE PRECISION DEFAULT 1.0,
    payment_term_days INTEGER DEFAULT 30,
    description TEXT,
    total_amount DOUBLE PRECISION DEFAULT 0,
    business_unit_id UUID REFERENCES mdm.business_units(business_unit_id),
    buyer_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    object_version_number INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    update_by VARCHAR(100)
);

-- ============================================================
-- po_lines
-- ============================================================
CREATE TABLE po.po_lines (
    po_line_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_id UUID NOT NULL REFERENCES po.po_headers(po_id) ON DELETE CASCADE,
    line_num INTEGER NOT NULL,
    item_id UUID REFERENCES mdm.items(item_id),
    item_description TEXT,
    uom_id UUID REFERENCES mdm.uoms(uom_id),
    qty_ordered DOUBLE PRECISION NOT NULL DEFAULT 0,
    qty_received DOUBLE PRECISION DEFAULT 0,
    qty_invoiced DOUBLE PRECISION DEFAULT 0,
    unit_price DOUBLE PRECISION NOT NULL DEFAULT 0,
    line_amount DOUBLE PRECISION DEFAULT 0,
    tax_amount DOUBLE PRECISION DEFAULT 0,
    charge_amount DOUBLE PRECISION DEFAULT 0,
    need_by_date DATE,
    promise_date DATE,
    line_type VARCHAR(30) DEFAULT 'GOODS',
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    object_version_number INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    update_by VARCHAR(100),
    UNIQUE(po_id, line_num)
);

-- ============================================================
-- po_shipments
-- ============================================================
CREATE TABLE po.po_shipments (
    po_shipment_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_id UUID NOT NULL REFERENCES po.po_headers(po_id) ON DELETE CASCADE,
    po_line_id UUID NOT NULL REFERENCES po.po_lines(po_line_id) ON DELETE CASCADE,
    shipment_num INTEGER NOT NULL,
    qty_ordered DOUBLE PRECISION NOT NULL DEFAULT 0,
    qty_received DOUBLE PRECISION DEFAULT 0,
    qty_accepted DOUBLE PRECISION DEFAULT 0,
    qty_rejected DOUBLE PRECISION DEFAULT 0,
    expected_receipt_date DATE,
    actual_receipt_date DATE,
    warehouse_id UUID REFERENCES mdm.warehouses(warehouse_id),
    locator_id UUID REFERENCES mdm.warehouse_locators(warehouse_locator_id),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    object_version_number INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    update_by VARCHAR(100),
    UNIQUE(po_line_id, shipment_num)
);

-- ============================================================
-- po_distributions
-- ============================================================
CREATE TABLE po.po_distributions (
    distribution_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_id UUID NOT NULL REFERENCES po.po_headers(po_id) ON DELETE CASCADE,
    po_line_id UUID NOT NULL REFERENCES po.po_lines(po_line_id) ON DELETE CASCADE,
    po_shipment_id UUID REFERENCES po.po_shipments(po_shipment_id),
    distribution_num INTEGER NOT NULL,
    account_code VARCHAR(100),
    amount DOUBLE PRECISION DEFAULT 0,
    percent DOUBLE PRECISION DEFAULT 100,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    object_version_number INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    update_by VARCHAR(100)
);

-- ============================================================
-- po_releases (scheduled releases for blanket POs)
-- ============================================================
CREATE TABLE po.po_releases (
    release_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_id UUID NOT NULL REFERENCES po.po_headers(po_id) ON DELETE CASCADE,
    release_num INTEGER NOT NULL,
    release_amount DOUBLE PRECISION DEFAULT 0,
    release_date DATE,
    expected_delivery_date DATE,
    status VARCHAR(20) DEFAULT 'OPEN',
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- ============================================================
-- po_amendments (change history)
-- ============================================================
CREATE TABLE po.po_amendments (
    amendment_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_id UUID NOT NULL REFERENCES po.po_headers(po_id) ON DELETE CASCADE,
    amendment_num INTEGER NOT NULL,
    change_type VARCHAR(50) NOT NULL,
    change_data JSONB,
    reason TEXT,
    approved_by VARCHAR(100),
    approved_date DATE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- ============================================================
-- po_approvals (approval workflow log)
-- ============================================================
CREATE TABLE po.po_approvals (
    approval_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    po_id UUID NOT NULL REFERENCES po.po_headers(po_id) ON DELETE CASCADE,
    approval_level INTEGER NOT NULL,
    approver_id UUID REFERENCES admin.users(user_id),
    approver_name VARCHAR(255),
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING','APPROVED','REJECTED')),
    comments TEXT,
    approved_date TIMESTAMPTZ,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- ============================================================
-- INDEXES
-- ============================================================
CREATE INDEX ix_po_headers_status ON po.po_headers(status);
CREATE INDEX ix_po_headers_supplier ON po.po_headers(supplier_id);
CREATE INDEX ix_po_lines_po_id ON po.po_lines(po_id);
CREATE INDEX ix_po_shipments_po_line ON po.po_shipments(po_line_id);
CREATE INDEX ix_po_distributions_po_shipment ON po.po_distributions(po_shipment_id);
