from __future__ import annotations

from typing import Union


Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # Addition: support Distance + Distance and Distance + number
    def __add__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: Number) -> Distance:
        # number + Distance
        return self.__add__(other)

    # Multiplication: only with numbers (int | float) per checklist
    def __mul__(self, other: Number) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: Number) -> Distance:
        return self.__mul__(other)

    # True division: only with numbers (int | float) per checklist
    def __truediv__(self, other: Number) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Distance(self.km / other)

    # Optionally support converting to float
    def __float__(self) -> float:
        return self.km

    # Comparisons: support comparing with Distance or with numbers
    def _as_number(self, other: Union[Distance, Number]) -> Number:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError(f"Cannot compare Distance with {type(other)!r}")
    def __lt__(self, other: Union[Distance, Number]) -> bool:
        return self.km < self._as_number(other)
    def __le__(self, other: Union[Distance, Number]) -> bool:
        return self.km <= self._as_number(other)
    def __gt__(self, other: Union[Distance, Number]) -> bool:
        return self.km > self._as_number(other)
    def __ge__(self, other: Union[Distance, Number]) -> bool:
        return self.km >= self._as_number(other)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, (Distance, int, float)):
            try:
                return self.km == self._as_number(other)  # type: ignore[arg-type]
            except TypeError:
                return False
        return False
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
