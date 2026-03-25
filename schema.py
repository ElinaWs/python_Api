from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int
    name: str
    gender: str = 'female'
    created_at: datetime | None = None
    friends: list[int] = []

class Config:
        from_attributes = True