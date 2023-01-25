from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            return Distance(other.km + self.km)
        return Distance(other + self.km)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km = other.km + self.km
        else:
            self.km = other + self.km
        return self

    def __mul__(self, number: float) -> Distance:
        self.km = self.km * number
        return self

    def __truediv__(self, number: float) -> Distance:
        self.km = round(self.km / number, 2)
        return self

    def __lt__(self, distance: Any) -> bool:
        if isinstance(distance, Distance):
            return self.km < distance.km
        return self.km < distance

    def __gt__(self, distance: Any) -> bool:
        if isinstance(distance, Distance):
            return self.km > distance.km
        return self.km > distance

    def __eq__(self, distance: Any) -> bool:
        if isinstance(distance, Distance):
            return self.km == distance.km
        return self.km == distance

    def __le__(self, distance: Any) -> bool:
        if isinstance(distance, Distance):
            return self.km <= distance.km
        return self.km <= distance

    def __ge__(self, distance: Any) -> bool:
        if isinstance(distance, Distance):
            return self.km >= distance.km
        return self.km >= distance

    def __round__(self, end: int) -> float:
        return round(self.km, end)
