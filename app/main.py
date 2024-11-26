from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def is_distance(some_data: Distance | int | float) -> Any:
        if isinstance(some_data, Distance):
            return some_data.km
        else:
            return some_data

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.is_distance(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.is_distance(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"Unsupported operation class Distance * {type(other)}"
            )
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"Unsupported operation class Distance / {type(other)}"
            )
        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.is_distance(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.is_distance(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.is_distance(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.is_distance(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.is_distance(other)
