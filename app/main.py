from __future__ import annotations
from __future__ import division
from typing import Union


class Distance:
    Validator = Union["Distance", int]

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Validator) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Validator) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    @staticmethod
    def is_a_instance(other: Validator) -> None:
        if isinstance(other, Distance):
            return None

    def __mul__(self, other: Validator) -> Distance:
        self.is_a_instance(other)
        return Distance(km=self.km * other)

    def __truediv__(self, other: Validator) -> Distance | None:
        self.is_a_instance(other)
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Validator) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Validator) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Validator) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Validator) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Validator) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
