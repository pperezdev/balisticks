from sqlalchemy import Column, Text
from dataclasses import dataclass
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class Projects(Base):
    __tablename__ = "Projects"

    