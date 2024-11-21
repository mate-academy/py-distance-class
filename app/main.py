from __future__ import annotations
from functools import wraps
from typing import Callable


class Distance:
    @staticmethod
    def param_check(func: Callable) -> Callable:
        @wraps(func)
        def wrapped(
                self: Distance,
                other: Distance | int | float
        ) -> Distance | bool:
            if isinstance(other, Distance):
                return func(self.km, other.km)
            return func(self.km, other)

        return wrapped

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @param_check
    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km = (self + other).km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    @param_check
    def __lt__(self, other: Distance | int | float) -> bool:
        return self < other

    @param_check
    def __gt__(self, other: Distance | int | float) -> bool:
        return self > other

    @param_check
    def __eq__(self, other: Distance | int | float) -> bool:
        return self == other

    @param_check
    def __le__(self, other: Distance | int | float) -> bool:
        return self <= other

    @param_check
    def __ge__(self, other: Distance | int | float) -> bool:
        return self >= other
