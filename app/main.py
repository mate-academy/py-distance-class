from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float, int]) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        if not isinstance(other, Distance):
            self.km = self.km + other
        else:
            self.km = self.km + other.km

        return self

    def __mul__(self, other: Union[float, int]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[Distance, float, int]) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km

    def __len__(self) -> Union[float, int]:
        return self.km
