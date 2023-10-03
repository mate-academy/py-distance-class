from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other : Any) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
        if isinstance(other, (int, float)):
            if self.km < other:
                return True
        return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
        if isinstance(other, (int, float)):
            if self.km > other:
                return True
        return False

    def __eq__(self, other : Any) -> bool:
        if isinstance(other, Distance) and self.km == other:
            return True
        if isinstance(other, (int, float)) and self.km == other:
            return True
        return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
            return False
        elif isinstance(other, (int, float)):
            if self.km <= other:
                return True
            return False

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
            return False
        elif isinstance(other, (int, float)):
            if self.km >= other:
                return True
            return False
