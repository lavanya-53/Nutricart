from typing import Dict


def optimize_quantities(
    *,
    required_ingredients: Dict[str, float],
    pantry_quantities: Dict[str, float],
) -> Dict[str, float]:
    """
    Calculates final grocery quantities after considering pantry stock.

    Rules:
    - Pantry stock is subtracted
    - Never return negative values
    - Never under-buy (minimum 0)
    """

    optimized: Dict[str, float] = {}

    for ingredient, required_qty in required_ingredients.items():
        pantry_qty = pantry_quantities.get(ingredient, 0)

        final_qty = required_qty - pantry_qty

        if final_qty > 0:
            optimized[ingredient] = round(final_qty, 2)

    return optimized
