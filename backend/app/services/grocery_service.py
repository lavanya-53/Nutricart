def derive_grocery_list(meal_plan, user):
    """
    Derives an explainable grocery list from a meal plan.
    Contract-safe, health-aware, rule-based.
    """

    grocery_map = {}

    for meal_entry in meal_plan.get("meals", []):

        # ----------------------------
        # Skip fallback meals
        # ----------------------------
        if not meal_entry.get("meal_id"):
            continue

        meal = meal_entry.get("meal_object")
        if not meal:
            continue  # Absolute safety

        portion_multiplier = meal_entry.get("portion_multiplier", 1.0)

        # ----------------------------
        # Extract recipe ingredients
        # ----------------------------
        recipe = meal.recipe or {}
        ingredients = recipe.get("ingredients", [])

        for item in ingredients:

            item_name = item.get("item")
            if not item_name:
                continue

            name_key = item_name.lower()

            # ----------------------------
            # Allergy safety
            # ----------------------------
            if user.allergies:
                if name_key in [a.lower() for a in user.allergies]:
                    continue

            quantity = item.get("quantity", 0) * portion_multiplier
            unit = item.get("unit", "")

            if quantity <= 0:
                continue

            # ----------------------------
            # Aggregate grocery items
            # ----------------------------
            if name_key not in grocery_map:
                grocery_map[name_key] = {
                    "name": item_name,
                    "quantity": 0,
                    "unit": unit,
                    "source_reason": []
                }

            grocery_map[name_key]["quantity"] += quantity
            grocery_map[name_key]["source_reason"].append({
                "meal": meal.name,
                "why": "ingredient required for planned meal"
            })

    return list(grocery_map.values())
