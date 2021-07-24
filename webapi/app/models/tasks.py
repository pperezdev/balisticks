from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from sqlalchemy.sql.functions import func

from .userstasks import Userstasks
from .tasksproperties import Taskproperties
from sqlalchemy.sql.sqltypes import DateTime
from .userstasks import Userstasks
from .tasksproperties import Taskproperties

from app import Base 

@dataclass
class Tasks(Base):
    __tablename__ = "tasks"

    id: int
    libelle: str
    create_data: datetime
    id_workspaces: int
    id_projects: int

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    create_data = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        index=False,
        unique=False,
        nullable=False
    )

    id_workspaces = Column(Integer, ForeignKey('workspaces.id'))
    id_projects = Column(Integer, ForeignKey('projects.id'))

    usertask = relationship("Userstasks")
    taskproperty = relationship("Taskproperties")