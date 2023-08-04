from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return "Distance: {} kilometers.".format(self.km)

    def __repr__(self) -> str:
        return "Distance(km={})".format(self.km)

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        return self + other

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if other == 0:
            raise Exception("Division by zero")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
