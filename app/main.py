from __future__ import annotations
from typing import Union

distTypes = Union[int, float]


class Distance:
    def __init__(self, km: distTypes) -> None:
        self.km = km

    def __str__(self) -> str:
        return "Distance: {} kilometers.".format(self.km)

    def __repr__(self) -> str:
        return "Distance(km={})".format(self.km)

    def __add__(self, other: Distance | distTypes) -> Distance:
        value = other if isinstance(other, distTypes) else other.km
        self.km += value
        return self

    def __iadd__(self, other: Distance | distTypes) -> Distance:
        return self + other

    def __mul__(self, other: distTypes) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: distTypes) -> Distance:
        if other == 0:
            raise Exception("Division by zero")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | distTypes) -> bool:
        value = other if isinstance(other, distTypes) else other.km
        return self.km < value

    def __gt__(self, other: Distance | distTypes) -> bool:
        value = other if isinstance(other, distTypes) else other.km
        return self.km > value

    def __eq__(self, other: Distance | distTypes) -> bool:
        value = other if isinstance(other, distTypes) else other.km
        return self.km == value

    def __le__(self, other: Distance | distTypes) -> bool:
        value = other if isinstance(other, distTypes) else other.km
        return self.km <= value

    def __ge__(self, other: Distance | distTypes) -> bool:
        value = other if isinstance(other, distTypes) else other.km
        return self.km >= value
