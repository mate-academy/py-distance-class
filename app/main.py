from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def class_or_number(other: Any) -> int | Distance:
        return other.km if isinstance(other, Distance) else other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        return Distance(self.km + self.class_or_number(other))

    def __iadd__(self, other: Any) -> Distance:
        self.km += self.class_or_number(other)
        return self

    def __mul__(self, other: Any) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Any) -> bool:
        return self.km > self.class_or_number(other)

    def __eq__(self, other: Any) -> bool:
        return self.km == self.class_or_number(other)

    def __le__(self, other: Any) -> bool:
        return self.km <= self.class_or_number(other)

    def __ge__(self, other: Any) -> bool:
        return self.km >= self.class_or_number(other)
