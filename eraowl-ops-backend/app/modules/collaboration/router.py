import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.collaboration.services import CollabService
from app.modules.collaboration.schemas import (
    TodoCreate, TodoUpdate, TodoOut,
    ActivityCreate, ActivityUpdate, ActivityOut,
    CalendarEventCreate, CalendarEventUpdate, CalendarEventOut,
    ChannelCreate, ChannelOut,
    ChannelMessageCreate, ChannelMessageOut,
    DmConversationCreate, DmConversationOut,
    DmMessageCreate, DmMessageOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


async def get_svc(db: AsyncSession = Depends(get_db)) -> CollabService:
    return CollabService(db)


# ── Todos ──
@router.get("/todos", response_model=PaginatedResponse[TodoOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_todos(page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), svc: CollabService = Depends(get_svc)):
    items, total = await svc.list_todos(page, page_size)
    tp = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=tp)


@router.post("/todos", response_model=TodoOut, status_code=201,
             dependencies=[check_privilege("collaboration", "manage_todos")])
async def create_todo(data: TodoCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_todo(data)


@router.put("/todos/{entity_id}", response_model=TodoOut,
            dependencies=[check_privilege("collaboration", "manage_todos")])
async def update_todo(entity_id: uuid.UUID, data: TodoUpdate, svc: CollabService = Depends(get_svc)):
    return await svc.update_todo(entity_id, data)


@router.delete("/todos/{entity_id}", status_code=204,
               dependencies=[check_privilege("collaboration", "manage_todos")])
async def delete_todo(entity_id: uuid.UUID, svc: CollabService = Depends(get_svc)):
    await svc.delete_todo(entity_id)


# ── Activities ──
@router.get("/activities", response_model=PaginatedResponse[ActivityOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_activities(page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), svc: CollabService = Depends(get_svc)):
    items, total = await svc.list_activities(page, page_size)
    tp = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=tp)


@router.post("/activities", response_model=ActivityOut, status_code=201,
             dependencies=[check_privilege("collaboration", "manage_activities")])
async def create_activity(data: ActivityCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_activity(data)


@router.put("/activities/{entity_id}", response_model=ActivityOut,
            dependencies=[check_privilege("collaboration", "manage_activities")])
async def update_activity(entity_id: uuid.UUID, data: ActivityUpdate, svc: CollabService = Depends(get_svc)):
    return await svc.update_activity(entity_id, data)


@router.delete("/activities/{entity_id}", status_code=204,
               dependencies=[check_privilege("collaboration", "manage_activities")])
async def delete_activity(entity_id: uuid.UUID, svc: CollabService = Depends(get_svc)):
    await svc.delete_activity(entity_id)


# ── Calendar Events ──
@router.get("/calendar-events", response_model=PaginatedResponse[CalendarEventOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_events(page: int = Query(1, ge=1), page_size: int = Query(50, ge=1, le=200), svc: CollabService = Depends(get_svc)):
    items, total = await svc.list_events(page, page_size)
    tp = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=tp)


@router.post("/calendar-events", response_model=CalendarEventOut, status_code=201,
             dependencies=[check_privilege("collaboration", "manage_events")])
async def create_event(data: CalendarEventCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_event(data)


@router.put("/calendar-events/{entity_id}", response_model=CalendarEventOut,
            dependencies=[check_privilege("collaboration", "manage_events")])
async def update_event(entity_id: uuid.UUID, data: CalendarEventUpdate, svc: CollabService = Depends(get_svc)):
    return await svc.update_event(entity_id, data)


@router.delete("/calendar-events/{entity_id}", status_code=204,
               dependencies=[check_privilege("collaboration", "manage_events")])
async def delete_event(entity_id: uuid.UUID, svc: CollabService = Depends(get_svc)):
    await svc.delete_event(entity_id)


# ── Channels ──
@router.get("/channels", response_model=list[ChannelOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_channels(svc: CollabService = Depends(get_svc)):
    return await svc.list_channels()


@router.post("/channels", response_model=ChannelOut, status_code=201,
             dependencies=[check_privilege("collaboration", "manage_channels")])
async def create_channel(data: ChannelCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_channel(data)


# ── Channel Messages ──
@router.get("/channels/{channel_id}/messages", response_model=PaginatedResponse[ChannelMessageOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_channel_messages(channel_id: uuid.UUID, page: int = Query(1, ge=1), page_size: int = Query(50, ge=1, le=200), svc: CollabService = Depends(get_svc)):
    items, total = await svc.list_channel_messages(channel_id, page, page_size)
    tp = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=tp)


@router.post("/channels/{channel_id}/messages", response_model=ChannelMessageOut, status_code=201,
             dependencies=[check_privilege("collaboration", "send_messages")])
async def create_channel_message(channel_id: uuid.UUID, data: ChannelMessageCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_channel_message(channel_id, data)


@router.delete("/channel-messages/{entity_id}", status_code=204,
               dependencies=[check_privilege("collaboration", "manage_channels")])
async def delete_channel_message(entity_id: uuid.UUID, svc: CollabService = Depends(get_svc)):
    await svc.delete_channel_message(entity_id)


# ── DM Conversations ──
@router.get("/dm-conversations", response_model=list[DmConversationOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_dm_conversations(svc: CollabService = Depends(get_svc)):
    return []


@router.post("/dm-conversations", response_model=DmConversationOut, status_code=201,
             dependencies=[check_privilege("collaboration", "send_messages")])
async def create_dm_conversation(data: DmConversationCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_dm_conversation(data)


# ── DM Messages ──
@router.get("/dm-conversations/{conversation_id}/messages", response_model=PaginatedResponse[DmMessageOut],
            dependencies=[check_privilege("collaboration", "view")])
async def list_dm_messages(conversation_id: uuid.UUID, page: int = Query(1, ge=1), page_size: int = Query(50, ge=1, le=200), svc: CollabService = Depends(get_svc)):
    items, total = await svc.list_dm_messages(conversation_id, page, page_size)
    tp = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=tp)


@router.post("/dm-conversations/{conversation_id}/messages", response_model=DmMessageOut, status_code=201,
             dependencies=[check_privilege("collaboration", "send_messages")])
async def create_dm_message(conversation_id: uuid.UUID, data: DmMessageCreate, svc: CollabService = Depends(get_svc)):
    return await svc.create_dm_message(conversation_id, data)


@router.delete("/dm-messages/{entity_id}", status_code=204,
               dependencies=[check_privilege("collaboration", "send_messages")])
async def delete_dm_message(entity_id: uuid.UUID, svc: CollabService = Depends(get_svc)):
    await svc.delete_dm_message(entity_id)