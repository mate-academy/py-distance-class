from __future__ import annotations
from functools import total_ordering
from typing import Any


@total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def fetch_distance_metric(other: Any) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        return Distance(self.km + self.fetch_distance_metric(other))

    def __iadd__(self, other: Any) -> Distance:
        self.km += self.fetch_distance_metric(other)
        return self

    def __mul__(self, times: int) -> Distance:
        return Distance(self.km * times)

    def __truediv__(self, divisor: int) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __eq__(self, other: Any) -> bool:
        return self.km == self.fetch_distance_metric(other)

    def __lt__(self, other: Any) -> bool:
        return self.km < self.fetch_distance_metric(other)
