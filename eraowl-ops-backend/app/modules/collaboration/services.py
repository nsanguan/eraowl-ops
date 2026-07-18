import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.modules.collaboration.models import (
    Todo, Activity, CalendarEvent, Channel, ChannelMessage,
    DmConversation, DmMessage,
)


class CollabService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def _paginate(self, model, page: int, page_size: int, filters: dict | None = None, order_by=None):
        q = select(model)
        if filters:
            for col, val in filters.items():
                if val is not None:
                    q = q.where(getattr(model, col) == val)
        count_q = select(func.count()).select_from(q.subquery())
        total = (await self.db.execute(count_q)).scalar() or 0
        if order_by is not None:
            q = q.order_by(order_by)
        else:
            q = q.order_by(model.created_at.desc())
        rows = (await self.db.execute(q.offset((page - 1) * page_size).limit(page_size))).scalars().all()
        return list(rows), total

    async def _get(self, model, entity_id: uuid.UUID):
        from app.core.exceptions import NotFoundError
        pk = list(model.__table__.primary_key.columns)[0].name
        row = (await self.db.execute(select(model).where(getattr(model, pk) == entity_id, model.is_deleted == False))).scalar_one_or_none()
        if not row:
            raise NotFoundError(entity=model.__name__)
        return row

    async def _create(self, model, data):
        inst = model(**data.model_dump())
        self.db.add(inst)
        await self.db.commit()
        await self.db.refresh(inst)
        return inst

    async def _update(self, model, entity_id: uuid.UUID, data):
        inst = await self._get(model, entity_id)
        for k, v in data.model_dump(exclude_unset=True).items():
            setattr(inst, k, v)
        await self.db.commit()
        await self.db.refresh(inst)
        return inst

    async def _delete(self, model, entity_id: uuid.UUID):
        inst = await self._get(model, entity_id)
        inst.is_deleted = True
        await self.db.commit()

    # Todos
    async def list_todos(self, page=1, page_size=20, user_id=None):
        f = {"user_id": user_id} if user_id else None
        return await self._paginate(Todo, page, page_size, f, Todo.created_at.desc())

    async def create_todo(self, data): return await self._create(Todo, data)
    async def update_todo(self, eid, data): return await self._update(Todo, eid, data)
    async def delete_todo(self, eid): await self._delete(Todo, eid)

    # Activities
    async def list_activities(self, page=1, page_size=20, user_id=None):
        f = {"user_id": user_id} if user_id else None
        return await self._paginate(Activity, page, page_size, f, Activity.created_at.desc())

    async def create_activity(self, data): return await self._create(Activity, data)
    async def update_activity(self, eid, data): return await self._update(Activity, eid, data)
    async def delete_activity(self, eid): await self._delete(Activity, eid)

    # Calendar Events
    async def list_events(self, page=1, page_size=50, user_id=None):
        f = {"user_id": user_id} if user_id else None
        return await self._paginate(CalendarEvent, page, page_size, f, CalendarEvent.event_date)

    async def create_event(self, data): return await self._create(CalendarEvent, data)
    async def update_event(self, eid, data): return await self._update(CalendarEvent, eid, data)
    async def delete_event(self, eid): await self._delete(CalendarEvent, eid)

    # Channels
    async def list_channels(self):
        rows = (await self.db.execute(select(Channel).where(Channel.is_deleted == False).order_by(Channel.name))).scalars().all()
        return list(rows)

    async def create_channel(self, data): return await self._create(Channel, data)

    # Channel Messages
    async def list_channel_messages(self, channel_id: uuid.UUID, page=1, page_size=50):
        return await self._paginate(ChannelMessage, page, page_size, {"channel_id": channel_id}, ChannelMessage.created_at)

    async def create_channel_message(self, channel_id: uuid.UUID, data):
        inst = ChannelMessage(channel_id=channel_id, **data.model_dump())
        self.db.add(inst)
        await self.db.commit()
        await self.db.refresh(inst)
        return inst

    async def delete_channel_message(self, eid: uuid.UUID): await self._delete(ChannelMessage, eid)

    # DM Conversations
    async def list_dm_conversations(self, user_id: uuid.UUID):
        rows = (await self.db.execute(
            select(DmConversation).where(
                DmConversation.is_deleted == False,
                ((DmConversation.participant_one == user_id) | (DmConversation.participant_two == user_id))
            ).order_by(DmConversation.created_at.desc())
        )).scalars().all()
        return list(rows)

    async def create_dm_conversation(self, data):
        existing = (await self.db.execute(
            select(DmConversation).where(
                ((DmConversation.participant_one == data.participant_one) & (DmConversation.participant_two == data.participant_two)) |
                ((DmConversation.participant_one == data.participant_two) & (DmConversation.participant_two == data.participant_one))
            )
        )).scalar_one_or_none()
        if existing:
            return existing
        return await self._create(DmConversation, data)

    # DM Messages
    async def list_dm_messages(self, conversation_id: uuid.UUID, page=1, page_size=50):
        return await self._paginate(DmMessage, page, page_size, {"conversation_id": conversation_id}, DmMessage.created_at)

    async def create_dm_message(self, conversation_id: uuid.UUID, data):
        inst = DmMessage(conversation_id=conversation_id, **data.model_dump())
        self.db.add(inst)
        await self.db.commit()
        await self.db.refresh(inst)
        return inst

    async def delete_dm_message(self, eid: uuid.UUID): await self._delete(DmMessage, eid)
