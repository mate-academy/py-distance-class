from __future__ import annotations
from typing import Union


Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km:g} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km:g})"

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += float(other)
        return self

    def __mul__(self, other: Number) -> Distance:
        return Distance(self.km * float(other))

    def __truediv__(self, other: Number) -> Distance:
        return Distance(round(self.km / float(other), 2))

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < float(other)

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > float(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return False

    def __le__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= float(other)

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= float(other)
