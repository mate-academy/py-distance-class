from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float, int]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s)")

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise TypeError("Unsupported operand type(s)")

    def __mul__(self, multiplier: float) -> Distance:
        if isinstance(multiplier, (int, float)):
            return Distance(self.km * multiplier)
        else:
            raise TypeError("Unsupported operand type(s)")

    def __truediv__(self, divider: float) -> Distance:
        if divider == 0:
            raise ValueError("Cannot divide by zero.")
        result_distance = self.km / divider
        result_distance = round(result_distance, 2)
        return Distance(result_distance)

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type(s)")

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type(s)")

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type(s)")

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type(s)")

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type(s)")
