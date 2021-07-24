from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime

from app import Base 

@dataclass
class Dates(Base):
    __tablename__ = "DATES"

    id: int
    date: datetime
    name: str
    id_DATETYPES: int

    id = Column(Integer, primary_key=True)

    date = Column(
        DateTime(timezone=True),
        index=False,
        unique=False,
        nullable=False
    )

    name = Column(String(50), nullable=False)

    id_DATETYPES = Column(Integer, ForeignKey('DATETYPES.id'))