from __future__ import annotations

from typing import Self


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
        self,
        other: Distance | float
    ) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __radd__(
        self,
        other: Distance | float
    ) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | float) -> Self:
        result = self.__add__(other)
        self.km = result.km
        return self

    def __mul__(self, other: float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError(
                "Distance cannot be multiplied by another Distance"
            )
        return Distance(self.km * other)

    def __rmul__(
        self,
        other: float
    ) -> Distance:
        return self.__mul__(other)

    def __truediv__(
        self,
        other: float
    ) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
