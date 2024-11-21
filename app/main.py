from __future__ import annotations
from typing import Union


class Distance:
    # Write your code here
    def __init__(self, km: Union[float, int]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(
            km=(self.km + other)
        )

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, int):
            self.km = self.km + other
        if isinstance(other, float):
            self.km = self.km + other
        if isinstance(other, Distance):
            self.km = self.km + other.km
        return self

    def __mul__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            raise TypeError
        self.km = self.km * other
        return self

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
