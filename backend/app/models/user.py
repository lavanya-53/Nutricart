print("LOADING USER MODEL FROM:", __file__)

from sqlalchemy import Column, Integer, String, Float, JSON
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    age = Column(Integer)
    gender = Column(String)
    weight = Column(Float)

    # 🔐 Multi-valued health data (SQLite-safe)
    health_conditions = Column(JSON, nullable=True)
    dietary_preferences = Column(JSON, nullable=True)
    allergies = Column(JSON, nullable=True)

    region = Column(String)
