from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(f"Unsupported operand type(s) for +: "
                        f"'Distance' and '{type(other).__name__}'")

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        raise TypeError(f"Unsupported operand type(s) for +=: "
                        f"'Distance' and '{type(other).__name__}'")

    def __mul__(self, other: Union[int, float]) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"Unsupported operand type(s) for *: "
                            f"'Distance' and '{type(other).__name__}'")
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"Unsupported operand type(s) for /: "
                            f"'Distance' and '{type(other).__name__}'")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(f"Unsupported operand type(s) for <: "
                        f"'Distance' and '{type(other).__name__}'")

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError(f"Unsupported operand type(s) for >: "
                        f"'Distance' and '{type(other).__name__}'")

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError(f"Unsupported operand type(s) for ==: "
                        f"'Distance' and '{type(other).__name__}'")

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError(f"Unsupported operand type(s) for <=: "
                        f"'Distance' and '{type(other).__name__}'")

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(f"Unsupported operand type(s) for >=: "
                        f"'Distance' and '{type(other).__name__}'")
