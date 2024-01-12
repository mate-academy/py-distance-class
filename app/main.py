from __future__ import annotations
from typing import Callable
from typing import Union
from functools import wraps


def check_other_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(self: Distance,
                other: Union[Distance, int, float]) -> Callable:
        if Distance.check_other(other):
            if isinstance(other, Distance):
                other = other.km
            return func(self, other)
        else:
            raise TypeError(
                "'Other' must be int/float or belong to Distance class"
            )
    return wrapper


class Distance:

    @staticmethod
    def check_other(other: Union[Distance, int, float]) -> bool:
        return isinstance(other, (Distance, int, float))

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @check_other_decorator
    def __add__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km + other)

    @check_other_decorator
    def __iadd__(self, other: Union[int, float]) -> Distance:
        self.km += other
        return self

    def __mul__(self, other: Union[Distance, int, float]) -> Distance:
        if Distance.check_other(other):
            return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, Union[int, float]):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other(other):
            return self.km < other

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other(other):
            return self.km > other

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other(other):
            return self.km == other

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other(other):
            return self.km <= other

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other(other):
            return self.km >= other
