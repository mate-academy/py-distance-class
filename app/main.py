from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def get_value(self, other: Union[Distance, int, float]) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError(
            f"unsupported operand type(s): 'Distance' and '{type(other)}'"
        )

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(km=self.km + self.get_value(other))

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km += self.get_value(other)
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        raise TypeError(
            f"unsupported operand type(s): 'Distance' and {type(other)}"
        )

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(km=round(self.km / other, 2))
        raise TypeError(
            f"unsupported operand type(s) for /: 'Distance' and {type(other)}"
        )

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < self.get_value(other)

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > self.get_value(other)

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self.km == self.get_value(other)

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= self.get_value(other)

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= self.get_value(other)
