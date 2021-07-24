from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from .checks import Checks

from app import Base 

@dataclass
class Checklists(Base):
    __tablename__ = "checklists"

    id: int
    name: str

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    check = relationship("Checks")