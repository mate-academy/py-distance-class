from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Any) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: Any) -> Distance:
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: Any) -> bool:
        return self.km < other

    def __gt__(self, other: Any) -> bool:
        return self.km > other

    def __eq__(self, other: Any) -> bool:
        return self.km == other

    def __le__(self, other: Any) -> bool:
        return self.km <= other

    def __ge__(self, other: Any) -> bool:
        return self.km >= other
