from fastapi import FastAPI

# -------------------------------
# DATABASE
# -------------------------------
from app.core.database import Base, engine



# -------------------------------
# MODELS (important for create_all)
# -------------------------------
from app.models import user, meal, meal_plan, feedback

# -------------------------------
# ROUTERS
# -------------------------------
from app.routers import auth, user as user_router
from app.routers import meals, meal_plan as meal_plan_router
from app.routers import feedback as feedback_router
from app.routers import health_summary

# -------------------------------
# CREATE TABLES
# -------------------------------
Base.metadata.create_all(bind=engine)

# -------------------------------
# APP INIT
# -------------------------------
app = FastAPI(title="NutriCart API")

# -------------------------------
# ROUTER REGISTRATION
# -------------------------------
app.include_router(auth.router)
app.include_router(user_router.router)
app.include_router(meals.router)
app.include_router(meal_plan_router.router)
app.include_router(feedback_router.router)
app.include_router(health_summary.router)
