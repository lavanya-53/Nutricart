from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.meal import Meal

router = APIRouter(
    prefix="/meals",
    tags=["meals"]
)

@router.get("/")
def list_meals(db: Session = Depends(get_db)):
    """
    List all meals available in the system.
    Used for meal planning and debugging.
    """
    return db.query(Meal).all()
