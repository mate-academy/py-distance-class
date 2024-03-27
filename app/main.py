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
        km = (
            self.km + other
            if isinstance(other, (float, int))
            else self.km + other.km
        )
        return Distance(km)

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        self.km += other if isinstance(other, (float, int)) else other.km
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        return self.km < (
            other if isinstance(other, (float, int)) else other.km
        )

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        return self.km > (
            other if isinstance(other, (float, int)) else other.km
        )

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        return self.km == (
            other if isinstance(other, (float, int)) else other.km
        )

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        return not self > other

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        return not self < other
