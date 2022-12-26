from __future__ import annotations
from __future__ import division


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, int):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __mul__(self, other: int) -> Distance:
        return Distance(km=self.km * other)

    def __round__(self, n=2):
        return round(self.km, n)

    def __truediv__(self, other: int) -> float:
        return round(Distance(km=self.km / other))
