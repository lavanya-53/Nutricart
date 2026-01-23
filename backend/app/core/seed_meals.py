from app.core.database import SessionLocal
from app.models.meal import Meal

db = SessionLocal()

# -------------------------
# Nutrition Templates
# -------------------------
NUTRITION = {
    "light_breakfast": {
        "calories": 300,
        "macros": {"protein": 12, "carbs": 45, "fat": 6},
        "key_micros": {"iron": 4, "fiber": 7}
    },
    "balanced_lunch": {
        "calories": 450,
        "macros": {"protein": 18, "carbs": 60, "fat": 10},
        "key_micros": {"iron": 6, "fiber": 9}
    },
    "light_dinner": {
        "calories": 350,
        "macros": {"protein": 14, "carbs": 40, "fat": 8},
        "key_micros": {"iron": 5, "fiber": 8}
    }
}

BASE_RECIPE = {
    "ingredients": [],
    "cooking_steps": ["Cook with minimal oil and salt"],
    "oil_used_tsp": 1,
    "serving_size": "1 serving"
}

# -------------------------
# 100 Meal Definitions
# -------------------------
MEALS = []

def add_meal(name, meal_type, region, nutrition_key, conditions):
    MEALS.append(
        Meal(
            name=name,
            type=meal_type,
            region=region,
            nutrition=NUTRITION[nutrition_key],
            suitability_conditions=conditions,
            recipe=dict(BASE_RECIPE)
        )
    )

# ---- South Indian (50) ----
south_breakfasts = [
    "Idli Sambar", "Ragi Idli", "Plain Dosa", "Masala Dosa",
    "Vegetable Upma", "Pongal", "Rava Dosa", "Vegetable Uttapam",
    "Curd Rice", "Lemon Rice", "Millet Idli", "Pesarattu",
    "Aval Upma", "Ragi Porridge", "Appam",
    "Set Dosa", "Kanchipuram Idli", "Oats Dosa", "Thinai Pongal", "Vegetable Soup"
]

south_lunches = [
    "Sambar Rice", "Rasam Rice", "Curd Rice with Veg",
    "Vegetable Khichdi", "Tomato Rice", "Coconut Rice",
    "Bisi Bele Bath", "Avial", "Vegetable Kootu",
    "Vegetable Poriyal Rice", "Drumstick Sambar Rice",
    "Millet Vegetable Rice", "Vegetable Pulav",
    "Beans Thoran", "Cabbage Poriyal",
    "Carrot Beans Curry", "Vegetable Stew",
    "Plain Rice + Curry", "Lemon Rasam Rice", "Mixed Veg Rice"
]

south_dinners = [
    "Chapati Veg Kurma", "Idiyappam Stew", "Ragi Roti",
    "Vegetable Upma Dinner", "Millet Khichdi",
    "Dosa Chutney", "Vegetable Soup Dinner",
    "Oats Upma", "Light Veg Curry Rice", "Thin Dosa"
]

for m in south_breakfasts:
    add_meal(m, "breakfast", "South Indian", "light_breakfast", ["diabetes"])

for m in south_lunches:
    add_meal(m, "lunch", "South Indian", "balanced_lunch", ["anemia"])

for m in south_dinners:
    add_meal(m, "dinner", "South Indian", "light_dinner", ["diabetes"])

# ---- North Indian (50) ----
north_breakfasts = [
    "Vegetable Poha", "Besan Chilla", "Moong Dal Chilla",
    "Sprouts Chaat", "Dalia Porridge", "Vegetable Sandwich",
    "Paneer Bhurji Toast", "Oats Porridge",
    "Vegetable Upma North", "Methi Paratha",
    "Plain Paratha Curd", "Paneer Poha",
    "Vegetable Omelette", "Millet Toast", "Fruit Chaat"
]

north_lunches = [
    "Dal Rice", "Rajma Rice", "Chole Rice", "Vegetable Khichdi",
    "Palak Dal Rice", "Kadhi Rice", "Lauki Chana Dal",
    "Bhindi Masala", "Aloo Gobi", "Mix Veg Sabzi Roti",
    "Methi Dal", "Vegetable Pulao",
    "Paneer Bhurji Roti", "Plain Dal Roti",
    "Jeera Rice Dal", "Spinach Rice",
    "Bottle Gourd Curry", "Cabbage Peas Sabzi",
    "Carrot Beans Sabzi", "Vegetable Stew North",
    "Tinda Masala", "Plain Dal Rice",
    "Vegetable Kofta Steamed", "Lemon Dal Rice", "Curd Rice North"
]

north_dinners = [
    "Roti Veg Curry", "Plain Khichdi",
    "Vegetable Soup Toast", "Paneer Tikka",
    "Dal Soup", "Light Veg Pulao",
    "Curd Roti", "Vegetable Sandwich Dinner",
    "Millet Roti Sabzi", "Veg Omelette Dinner"
]

for m in north_breakfasts:
    add_meal(m, "breakfast", "North Indian", "light_breakfast", ["diabetes"])

for m in north_lunches:
    add_meal(m, "lunch", "North Indian", "balanced_lunch", ["anemia"])

for m in north_dinners:
    add_meal(m, "dinner", "North Indian", "light_dinner", ["diabetes"])

# -------------------------
# Insert into DB
# -------------------------
db.add_all(MEALS)
db.commit()
db.close()

print("✅ 100 Indian meals seeded successfully")
