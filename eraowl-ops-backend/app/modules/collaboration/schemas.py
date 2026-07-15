from typing import Optional
import uuid
from datetime import date, datetime
from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    priority: str = "medium"
    due_date: Optional[date] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[date] = None
    is_complete: Optional[bool] = None


class TodoOut(BaseModel):
    todo_id: uuid.UUID
    title: str
    priority: str
    due_date: Optional[date] = None
    is_complete: bool
    created_at: datetime
    model_config = {"from_attributes": True}


class ActivityCreate(BaseModel):
    activity_type: str
    subject: str
    description: Optional[str] = None
    due_date: Optional[date] = None


class ActivityUpdate(BaseModel):
    status: Optional[str] = None
    subject: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None


class ActivityOut(BaseModel):
    activity_id: uuid.UUID
    activity_type: str
    subject: str
    description: Optional[str] = None
    status: str
    due_date: Optional[date] = None
    created_at: datetime
    model_config = {"from_attributes": True}


class CalendarEventCreate(BaseModel):
    title: str
    event_type: str = "meeting"
    event_date: date
    all_day: bool = False


class CalendarEventUpdate(BaseModel):
    title: Optional[str] = None
    event_type: Optional[str] = None
    event_date: Optional[date] = None
    all_day: Optional[bool] = None


class CalendarEventOut(BaseModel):
    event_id: uuid.UUID
    title: str
    event_type: str
    event_date: date
    all_day: bool
    created_at: datetime
    model_config = {"from_attributes": True}


class ChannelCreate(BaseModel):
    name: str
    topic: Optional[str] = None
    is_private: bool = False


class ChannelOut(BaseModel):
    channel_id: uuid.UUID
    name: str
    topic: Optional[str] = None
    is_private: bool
    created_at: datetime
    model_config = {"from_attributes": True}


class ChannelMessageCreate(BaseModel):
    content: str
    author_name: Optional[str] = None


class ChannelMessageOut(BaseModel):
    message_id: uuid.UUID
    channel_id: uuid.UUID
    author_name: Optional[str] = None
    content: str
    created_at: datetime
    model_config = {"from_attributes": True}


class DmConversationCreate(BaseModel):
    participant_one: uuid.UUID
    participant_two: uuid.UUID


class DmConversationOut(BaseModel):
    conversation_id: uuid.UUID
    participant_one: Optional[uuid.UUID] = None
    participant_two: Optional[uuid.UUID] = None
    created_at: datetime
    model_config = {"from_attributes": True}


class DmMessageCreate(BaseModel):
    content: str
    sender_name: Optional[str] = None


class DmMessageOut(BaseModel):
    message_id: uuid.UUID
    conversation_id: uuid.UUID
    sender_name: Optional[str] = None
    content: str
    created_at: datetime
    model_config = {"from_attributes": True}
