from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @classmethod
    def checker(cls, other: Union[int, float]) -> bool:
        return isinstance(other, cls)

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        if not Distance.checker(other):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        if not Distance.checker(other):
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        if not Distance.checker(other):
            return self.km > other
        else:
            return self.km > other.km

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        if not Distance.checker(other):
            return self.km >= other
        else:
            return self.km >= other.km

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        if not Distance.checker(other):
            return self.km == other
        else:
            return self.km == other.km

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        if not Distance.checker(other):
            return self.km < other
        else:
            return self.km < other.km

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        if not Distance.checker(other):
            return self.km <= other
        else:
            return self.km <= other.km
