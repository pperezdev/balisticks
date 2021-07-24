from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass


from app import Base 

@dataclass
class Taskproperties(Base):
    __tablename__ = "tasksproperties"

    id: int
    id_properties:int
    id_tasks: int 

    id = Column(Integer, primary_key=True)

    id_properties = Column(Integer, ForeignKey('properties.id'))
    id_tasks = Column(Integer, ForeignKey('tasks.id'))