from __future__ import annotations
from typing import Any


class Distance:

    def __init__(self, km: Any) -> None:
        self.km = km
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        self.messege = f"Distance(km={self.km})"
        return self.messege

    def __add__(self, other: Any) -> int:
        result = 0
        if isinstance(other, Distance):
            result = self.km + other.km
            return Distance(result)
        if isinstance(other, (int, float)):
            result = self.km + other.real
            return Distance(result)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        if isinstance(other, (int, float)):
            self.km = self.km + other.real
            return self

    def __mul__(self: Any, other: Any) -> Distance:
        if isinstance(other, (int, float)):
            result = self.km * other
            return Distance(result)

    def __truediv__(self: Any, other: Any) -> Distance:
        if isinstance(other, (int, float)):
            result = self.km / other
            result = round(result, 2)
            return Distance(result)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other.real

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other.real

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other.real

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other.real

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other.real
