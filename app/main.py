from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        elif isinstance(other, Distance):
            self.km += other.km
            return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            self.km *= other
            return self

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            self.km /= other
            self.km = round(self.km, 2)
            return self

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
