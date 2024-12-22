from typing import Any


class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        if isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other: (int, float)) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: (int, float)) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
