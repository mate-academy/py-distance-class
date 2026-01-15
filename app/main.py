from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_dist: int | float | Distance) -> "Distance":
        if isinstance(other_dist, (int | float)):
            return Distance(self.km + other_dist)
        return Distance(self.km + other_dist.km)

    def __iadd__(self, other_dist: int | float | Distance) -> "Distance":
        if isinstance(other_dist, (int | float)):
            self.km = self.km + other_dist
            return self
        self.km = self.km + other_dist.km
        return self

    def __mul__(self, other_dist: "int | float ") -> "Distance":
        return Distance(self.km * other_dist)

    def __truediv__(self, other_dist: "int | float") -> "Distance":
        return Distance(round(self.km / other_dist, 2))

    def __lt__(self, other_dist: int | float | Distance) -> bool:
        if isinstance(other_dist, (int | float)):
            return self.km < other_dist
        return self.km < other_dist.km

    def __gt__(self, other_dist: int | float | Distance) -> bool:
        if isinstance(other_dist, (int | float)):
            return self.km > other_dist
        return self.km > other_dist.km

    def __eq__(self, other_dist: int | float | Distance) -> bool:
        if isinstance(other_dist, (int | float)):
            return self.km == other_dist
        return self.km == other_dist.km

    def __le__(self, other_dist: int | float | Distance) -> bool:
        if isinstance(other_dist, (int | float)):
            return self.km <= other_dist
        return self.km <= other_dist.km

    def __ge__(self, other_dist: int | float | Distance) -> bool:
        if isinstance(other_dist, (int | float)):
            return self.km >= other_dist
        return self.km >= other_dist.km
