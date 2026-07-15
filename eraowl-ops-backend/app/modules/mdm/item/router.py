import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.shared.pagination import PaginatedResponse
from app.modules.mdm.item.services import ItemService
from app.modules.mdm.item.schemas import (
    UomOut,
    UomCreate,
    UomUpdate,
    UomConversionOut,
    UomConversionCreate,
    UomConversionUpdate,
    ItemCategoryOut,
    ItemCategoryCreate,
    ItemCategoryUpdate,
    ItemOut,
    ItemCreate,
    ItemUpdate,
    ItemCategoryAssignmentOut,
    ItemCategoryAssignmentCreate,
    ItemCategoryAssignmentUpdate,
    ItemOrganizationOut,
    ItemOrganizationCreate,
    ItemOrganizationUpdate,
    ItemSupplierXrefOut,
    ItemSupplierXrefCreate,
    ItemSupplierXrefUpdate,
)

router = APIRouter()


# --- UOMs ---
@router.get("/uoms", response_model=PaginatedResponse[UomOut])
async def list_uoms(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_uoms(page, page_size)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/uoms/{entity_id}", response_model=UomOut)
async def get_uom(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_uom(entity_id)


@router.post("/uoms", response_model=UomOut, status_code=201)
async def create_uom(data: UomCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_uom(data)


@router.put("/uoms/{entity_id}", response_model=UomOut)
async def update_uom(entity_id: uuid.UUID, data: UomUpdate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.update_uom(entity_id, data)


@router.delete("/uoms/{entity_id}", status_code=204)
async def delete_uom(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_uom(entity_id)


# --- UOM Conversions ---
@router.get("/uom-conversions", response_model=PaginatedResponse[UomConversionOut])
async def list_uom_conversions(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    from_uom_id: uuid.UUID | None = Query(None),
    to_uom_id: uuid.UUID | None = Query(None),
    item_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_uom_conversions(page, page_size, from_uom_id, to_uom_id, item_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/uom-conversions/{entity_id}", response_model=UomConversionOut)
async def get_uom_conversion(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_uom_conversion(entity_id)


@router.post("/uom-conversions", response_model=UomConversionOut, status_code=201)
async def create_uom_conversion(data: UomConversionCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_uom_conversion(data)


@router.put("/uom-conversions/{entity_id}", response_model=UomConversionOut)
async def update_uom_conversion(entity_id: uuid.UUID, data: UomConversionUpdate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.update_uom_conversion(entity_id, data)


@router.delete("/uom-conversions/{entity_id}", status_code=204)
async def delete_uom_conversion(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_uom_conversion(entity_id)


# --- Item Categories ---
@router.get("/item-categories", response_model=PaginatedResponse[ItemCategoryOut])
async def list_item_categories(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    category_set: str | None = Query(None),
    parent_category_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_item_categories(page, page_size, category_set, parent_category_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/item-categories/{entity_id}", response_model=ItemCategoryOut)
async def get_item_category(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_item_category(entity_id)


@router.post("/item-categories", response_model=ItemCategoryOut, status_code=201)
async def create_item_category(data: ItemCategoryCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_item_category(data)


@router.put("/item-categories/{entity_id}", response_model=ItemCategoryOut)
async def update_item_category(entity_id: uuid.UUID, data: ItemCategoryUpdate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.update_item_category(entity_id, data)


@router.delete("/item-categories/{entity_id}", status_code=204)
async def delete_item_category(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_item_category(entity_id)


# --- Items ---
@router.get("/items", response_model=PaginatedResponse[ItemOut])
async def list_items(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    item_type: str | None = Query(None),
    status: str | None = Query(None),
    primary_uom_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_items(page, page_size, item_type, status, primary_uom_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/items/{entity_id}", response_model=ItemOut)
async def get_item(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_item(entity_id)


@router.post("/items", response_model=ItemOut, status_code=201)
async def create_item(data: ItemCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_item(data)


@router.put("/items/{entity_id}", response_model=ItemOut)
async def update_item(entity_id: uuid.UUID, data: ItemUpdate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.update_item(entity_id, data)


@router.delete("/items/{entity_id}", status_code=204)
async def delete_item(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_item(entity_id)


# --- Item Category Assignments ---
@router.get("/item-category-assignments", response_model=PaginatedResponse[ItemCategoryAssignmentOut])
async def list_item_category_assignments(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    item_id: uuid.UUID | None = Query(None),
    category_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_item_category_assignments(page, page_size, item_id, category_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/item-category-assignments/{entity_id}", response_model=ItemCategoryAssignmentOut)
async def get_item_category_assignment(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_item_category_assignment(entity_id)


@router.post("/item-category-assignments", response_model=ItemCategoryAssignmentOut, status_code=201)
async def create_item_category_assignment(data: ItemCategoryAssignmentCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_item_category_assignment(data)


@router.put("/item-category-assignments/{entity_id}", response_model=ItemCategoryAssignmentOut)
async def update_item_category_assignment(
    entity_id: uuid.UUID, data: ItemCategoryAssignmentUpdate, db: AsyncSession = Depends(get_db)
):
    svc = ItemService(db)
    return await svc.update_item_category_assignment(entity_id, data)


@router.delete("/item-category-assignments/{entity_id}", status_code=204)
async def delete_item_category_assignment(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_item_category_assignment(entity_id)


# --- Item Organizations ---
@router.get("/item-organizations", response_model=PaginatedResponse[ItemOrganizationOut])
async def list_item_organizations(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    item_id: uuid.UUID | None = Query(None),
    warehouse_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_item_organizations(page, page_size, item_id, warehouse_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/item-organizations/{entity_id}", response_model=ItemOrganizationOut)
async def get_item_organization(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_item_organization(entity_id)


@router.post("/item-organizations", response_model=ItemOrganizationOut, status_code=201)
async def create_item_organization(data: ItemOrganizationCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_item_organization(data)


@router.put("/item-organizations/{entity_id}", response_model=ItemOrganizationOut)
async def update_item_organization(
    entity_id: uuid.UUID, data: ItemOrganizationUpdate, db: AsyncSession = Depends(get_db)
):
    svc = ItemService(db)
    return await svc.update_item_organization(entity_id, data)


@router.delete("/item-organizations/{entity_id}", status_code=204)
async def delete_item_organization(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_item_organization(entity_id)


# --- Item Supplier Xrefs ---
@router.get("/item-supplier-xrefs", response_model=PaginatedResponse[ItemSupplierXrefOut])
async def list_item_supplier_xrefs(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    item_id: uuid.UUID | None = Query(None),
    supplier_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = ItemService(db)
    items, total = await svc.list_item_supplier_xrefs(page, page_size, item_id, supplier_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/item-supplier-xrefs/{entity_id}", response_model=ItemSupplierXrefOut)
async def get_item_supplier_xref(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.get_item_supplier_xref(entity_id)


@router.post("/item-supplier-xrefs", response_model=ItemSupplierXrefOut, status_code=201)
async def create_item_supplier_xref(data: ItemSupplierXrefCreate, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    return await svc.create_item_supplier_xref(data)


@router.put("/item-supplier-xrefs/{entity_id}", response_model=ItemSupplierXrefOut)
async def update_item_supplier_xref(
    entity_id: uuid.UUID, data: ItemSupplierXrefUpdate, db: AsyncSession = Depends(get_db)
):
    svc = ItemService(db)
    return await svc.update_item_supplier_xref(entity_id, data)


@router.delete("/item-supplier-xrefs/{entity_id}", status_code=204)
async def delete_item_supplier_xref(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = ItemService(db)
    await svc.delete_item_supplier_xref(entity_id)
