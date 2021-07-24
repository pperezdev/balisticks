from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Checks(Base):
    __tablename__ = "checks"

    id: int
    libelle: str
    isCheck: bool
    id_checklists: int

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    id_checklists = Column(Integer, ForeignKey('checklists.id'))