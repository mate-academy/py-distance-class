from __future__ import annotations
from typing import Union


# noinspection PyUnresolvedReferences,PyTypeChecker
class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        return not self > other

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        return not self < other

    def __len__(self) -> int:
        return self.km
