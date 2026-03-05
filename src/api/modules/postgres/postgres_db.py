import datetime
import enum
import logging
from uuid import UUID, uuid4

import sqlalchemy.orm
from sqlalchemy import create_engine, schema, String, DateTime, Enum, Sequence
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Status(enum.Enum) :
    CREATED = 'CREATED',
    DELETED = 'DELETED'


class Bamba(Base):
    __tablename__ = "bamba"

    id: Mapped[UUID] = mapped_column(default=uuid4(), primary_key=True)
    db_name: Mapped[str] = mapped_column(String(50))
    status: Mapped[Enum] = mapped_column(Enum(Status))
    username: Mapped[str] = mapped_column(String(50))
    creation_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    #important_identifier: Mapped[str] = mapped_column(active_history=True)

