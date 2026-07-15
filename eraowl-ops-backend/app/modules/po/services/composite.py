import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.po.dto.schemas import (
    CreatePoCompositeRequest,
    CreatePoDistributionItem,
    CreatePoLineItem,
    CreatePoShipmentItem,
    UpdatePoCompositeRequest,
    UpdatePoDistributionItem,
    UpdatePoLineItem,
    UpdatePoShipmentItem,
)
from app.modules.po.models import (
    PoAmendment,
    PoApproval,
    PoDistribution,
    PoHeader,
    PoLine,
    PoRelease,
    PoShipment,
)


class PoCompositeService:
    """
    Master-detail composite CRUD for Purchase Orders.
    Mirrors axon-os PoHeadersService pattern:
     - Composite query: header + lines + shipments + distributions
     - Composite create: single transaction
     - Composite update: diff-based upsert with soft-delete
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_composite(self, po_id: uuid.UUID) -> dict:
        """Load full PO composite: header -> lines -> shipments -> distributions."""
        header = await self._get_header(po_id)
        if not header:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity="PoHeader")

        lines_result = await self.db.execute(
            select(PoLine).where(PoLine.po_id == po_id, PoLine.is_deleted == False)
            .order_by(PoLine.line_num)
        )
        lines = lines_result.scalars().all()

        line_ids = [l.po_line_id for l in lines]
        shipments = []
        if line_ids:
            shipments_result = await self.db.execute(
                select(PoShipment).where(PoShipment.po_line_id.in_(line_ids), PoShipment.is_deleted == False)
                .order_by(PoShipment.shipment_num)
            )
            shipments = shipments_result.scalars().all()

        shipment_ids = [s.po_shipment_id for s in shipments]
        distributions = []
        if shipment_ids:
            dist_result = await self.db.execute(
                select(PoDistribution).where(
                    PoDistribution.po_shipment_id.in_(shipment_ids), PoDistribution.is_deleted == False
                )
                .order_by(PoDistribution.distribution_num)
            )
            distributions = dist_result.scalars().all()

        releases_result = await self.db.execute(
            select(PoRelease).where(PoRelease.po_id == po_id, PoRelease.is_deleted == False)
            .order_by(PoRelease.release_num)
        )
        releases = releases_result.scalars().all()

        amendments_result = await self.db.execute(
            select(PoAmendment).where(PoAmendment.po_id == po_id, PoAmendment.is_deleted == False)
            .order_by(PoAmendment.amendment_num)
        )
        amendments = amendments_result.scalars().all()

        approvals_result = await self.db.execute(
            select(PoApproval).where(PoApproval.po_id == po_id, PoApproval.is_deleted == False)
            .order_by(PoApproval.approval_level)
        )
        approvals = approvals_result.scalars().all()

        dist_map: dict[uuid.UUID, list[dict]] = {}
        for d in distributions:
            dist_map.setdefault(d.po_shipment_id, []).append(d)

        ship_map: dict[uuid.UUID, list[dict]] = {}
        for s in shipments:
            s_dict = self._model_to_dict(s)
            s_dict["distributions"] = [self._model_to_dict(d) for d in dist_map.get(s.po_shipment_id, [])]
            ship_map.setdefault(s.po_line_id, []).append(s_dict)

        lines_out = []
        for line in lines:
            l_dict = self._model_to_dict(line)
            l_dict["shipments"] = ship_map.get(line.po_line_id, [])
            lines_out.append(l_dict)

        return {
            "header": self._model_to_dict(header),
            "lines": lines_out,
            "releases": [self._model_to_dict(r) for r in releases],
            "amendments": [self._model_to_dict(a) for a in amendments],
            "approvals": [self._model_to_dict(a) for a in approvals],
        }

    async def create_composite(self, data: CreatePoCompositeRequest) -> dict:
        """Create PO with all children in a single transaction."""
        header = PoHeader(**data.header.model_dump())
        self.db.add(header)
        await self.db.flush()

        for line_item in data.lines:
            line = await self._create_line(header.po_id, line_item)
            for ship_item in line_item.shipments:
                shipment = await self._create_shipment(header.po_id, line.po_line_id, ship_item)
                for dist_item in ship_item.distributions:
                    await self._create_distribution(header.po_id, line.po_line_id, shipment.po_shipment_id, dist_item)

        for rel in data.releases:
            release = PoRelease(po_id=header.po_id, **rel.model_dump(exclude={"po_id"}))
            self.db.add(release)

        for amd in data.amendments:
            amendment = PoAmendment(po_id=header.po_id, **amd.model_dump(exclude={"po_id"}))
            self.db.add(amendment)

        await self.db.commit()
        return await self.get_composite(header.po_id)

    async def update_composite(self, po_id: uuid.UUID, data: UpdatePoCompositeRequest) -> dict:
        """Full reconcile: header update + diff-based upsert for children."""
        header = await self._get_header(po_id)
        if not header:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity="PoHeader")

        for key, val in data.header.model_dump(exclude_unset=True).items():
            setattr(header, key, val)
        header.object_version_number = (header.object_version_number or 0) + 1

        existing_lines = (
            await self.db.execute(
                select(PoLine).where(PoLine.po_id == po_id, PoLine.is_deleted == False)
            )
        ).scalars().all()

        existing_line_ids = {l.po_line_id for l in existing_lines}
        incoming_line_ids = {l.po_line_id for l in data.lines if l.po_line_id}

        for line in existing_lines:
            if line.po_line_id not in incoming_line_ids:
                line.is_deleted = True

        for line_item in data.lines:
            if line_item.po_line_id:
                line = next((l for l in existing_lines if l.po_line_id == line_item.po_line_id), None)
                if not line:
                    continue
                for key, val in line_item.model_dump(exclude={"po_line_id", "shipments"}, exclude_unset=True).items():
                    setattr(line, key, val)
                line.object_version_number = (line.object_version_number or 0) + 1
            else:
                line = await self._create_line(po_id, line_item)

            await self._reconcile_shipments(po_id, line.po_line_id, line_item.shipments)

        existing_releases = (
            await self.db.execute(
                select(PoRelease).where(PoRelease.po_id == po_id, PoRelease.is_deleted == False)
            )
        ).scalars().all()

        existing_rel_ids = {r.release_id for r in existing_releases}
        incoming_rel_ids = {r.release_id for r in data.releases if hasattr(r, "release_id") and r.release_id}

        for rel in existing_releases:
            if rel.release_id not in incoming_rel_ids:
                rel.is_deleted = True

        for rel_item in data.releases:
            if hasattr(rel_item, "release_id") and rel_item.release_id:
                rel = next((r for r in existing_releases if r.release_id == rel_item.release_id), None)
                if not rel:
                    continue
                for key, val in rel_item.model_dump(exclude={"release_id", "po_id"}, exclude_unset=True).items():
                    setattr(rel, key, val)
                rel.object_version_number = (rel.object_version_number or 0) + 1
            else:
                rel = PoRelease(po_id=po_id, **rel_item.model_dump(exclude={"release_id", "po_id"}))
                self.db.add(rel)

        existing_amendments = (
            await self.db.execute(
                select(PoAmendment).where(PoAmendment.po_id == po_id, PoAmendment.is_deleted == False)
            )
        ).scalars().all()

        existing_amd_ids = {a.amendment_id for a in existing_amendments}
        incoming_amd_ids = {a.amendment_id for a in data.amendments if hasattr(a, "amendment_id") and a.amendment_id}

        for amd in existing_amendments:
            if amd.amendment_id not in incoming_amd_ids:
                amd.is_deleted = True

        for amd_item in data.amendments:
            if hasattr(amd_item, "amendment_id") and amd_item.amendment_id:
                amd = next((a for a in existing_amendments if a.amendment_id == amd_item.amendment_id), None)
                if not amd:
                    continue
                for key, val in amd_item.model_dump(exclude={"amendment_id", "po_id"}, exclude_unset=True).items():
                    setattr(amd, key, val)
                amd.object_version_number = (amd.object_version_number or 0) + 1
            else:
                amd = PoAmendment(po_id=po_id, **amd_item.model_dump(exclude={"amendment_id", "po_id"}))
                self.db.add(amd)

        await self.db.commit()
        return await self.get_composite(po_id)

    async def _get_header(self, po_id: uuid.UUID):
        row = (await self.db.execute(
            select(PoHeader).where(PoHeader.po_id == po_id, PoHeader.is_deleted == False)
        )).scalar_one_or_none()
        return row

    async def _create_line(self, po_id: uuid.UUID, line_item: CreatePoLineItem):
        line = PoLine(po_id=po_id, **line_item.model_dump(exclude={"shipments"}))
        self.db.add(line)
        await self.db.flush()
        return line

    async def _create_shipment(self, po_id: uuid.UUID, po_line_id: uuid.UUID, ship_item: CreatePoShipmentItem):
        shipment = PoShipment(po_id=po_id, po_line_id=po_line_id, **ship_item.model_dump(exclude={"distributions"}))
        self.db.add(shipment)
        await self.db.flush()
        return shipment

    async def _create_distribution(self, po_id: uuid.UUID, po_line_id: uuid.UUID, po_shipment_id: uuid.UUID, dist_item: CreatePoDistributionItem):
        dist = PoDistribution(po_id=po_id, po_line_id=po_line_id, po_shipment_id=po_shipment_id, **dist_item.model_dump())
        self.db.add(dist)
        await self.db.flush()
        return dist

    async def _reconcile_shipments(self, po_id: uuid.UUID, po_line_id: uuid.UUID, ship_items: list[UpdatePoShipmentItem]):
        existing_ships = (
            await self.db.execute(
                select(PoShipment).where(PoShipment.po_line_id == po_line_id, PoShipment.is_deleted == False)
            )
        ).scalars().all()

        existing_ship_ids = {s.po_shipment_id for s in existing_ships}
        incoming_ship_ids = {s.po_shipment_id for s in ship_items if s.po_shipment_id}

        for ship in existing_ships:
            if ship.po_shipment_id not in incoming_ship_ids:
                ship.is_deleted = True

        for ship_item in ship_items:
            if ship_item.po_shipment_id:
                ship = next((s for s in existing_ships if s.po_shipment_id == ship_item.po_shipment_id), None)
                if not ship:
                    continue
                for key, val in ship_item.model_dump(exclude={"po_shipment_id", "distributions"}, exclude_unset=True).items():
                    setattr(ship, key, val)
                ship.object_version_number = (ship.object_version_number or 0) + 1
            else:
                ship = PoShipment(po_id=po_id, po_line_id=po_line_id, **ship_item.model_dump(exclude={"po_shipment_id", "distributions"}))
                self.db.add(ship)
                await self.db.flush()

            await self._reconcile_distributions(po_id, po_line_id, ship.po_shipment_id, ship_item.distributions)

    async def _reconcile_distributions(self, po_id: uuid.UUID, po_line_id: uuid.UUID, po_shipment_id: uuid.UUID, dist_items: list[UpdatePoDistributionItem]):
        existing_dists = (
            await self.db.execute(
                select(PoDistribution).where(
                    PoDistribution.po_shipment_id == po_shipment_id, PoDistribution.is_deleted == False
                )
            )
        ).scalars().all()

        existing_dist_ids = {d.distribution_id for d in existing_dists}
        incoming_dist_ids = {d.distribution_id for d in dist_items if d.distribution_id}

        for dist in existing_dists:
            if dist.distribution_id not in incoming_dist_ids:
                dist.is_deleted = True

        for dist_item in dist_items:
            if dist_item.distribution_id:
                dist = next((d for d in existing_dists if d.distribution_id == dist_item.distribution_id), None)
                if not dist:
                    continue
                for key, val in dist_item.model_dump(exclude={"distribution_id"}, exclude_unset=True).items():
                    setattr(dist, key, val)
                dist.object_version_number = (dist.object_version_number or 0) + 1
            else:
                dist = PoDistribution(po_id=po_id, po_line_id=po_line_id, po_shipment_id=po_shipment_id, **dist_item.model_dump(exclude={"distribution_id"}))
                self.db.add(dist)

    def _model_to_dict(self, instance) -> dict:
        """Convert a SQLModel instance to a plain dict with stringified UUIDs."""
        result = {}
        for column in instance.__table__.columns:
            val = getattr(instance, column.name)
            if isinstance(val, uuid.UUID):
                result[column.name] = str(val)
            elif isinstance(val, datetime):
                result[column.name] = val.isoformat()
            else:
                result[column.name] = val
        return result
