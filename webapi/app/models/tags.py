from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Tags(Base):
    __tablename__ = "TAGS"

    id: int
    name: str
    id_TAGTYPE: int
    id_PROPERTIES: int

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    id_TAGTYPE = Column(Integer, ForeignKey('TAGTYPE.id'))