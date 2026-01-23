from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.meal_plan import MealPlan
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate

router = APIRouter(
    prefix="/feedback",
    tags=["feedback"]
)


@router.post("/")
def submit_feedback(payload: FeedbackCreate, db: Session = Depends(get_db)):
    """
    Store user feedback for a meal.
    Triggers meal plan re-engineering.
    """

    feedback = Feedback(
        user_id=payload.user_id,
        meal_id=payload.meal_id,
        status=payload.status
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    # Mark latest meal plan as re-engineered
    plan = (
        db.query(MealPlan)
        .filter(MealPlan.user_id == payload.user_id)
        .order_by(MealPlan.date.desc())
        .first()
    )

    if plan:
        plan.is_reengineered = True
        plan.generated_reason = "user feedback received"
        db.commit()

    return {"message": "Feedback recorded"}
