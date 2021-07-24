from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Texts(Base):
    __tablename__ = "texts"

    id: int
    content: str

    id = Column(Integer, primary_key=True)
    content = Column(String(50), nullable=False)
