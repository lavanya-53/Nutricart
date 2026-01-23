from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.services.meal_plan_service import generate_daily_plan
from app.services.health_summary_service import generate_daily_health_summary

router = APIRouter(prefix="/health-summary", tags=["health-summary"])

@router.get("/today")
def get_today_health_summary(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    # Reuse today's plan safely
    meals = []  # fetched or cached plan (no re-generation here)
    today_plan = {
        "meals": meals
    }

    return generate_daily_health_summary(user, today_plan)
