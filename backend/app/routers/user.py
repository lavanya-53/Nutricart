from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserUpdate, UserResponse

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# -----------------------------
# GET USER PROFILE
# -----------------------------
@router.get("/profile", response_model=UserResponse)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch user profile details.
    """

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# -----------------------------
# UPDATE USER PROFILE
# -----------------------------
@router.put("/profile", response_model=UserResponse)
def update_user_profile(
    payload: UserUpdate,
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Update user health and preference data.
    """

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in payload.dict().items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user
