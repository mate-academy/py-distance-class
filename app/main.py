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
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km += other if isinstance(other, (int, float)) else other.km
        return self

    def __mul__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(km=round((self.km / other), 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other

        return self.km >= other.km
