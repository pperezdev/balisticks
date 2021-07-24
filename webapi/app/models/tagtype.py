from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from .tags import Tags

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Tagtype(Base):
    __tablename__ = "tagtype"

    id: int
    libelle: str

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    tag = relationship("Tags")