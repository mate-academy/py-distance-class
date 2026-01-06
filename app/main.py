from __future__ import annotations
from typing import Callable


def magic_test(func: Callable) -> Callable:
    def inner(self: object, other: object) -> bool:
        if isinstance(other, Distance):
            rhs = other.km
        elif isinstance(other, (int, float)):
            rhs = other
        else:
            return NotImplemented
        return func(self, rhs)

    return inner


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Distance(round(self.km / other, 2))

    @magic_test
    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    @magic_test
    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    @magic_test
    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    @magic_test
    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    @magic_test
    def __ge__(self, other: int | float) -> bool:
        return self.km >= other
