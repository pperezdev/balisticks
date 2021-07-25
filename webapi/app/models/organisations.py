from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from sqlalchemy.sql.functions import func

from .projects import Projects
from .organisationsusers import Organisationsusers

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Organisations(Base):
    __tablename__ = "organisations"

    id: int
    name: str
    picture: str
    banner: str
    creationdate: datetime

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    picture = Column(String(10), nullable=True)
    banner = Column(String(10), nullable=True)

    creationdate = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        index=False,
        unique=False,
        nullable=False
    )

    project = relationship("Projects")
    organisationuser = relationship("Organisationsusers")  