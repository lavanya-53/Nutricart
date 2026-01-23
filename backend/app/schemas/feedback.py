from pydantic import BaseModel


class FeedbackCreate(BaseModel):
    user_id: int
    meal_id: int
    status: str
