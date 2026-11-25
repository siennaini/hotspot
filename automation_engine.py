def clamp(value, minimum=0, maximum=100):
    return max(minimum, min(value, maximum))


def calculate_trust_score(current_score, recommendation_source):
    changes = {
        "friend": 8,
        "verified_review": 5,
        "expert": 6,
        "unknown": -4,
    }

    change = changes.get(recommendation_source, 0)
    return clamp(current_score + change)


def calculate_taste_match(current_score, matches_preferences):
    if matches_preferences:
        return clamp(current_score + 12)

    return clamp(current_score - 10)


def calculate_decision_friction(current_friction, has_clear_choice):
    if has_clear_choice:
        return clamp(current_friction - 15)

    return clamp(current_friction + 10)


def check_restaurant(rating, matches_preferences):
    if rating >= 4.0 and matches_preferences:
        return "Recommended"

    return "Not recommended"


def check_warning(scores):
    warnings = []

    if scores["Trust Score"] < 50:
        warnings.append(
            "WARNING: This recommendation has a low Trust Score."
        )

    if scores["Decision Friction"] > 55:
        warnings.append(
            "WARNING: Too much uncertainty may be making this decision harder."
        )

    return warnings