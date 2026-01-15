from __future__ import annotations
from typing import Any, Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: Union[Distance, int, float]) -> Distance:
        if hasattr(distance, "km"):
            return Distance(km=self.km + distance.km)
        return Distance(km=self.km + distance)

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if hasattr(other, "km"):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, distance: Union[int, float]) -> Distance:
        return Distance(km=self.km * distance)

    def __truediv__(self, distance: Union[int, float]) -> Distance:
        return Distance(km=round(self.km / distance, 2))

    def __lt__(self, other: Any) -> bool:
        if hasattr(other, "km"):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[int, float]) -> bool:
        if hasattr(other, "km"):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[int, float]) -> bool:
        if hasattr(other, "km"):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[int, float]) -> bool:
        if hasattr(other, "km"):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[int, float]) -> bool:
        if hasattr(other, "km"):
            return self.km >= other.km
        return self.km >= other
