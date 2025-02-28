from __future__ import annotations
from typing import Any


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        if isinstance(other, int) or isinstance(other, float):
            self.km = self.km + other
        return self

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __lt__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km < other

    def __gt__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km > other

    def __eq__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km == other

    def __le__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km <= other

    def __ge__(self, other: Distance) -> Any:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km >= other
