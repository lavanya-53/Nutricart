def is_meal_suitable(meal, user_conditions):
    """
    Rule-based health suitability check.
    Returns (bool, explanation_list)
    """

    explanations = []

    # ----------------------------
    # Diabetes safety
    # ----------------------------
    if "diabetes" in user_conditions:
        carbs = meal.nutrition.get("macros", {}).get("carbs", 0)
        if carbs > 60:
            return False, [
                "High carbohydrate load not suitable for diabetes"
            ]
        explanations.append("Carbohydrate level within safe range for diabetes")

    # ----------------------------
    # Anemia safety
    # ----------------------------
    if "anemia" in user_conditions:
        iron = meal.nutrition.get("key_micros", {}).get("iron", 0)
        if iron < 5:
            return False, [
                "Iron content insufficient for anemia"
            ]
        explanations.append("Iron content supports anemia requirements")

    # ----------------------------
    # Default safe
    # ----------------------------
    if not explanations:
        explanations.append("No conflicting health conditions detected")

    return True, explanations
