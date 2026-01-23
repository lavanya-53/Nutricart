from datetime import date


def generate_daily_health_summary(user, today_plan):
    """
    Generates daily nutrition and health insight summary.
    Contract-safe, rule-based, explainable.
    """

    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "iron": 0,
        "fiber": 0
    }

    for meal_entry in today_plan.get("meals", []):

        meal = meal_entry.get("meal_object")
        if not meal:
            continue  # Skip fallback meals safely

        portion = meal_entry.get("portion_multiplier", 1.0)
        nutrition = meal.nutrition or {}

        totals["calories"] += nutrition.get("calories", 0) * portion
        totals["protein"] += nutrition.get("macros", {}).get("protein", 0) * portion
        totals["carbs"] += nutrition.get("macros", {}).get("carbs", 0) * portion
        totals["fat"] += nutrition.get("macros", {}).get("fat", 0) * portion
        totals["iron"] += nutrition.get("key_micros", {}).get("iron", 0) * portion
        totals["fiber"] += nutrition.get("key_micros", {}).get("fiber", 0) * portion

    risk_flags = {}
    insight = "Meals are nutritionally balanced today."

    # ----------------------------
    # Anemia Safety
    # ----------------------------
    if "anemia" in user.health_conditions and totals["iron"] < 18:
        risk_flags["iron"] = "Low iron intake today"
        insight = (
            "Iron intake was below recommended levels. "
            "Iron-rich meals were emphasized."
        )

    # ----------------------------
    # Diabetes Safety
    # ----------------------------
    if "diabetes" in user.health_conditions and totals["carbs"] > 250:
        risk_flags["carbs"] = "High carbohydrate intake"
        insight = (
            "Carbohydrate intake was moderated to prevent glucose spikes."
        )

    return {
        "date": str(date.today()),
        "nutrition_totals": totals,
        "key_insights": insight,
        "health_risk_flags": risk_flags
    }
