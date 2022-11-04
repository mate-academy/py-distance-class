from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> Union.Distance[int, float]:
        self.km = km

    def __str__(self) -> Union.Distance[int, float]:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> Union.Distance[int, float]:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float]) -> Union.Distance[int, float]:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Union[int, float]) -> Union.Distance[int, float]:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> Union.Distance[int, float]:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) \
            -> Union.Distance[int, float]:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other

    def __len__(self) -> Union[int, float]:
        return self.km
