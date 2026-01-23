from backend.app.core.database import engine, Base

# import ALL models so metadata is fully populated
from backend.app.models.user import User
from backend.app.models.meal import Meal
from backend.app.models.meal_plan import MealPlan
from backend.app.models.feedback import Feedback


def init_db():
    print("Initializing NutriCart SQLite database...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("NutriCart DB initialized successfully")