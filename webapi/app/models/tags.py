from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Tags(Base):
    __tablename__ = "tags"

    id: int
    name: str
    id_tagtype: int

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    id_tagtype = Column(Integer, ForeignKey('tagtype.id'))