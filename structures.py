from dataclasses import dataclass


@dataclass
class Restaurant:
    name: str
    cuisine: str
    rating: float
    recommendation_source: str
    matches_preferences: bool