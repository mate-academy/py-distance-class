from __future__ import annotations
from typing import Callable, Any
import functools


def validate_operand(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(self: Distance, other: (Distance, int, float)) -> Any:
        if isinstance(other, Distance):
            return func(self, other.km)
        elif isinstance(other, (int, float)):
            return func(self, other)
        else:
            raise TypeError(f"Unsupported operand type for {func.__name__}")

    return wrapper


class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @validate_operand
    def __add__(self, other: (Distance, int, float)) -> Distance:
        return Distance(self.km + other)

    @validate_operand
    def __iadd__(self, other: (Distance, int, float)) -> Distance:
        self.km += other
        return self

    def __mul__(self, other: (int, float)) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other: int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type for /")

    def __lt__(self, other: (Distance, int, float)) -> bool:
        return self.km < other

    def __gt__(self, other: (Distance, int, float)) -> bool:
        return self.km > other

    def __eq__(self, other: (Distance, int, float)) -> bool:
        return self.km == other

    def __le__(self, other: (Distance, int, float)) -> bool:
        return not self > other

    def __ge__(self, other: (Distance, int, float)) -> bool:
        return not self < other
