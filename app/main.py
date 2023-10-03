from typing import Any


class Distance:
    def __init__(self, km: Any) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, (int, float)):
            result = self.km + other
        elif isinstance(other, Distance):
            result = self.km + other.km
        return Distance(result)

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other

    def __eq__(self, other: "Distance") -> bool:
        return self.km == other

    def __le__(self, other: "Distance") -> bool:
        return self.km <= other

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other
