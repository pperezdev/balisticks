from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass


from app import Base 

@dataclass
class Taskproperties(Base):
    __tablename__ = "TASKPROPERTIES"

    id: int
    id_PROPERTIES:int
    id_TASKS: int 

    id = Column(Integer, primary_key=True)

    id_PROPERTIES = Column(Integer, ForeignKey('PROPERTIES.id'))
    id_TASKS = Column(Integer, ForeignKey('TASK.id'))