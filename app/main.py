from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    @classmethod
    def validate(cls, value: Any) -> bool:
        return isinstance(value, cls)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if self.validate(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> None:
        if self.validate(other):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: Distance | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | int) -> Distance:
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: Distance | int) -> bool:
        if self.validate(other):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int) -> bool:
        if self.validate(other):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | int) -> bool:
        if self.validate(other):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | int) -> bool:
        if self.validate(other):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | int) -> bool:
        if self.validate(other):
            return self.km >= other.km
        return self.km >= other
