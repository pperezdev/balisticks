from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Userstasks(Base):
    __tablename__ = "userstasks"

    id: int
    id_userstype: str
    id_tasks: datetime
    id_users: int

    id = Column(Integer, primary_key=True)

    id_userstype = Column(Integer, ForeignKey('userstype.id'))
    id_tasks = Column(Integer, ForeignKey('tasks.id'))
    id_users = Column(Integer, ForeignKey('users.id'))