from __future__ import annotations
from typing import Any, Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[float, int, Distance]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __iadd__(self, other: Union[float, int, Distance]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[float, int, Distance]) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km * other.km
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km /= other.km
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[float, int, Distance]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[float, int, Distance]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[float, int, Distance]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __ge__(self, other: Union[float, int, Distance]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __le__(self, other: Union[float, int, Distance]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other
