from __future__ import annotations
from typing import Callable
from typing import Union
from functools import wraps


def check_other_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(self: Distance,
                other: Union[Distance, int, float]) -> Callable:
        if isinstance(other, (Distance, int, float)):
            if isinstance(other, Distance):
                if func.__name__ in ["__mul__", "__truediv__"]:
                    return func(self, other)
                other = other.km
            return func(self, other)
        else:
            raise TypeError(
                "'Other' must be int/float or belong to Distance class"
            )
    return wrapper


class Distance:

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

    @check_other_decorator
    def __mul__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(self.km * other)

    @check_other_decorator
    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    @check_other_decorator
    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < other

    @check_other_decorator
    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > other

    @check_other_decorator
    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self.km == other

    @check_other_decorator
    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= other

    @check_other_decorator
    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= other
