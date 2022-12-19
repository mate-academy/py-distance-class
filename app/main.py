from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if type(other) in (int, float):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        if type(other) in (int, float):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, divisor: Union[Distance, int, float]) -> Distance:
        return Distance(round((self.km / divisor), 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if type(other) is Distance:
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if type(other) is Distance:
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if type(other) is Distance:
            return self.km == other.km
        return self.km == other

    def __le__(self, other: [Distance, int, float]) -> bool:
        if type(other) is Distance:
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if type(other) is Distance:
            return self.km >= other.km
        return self.km >= other
