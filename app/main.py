from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        raise TypeError

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        raise TypeError

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        raise TypeError

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        raise TypeError

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        raise TypeError

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        raise TypeError
