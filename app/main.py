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
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
