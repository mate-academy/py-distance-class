from __future__ import annotations

from typing import Union

# Псевдоніми типів для чистоти коду та лінтера
Numeric = Union[int, float]
DistanceOrNumber = Union["Distance", Numeric]


class Distance:
    def __init__(self, km: Numeric) -> None:
        self.km: Numeric = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: DistanceOrNumber) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: DistanceOrNumber) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: Numeric) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("'__mul__' method should not accept /n"
                            "Distance instance")
        return Distance(self.km * other)

    def __truediv__(self, other: Numeric) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("'__truediv__' method should not /n"
                            "accept Distance instance")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: DistanceOrNumber) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: DistanceOrNumber) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: DistanceOrNumber) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: DistanceOrNumber) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
