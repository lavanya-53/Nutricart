from sqlalchemy import Column, Integer, Boolean, Date, JSON, String
from app.core.database import Base

class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    date = Column(Date, index=True)

    meals = Column(JSON, nullable=False)
    generated_reason = Column(String, nullable=False)
    is_reengineered = Column(Boolean, default=False)
