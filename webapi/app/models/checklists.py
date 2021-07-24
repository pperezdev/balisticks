from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship

from app import Base 

@dataclass
class Checklists(Base):
    __tablename__ = "CHECKLISTS"

    id: int
    name: str
    id_PROPERTIES: int

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    check = relationship("Checks")