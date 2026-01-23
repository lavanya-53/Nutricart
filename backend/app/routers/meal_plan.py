from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.models.meal import Meal
from app.services.meal_plan_service import generate_daily_plan

router = APIRouter(
    prefix="/meal-plan",
    tags=["meal-plan"]
)


@router.get("/today")
def get_today_meal_plan(user_id: int, db: Session = Depends(get_db)):
    """
    Generate today's meal plan for a user.
    """

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    meals = db.query(Meal).filter(Meal.region == user.region).all()

    meals_by_type = {
        "breakfast": [m for m in meals if m.type == "breakfast"],
        "lunch": [m for m in meals if m.type == "lunch"],
        "dinner": [m for m in meals if m.type == "dinner"],
        "snack": [m for m in meals if m.type == "snack"],
    }

    return generate_daily_plan(user, meals_by_type)
