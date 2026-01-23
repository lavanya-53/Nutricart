from datetime import date
from typing import Dict, List, Tuple


def _is_expired(expiry: date | None) -> bool:
    if expiry is None:
        return False
    return expiry < date.today()


def check_pantry_feasibility(
    *,
    required_ingredients: Dict[str, Tuple[float, str]],
    pantry_items: Dict[str, Dict],
) -> Dict:
    """
    Checks whether required ingredients are available in pantry.

    required_ingredients:
        { ingredient_name: (required_quantity, unit) }

    pantry_items:
        {
          ingredient_name: {
            "quantity": float,
            "unit": str,
            "expiry": date | None
          }
        }
    """

    missing_items: List[str] = []
    partial_shortage = False

    # Missing pantry data → minimal safe pantry assumed
    if not pantry_items:
        return {
            "is_pantry_feasible": True,
            "has_partial_shortage": False,
            "missing_items": [],
            "used_safe_default": True,
        }

    for ingredient, (req_qty, _) in required_ingredients.items():
        pantry_entry = pantry_items.get(ingredient)

        if not pantry_entry:
            missing_items.append(ingredient)
            continue

        if _is_expired(pantry_entry.get("expiry")):
            missing_items.append(ingredient)
            continue

        available_qty = pantry_entry.get("quantity", 0)

        if available_qty <= 0:
            missing_items.append(ingredient)
        elif available_qty < req_qty:
            partial_shortage = True

    return {
        "is_pantry_feasible": len(missing_items) == 0,
        "has_partial_shortage": partial_shortage,
        "missing_items": missing_items,
        "used_safe_default": False,
    }

