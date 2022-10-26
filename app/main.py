from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: Any(int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any(Distance, float, int)) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: Any(Distance, float, int)) -> Distance:
        if not isinstance(other, Distance):
            self.km = self.km + other
        else:
            self.km = self.km + other.km

        return self

    def __mul__(self, other: Any(float, int)) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Any(Distance, float, int)) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Any(Distance, float, int)) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        else:
            return self.km < other

    def __gt__(self, other: Any(Distance, float, int)) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        else:
            return self.km > other

    def __eq__(self, other: Any(Distance, float, int)) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        else:
            return self.km == other

    def __le__(self, other: Any(Distance, float, int)) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        else:
            return self.km <= other

    def __ge__(self, other: Any(Distance, float, int)) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        else:
            return self.km >= other

    def __len__(self) -> Any(float, int):
        return self.km
