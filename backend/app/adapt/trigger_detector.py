from enum import Enum
from typing import List, Optional


class AdaptTrigger(str, Enum):
    MEAL_SKIPPED = "MEAL_SKIPPED"
    FEEDBACK_CHANGED = "FEEDBACK_CHANGED"
    PANTRY_SHORTAGE = "PANTRY_SHORTAGE"
    HEALTH_DATA_UPDATED = "HEALTH_DATA_UPDATED"
    SEASON_CHANGED = "SEASON_CHANGED"


def detect_triggers(
    *,
    current_feedback: Optional[dict] = None,
    previous_feedback: Optional[dict] = None,
    pantry_shortage: bool = False,
    health_data_changed: bool = False,
    season_changed: bool = False,
) -> List[AdaptTrigger]:
    """
    Detects adaptation triggers based on factual input signals.

    This function:
    - Detects facts only
    - Does NOT decide actions
    - Does NOT modify state
    - Does NOT infer nutrition or meals
    """

    triggers: List[AdaptTrigger] = []

    # MEAL_SKIPPED
    if current_feedback:
        if current_feedback.get("status") == "skipped":
            triggers.append(AdaptTrigger.MEAL_SKIPPED)

    # FEEDBACK_CHANGED
    if current_feedback and previous_feedback:
        if current_feedback.get("status") != previous_feedback.get("status"):
            triggers.append(AdaptTrigger.FEEDBACK_CHANGED)

    # PANTRY_SHORTAGE
    if pantry_shortage:
        triggers.append(AdaptTrigger.PANTRY_SHORTAGE)

    # HEALTH_DATA_UPDATED
    if health_data_changed:
        triggers.append(AdaptTrigger.HEALTH_DATA_UPDATED)

    # SEASON_CHANGED
    if season_changed:
        triggers.append(AdaptTrigger.SEASON_CHANGED)

    return triggers
