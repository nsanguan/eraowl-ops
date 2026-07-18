"""Initial schema: mdm (org_structure + party + item + bom), admin

Revision ID: 001
Revises:
Create Date: 2026-07-14
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS mdm")
    op.execute("CREATE SCHEMA IF NOT EXISTS bom")
    op.execute("CREATE SCHEMA IF NOT EXISTS admin")

    # =========================================================================
    # mdm schema — addresses (created first: mdm.sites references it via FK)
    # =========================================================================

    op.create_table(
        "addresses",
        sa.Column("address_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("address_line1", sa.String(255), nullable=True),
        sa.Column("address_line2", sa.String(255), nullable=True),
        sa.Column("city", sa.String(100), nullable=True),
        sa.Column("state_province", sa.String(100), nullable=True),
        sa.Column("postal_code", sa.String(20), nullable=True),
        sa.Column("country_code", sa.String(10), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    # =========================================================================
    # mdm schema — org_structure
    # =========================================================================

    op.create_table(
        "corporates",
        sa.Column("corporate_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("corp_name", sa.String(255), nullable=False),
        sa.Column("corp_code", sa.String(50), nullable=False, unique=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "companies",
        sa.Column("company_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("corporate_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.corporates.corporate_id"), nullable=False),
        sa.Column("legal_name", sa.String(255), nullable=True),
        sa.Column("tax_id", sa.String(50), nullable=True),
        sa.Column("company_code", sa.String(50), nullable=True, unique=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "business_units",
        sa.Column("business_unit_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("company_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.companies.company_id"), nullable=False),
        sa.Column("bu_name", sa.String(255), nullable=True),
        sa.Column("bu_code", sa.String(50), nullable=True, unique=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "sites",
        sa.Column("site_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("business_unit_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.business_units.business_unit_id"), nullable=False),
        sa.Column("site_name", sa.String(255), nullable=True),
        sa.Column("site_code", sa.String(50), nullable=True),
        sa.Column("address_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.addresses.address_id"), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "warehouses",
        sa.Column("warehouse_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("site_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.sites.site_id"), nullable=False),
        sa.Column("warehouse_name", sa.String(255), nullable=True),
        sa.Column("warehouse_code", sa.String(50), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "warehouse_locators",
        sa.Column("warehouse_locator_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("warehouse_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.warehouses.warehouse_id"), nullable=False),
        sa.Column("zone", sa.String(50), nullable=True),
        sa.Column("aisle", sa.String(50), nullable=True),
        sa.Column("rack", sa.String(50), nullable=True),
        sa.Column("bin", sa.String(50), nullable=True),
        sa.Column("locator_code", sa.String(100), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    # =========================================================================
    # mdm schema — party
    # =========================================================================

    op.create_table(
        "parties",
        sa.Column("party_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("party_type", sa.String(20), nullable=False),
        sa.Column("party_name", sa.String(255), nullable=False),
        sa.Column("tax_id", sa.String(50), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "party_sites",
        sa.Column("party_site_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("party_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.parties.party_id"), nullable=True),
        sa.Column("address_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.addresses.address_id"), nullable=True),
        sa.Column("site_name", sa.String(255), nullable=True),
        sa.Column("is_primary", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "party_site_uses",
        sa.Column("party_site_use_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("party_site_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.party_sites.party_site_id"), nullable=True),
        sa.Column("use_type", sa.String(20), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "party_roles",
        sa.Column("party_role_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("party_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.parties.party_id"), nullable=True),
        sa.Column("role_type", sa.String(20), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.UniqueConstraint("party_id", "role_type"),
        schema="mdm",
    )

    op.create_table(
        "suppliers",
        sa.Column("supplier_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("party_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.parties.party_id"), nullable=True, unique=True),
        sa.Column("supplier_code", sa.String(50), nullable=True, unique=True),
        sa.Column("payment_term_days", sa.Integer(), server_default=sa.text("30")),
        sa.Column("currency", sa.String(10), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "customers",
        sa.Column("customer_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("party_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.parties.party_id"), nullable=True, unique=True),
        sa.Column("customer_code", sa.String(50), nullable=True, unique=True),
        sa.Column("credit_limit", sa.Float(), nullable=True),
        sa.Column("payment_term_days", sa.Integer(), server_default=sa.text("30")),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    # =========================================================================
    # mdm schema — item
    # =========================================================================

    op.create_table(
        "uoms",
        sa.Column("uom_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("uom_code", sa.String(50), nullable=True, unique=True),
        sa.Column("uom_name", sa.String(100), nullable=True),
        sa.Column("uom_type", sa.String(20), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "item_categories",
        sa.Column("item_category_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("category_set", sa.String(20), nullable=True),
        sa.Column("category_code", sa.String(50), nullable=True),
        sa.Column("category_name", sa.String(255), nullable=True),
        sa.Column("parent_category_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.item_categories.item_category_id"), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "items",
        sa.Column("item_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("item_code", sa.String(50), nullable=True, unique=True),
        sa.Column("item_name", sa.String(255), nullable=True),
        sa.Column("item_type", sa.String(30), nullable=True),
        sa.Column("primary_uom_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.uoms.uom_id"), nullable=True),
        sa.Column("status", sa.String(20), server_default=sa.text("'ACTIVE'")),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "uom_conversions",
        sa.Column("uom_conversion_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("from_uom_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.uoms.uom_id"), nullable=True),
        sa.Column("to_uom_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.uoms.uom_id"), nullable=True),
        sa.Column("item_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.items.item_id"), nullable=True),
        sa.Column("conversion_factor", sa.Float(), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "item_category_assignments",
        sa.Column("item_category_assignment_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("item_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.items.item_id"), nullable=True),
        sa.Column("category_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.item_categories.item_category_id"), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.UniqueConstraint("item_id", "category_id"),
        schema="mdm",
    )

    op.create_table(
        "item_organizations",
        sa.Column("item_organization_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("item_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.items.item_id"), nullable=True),
        sa.Column("warehouse_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.warehouses.warehouse_id"), nullable=True),
        sa.Column("min_qty", sa.Float(), server_default=sa.text("0")),
        sa.Column("max_qty", sa.Float(), nullable=True),
        sa.Column("lead_time_days", sa.Integer(), server_default=sa.text("0")),
        sa.Column("costing_method", sa.String(20), nullable=True),
        sa.Column("standard_cost", sa.Float(), nullable=True),
        sa.Column("is_enabled", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    op.create_table(
        "item_supplier_xref",
        sa.Column("item_supplier_xref_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("item_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.items.item_id"), nullable=True),
        sa.Column("supplier_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.suppliers.supplier_id"), nullable=True),
        sa.Column("supplier_item_code", sa.String(100), nullable=True),
        sa.Column("is_preferred", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="mdm",
    )

    # =========================================================================
    # admin schema
    # =========================================================================

    op.create_table(
        "users",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("username", sa.String(100), nullable=False, unique=True),
        sa.Column("email", sa.String(255), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("permission_version", sa.Integer(), server_default=sa.text("0")),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("last_login_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="admin",
    )

    op.create_table(
        "roles",
        sa.Column("role_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("role_name", sa.String(100), nullable=False, unique=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="admin",
    )

    op.create_table(
        "privileges",
        sa.Column("privilege_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("module", sa.String(100), nullable=False),
        sa.Column("action", sa.String(100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        schema="admin",
    )

    op.create_table(
        "user_roles",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.users.user_id"), primary_key=True),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.roles.role_id"), primary_key=True),
        schema="admin",
    )

    op.create_table(
        "role_privileges",
        sa.Column("role_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.roles.role_id"), primary_key=True),
        sa.Column("privilege_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.privileges.privilege_id"), primary_key=True),
        schema="admin",
    )

    op.create_table(
        "user_business_units",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.users.user_id"), primary_key=True),
        sa.Column("bu_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.business_units.business_unit_id"), primary_key=True),
        schema="admin",
    )

    op.create_table(
        "audit_logs",
        sa.Column("audit_log_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.users.user_id"), nullable=True),
        sa.Column("action", sa.String(255), nullable=False),
        sa.Column("target_entity", sa.String(100), nullable=False),
        sa.Column("target_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("old_value", postgresql.JSONB(), nullable=True),
        sa.Column("new_value", postgresql.JSONB(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="admin",
    )

    op.create_table(
        "refresh_tokens",
        sa.Column("refresh_token_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.users.user_id"), nullable=True),
        sa.Column("token_hash", sa.String(512), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("revoked_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="admin",
    )

    op.create_table(
        "objects",
        sa.Column("object_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("object_type", sa.String(50), nullable=False),
        sa.Column("module_name", sa.String(100), nullable=True),
        sa.Column("object_name", sa.String(255), nullable=False),
        sa.Column("parent_object_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.objects.object_id"), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("metadata", postgresql.JSONB(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="admin",
    )
    op.create_index("ix_objects_type", "objects", ["object_type"], schema="admin")
    op.create_index("ix_objects_module", "objects", ["module_name"], schema="admin")
    op.create_index("ix_objects_parent", "objects", ["parent_object_id"], schema="admin")

    # =========================================================================
    # bom schema
    # =========================================================================

    op.create_table(
        "bom_headers",
        sa.Column("bom_header_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("item_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.items.item_id"), nullable=False),
        sa.Column("alternate_bom_code", sa.String(50), nullable=True),
        sa.Column("revision", sa.String(50), nullable=False),
        sa.Column("status", sa.String(30), server_default=sa.text("'PENDING_APPROVAL'")),
        sa.Column("effective_date_from", sa.Date(), nullable=False),
        sa.Column("effective_date_to", sa.Date(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="bom",
    )

    op.create_table(
        "bom_components",
        sa.Column("bom_component_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("bom_header_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("bom.bom_headers.bom_header_id"), nullable=False),
        sa.Column("component_item_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.items.item_id"), nullable=False),
        sa.Column("quantity_per", sa.Float(), nullable=False),
        sa.Column("uom_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("mdm.uoms.uom_id"), nullable=False),
        sa.Column("operation_seq", sa.Integer(), nullable=True),
        sa.Column("effective_date_from", sa.Date(), nullable=False),
        sa.Column("effective_date_to", sa.Date(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        schema="bom",
    )

    # =========================================================================
    # Indexes
    # =========================================================================

    op.create_index("ix_users_username", "users", ["username"], schema="admin")
    op.create_index("ix_users_email", "users", ["email"], schema="admin")
    op.create_index("ix_refresh_tokens_token_hash", "refresh_tokens", ["token_hash"], schema="admin")
    op.create_index("ix_refresh_tokens_user_id", "refresh_tokens", ["user_id"], schema="admin")
    op.create_index("ix_items_item_code", "items", ["item_code"], schema="mdm")
    op.create_index("ix_privileges_module_action", "privileges", ["module", "action"], schema="admin")
    op.create_index("ix_audit_logs_user_id", "audit_logs", ["user_id"], schema="admin")
    op.create_index("ix_audit_logs_target", "audit_logs", ["target_entity", "target_id"], schema="admin")


def downgrade() -> None:
    # =========================================================================
    # Indexes
    # =========================================================================

    op.drop_index("ix_audit_logs_target", table_name="audit_logs", schema="admin")
    op.drop_index("ix_audit_logs_user_id", table_name="audit_logs", schema="admin")
    op.drop_index("ix_privileges_module_action", table_name="privileges", schema="admin")
    op.drop_index("ix_items_item_code", table_name="items", schema="mdm")
    op.drop_index("ix_refresh_tokens_user_id", table_name="refresh_tokens", schema="admin")
    op.drop_index("ix_refresh_tokens_token_hash", table_name="refresh_tokens", schema="admin")
    op.drop_index("ix_users_email", table_name="users", schema="admin")
    op.drop_index("ix_users_username", table_name="users", schema="admin")

    # =========================================================================
    # bom schema
    # =========================================================================

    op.drop_table("bom_components", schema="bom")
    op.drop_table("bom_headers", schema="bom")

    # =========================================================================
    # admin schema
    # =========================================================================

    op.drop_index("ix_objects_parent", table_name="objects", schema="admin")
    op.drop_index("ix_objects_module", table_name="objects", schema="admin")
    op.drop_index("ix_objects_type", table_name="objects", schema="admin")
    op.drop_table("objects", schema="admin")
    op.drop_table("refresh_tokens", schema="admin")
    op.drop_table("audit_logs", schema="admin")
    op.drop_table("user_business_units", schema="admin")
    op.drop_table("role_privileges", schema="admin")
    op.drop_table("user_roles", schema="admin")
    op.drop_table("privileges", schema="admin")
    op.drop_table("roles", schema="admin")
    op.drop_table("users", schema="admin")

    # =========================================================================
    # mdm schema — item
    # =========================================================================

    op.drop_table("item_supplier_xref", schema="mdm")
    op.drop_table("item_organizations", schema="mdm")
    op.drop_table("item_category_assignments", schema="mdm")
    op.drop_table("uom_conversions", schema="mdm")
    op.drop_table("items", schema="mdm")
    op.drop_table("item_categories", schema="mdm")
    op.drop_table("uoms", schema="mdm")

    # =========================================================================
    # mdm schema — party
    # =========================================================================

    op.drop_table("customers", schema="mdm")
    op.drop_table("suppliers", schema="mdm")
    op.drop_table("party_roles", schema="mdm")
    op.drop_table("party_site_uses", schema="mdm")
    op.drop_table("party_sites", schema="mdm")
    op.drop_table("parties", schema="mdm")

    # =========================================================================
    # mdm schema — org_structure
    # =========================================================================

    op.drop_table("warehouse_locators", schema="mdm")
    op.drop_table("warehouses", schema="mdm")
    op.drop_table("sites", schema="mdm")
    op.drop_table("business_units", schema="mdm")
    op.drop_table("companies", schema="mdm")
    op.drop_table("corporates", schema="mdm")

    # addresses dropped last: mdm.sites references it via FK
    op.drop_table("addresses", schema="mdm")

    # =========================================================================
    # Schemas
    # =========================================================================

    op.execute("DROP SCHEMA IF EXISTS bom CASCADE")
    op.execute("DROP SCHEMA IF EXISTS mdm CASCADE")
    op.execute("DROP SCHEMA IF EXISTS admin CASCADE")
