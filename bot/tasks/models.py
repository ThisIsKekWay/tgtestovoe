from sqlalchemy import Column, Integer, String

from database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task_name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
