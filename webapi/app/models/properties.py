from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from .tasksproperties import Taskproperties

from app import Base 

@dataclass
class Properties(Base):
    __tablename__ = "properties"

    id: int
    name: str

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    taskproperty = relationship("Tasksproperties")