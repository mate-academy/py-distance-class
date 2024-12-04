from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int]) -> Distance:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        return Distance(
            km=self.km + other
        )

    def __iadd__(self, other: Union[Distance, int]) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int) -> Distance:
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
