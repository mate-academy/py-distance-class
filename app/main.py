from __future__ import annotations

import operator
from typing import Union, Callable


class Distance:
    def __init__(self, km: float) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("km must be a number")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(
            self.km + other.km
            if isinstance(other, Distance)
            else self.km + other
        )

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[float, Distance]) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Unsupported operation.")
        return Distance(round(self.km / other, 2))

    def _compare_with_operand(
            self,
            other: Union[Distance, float],
            comparison_operator: Callable
    ) -> bool:
        return comparison_operator(
            self.km,
            other.km if isinstance(other, Distance) else other
        )

    def __lt__(self, other: Union[Distance, float]) -> bool:
        return self._compare_with_operand(other, operator.lt)

    def __gt__(self, other: Union[Distance, float]) -> bool:
        return self._compare_with_operand(other, operator.gt)

    def __eq__(self, other: Union[Distance, float]) -> bool:
        return self._compare_with_operand(other, operator.eq)

    def __le__(self, other: Union[Distance, float]) -> bool:
        return self._compare_with_operand(other, operator.le)

    def __ge__(self, other: Union[Distance, float]) -> bool:
        return self._compare_with_operand(other, operator.ge)
