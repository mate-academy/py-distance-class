from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Operand must be a number")

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Operand must be a number")

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(
                "Operand must be an instance of Distance or a number"
            )
