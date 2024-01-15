from __future__ import annotations
import functools


@functools.total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.to_number(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.to_number(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.to_number(other)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.to_number(other)

    @staticmethod
    def to_number(number: Distance | int | float) -> int | float:
        if isinstance(number, Distance):
            return number.km
        return number
