from __future__ import annotations
from typing import Union

class Distance:
    def __init__(self, kilometers: int | float) -> None:
        self.km: int | float = kilometers

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_val(self, other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError(f"Unsupported operand type: {type(other)}")

    # Arithmetic Methods
    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self._get_val(other))

    def __radd__(self, other: Distance | int | float) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self._get_val(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(f"Unsupported operand type for *: {type(other)}")

    def __rmul__(self, other: int | float) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / other, 2))
        raise TypeError(f"Unsupported operand type for /: {type(other)}")

    # Comparison Methods
    def __eq__(self, other: Distance | int | float) -> bool:
        try:
            return self.km == self._get_val(other)
        except TypeError:
            return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        try:
            return self.km < self._get_val(other)
        except TypeError:
            return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        try:
            return self.km > self._get_val(other)
        except TypeError:
            return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        try:
            return self.km <= self._get_val(other)
        except TypeError:
            return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        try:
            return self.km >= self._get_val(other)
        except TypeError:
            return NotImplemented
