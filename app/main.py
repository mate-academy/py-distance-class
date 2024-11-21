from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:

    @staticmethod
    def get_km(other: int | float | Distance) -> float:
        return getattr(other, "km", other)

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(km=self.km + self.get_km(other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += self.get_km(other)
        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.get_km(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self.get_km(other)
