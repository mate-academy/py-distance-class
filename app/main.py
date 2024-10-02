from __future__ import annotations
from functools import total_ordering
from typing import Union


@total_ordering
class Distance:
    # Write your code here
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    @staticmethod
    def validate(other: Union[int, float, Distance]) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(f"Unsupported type for operation: {type(other)}")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        return Distance(self.km + self.validate(other))

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        self.km += self.validate(other)
        return self

    def __mul__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance instance is not supported")
        return Distance(self.km * self.validate(other))

    def __truediv__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance instance is not supported")
        return Distance(round(self.km / self.validate(other), 2))

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        return self.km < self.validate(other)

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        return self.km == self.validate(other)
