from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: NumericType) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: DistanceType) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, NumericType):
            return Distance(self.km + other)
        else:
            raise Distance.err(other)

    def __iadd__(self, other: DistanceType) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, NumericType):
            self.km += other
        else:
            raise Distance.err(other)
        return self

    def __mul__(self, other: NumericType) -> Distance:
        if isinstance(other, NumericType):
            return Distance(self.km * other)
        else:
            raise Distance.err(other)

    def __truediv__(self, other: NumericType) -> Distance:
        if isinstance(other, NumericType):
            return Distance(round(self.km / other, 2))
        else:
            raise Distance.err(other)

    def __lt__(self, other: DistanceType) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, NumericType):
            return self.km < other
        else:
            raise Distance.err(other)

    def __gt__(self, other: DistanceType) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, NumericType):
            return self.km > other
        else:
            raise Distance.err(other)

    def __eq__(self, other: DistanceType) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, NumericType):
            return self.km == other
        else:
            raise Distance.err(other)

    def __le__(self, other: DistanceType) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, NumericType):
            return self.km <= other
        else:
            raise Distance.err(other)

    def __ge__(self, other: DistanceType) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, NumericType):
            return self.km >= other
        else:
            raise Distance.err(other)

    @staticmethod
    def err(other: Any) -> TypeError:
        return TypeError(f"Error type: {type(other).__name__} is not valid")


DistanceType = Distance | int | float
NumericType = int | float
