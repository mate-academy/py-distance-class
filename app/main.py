from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_km(distance))

    def __iadd__(self, distance: Distance | int | float) -> Distance:
        self.km += self.get_km(distance)
        return self

    def __mul__(self, km: int | float) -> Distance:
        return Distance(self.km * km)

    def __truediv__(self, km: int | float) -> Distance:
        return Distance(round(self.km / km, 2))

    def __lt__(self, distance: Distance | int | float) -> bool:
        return self.km < self.get_km(distance)

    def __eq__(self, distance: Distance | int | float) -> bool:
        return self.km == self.get_km(distance)

    @staticmethod
    def get_km(distance: Distance | int | float) -> float:
        return distance.km if isinstance(distance, Distance) else distance
