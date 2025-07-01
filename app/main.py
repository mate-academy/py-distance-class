from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def type_checking(other: Union[int, float, Distance]) -> int | float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        return Distance(self.km + self.type_checking(other))

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        self.km += self.type_checking(other)
        return self

    def __mul__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        return self.km == self.type_checking(other)

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        return self.km > self.type_checking(other)

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        return self.km < self.type_checking(other)

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        return self.__lt__(other) or self.__eq__(other)
