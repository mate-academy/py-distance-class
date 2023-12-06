from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise ValueError("Unsupported operand type")

    def __iadd__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError("Unsupported operand type")
        return self

    def __mul__(self, scalar: int | float | None) -> None:
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, divisor: int) -> None:
        if isinstance(divisor, (int, float)):
            result = self.km / divisor
            return Distance(round(result, 2))
        else:
            raise TypeError("Unsupported operand type")

    def __lt__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[int, float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
