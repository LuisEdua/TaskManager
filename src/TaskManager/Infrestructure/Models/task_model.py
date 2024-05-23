from src.DataBase.connection import Base
from sqlalchemy import Column, String, Boolean

class TaskModel(Base):
    __tablename__ = 'tasks'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    uploaded = Column(Boolean, default=False)
