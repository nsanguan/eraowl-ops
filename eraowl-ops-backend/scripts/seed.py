#!/usr/bin/env python3
"""Seed all modules with default data."""

import asyncio
import hashlib
import uuid
from datetime import date, datetime, timedelta, timezone

from passlib.context import CryptContext
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = "postgresql+asyncpg://eraowlopsadmin:EraOwl2026@202.71.1.13:5435/eraowlops"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pw(password: str) -> str:
    return pwd_context.hash(password)


async def seed():
    engine = create_async_engine(DATABASE_URL, echo=True)
    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    # Run schema DDL
    async with engine.begin() as conn:
        with open("scripts/001_schema.sql") as f:
            schema_sql = f.read()
        for stmt in schema_sql.split(";\n"):
            stmt = stmt.strip()
            if stmt and not stmt.startswith("--"):
                await conn.execute(text(stmt))

    async with factory() as db:
        admin_pw = hash_pw("Admin@2026")
        operator_pw = hash_pw("Operator@2026")

        # --- PRIVILEGES ---
        privilege_data = [
            ("admin", "view", "View admin"),
            ("admin", "manage_users", "Manage users"),
            ("admin", "manage_roles", "Manage roles"),
            ("admin", "assign_privileges", "Assign privileges"),
            ("admin", "view_audit_logs", "View audit logs"),
            ("org_structure", "view", "View org structure"),
            ("org_structure", "manage_corporate", "Manage corporates"),
            ("org_structure", "manage_company", "Manage companies"),
            ("org_structure", "manage_site", "Manage sites"),
            ("org_structure", "manage_warehouse", "Manage warehouses"),
            ("org_structure", "manage_locator", "Manage locators"),
            ("party", "view", "View parties"),
            ("party", "manage_supplier", "Manage suppliers"),
            ("party", "manage_customer", "Manage customers"),
            ("party", "manage_address", "Manage addresses"),
            ("item", "view", "View items"),
            ("item", "manage_item", "Manage items"),
            ("item", "manage_category", "Manage categories"),
            ("item", "manage_uom", "Manage UOMs"),
            ("item", "manage_item_organization", "Manage item-org"),
            ("bom", "view", "View BOMs"),
            ("bom", "create", "Create BOMs"),
            ("bom", "edit", "Edit BOMs"),
            ("bom", "approve", "Approve BOMs"),
        ]
        priv_ids = {}
        for module, action, desc in privilege_data:
            pid = uuid.uuid4()
            priv_ids[f"{module}.{action}"] = pid
            await db.execute(text(
                "INSERT INTO admin.privileges (id, module, action, description) VALUES (:id, :mod, :act, :desc)"
            ), {"id": pid, "mod": module, "act": action, "desc": desc})

        # --- ROLES ---
        admin_role_id = uuid.uuid4()
        manager_role_id = uuid.uuid4()
        operator_role_id = uuid.uuid4()

        await db.execute(text(
            "INSERT INTO admin.roles (id, role_name, description) VALUES (:id, :name, :desc)"
        ), {"id": admin_role_id, "name": "Administrator", "desc": "Full system access"})
        await db.execute(text(
            "INSERT INTO admin.roles (id, role_name, description) VALUES (:id, :name, :desc)"
        ), {"id": manager_role_id, "name": "Manager", "desc": "Manage transactions"})
        await db.execute(text(
            "INSERT INTO admin.roles (id, role_name, description) VALUES (:id, :name, :desc)"
        ), {"id": operator_role_id, "name": "Operator", "desc": "Operational access"})

        # Admin role gets ALL privileges
        for priv in priv_ids.values():
            await db.execute(text(
                "INSERT INTO admin.role_privileges (role_id, privilege_id) VALUES (:rid, :pid)"
            ), {"rid": admin_role_id, "pid": priv})

        # Manager role gets view+create/edit for all modules
        manager_privs = [
            "admin.view", "admin.manage_users",
            "org_structure.view", "org_structure.manage_company", "org_structure.manage_site", "org_structure.manage_warehouse",
            "party.view", "party.manage_supplier", "party.manage_customer",
            "item.view", "item.manage_item", "item.manage_category",
            "bom.view", "bom.create", "bom.edit",
        ]
        for key in manager_privs:
            if key in priv_ids:
                await db.execute(text(
                    "INSERT INTO admin.role_privileges (role_id, privilege_id) VALUES (:rid, :pid)"
                ), {"rid": manager_role_id, "pid": priv_ids[key]})

        # Operator role — view-only for everything
        operator_privs = ["admin.view", "org_structure.view", "party.view", "item.view", "bom.view"]
        for key in operator_privs:
            if key in priv_ids:
                await db.execute(text(
                    "INSERT INTO admin.role_privileges (role_id, privilege_id) VALUES (:rid, :pid)"
                ), {"rid": operator_role_id, "pid": priv_ids[key]})

        # --- USERS ---
        admin_user_id = uuid.uuid4()
        manager_user_id = uuid.uuid4()
        operator_user_id = uuid.uuid4()

        await db.execute(text(
            "INSERT INTO admin.users (id, username, email, hashed_password, permission_version, is_active) VALUES (:id, :u, :e, :p, 0, true)"
        ), {"id": admin_user_id, "u": "admin", "e": "admin@eraowl.com", "p": admin_pw})
        await db.execute(text(
            "INSERT INTO admin.users (id, username, email, hashed_password, permission_version, is_active) VALUES (:id, :u, :e, :p, 0, true)"
        ), {"id": manager_user_id, "u": "manager", "e": "manager@eraowl.com", "p": admin_pw})
        await db.execute(text(
            "INSERT INTO admin.users (id, username, email, hashed_password, permission_version, is_active) VALUES (:id, :u, :e, :p, 0, true)"
        ), {"id": operator_user_id, "u": "operator", "e": "operator@eraowl.com", "p": operator_pw})

        # Assign roles
        for uid, rid in [(admin_user_id, admin_role_id), (manager_user_id, manager_role_id), (operator_user_id, operator_role_id)]:
            await db.execute(text(
                "INSERT INTO admin.user_roles (user_id, role_id) VALUES (:uid, :rid)"
            ), {"uid": uid, "rid": rid})

        # --- org_structure ---
        corp_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.corporates (id, corp_name, corp_code) VALUES (:id, :name, :code)"
        ), {"id": corp_id, "name": "EraOwl Group Co., Ltd.", "code": "ERAOWL"})

        company_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.companies (id, corporate_id, legal_name, tax_id, company_code) VALUES (:id, :cid, :name, :tax, :code)"
        ), {"id": company_id, "cid": corp_id, "name": "EraOwl Manufacturing Co., Ltd.", "tax": "0105556000001", "code": "EOMFG"})

        bu_id = uuid.uuid4()
        bu_id2 = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.business_units (id, company_id, bu_name, bu_code) VALUES (:id, :cid, :name, :code)"
        ), {"id": bu_id, "cid": company_id, "name": "Bangkok Operations", "code": "BKK-OPS"})
        await db.execute(text(
            "INSERT INTO mdm.business_units (id, company_id, bu_name, bu_code) VALUES (:id, :cid, :name, :code)"
        ), {"id": bu_id2, "cid": company_id, "name": "Eastern Seaboard Operations", "code": "ESB-OPS"})

        # Assign user to BU
        await db.execute(text(
            "INSERT INTO admin.user_business_units (user_id, bu_id) VALUES (:uid, :bu)"
        ), {"uid": admin_user_id, "bu": bu_id})

        # Sites
        site_id = uuid.uuid4()
        addr_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.addresses (id, address_line1, city, postal_code, country_code) VALUES (:id, :a1, :c, :p, :cc)"
        ), {"id": addr_id, "a1": "123 Ratchadaphisek Road", "c": "Bangkok", "p": "10400", "cc": "TH"})

        await db.execute(text(
            "INSERT INTO mdm.sites (id, business_unit_id, site_name, site_code, address_id) VALUES (:id, :bu, :name, :code, :addr)"
        ), {"id": site_id, "bu": bu_id, "name": "Bangkok HQ", "code": "BKK-HQ", "addr": addr_id})

        # Warehouse
        wh_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.warehouses (id, site_id, warehouse_name, warehouse_code) VALUES (:id, :sid, :name, :code)"
        ), {"id": wh_id, "sid": site_id, "name": "Main Warehouse", "code": "WH-MAIN"})

        # Locators
        for zone in ["A", "B", "C"]:
            for aisle in ["01", "02"]:
                for rack in ["01", "02"]:
                    loc_code = f"Z{zone}-A{aisle}-R{rack}-B01"
                    await db.execute(text(
                        "INSERT INTO mdm.warehouse_locators (id, warehouse_id, zone, aisle, rack, bin, locator_code) VALUES (:id, :wh, :z, :a, :r, :b, :lc)"
                    ), {"id": uuid.uuid4(), "wh": wh_id, "z": zone, "a": aisle, "r": rack, "b": "01", "lc": loc_code})

        # --- party: Suppliers & Customers ---
        sup_party_id = uuid.uuid4()
        cust_party_id = uuid.uuid4()
        both_party_id = uuid.uuid4()

        supplier_ids = []
        customer_ids = []

        # Supplier 1
        await db.execute(text(
            "INSERT INTO mdm.parties (id, party_type, party_name, tax_id) VALUES (:id, 'ORGANIZATION', :name, :tax)"
        ), {"id": sup_party_id, "name": "Siam Steel Co., Ltd.", "tax": "0105556000002"})
        await db.execute(text(
            "INSERT INTO mdm.party_roles (id, party_id, role_type) VALUES (:id, :pid, 'SUPPLIER')"
        ), {"id": uuid.uuid4(), "pid": sup_party_id})
        sup_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.suppliers (id, party_id, supplier_code, payment_term_days, currency) VALUES (:id, :pid, :code, :term, :cur)"
        ), {"id": sup_id, "pid": sup_party_id, "code": "SUP-001", "term": 30, "cur": "THB"})
        supplier_ids.append(sup_id)

        # Supplier address
        sup_addr_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.addresses (id, address_line1, city, postal_code, country_code) VALUES (:id, :a1, :c, :p, :cc)"
        ), {"id": sup_addr_id, "a1": "789 Rama IV Road", "c": "Bangkok", "p": "10500", "cc": "TH"})
        sup_site_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.party_sites (id, party_id, address_id, site_name, is_primary) VALUES (:id, :pid, :aid, :sn, true)"
        ), {"id": sup_site_id, "pid": sup_party_id, "aid": sup_addr_id, "sn": "Headquarters"})
        await db.execute(text(
            "INSERT INTO mdm.party_site_uses (id, party_site_id, use_type) VALUES (:id, :psid, :ut)"
        ), {"id": uuid.uuid4(), "psid": sup_site_id, "ut": "BILL_TO"})

        # Customer 1
        await db.execute(text(
            "INSERT INTO mdm.parties (id, party_type, party_name, tax_id) VALUES (:id, 'ORGANIZATION', :name, :tax)"
        ), {"id": cust_party_id, "name": "Mega Retail Co., Ltd.", "tax": "0105556000003"})
        await db.execute(text(
            "INSERT INTO mdm.party_roles (id, party_id, role_type) VALUES (:id, :pid, 'CUSTOMER')"
        ), {"id": uuid.uuid4(), "pid": cust_party_id})
        cust_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.customers (id, party_id, customer_code, credit_limit, payment_term_days) VALUES (:id, :pid, :code, :cl, :term)"
        ), {"id": cust_id, "pid": cust_party_id, "code": "CUST-001", "cl": 5000000.0, "term": 60})
        customer_ids.append(cust_id)

        # Customer address
        cust_addr_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.addresses (id, address_line1, city, postal_code, country_code) VALUES (:id, :a1, :c, :p, :cc)"
        ), {"id": cust_addr_id, "a1": "456 Sukhumvit Road", "c": "Bangkok", "p": "10110", "cc": "TH"})
        cust_site_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.party_sites (id, party_id, address_id, site_name, is_primary) VALUES (:id, :pid, :aid, :sn, true)"
        ), {"id": cust_site_id, "pid": cust_party_id, "aid": cust_addr_id, "sn": "Headquarters"})
        await db.execute(text(
            "INSERT INTO mdm.party_site_uses (id, party_site_id, use_type) VALUES (:id, :psid, :ut)"
        ), {"id": uuid.uuid4(), "psid": cust_site_id, "ut": "SHIP_TO"})

        # Both Supplier + Customer
        await db.execute(text(
            "INSERT INTO mdm.parties (id, party_type, party_name, tax_id) VALUES (:id, 'ORGANIZATION', :name, :tax)"
        ), {"id": both_party_id, "name": "Bangkok Industrial Trading Co., Ltd.", "tax": "0105556000004"})
        await db.execute(text(
            "INSERT INTO mdm.party_roles (id, party_id, role_type) VALUES (:id, :pid, 'SUPPLIER')"
        ), {"id": uuid.uuid4(), "pid": both_party_id})
        await db.execute(text(
            "INSERT INTO mdm.party_roles (id, party_id, role_type) VALUES (:id, :pid, 'CUSTOMER')"
        ), {"id": uuid.uuid4(), "pid": both_party_id})
        both_sup_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.suppliers (id, party_id, supplier_code, payment_term_days, currency) VALUES (:id, :pid, :code, :term, :cur)"
        ), {"id": both_sup_id, "pid": both_party_id, "code": "SUP-002", "term": 45, "cur": "THB"})
        supplier_ids.append(both_sup_id)
        both_cust_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.customers (id, party_id, customer_code, credit_limit, payment_term_days) VALUES (:id, :pid, :code, :cl, :term)"
        ), {"id": both_cust_id, "pid": both_party_id, "code": "CUST-002", "cl": 3000000.0, "term": 30})
        customer_ids.append(both_cust_id)

        both_addr_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.addresses (id, address_line1, city, postal_code, country_code) VALUES (:id, :a1, :c, :p, :cc)"
        ), {"id": both_addr_id, "a1": "321 Silom Road", "c": "Bangkok", "p": "10500", "cc": "TH"})
        both_site_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO mdm.party_sites (id, party_id, address_id, site_name, is_primary) VALUES (:id, :pid, :aid, :sn, true)"
        ), {"id": both_site_id, "pid": both_party_id, "aid": both_addr_id, "sn": "Main Office"})

        # --- item: UOMs ---
        each_id = uuid.uuid4()
        kg_id = uuid.uuid4()
        meter_id = uuid.uuid4()
        box_id = uuid.uuid4()
        liter_id = uuid.uuid4()
        uom_data = [
            (each_id, "EA", "Each", "QUANTITY"),
            (kg_id, "KG", "Kilogram", "WEIGHT"),
            (meter_id, "M", "Meter", "LENGTH"),
            (box_id, "BOX", "Box", "QUANTITY"),
            (liter_id, "L", "Liter", "VOLUME"),
        ]
        for uid, code, name, utype in uom_data:
            await db.execute(text(
                "INSERT INTO mdm.uoms (id, uom_code, uom_name, uom_type) VALUES (:id, :code, :name, :type)"
            ), {"id": uid, "code": code, "name": name, "type": utype})

        # UOM conversions
        await db.execute(text(
            "INSERT INTO mdm.uom_conversions (id, from_uom_id, to_uom_id, conversion_factor) VALUES (:id, :f, :t, :cf)"
        ), {"id": uuid.uuid4(), "f": box_id, "t": each_id, "cf": 12.0})

        # --- item: Categories ---
        cat_pur_id = uuid.uuid4()
        cat_inv_id = uuid.uuid4()
        cat_sale_id = uuid.uuid4()
        cat_rm_id = uuid.uuid4()
        cat_fg_id = uuid.uuid4()

        cat_data = [
            (cat_pur_id, "PURCHASING", "PUR-ALL", "All Purchasing", None),
            (cat_inv_id, "INVENTORY", "INV-ALL", "All Inventory", None),
            (cat_sale_id, "SALES", "SAL-ALL", "All Sales", None),
            (cat_rm_id, "INVENTORY", "INV-RM", "Raw Materials", cat_inv_id),
            (cat_fg_id, "INVENTORY", "INV-FG", "Finished Goods", cat_inv_id),
        ]
        for cid, cset, code, name, parent in cat_data:
            await db.execute(text(
                "INSERT INTO mdm.item_categories (id, category_set, category_code, category_name, parent_category_id) VALUES (:id, :set, :code, :name, :parent)"
            ), {"id": cid, "set": cset, "code": code, "name": name, "parent": parent})

        # --- item: Items ---
        rm_item_id = uuid.uuid4()
        sa_item_id = uuid.uuid4()
        fg_item_id = uuid.uuid4()
        svc_item_id = uuid.uuid4()

        item_data = [
            (rm_item_id, "RM-001", "Steel Sheet 2mm", "RAW_MATERIAL", kg_id, "Stainless steel sheet, grade 304, 2mm thickness"),
            (sa_item_id, "SA-001", "Motor Assembly Unit", "SUB_ASSEMBLY", each_id, "Electric motor sub-assembly for pumps"),
            (fg_item_id, "FG-001", "Industrial Water Pump 5HP", "FINISHED_GOOD", each_id, "5HP centrifugal water pump, cast iron body"),
            (svc_item_id, "SVC-001", "Installation Service", "SERVICE", each_id, "On-site pump installation and commissioning"),
        ]
        for item_id, code, name, itype, uom, desc in item_data:
            await db.execute(text(
                "INSERT INTO mdm.items (id, item_code, item_name, item_type, primary_uom_id, description) VALUES (:id, :code, :name, :type, :uom, :desc)"
            ), {"id": item_id, "code": code, "name": name, "type": itype, "uom": uom, "desc": desc})

        # Category assignments
        await db.execute(text(
            "INSERT INTO mdm.item_category_assignments (id, item_id, category_id) VALUES (:id, :iid, :cid)"
        ), {"id": uuid.uuid4(), "iid": rm_item_id, "cid": cat_rm_id})
        await db.execute(text(
            "INSERT INTO mdm.item_category_assignments (id, item_id, category_id) VALUES (:id, :iid, :cid)"
        ), {"id": uuid.uuid4(), "iid": fg_item_id, "cid": cat_fg_id})
        await db.execute(text(
            "INSERT INTO mdm.item_category_assignments (id, item_id, category_id) VALUES (:id, :iid, :cid)"
        ), {"id": uuid.uuid4(), "iid": fg_item_id, "cid": cat_sale_id})

        # Item-Org assignments
        for item_id, cost in [(rm_item_id, 150.0), (sa_item_id, 2500.0), (fg_item_id, 15000.0)]:
            await db.execute(text(
                "INSERT INTO mdm.item_organizations (id, item_id, warehouse_id, min_qty, max_qty, lead_time_days, standard_cost, is_enabled) VALUES (:id, :iid, :wh, :minq, :maxq, :lt, :cost, true)"
            ), {"id": uuid.uuid4(), "iid": item_id, "wh": wh_id, "minq": 10, "maxq": 1000, "lt": 7, "cost": cost})

        # Supplier Xref
        await db.execute(text(
            "INSERT INTO mdm.item_supplier_xref (id, item_id, supplier_id, supplier_item_code, is_preferred) VALUES (:id, :iid, :sid, :code, true)"
        ), {"id": uuid.uuid4(), "iid": rm_item_id, "sid": supplier_ids[0], "code": "SIA-STL-2MM"})
        await db.execute(text(
            "INSERT INTO mdm.item_supplier_xref (id, item_id, supplier_id, supplier_item_code, is_preferred) VALUES (:id, :iid, :sid, :code, false)"
        ), {"id": uuid.uuid4(), "iid": rm_item_id, "sid": supplier_ids[1], "code": "BIT-STL-2MM"})

        # --- BOM ---
        # BOM for FG-001 (Industrial Water Pump)
        bom_header_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO bom.bom_headers (id, item_id, revision, status, effective_date_from) VALUES (:id, :iid, :rev, :status, :eff)"
        ), {"id": bom_header_id, "iid": fg_item_id, "rev": "A", "status": "ACTIVE", "eff": date.today()})

        # BOM lines
        bom_line_data = [
            (rm_item_id, 25.0, kg_id, 10),       # 25 kg steel per pump
            (sa_item_id, 1.0, each_id, 20),       # 1 motor assembly per pump
        ]
        for comp_id, qty, uom, seq in bom_line_data:
            await db.execute(text(
                "INSERT INTO bom.bom_lines (id, bom_header_id, component_item_id, quantity_per, uom_id, operation_seq, effective_date_from) VALUES (:id, :bid, :cid, :qty, :uom, :seq, :eff)"
            ), {"id": uuid.uuid4(), "bid": bom_header_id, "cid": comp_id, "qty": qty, "uom": uom, "seq": seq, "eff": date.today()})

        # BOM for SA-001 (Motor Assembly)
        bom2_header_id = uuid.uuid4()
        await db.execute(text(
            "INSERT INTO bom.bom_headers (id, item_id, revision, status, effective_date_from) VALUES (:id, :iid, :rev, :status, :eff)"
        ), {"id": bom2_header_id, "iid": sa_item_id, "rev": "A", "status": "ACTIVE", "eff": date.today()})
        await db.execute(text(
            "INSERT INTO bom.bom_lines (id, bom_header_id, component_item_id, quantity_per, uom_id, operation_seq, effective_date_from) VALUES (:id, :bid, :cid, :qty, :uom, :seq, :eff)"
        ), {"id": uuid.uuid4(), "bid": bom2_header_id, "cid": rm_item_id, "qty": 5.0, "uom": kg_id, "seq": 10, "eff": date.today()})

        await db.commit()

    await engine.dispose()
    print()
    print("=" * 50)
    print("SEED COMPLETE")
    print("=" * 50)
    print()
    print("Users:")
    print("  admin    / Admin@2026    — Full system access")
    print("  manager  / Admin@2026    — Manage transactions")
    print("  operator / Operator@2026 — View-only access")
    print()
    print("API: http://localhost:8000/docs")
    print("Frontend: http://localhost:3100")


if __name__ == "__main__":
    asyncio.run(seed())
