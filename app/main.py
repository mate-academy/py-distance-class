from __future__ import annotations
from typing import Any
from functools import total_ordering


@total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def check_distance(other: Any) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        return Distance(self.km + self.check_distance(other))

    def __iadd__(self, other: Any) -> Distance:
        self.km += self.check_distance(other)
        return self

    def __mul__(self, times: int) -> Distance:
        return Distance(self.km * times)

    def __truediv__(self, divisor: int) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: Any) -> bool:
        other_km = self.check_distance(other)
        return self.km < other_km

    def __gt__(self, other: Any) -> bool:
        other_km = self.check_distance(other)
        return self.km > other_km

    def __eq__(self, other: Any) -> bool:
        other_km = self.check_distance(other)
        return self.km == other_km

    def __le__(self, other: Any) -> bool:
        other_km = self.check_distance(other)
        return self.km <= other_km

    def __ge__(self, other: Any) -> bool:
        other_km = self.check_distance(other)
        return self.km >= other_km
