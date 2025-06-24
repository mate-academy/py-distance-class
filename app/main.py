from __future__ import annotations
from functools import wraps
from typing import Union, Any, Callable


def validate_type(
    supported_types: tuple[type, ...] = (int, float),
    allow_same_type: bool = True
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self: Distance, other: Any, *args, **kwargs) -> Any:
            all_types = supported_types + (
                (type(self),) if allow_same_type else ()
            )
            if not isinstance(other, all_types):
                raise TypeError(
                    f"Unsupported type for operation: {type(other)}"
                )
            other_value = other.km if isinstance(other, type(self)) else other
            return func(self, other_value, *args, **kwargs)
        return wrapper
    return decorator


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number")
        if km < 0:
            raise ValueError("Distance cannot be negative")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @validate_type()
    def __add__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km + other)

    @validate_type()
    def __iadd__(self, other: Union[int, float]) -> Distance:
        self.km += other
        return self

    @validate_type()
    def __sub__(self, other: Union[int, float]) -> Distance:
        result = self.km - other
        if result < 0:
            raise ValueError("Resulting distance cannot be negative")
        return Distance(result)

    @validate_type()
    def __isub__(self, other: Union[int, float]) -> Distance:
        result = self.km - other
        if result < 0:
            raise ValueError("Resulting distance cannot be negative")
        self.km = result
        return self

    @validate_type()
    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    @validate_type()
    def __imul__(self, other: Union[int, float]) -> Distance:
        self.km *= other
        return self

    @validate_type(allow_same_type=False)
    def __truediv__(self, other: Union[int, float]) -> Distance:
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(self.km / other)

    @validate_type(allow_same_type=False)
    def __itruediv__(self, other: Union[int, float]) -> Distance:
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.km /= other
        return self

    @validate_type()
    def __eq__(self, other: Union[int, float]) -> bool:
        return self.km == other

    @validate_type()
    def __lt__(self, other: Union[int, float]) -> bool:
        return self.km < other

    @validate_type()
    def __le__(self, other: Union[int, float]) -> bool:
        return self.km <= other

    @validate_type()
    def __gt__(self, other: Union[int, float]) -> bool:
        return self.km > other

    @validate_type()
    def __ge__(self, other: Union[int, float]) -> bool:
        return self.km >= other

    def __radd__(self, other: Union[int, float]) -> Distance:
        return self + other

    def __rsub__(self, other: Union[int, float]) -> Distance:
        result = other - self.km
        if result < 0:
            raise ValueError("Resulting distance cannot be negative")
        return Distance(result)

    def __rmul__(self, other: Union[int, float]) -> Distance:
        return self * other

    def __rtruediv__(self, other: Union[int, float]) -> Distance:
        raise TypeError("Division of number by Distance is not supported")
