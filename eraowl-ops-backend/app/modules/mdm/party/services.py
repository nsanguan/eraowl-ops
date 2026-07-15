import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import func

from app.modules.mdm.party.models import (
    Address, Party, PartySite, PartySiteUse, PartyRole, Supplier, Customer,
    SupplierSite, CustomerSite,
)
from app.modules.mdm.party.schemas import (
    AddressCreate, AddressUpdate,
    PartyCreate, PartyUpdate,
    PartySiteCreate, PartySiteUpdate,
    PartySiteUseCreate, PartySiteUseUpdate,
    PartyRoleCreate, PartyRoleUpdate,
    SupplierCreate, SupplierUpdate, SupplierOut,
    SupplierSiteCreate, SupplierSiteUpdate,
    CustomerCreate, CustomerUpdate, CustomerOut,
    CustomerSiteCreate, CustomerSiteUpdate,
)
from app.modules.mdm.party.exceptions import PartyNotFoundError


class PartyService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def _paginate(self, model, page: int, page_size: int, filters: dict | None = None):
        query = select(model).where(model.is_deleted == False)
        if filters:
            for col, val in filters.items():
                query = query.where(getattr(model, col) == val)
        count_q = select(func.count()).select_from(query.subquery())
        total = (await self.db.execute(count_q)).scalar() or 0
        rows = (await self.db.execute(query.offset((page - 1) * page_size).limit(page_size))).scalars().all()
        return list(rows), total

    async def _get_by_id(self, model, entity_id: uuid.UUID):
        pk_col = next(iter(model.__table__.primary_key.columns))
        row = (await self.db.execute(
            select(model).where(pk_col == entity_id, model.is_deleted == False)
        )).scalar_one_or_none()
        if not row:
            raise PartyNotFoundError(entity=model.__name__)
        return row

    async def _create(self, model, data):
        instance = model(**data.model_dump())
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def _update(self, model, entity_id: uuid.UUID, data):
        instance = await self._get_by_id(model, entity_id)
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(instance, key, val)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def _delete(self, model, entity_id: uuid.UUID):
        instance = await self._get_by_id(model, entity_id)
        instance.is_deleted = True
        await self.db.commit()

    # --- Addresses ---
    async def list_addresses(self, page: int = 1, page_size: int = 20):
        return await self._paginate(Address, page, page_size)

    async def get_address(self, entity_id: uuid.UUID):
        return await self._get_by_id(Address, entity_id)

    async def create_address(self, data: AddressCreate):
        return await self._create(Address, data)

    async def update_address(self, entity_id: uuid.UUID, data: AddressUpdate):
        return await self._update(Address, entity_id, data)

    async def delete_address(self, entity_id: uuid.UUID):
        await self._delete(Address, entity_id)

    # --- Parties ---
    async def list_parties(self, page: int = 1, page_size: int = 20, party_type: str | None = None):
        filters = {"party_type": party_type} if party_type else None
        return await self._paginate(Party, page, page_size, filters)

    async def get_party(self, entity_id: uuid.UUID):
        return await self._get_by_id(Party, entity_id)

    async def create_party(self, data: PartyCreate):
        return await self._create(Party, data)

    async def update_party(self, entity_id: uuid.UUID, data: PartyUpdate):
        return await self._update(Party, entity_id, data)

    async def delete_party(self, entity_id: uuid.UUID):
        await self._delete(Party, entity_id)

    # --- Party Sites ---
    async def list_party_sites(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(PartySite, page, page_size, filters)

    async def get_party_site(self, entity_id: uuid.UUID):
        return await self._get_by_id(PartySite, entity_id)

    async def create_party_site(self, data: PartySiteCreate):
        return await self._create(PartySite, data)

    async def update_party_site(self, entity_id: uuid.UUID, data: PartySiteUpdate):
        return await self._update(PartySite, entity_id, data)

    async def delete_party_site(self, entity_id: uuid.UUID):
        await self._delete(PartySite, entity_id)

    # --- Party Site Uses ---
    async def list_party_site_uses(self, page: int = 1, page_size: int = 20, party_site_id: uuid.UUID | None = None):
        filters = {"party_site_id": party_site_id} if party_site_id else None
        return await self._paginate(PartySiteUse, page, page_size, filters)

    async def get_party_site_use(self, entity_id: uuid.UUID):
        return await self._get_by_id(PartySiteUse, entity_id)

    async def create_party_site_use(self, data: PartySiteUseCreate):
        return await self._create(PartySiteUse, data)

    async def update_party_site_use(self, entity_id: uuid.UUID, data: PartySiteUseUpdate):
        return await self._update(PartySiteUse, entity_id, data)

    async def delete_party_site_use(self, entity_id: uuid.UUID):
        await self._delete(PartySiteUse, entity_id)

    # --- Party Roles ---
    async def list_party_roles(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(PartyRole, page, page_size, filters)

    async def get_party_role(self, entity_id: uuid.UUID):
        return await self._get_by_id(PartyRole, entity_id)

    async def create_party_role(self, data: PartyRoleCreate):
        return await self._create(PartyRole, data)

    async def update_party_role(self, entity_id: uuid.UUID, data: PartyRoleUpdate):
        return await self._update(PartyRole, entity_id, data)

    async def delete_party_role(self, entity_id: uuid.UUID):
        await self._delete(PartyRole, entity_id)

    # --- Suppliers ---
    async def list_suppliers(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        items, total = await self._paginate(Supplier, page, page_size, filters)

        if not items:
            return items, total

        party_ids = list({s.party_id for s in items})
        from sqlalchemy import select
        result = await self.db.execute(select(Party).where(Party.party_id.in_(party_ids)))
        party_map = {p.party_id: p for p in result.scalars().all()}

        enriched = []
        for s in items:
            out = SupplierOut.model_validate(s)
            party = party_map.get(s.party_id)
            if party:
                out.party_code = party.party_code
                out.party_name = party.party_name
            enriched.append(out)

        return enriched, total

    async def get_supplier(self, entity_id: uuid.UUID):
        s = await self._get_by_id(Supplier, entity_id)
        out = SupplierOut.model_validate(s)
        party = await self._get_by_id(Party, s.party_id)
        if party:
            out.party_code = party.party_code
            out.party_name = party.party_name
        return out

    async def create_supplier(self, data: SupplierCreate):
        return await self._create(Supplier, data)

    async def update_supplier(self, entity_id: uuid.UUID, data: SupplierUpdate):
        return await self._update(Supplier, entity_id, data)

    async def delete_supplier(self, entity_id: uuid.UUID):
        await self._delete(Supplier, entity_id)

    # --- Supplier Sites ---
    async def list_supplier_sites(self, page: int = 1, page_size: int = 20, supplier_id: uuid.UUID | None = None):
        filters = {"supplier_id": supplier_id} if supplier_id else None
        return await self._paginate(SupplierSite, page, page_size, filters)

    async def get_supplier_site(self, entity_id: uuid.UUID):
        return await self._get_by_id(SupplierSite, entity_id)

    async def create_supplier_site(self, data: SupplierSiteCreate):
        return await self._create(SupplierSite, data)

    async def update_supplier_site(self, entity_id: uuid.UUID, data: SupplierSiteUpdate):
        return await self._update(SupplierSite, entity_id, data)

    async def delete_supplier_site(self, entity_id: uuid.UUID):
        await self._delete(SupplierSite, entity_id)

    # --- Customers ---
    async def list_customers(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(Customer, page, page_size, filters)

    async def get_customer(self, entity_id: uuid.UUID):
        c = await self._get_by_id(Customer, entity_id)
        out = CustomerOut.model_validate(c)
        party = await self._get_by_id(Party, c.party_id)
        if party:
            out.party_code = party.party_code
            out.party_name = party.party_name
        return out

    async def create_customer(self, data: CustomerCreate):
        return await self._create(Customer, data)

    async def update_customer(self, entity_id: uuid.UUID, data: CustomerUpdate):
        return await self._update(Customer, entity_id, data)

    async def delete_customer(self, entity_id: uuid.UUID):
        await self._delete(Customer, entity_id)

    # --- Customer Sites ---
    async def list_customer_sites(self, page: int = 1, page_size: int = 20, customer_id: uuid.UUID | None = None):
        filters = {"customer_id": customer_id} if customer_id else None
        return await self._paginate(CustomerSite, page, page_size, filters)

    async def get_customer_site(self, entity_id: uuid.UUID):
        return await self._get_by_id(CustomerSite, entity_id)

    async def create_customer_site(self, data: CustomerSiteCreate):
        return await self._create(CustomerSite, data)

    async def update_customer_site(self, entity_id: uuid.UUID, data: CustomerSiteUpdate):
        return await self._update(CustomerSite, entity_id, data)

    async def delete_customer_site(self, entity_id: uuid.UUID):
        await self._delete(CustomerSite, entity_id)

    # ── TCA Composite ──
    async def create_composite_party(self, data) -> Party:
        from app.modules.mdm.party.schemas import CompositePartyCreate
        from sqlalchemy import text

        party = Party(
            party_number=data.party_number,
            party_name=data.party_name,
            party_type=data.party_type,
            tax_reference=data.tax_reference,
        )
        self.db.add(party)
        await self.db.flush()

        registered_roles = []
        for role_type in data.roles:
            pr = PartyRole(party_id=party.party_id, role_type=role_type)
            self.db.add(pr)
            await self.db.flush()
            registered_roles.append(pr)

            if role_type == "SUPPLIER":
                supp = Supplier(
                    party_id=party.party_id,
                    party_role_id=pr.party_role_id,
                    vendor_type_lookup_code=data.vendor_type_lookup_code,
                    payment_method_code=data.payment_method_code,
                )
                self.db.add(supp)
            elif role_type == "CUSTOMER":
                cust = Customer(
                    party_id=party.party_id,
                    party_role_id=pr.party_role_id,
                    customer_class_code=data.customer_class_code,
                    credit_limit=data.credit_limit,
                )
                self.db.add(cust)

        for site_data in data.sites:
            addr = Address(
                country=site_data.country,
                address_line1=site_data.address_line1,
                address_line2=site_data.address_line2,
                city=site_data.city,
                state=site_data.state,
                postal_code=site_data.postal_code,
            )
            self.db.add(addr)
            await self.db.flush()

            ps = PartySite(
                party_id=party.party_id,
                address_id=addr.address_id,
                party_site_number=f"{party.party_number}-{addr.address_id.hex[:6].upper()}",
                site_name=site_data.site_name,
            )
            self.db.add(ps)
            await self.db.flush()

            for idx, su_type in enumerate(site_data.site_uses):
                psu = PartySiteUse(
                    party_site_id=ps.party_site_id,
                    site_use_type=su_type,
                    is_primary=(idx == 0),
                )
                self.db.add(psu)

        await self.db.commit()
        await self.db.refresh(party)
        return party

    async def get_tca_view(self, party_id: uuid.UUID) -> dict:
        party = await self._get_by_id(Party, party_id)

        roles_result = await self.db.execute(
            select(PartyRole).where(PartyRole.party_id == party_id, PartyRole.is_deleted == False)
        )
        roles = list(roles_result.scalars().all())

        supplier = None
        customer = None
        role_types = [r.role_type for r in roles]
        if "SUPPLIER" in role_types:
            sr = await self.db.execute(
                select(Supplier).where(Supplier.party_id == party_id, Supplier.is_deleted == False)
            )
            supplier = sr.scalar_one_or_none()
        if "CUSTOMER" in role_types:
            cr = await self.db.execute(
                select(Customer).where(Customer.party_id == party_id, Customer.is_deleted == False)
            )
            customer = cr.scalar_one_or_none()

        sites_result = await self.db.execute(
            select(PartySite).where(PartySite.party_id == party_id, PartySite.is_deleted == False)
        )
        sites = list(sites_result.scalars().all())

        tca_sites = []
        for ps in sites:
            addr = None
            if ps.address_id:
                addr_result = await self.db.execute(
                    select(Address).where(Address.address_id == ps.address_id)
                )
                addr = addr_result.scalar_one_or_none()

            su_result = await self.db.execute(
                select(PartySiteUse).where(PartySiteUse.party_site_id == ps.party_site_id, PartySiteUse.is_deleted == False)
            )
            site_uses = list(su_result.scalars().all())

            tca_sites.append({
                "party_site_id": ps.party_site_id,
                "party_site_number": ps.party_site_number,
                "site_name": ps.site_name,
                "address": addr,
                "site_uses": site_uses,
            })

        return {
            "party": party,
            "roles": roles,
            "supplier": supplier,
            "customer": customer,
            "sites": tca_sites,
        }

    # ── Tree View ──
    async def get_party_tree(self, party_id: uuid.UUID) -> list[dict]:
        party = await self._get_by_id(Party, party_id)

        # Build role nodes with supplier/customer info
        role_nodes = []
        roles_result = await self.db.execute(
            select(PartyRole).where(PartyRole.party_id == party_id, PartyRole.is_deleted == False)
        )
        roles = list(roles_result.scalars().all())

        # Get all party sites for this party (shared across roles)
        ps_result = await self.db.execute(
            select(PartySite).where(PartySite.party_id == party_id, PartySite.is_deleted == False)
        )
        party_sites = list(ps_result.scalars().all())

        for r in roles:
            children = []
            # Add party sites as children under SUPPLIER or CUSTOMER role
            if r.role_type in ("SUPPLIER", "CUSTOMER"):
                prefix = "supplier-site" if r.role_type == "SUPPLIER" else "customer-site"
                for ps in party_sites:
                    addr = None
                    if ps.address_id:
                        addr_result = await self.db.execute(select(Address).where(Address.address_id == ps.address_id))
                        addr = addr_result.scalar_one_or_none()
                    children.append({
                        "node_id": f"{prefix}-{ps.party_site_id}",
                        "node_type": "site_item",
                        "label": ps.site_name or ps.party_site_number or "Site",
                        "entity": {
                            "party_site_id": str(ps.party_site_id),
                            "party_site_number": ps.party_site_number,
                            "site_name": ps.site_name,
                            "address": {
                                "country": addr.country if addr else "",
                                "address_line1": addr.address_line1 if addr else "",
                                "city": addr.city if addr else "",
                                "state": addr.state if addr else "",
                                "postal_code": addr.postal_code if addr else "",
                            } if addr else None,
                        },
                        "children": [],
                    })

            role_nodes.append({
                "node_id": f"role-{r.party_role_id}",
                "node_type": "role_item",
                "label": r.role_type,
                "entity": {"party_role_id": str(r.party_role_id), "role_type": r.role_type},
                "children": children if children else [],
            })

        site_nodes = []
        sites_result = await self.db.execute(
            select(PartySite).where(PartySite.party_id == party_id, PartySite.is_deleted == False)
        )
        sites = list(sites_result.scalars().all())
        for ps in sites:
            addr = None
            if ps.address_id:
                addr_result = await self.db.execute(select(Address).where(Address.address_id == ps.address_id))
                addr = addr_result.scalar_one_or_none()

            su_result = await self.db.execute(
                select(PartySiteUse).where(PartySiteUse.party_site_id == ps.party_site_id, PartySiteUse.is_deleted == False)
            )
            site_uses = list(su_result.scalars().all())

            use_nodes = []
            for su in site_uses:
                use_nodes.append({
                    "node_id": f"use-{su.site_use_id}",
                    "node_type": "site_use",
                    "label": f"{su.site_use_type}{' ★' if su.is_primary else ''}",
                    "entity": {
                        "site_use_id": str(su.site_use_id),
                        "site_use_type": su.site_use_type,
                        "is_primary": su.is_primary,
                    },
                })

            addr_label = f"{addr.address_line1}, {addr.city}" if addr else "No address"
            site_nodes.append({
                "node_id": f"site-{ps.party_site_id}",
                "node_type": "site_item",
                "label": ps.site_name or ps.party_site_number,
                "entity": {
                    "party_site_id": str(ps.party_site_id),
                    "party_site_number": ps.party_site_number,
                    "site_name": ps.site_name,
                    "address": {
                        "country": addr.country if addr else "",
                        "address_line1": addr.address_line1 if addr else "",
                        "city": addr.city if addr else "",
                        "state": addr.state if addr else "",
                        "postal_code": addr.postal_code if addr else "",
                    } if addr else None,
                },
                "children": use_nodes,
            })

        profile_node = {
            "node_id": f"profile-{party.party_id}",
            "node_type": "profile",
            "label": f"{party.party_name} ({party.party_number})",
            "entity": {
                "party_id": str(party.party_id),
                "party_name": party.party_name,
                "party_number": party.party_number,
                "party_type": party.party_type,
                "tax_reference": party.tax_reference,
            },
        }

        role_group = {
            "node_id": f"roles-{party.party_id}",
            "node_type": "role_group",
            "label": f"Business Roles ({len(role_nodes)})",
            "children": role_nodes,
        }

        site_group = {
            "node_id": f"sites-{party.party_id}",
            "node_type": "site_group",
            "label": f"Sites & Addresses ({len(site_nodes)})",
            "children": site_nodes,
        }

        return [profile_node, role_group, site_group]

    async def update_tree_node(self, party_id: uuid.UUID, node_type: str, action: str, entity: dict) -> None:
        party = await self._get_by_id(Party, party_id)

        if node_type == "profile" and action == "update":
            for field in ["party_name", "party_number", "party_type", "tax_reference"]:
                if field in entity:
                    setattr(party, field, entity[field])

        elif node_type == "role_item" and action in ("add", "delete"):
            if action == "add":
                role_type = entity.get("role_type", "UNKNOWN")
                pr = PartyRole(party_id=party_id, role_type=role_type)
                self.db.add(pr)
                await self.db.flush()

                if role_type == "SUPPLIER":
                    supplier_code = entity.get("supplier_code") or f"SUP-{pr.party_role_id.hex[:8].upper()}"
                    supplier = Supplier(
                        party_id=party_id,
                        party_role_id=pr.party_role_id,
                        supplier_code=supplier_code,
                        currency_code=entity.get("currency_code"),
                        payment_term_days=int(entity.get("payment_term_days", 30)),
                    )
                    self.db.add(supplier)
                elif role_type == "CUSTOMER":
                    customer_code = entity.get("customer_code") or f"CUS-{pr.party_role_id.hex[:8].upper()}"
                    customer = Customer(
                        party_id=party_id,
                        party_role_id=pr.party_role_id,
                        customer_code=customer_code,
                        credit_limit=float(entity.get("credit_limit", 0)),
                        payment_term_days=int(entity.get("payment_term_days", 30)),
                    )
                    self.db.add(customer)

            elif action == "delete" and "party_role_id" in entity:
                pr = await self._get_by_id(PartyRole, uuid.UUID(entity["party_role_id"]))
                pr.is_deleted = True

        elif node_type in ("site_item", "site_group") and action == "add":
            from app.modules.mdm.party.models import Address as AddrModel
            addr = AddrModel(
                country=entity.get("country", ""),
                address_line1=entity.get("address_line1", ""),
                address_line2=entity.get("address_line2"),
                city=entity.get("city", ""),
                state=entity.get("state"),
                postal_code=entity.get("postal_code"),
            )
            self.db.add(addr)
            await self.db.flush()

            ps = PartySite(
                party_id=party_id,
                address_id=addr.address_id,
                party_site_number=entity.get("party_site_number", f"SITE-{addr.address_id.hex[:8].upper()}"),
                site_name=entity.get("site_name"),
            )
            self.db.add(ps)

        elif node_type == "site_item" and action == "delete":
            if "party_site_id" in entity:
                ps = await self._get_by_id(PartySite, uuid.UUID(entity["party_site_id"]))
                ps.is_deleted = True

        elif node_type == "site_item" and action == "update":
            if "party_site_id" in entity:
                from app.modules.mdm.party.models import Address as AddrModel
                ps = await self._get_by_id(PartySite, uuid.UUID(entity["party_site_id"]))
                if "site_name" in entity:
                    ps.site_name = entity["site_name"]
                if ps.address_id:
                    addr = await self._get_by_id(AddrModel, ps.address_id)
                    for field in ["country", "address_line1", "address_line2", "city", "state", "postal_code"]:
                        if field in entity:
                            setattr(addr, field, entity[field])

        elif node_type == "site_use" and action == "add":
            psu = PartySiteUse(
                party_site_id=uuid.UUID(entity["party_site_id"]),
                site_use_type=entity.get("site_use_type", "BILL_TO"),
                is_primary=entity.get("is_primary", False),
            )
            self.db.add(psu)

        elif node_type == "site_use" and action in ("update", "delete"):
            if "site_use_id" in entity:
                psu = await self._get_by_id(PartySiteUse, uuid.UUID(entity["site_use_id"]))
                if action == "delete":
                    psu.is_deleted = True
                else:
                    if "site_use_type" in entity:
                        psu.site_use_type = entity["site_use_type"]
                    if "is_primary" in entity:
                        psu.is_primary = entity["is_primary"]

        await self.db.commit()
