from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from app.core.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    meal_id = Column(Integer, index=True, nullable=False)
    status = Column(String, nullable=False)  # eaten / skipped / partial
    timestamp = Column(DateTime, default=datetime.utcnow)
