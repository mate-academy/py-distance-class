from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

        raise TypeError("Unsupported element type")

    def __iadd__(self, other: Union[Distance, int, float]) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self

        raise TypeError("Unsupported element type")

    def __mul__(self, other: Union[Distance, int, float]) -> object:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

        raise TypeError("Unsupported element type")

    def __truediv__(self, other: Union[int, float]) -> object:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

        raise TypeError("Unsupported element type")

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

        raise TypeError("Unsupported element type")

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

        raise TypeError("Unsupported element type")

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

        raise TypeError("Unsupported element type")

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

        raise TypeError("Unsupported element type")

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other

        raise TypeError("Unsupported element type")
