from sqlalchemy import Column, Integer, String, DateTime, func
from datetime import datetime
from database import Base


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, default="female")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)