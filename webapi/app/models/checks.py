from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Checks(Base):
    __tablename__ = "CHECKS"

    id: int
    libelle: str
    isCheck: bool
    id_CHECKSLISTS: int

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    id_CHECKSLISTS = Column(Integer, ForeignKey('CHECKSLISTS.id'))