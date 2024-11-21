from __future__ import annotations, division
from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, Distance]) -> Distance:
        if isinstance(other, Distance):
            other = other.km
        return Distance(km=self.km + other)

    def __iadd__(self, other: Union[int, Distance]) -> Distance:
        if isinstance(other, Distance):
            other = other.km
        self.km = self.km + other
        return self

    def __mul__(self, other: Union[int, Distance]) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km < other

    def __gt__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km > other

    def __eq__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km == other

    def __le__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km <= other

    def __ge__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km >= other
