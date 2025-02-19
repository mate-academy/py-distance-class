from __future__ import annotations


class Distance:

    def __init__(self, km: int = 0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, num: int) -> "Distance":
        self.km = self.km * num
        return self

    def __truediv__(self, num: int) -> "Distance":
        self.km = round(self.km / num, 2)
        return self

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
