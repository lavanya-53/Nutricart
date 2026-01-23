from enum import Enum
from typing import List, Tuple
from .trigger_detector import AdaptTrigger


class AdaptAction(str, Enum):
    REPLACE_MEAL = "REPLACE_MEAL"
    ADJUST_PORTION = "ADJUST_PORTION"
    SUBSTITUTE_INGREDIENT = "SUBSTITUTE_INGREDIENT"
    REBALANCE_NUTRIENTS = "REBALANCE_NUTRIENTS"
    NO_ACTION = "NO_ACTION"


ActionDecision = Tuple[AdaptAction, str]


def evaluate_rules(
    *,
    triggers: List[AdaptTrigger],
    health_safe: bool,
    pantry_feasible: bool,
    nutrition_balanced: bool,
    preference_conflict: bool,
) -> List[ActionDecision]:
    """
    Applies deterministic adaptation rules based on trigger priority.

    Returns:
    - Ordered list of (AdaptAction, reason)
    - OR a single NO_ACTION if change is unsafe
    """

    decisions: List[ActionDecision] = []

    # 1️⃣ Health safety — highest priority
    if not health_safe:
        return [
            (
                AdaptAction.NO_ACTION,
                "No change made because health safety could not be guaranteed.",
            )
        ]

    # 2️⃣ Pantry feasibility
    if AdaptTrigger.PANTRY_SHORTAGE in triggers:
        if pantry_feasible:
            decisions.append(
                (
                    AdaptAction.SUBSTITUTE_INGREDIENT,
                    "Ingredient unavailable in pantry; safe substitution required.",
                )
            )
        else:
            decisions.append(
                (
                    AdaptAction.REPLACE_MEAL,
                    "Meal infeasible due to pantry shortage; replacement required.",
                )
            )

    # 3️⃣ Nutrition balance
    if AdaptTrigger.MEAL_SKIPPED in triggers or not nutrition_balanced:
        decisions.append(
            (
                AdaptAction.REBALANCE_NUTRIENTS,
                "Nutrition imbalance detected after skipped or partial meal.",
            )
        )

    # 4️⃣ Preferences (can be blocked)
    if preference_conflict:
        return [
            (
                AdaptAction.NO_ACTION,
                "No change made because preference conflict outweighs benefit.",
            )
        ]

    # 5️⃣ Seasonality (lowest priority)
    if AdaptTrigger.SEASON_CHANGED in triggers:
        decisions.append(
            (
                AdaptAction.ADJUST_PORTION,
                "Season change detected; portion adjustment suggested.",
            )
        )

    if not decisions:
        return [
            (
                AdaptAction.NO_ACTION,
                "No adaptation required based on current conditions.",
            )
        ]

    return decisions
