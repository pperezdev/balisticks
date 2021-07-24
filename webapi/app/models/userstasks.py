from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Userstasks(Base):
    __tablename__ = "USERSTASKS"

    id: int
    id_USERSTYPE: str
    id_TASKS: datetime
    id_USERS: int

    id = Column(Integer, primary_key=True)

    id_USERSTYPE = Column(Integer, ForeignKey('USERSTYPE.id'))
    id_TASKS = Column(Integer, ForeignKey('TASK.id'))
    id_USERS = Column(Integer, ForeignKey('USERS.id'))