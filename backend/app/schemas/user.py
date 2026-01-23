from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    age: Optional[int]
    gender: Optional[str]
    weight: Optional[float]
    health_conditions: Optional[List[str]]
    dietary_preferences: Optional[List[str]]
    allergies: Optional[List[str]]
    region: Optional[str]


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    email: str

    class Config:
        from_attributes = True
