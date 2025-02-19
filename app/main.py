from __future__ import annotations

import operator


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.lt)

    def __gt__(self, other: Distance | int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.gt)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self._compare_with_operand(other, operator.eq)

    def __ge__(self, other: Distance | int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.ge)

    def __le__(self, other: Distance | int | float) -> bool | TypeError:
        return self._compare_with_operand(other, operator.le)

    def _compare_with_operand(
            self,
            other: Distance | float | int,
            comparison_operator: callable
    ) -> bool | TypeError:
        if isinstance(other, Distance):
            return comparison_operator(self.km, other.km)
        if isinstance(other, (int, float)):
            return comparison_operator(self.km, other)

        raise TypeError("Unsupported type for comparison.")
