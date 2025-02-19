from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.check_instance(other)
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.check_instance(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.check_instance(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.check_instance(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.check_instance(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.check_instance(other)

    @staticmethod
    def check_instance(other: Any) -> Any:
        return other.km if isinstance(other, Distance) else other
