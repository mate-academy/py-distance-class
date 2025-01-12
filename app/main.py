from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: "Distance") -> "Distance":
        other_km = other if isinstance(other, (int, float)) else other.km
        return Distance(
            km=self.km + other_km
        )

    def __iadd__(self, other: Any) -> "Distance":
        other_km = other if isinstance(other, (int, float)) else other.km
        self.km = self.km + other_km
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        return Distance(km=round(self.km / other, ndigits=2))

    def __lt__(self, other: Any) -> bool:
        other_km = other if isinstance(other, (int, float)) else other.km
        return self.km < other_km

    def __gt__(self, other: Any) -> bool:
        other_km = other if isinstance(other, (int, float)) else other.km
        return self.km > other_km

    def __eq__(self, other: Any) -> bool:
        other_km = other if isinstance(other, (int, float)) else other.km
        return self.km == other_km

    def __le__(self, other: Any) -> bool:
        other_km = other if isinstance(other, (int, float)) else other.km
        return self.km <= other_km

    def __ge__(self, other: Any) -> bool:
        other_km = other if isinstance(other, (int, float)) else other.km
        return self.km >= other_km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
