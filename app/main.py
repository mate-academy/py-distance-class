from __future__ import annotations

from typing import Union, Callable


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        return self._math_operation(
            other,
            lambda a, b: a + b,
            new=True
        )

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        return self._math_operation(
            other,
            lambda a, b: a + b
        )

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return self._math_operation(
                other,
                lambda a, b: a * b,
                new=True
            )

    def __truediv__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return self._math_operation(
                other,
                lambda a, b: round(a / b, 2),
                new=True
            )

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self._bool_operations(other, lambda a, b: a < b)

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self._bool_operations(other, lambda a, b: a > b)

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self._bool_operations(other, lambda a, b: a == b)

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self._bool_operations(other, lambda a, b: a <= b)

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self._bool_operations(other, lambda a, b: a >= b)

    def _math_operation(
            self,
            other: Union[Distance, int, float],
            operations: Callable,
            new: bool = False
    ) -> Distance:

        other_km = other.km if isinstance(other, Distance) else other
        km = operations(self.km, other_km)

        if new:
            return Distance(km=km)

        self.km = km
        return self

    def _bool_operations(
            self,
            other: Union[Distance, int, float],
            operations: Callable
    ) -> bool:

        other_km = other.km if isinstance(other, Distance) else other
        return operations(self.km, other_km)
