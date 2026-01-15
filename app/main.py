from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(other.km + self.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km = self.__add__(other).km
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError
