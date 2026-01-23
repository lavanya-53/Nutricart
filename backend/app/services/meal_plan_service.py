from datetime import date

DEFAULT_PORTION = 1.0


# ------------------------------------------------------
# Portion Control Logic
# ------------------------------------------------------
def portion_multiplier(user):
    """
    Adjust portion size based on user weight.
    Health safety > optimization.
    """
    if user.weight:
        if user.weight > 80:
            return 0.9
        if user.weight < 50:
            return 1.1
    return DEFAULT_PORTION


# ------------------------------------------------------
# Meal Selection Logic (Health + Allergy Safe)
# ------------------------------------------------------
def select_meal(meals, user):
    """
    Select the safest suitable meal for a user with explainability.
    """

    for meal in meals:

        # ----------------------------
        # Allergy Safety (Ingredient-based)
        # ----------------------------
        if user.allergies:
            ingredients = meal.recipe.get("ingredients", [])
            ingredient_names = [i["item"].lower() for i in ingredients]

            if any(allergy.lower() in ingredient_names for allergy in user.allergies):
                continue

        # ----------------------------
        # Health Condition Safety
        # ----------------------------
        if user.health_conditions:
            if not any(
                condition in meal.suitability_conditions
                for condition in user.health_conditions
            ):
                continue

        # ----------------------------
        # Meal Accepted
        # ----------------------------
        explanation = {
            "what_changed": "meal selected",
            "why_changed": "matches health profile and allergy safety",
            "health_impact": "supports balanced nutrition and condition safety"
        }

        return meal, explanation

    # ----------------------------
    # No Safe Meal Found
    # ----------------------------
    return None, {
        "what_changed": "no meal selected",
        "why_changed": "no suitable meals matched safety constraints",
        "health_impact": "fallback meal required"
    }


# ------------------------------------------------------
# Daily Meal Plan Generation
# ------------------------------------------------------
def generate_daily_plan(user, meals_by_type):
    """
    Generate a daily meal plan with portion control and explainability.
    """

    plan_meals = []
    portion = portion_multiplier(user)

    for meal_type, meals in meals_by_type.items():
        meal, explanation = select_meal(meals, user)

        # ----------------------------
        # Safe Fallback
        # ----------------------------
        if not meal:
            plan_meals.append({
                "meal_id": None,
                "meal_object": None,  # Explicitly None for safety
                "name": "Balanced Vegetable Khichdi",
                "type": meal_type,
                "portion_multiplier": 1.0,
                "explainability": {
                    "what_changed": "fallback meal used",
                    "why_changed": "no safe meals available",
                    "health_impact": "neutral, balanced nutrition"
                }
            })
            continue

        # ----------------------------
        # Normal Selection
        # ----------------------------
        plan_meals.append({
            "meal_id": meal.id,
            "meal_object": meal,  # INTERNAL ONLY (for grocery derivation)
            "name": meal.name,
            "type": meal_type,
            "portion_multiplier": portion,
            "explainability": {
                **explanation,
                "portion_reason": (
                    "reduced due to higher body weight"
                    if portion < 1.0 else
                    "increased due to lower body weight"
                    if portion > 1.0 else
                    "standard portion"
                )
            }
        })

    return {
        "user_id": user.id,
        "date": date.today(),
        "meals": plan_meals,
        "generated_reason": "initial plan",
        "is_reengineered": False
    }


# ------------------------------------------------------
# Plan Re-engineering Logic (Feedback-driven)
# ------------------------------------------------------
def reengineer_plan(existing_plan, feedback, user):
    """
    Re-engineer meal plan based on user feedback.
    """

    updated_meals = []

    for meal in existing_plan["meals"]:
        if meal["meal_id"] == feedback.meal_id and feedback.status == "skipped":
            meal["explainability"] = {
                "what_changed": "meal skipped",
                "why_changed": "user skipped meal",
                "health_impact": "nutrients will be compensated in next meals"
            }
            existing_plan["is_reengineered"] = True
            existing_plan["generated_reason"] = "meal skipped"

        updated_meals.append(meal)

    existing_plan["meals"] = updated_meals
    return existing_plan
