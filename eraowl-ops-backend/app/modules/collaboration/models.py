import uuid
from datetime import date, datetime
from typing import Optional
from sqlalchemy import Boolean, Column, Date, DateTime, String, Text, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    __tablename__ = "todos"
    __table_args__ = {"schema": "collab"}
    todo_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    title: str = Field(sa_column=Column(String(255), nullable=False))
    priority: str = Field(default="medium", sa_column=Column(String(10), default="medium"))
    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    is_complete: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    user_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class Activity(SQLModel, table=True):
    __tablename__ = "activities"
    __table_args__ = {"schema": "collab"}
    activity_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    activity_type: str = Field(sa_column=Column(String(30), nullable=False))
    subject: str = Field(sa_column=Column(String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    status: str = Field(default="open", sa_column=Column(String(20), default="open"))
    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    res_model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))
    res_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    user_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class CalendarEvent(SQLModel, table=True):
    __tablename__ = "calendar_events"
    __table_args__ = {"schema": "collab"}
    event_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    title: str = Field(sa_column=Column(String(255), nullable=False))
    event_type: str = Field(default="meeting", sa_column=Column(String(20), default="meeting"))
    event_date: date = Field(sa_column=Column(Date, nullable=False))
    all_day: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    user_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class Channel(SQLModel, table=True):
    __tablename__ = "channels"
    __table_args__ = {"schema": "collab"}
    channel_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    name: str = Field(sa_column=Column(String(100), unique=True, nullable=False))
    topic: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    is_private: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class ChannelMessage(SQLModel, table=True):
    __tablename__ = "channel_messages"
    __table_args__ = {"schema": "collab"}
    message_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    channel_id: uuid.UUID = Field(foreign_key="collab.channels.channel_id", nullable=False)
    author_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    author_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))
    content: str = Field(sa_column=Column(Text, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class DmConversation(SQLModel, table=True):
    __tablename__ = "dm_conversations"
    __table_args__ = {"schema": "collab"}
    conversation_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    participant_one: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    participant_two: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class DmMessage(SQLModel, table=True):
    __tablename__ = "dm_messages"
    __table_args__ = {"schema": "collab"}
    message_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    conversation_id: uuid.UUID = Field(foreign_key="collab.dm_conversations.conversation_id", nullable=False)
    sender_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(UUID(as_uuid=True), nullable=True))
    sender_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))
    content: str = Field(sa_column=Column(Text, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
