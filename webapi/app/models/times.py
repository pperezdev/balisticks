from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Times(Base):
    __tablename__ = "times"

    id: int
    libelle: str

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)