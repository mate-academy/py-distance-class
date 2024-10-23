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
        if isinstance((other), Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, float) or isinstance(other, int):
            return Distance(self.km + other)
        else:
            return self

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        elif (isinstance(other, float) or isinstance(other, int)):
            self.km = self.km + other
        return self

    def __mul__(self, num: float) -> Distance:
        return Distance(self.km * num)

    def __truediv__(self, num: float) -> Distance:
        if num != 0:
            return Distance(round(self.km / num, 2))
        else:
            return self

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, float) or isinstance(other, int):
            return self.km < other
        else:
            return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, float) or isinstance(other, int):
            return self.km <= other
        else:
            return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, float) or isinstance(other, int):
            return self.km > other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, float) or isinstance(other, int):
            return self.km >= other
        else:
            return False

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, float) or isinstance(other, int):
            return self.km == other
        else:
            return False
