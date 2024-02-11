from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    @staticmethod
    def validation(other: Union[Distance, int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            other = other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        other = self.validation(other)
        return Distance(self.km + other)

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        other = self.validation(other)
        self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        other = self.validation(other)
        return self.km < other

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        other = self.validation(other)
        return not self.__le__(other)

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        other = self.validation(other)
        return self.km == other

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        other = self.validation(other)
        return self.km <= other

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        other = self.validation(other)
        return not self.__lt__(other)

    def __ne__(self, other: Union[Distance, int, float]) -> bool:
        other = self.validation(other)
        return not self.__eq__(other)
