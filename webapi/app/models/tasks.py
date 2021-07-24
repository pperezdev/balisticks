from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Tasks(Base):
    __tablename__ = "TASK"

    id: int
    libelle: str
    create_data: datetime
    id_WORKSPACES: int
    id_PROJECTS: int

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    create_data = Column(
        DateTime(timezone=True),
        index=False,
        unique=False,
        nullable=False
    )

    id_WORKSPACES = Column(Integer, ForeignKey('WORKSPACES.id'))
    id_PROJECTS = Column(Integer, ForeignKey('PROJECTS.id'))

    usertask = relationship("Userstasks")
    taskproperty = relationship("Taskproperties")