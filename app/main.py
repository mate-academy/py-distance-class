from __future__ import annotations

from typing import Union


class Distance:
    def __init__(self, km: float)-> None:
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
        return NotImplemented

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
