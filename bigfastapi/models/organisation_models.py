import datetime as _dt
from sqlite3 import Timestamp
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime, Boolean, ARRAY, Text
from sqlalchemy import ForeignKey
from uuid import UUID, uuid4
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
import bigfastapi.db.database as _database


class Organization(_database.Base):
    __tablename__ = "businesses"
    id = Column(String(255), primary_key=True, index=True, default=uuid4().hex)
    creator = Column(String(255), ForeignKey("users.id", ondelete="CASCADE"))
    mission = Column(String(255), index=True)
    vision = Column(String(255), index=True)
    values = Column(String(255), index=True)
    currency = Column(String(5), index=True)
    name = Column(String(255), unique=True, index=True, default="")
    country = Column(String(255), index=True)
    state = Column(String(255), index=True)
    address = Column(String(), index=True)
    tagline = Column(String(255), index=True)
    image = Column(String(), default="")
    is_deleted = Column(Boolean(), default=False)
    current_subscription = Column(String(225), default="")
    credit_balance = Column(Integer, default=5000) 
    currency_preference = Column(String, default="")
    date_created = Column(DateTime, default=_dt.datetime.utcnow)
    last_updated = Column(DateTime, default=_dt.datetime.utcnow)

