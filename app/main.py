from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: Number = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            total_distance = self.km + other.km
        elif isinstance(other, (int, float)):
            total_distance = self.km + other
        else:
            return NotImplemented
        return Distance(total_distance)

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Number) -> Distance:
        if isinstance(other, (int, float)):
            total_distance = self.km * other
        else:
            return NotImplemented
        return Distance(total_distance)

    def __rmul__(self, other: Number) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: Number) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            total_distance = self.km / other
        else:
            return NotImplemented
        return Distance(round(total_distance, 2))

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __le__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented
