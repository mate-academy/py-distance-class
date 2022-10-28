from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: Union[int, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other: int) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Union[int, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km
