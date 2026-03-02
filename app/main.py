from __future__ import annotations

from typing import Union


class Distance:
    def __init__(self, km: int or float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self

        self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km *= other
            return self

        raise TypeError(f"{other} must be number of type: int or float")

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise TypeError(f"{other} cannot be division on zero!")

        if isinstance(other, (int, float)):
            self.km /= other
            self.km = round(self.km, 2)
            return self

        raise TypeError(f"{other} must be number of type: int or float")

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        else:
            return self.km >= other.km
