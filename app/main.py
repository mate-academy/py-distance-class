from __future__ import annotations
from __future__ import division
from typing import Union, Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)) is True:
            return Distance(self.km + other)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance) is True:
            self.km = self.km + other.km
            return self
        if isinstance(other, (int, float)) is True:
            self.km = self.km + other
            return self

    def __mul__(self, other: Any) -> Union[Distance, NotImplemented]:
        if isinstance(other, (int, float)) is True:
            self.km = self.km * other
            return self
        elif isinstance(other, Distance):
            return NotImplemented
        else:
            raise TypeError

    def __truediv__(self, other: Any) -> Union[Distance, NotImplemented]:
        if isinstance(other, (int, float)) is True:
            self.km = round((self.km / other), 2)
            return self
        elif isinstance(other, Distance):
            return NotImplemented
        else:
            raise TypeError

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance) is True:
            return self.km < other.km
        if isinstance(other, (int, float)) is True:
            return self.km < other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance) is True:
            return self.km > other.km
        if isinstance(other, (int, float)) is True:
            return self.km > other

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance) is True:
            return self.km == other.km
        if isinstance(other, (int, float)) is True:
            return self.km == other

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance) is True:
            return self.km <= other.km
        if isinstance(other, (int, float)) is True:
            return self.km <= other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance) is True:
            return self.km >= other.km
        if isinstance(other, (int, float)) is True:
            return self.km >= other
