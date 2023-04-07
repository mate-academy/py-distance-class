from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, Distance]) -> Distance:
        if type(other) != Distance:
            self.km = self.km + other
            return Distance(self.km)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[int, Distance]) -> Distance:
        if type(other) != Distance:
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, Distance]) -> Distance:
        if type(other) != Distance:
            self.km = round((self.km / other), 2)
            return Distance(self.km)
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Union[int, Distance]) -> bool:
        if type(other) != Distance:
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union[int, Distance]) -> bool:
        if type(other) != Distance:
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union[int, Distance]) -> bool:
        if type(other) != Distance:
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union[int, Distance]) -> bool:
        if type(other) != Distance:
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Union[int, Distance]) -> bool:
        if type(other) != Distance:
            return self.km >= other
        return self.km >= other.km
