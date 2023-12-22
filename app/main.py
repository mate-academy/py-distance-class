from __future__ import annotations
from typing import Callable, Any
from functools import wraps


def _int_float_types_execption(func: Callable) -> Callable:
    @wraps(func)
    def inner(self: Any, other: Any) -> Callable:
        if isinstance(other, (int, float)):
            return func(self, other=Distance(other))
        return func(self, other)
    return inner


class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @_int_float_types_execption
    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + other.km)

    @_int_float_types_execption
    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.km
        return self

    def __mul__(self, coefficient: int | float) -> Distance:
        return Distance(self.km * coefficient)

    def __truediv__(self, divider: int | float) -> Distance:
        return Distance(round(self.km / divider, 2))

    @_int_float_types_execption
    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other.km

    @_int_float_types_execption
    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other.km

    @_int_float_types_execption
    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other.km

    @_int_float_types_execption
    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other.km

    @_int_float_types_execption
    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other.km
