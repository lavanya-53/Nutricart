from sqlalchemy import Column, Integer, String, JSON
from app.core.database import Base


class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # breakfast / lunch / dinner / snack

    nutrition = Column(JSON, nullable=False)
    suitability_conditions = Column(JSON, nullable=False)
    region = Column(String, nullable=False)
    recipe = Column(JSON, nullable=False)

