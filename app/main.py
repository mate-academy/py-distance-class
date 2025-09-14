from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
        self,
        other: Union[Distance, float, int]
    ) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        return Distance(self.km + other)

    def __radd__(
        self,
        other: Union[Distance, float, int]
    ) -> Distance:
        return self.__add__(other)

    def __iadd__(
        self,
        new_km: Union[Distance, float, int]
    ) -> Distance:
        if isinstance(new_km, Distance):
            self.km += new_km.km
            return self

        self.km += new_km
        return self

    def __mul__(self, mul: Union[float, int]) -> Distance:
        return Distance(self.km * mul)

    def __truediv__(self, div: Union[float, int]) -> Distance:
        return Distance(round(self.km / div, 2))

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km

        return self.km < other

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km

        return self.km > other

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        return self.km == other

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km

        return self.km <= other

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km

        return self.km >= other
