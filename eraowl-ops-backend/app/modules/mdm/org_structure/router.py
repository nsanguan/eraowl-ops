import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.shared.pagination import PaginatedResponse
from app.modules.mdm.org_structure.services import OrgStructureService
from app.modules.mdm.org_structure.schemas import (
    OrgCorporateOut, OrgCorporateCreate, OrgCorporateUpdate,
    OrgCompanyOut, OrgCompanyCreate, OrgCompanyUpdate,
    OrgBusinessUnitOut, OrgBusinessUnitCreate, OrgBusinessUnitUpdate,
    OrgSiteOut, OrgSiteCreate, OrgSiteUpdate,
    OrgWarehouseOut, OrgWarehouseCreate, OrgWarehouseUpdate,
    OrgWarehouseLocatorOut, OrgWarehouseLocatorCreate, OrgWarehouseLocatorUpdate,
)

router = APIRouter()


# --- Corporates ---
@router.get("/corporates", response_model=PaginatedResponse[OrgCorporateOut])
async def list_corporates(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    svc = OrgStructureService(db)
    items, total = await svc.list_corporates(page, page_size)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/corporates/{entity_id}", response_model=OrgCorporateOut)
async def get_corporate(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.get_corporate(entity_id)


@router.post("/corporates", response_model=OrgCorporateOut, status_code=201)
async def create_corporate(data: OrgCorporateCreate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.create_corporate(data)


@router.put("/corporates/{entity_id}", response_model=OrgCorporateOut)
async def update_corporate(entity_id: uuid.UUID, data: OrgCorporateUpdate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.update_corporate(entity_id, data)


@router.delete("/corporates/{entity_id}", status_code=204)
async def delete_corporate(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    await svc.delete_corporate(entity_id)


# --- Companies ---
@router.get("/companies", response_model=PaginatedResponse[OrgCompanyOut])
async def list_companies(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    svc = OrgStructureService(db)
    items, total = await svc.list_companies(page, page_size)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/companies/{entity_id}", response_model=OrgCompanyOut)
async def get_company(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.get_company(entity_id)


@router.post("/companies", response_model=OrgCompanyOut, status_code=201)
async def create_company(data: OrgCompanyCreate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.create_company(data)


@router.put("/companies/{entity_id}", response_model=OrgCompanyOut)
async def update_company(entity_id: uuid.UUID, data: OrgCompanyUpdate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.update_company(entity_id, data)


@router.delete("/companies/{entity_id}", status_code=204)
async def delete_company(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    await svc.delete_company(entity_id)


# --- Business Units ---
@router.get("/business-units", response_model=PaginatedResponse[OrgBusinessUnitOut])
async def list_business_units(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    company_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = OrgStructureService(db)
    items, total = await svc.list_business_units(page, page_size, company_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/business-units/{entity_id}", response_model=OrgBusinessUnitOut)
async def get_business_unit(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.get_business_unit(entity_id)


@router.post("/business-units", response_model=OrgBusinessUnitOut, status_code=201)
async def create_business_unit(data: OrgBusinessUnitCreate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.create_business_unit(data)


@router.put("/business-units/{entity_id}", response_model=OrgBusinessUnitOut)
async def update_business_unit(entity_id: uuid.UUID, data: OrgBusinessUnitUpdate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.update_business_unit(entity_id, data)


@router.delete("/business-units/{entity_id}", status_code=204)
async def delete_business_unit(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    await svc.delete_business_unit(entity_id)


# --- Sites ---
@router.get("/sites", response_model=PaginatedResponse[OrgSiteOut])
async def list_sites(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    business_unit_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = OrgStructureService(db)
    items, total = await svc.list_sites(page, page_size, business_unit_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/sites/{entity_id}", response_model=OrgSiteOut)
async def get_site(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.get_site(entity_id)


@router.post("/sites", response_model=OrgSiteOut, status_code=201)
async def create_site(data: OrgSiteCreate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.create_site(data)


@router.put("/sites/{entity_id}", response_model=OrgSiteOut)
async def update_site(entity_id: uuid.UUID, data: OrgSiteUpdate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.update_site(entity_id, data)


@router.delete("/sites/{entity_id}", status_code=204)
async def delete_site(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    await svc.delete_site(entity_id)


# --- Warehouses ---
@router.get("/warehouses", response_model=PaginatedResponse[OrgWarehouseOut])
async def list_warehouses(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    site_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = OrgStructureService(db)
    items, total = await svc.list_warehouses(page, page_size, site_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/warehouses/{entity_id}", response_model=OrgWarehouseOut)
async def get_warehouse(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.get_warehouse(entity_id)


@router.post("/warehouses", response_model=OrgWarehouseOut, status_code=201)
async def create_warehouse(data: OrgWarehouseCreate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.create_warehouse(data)


@router.put("/warehouses/{entity_id}", response_model=OrgWarehouseOut)
async def update_warehouse(entity_id: uuid.UUID, data: OrgWarehouseUpdate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.update_warehouse(entity_id, data)


@router.delete("/warehouses/{entity_id}", status_code=204)
async def delete_warehouse(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    await svc.delete_warehouse(entity_id)


# --- Warehouse Locators ---
@router.get("/locators", response_model=PaginatedResponse[OrgWarehouseLocatorOut])
async def list_locators(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    warehouse_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = OrgStructureService(db)
    items, total = await svc.list_locators(page, page_size, warehouse_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/locators/{entity_id}", response_model=OrgWarehouseLocatorOut)
async def get_locator(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.get_locator(entity_id)


@router.post("/locators", response_model=OrgWarehouseLocatorOut, status_code=201)
async def create_locator(data: OrgWarehouseLocatorCreate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.create_locator(data)


@router.put("/locators/{entity_id}", response_model=OrgWarehouseLocatorOut)
async def update_locator(entity_id: uuid.UUID, data: OrgWarehouseLocatorUpdate, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    return await svc.update_locator(entity_id, data)


@router.delete("/locators/{entity_id}", status_code=204)
async def delete_locator(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = OrgStructureService(db)
    await svc.delete_locator(entity_id)
