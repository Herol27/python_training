from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TodoList(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)
