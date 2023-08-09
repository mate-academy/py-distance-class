from __future__ import annotations
from typing import Callable


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Callable) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        else:
            return Distance(
                km=self.km + other.km
            )

    def __iadd__(self, other: int | float | Callable) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other: int | float | Callable) -> "Distance":
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int | float | Callable) -> "Distance":
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: int | float | Callable) -> bool:
        return self.km < other

    def __gt__(self, other: int | float | Callable) -> bool:
        return self.km > other

    def __eq__(self, other: int | float | Callable) -> bool:
        return self.km == other

    def __le__(self, other: int | float | Callable) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float | Callable) -> bool:
        return self.km >= other
