from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        if self.km.is_integer():
            return f"Distance: {int(self.km)} kilometers."
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        if self.km.is_integer():
            return f"Distance(km={int(self.km)})"
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km += other.km if isinstance(other, Distance) else float(other)
        return self

    def __mul__(self, factor: Union[int, float]) -> Distance:
        return Distance(self.km * float(factor))

    def __truediv__(self, divisor: Union[int, float]) -> Distance:
        result = self.km / float(divisor)
        return Distance(round(result, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km < other_km

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return NotImplemented

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km <= other_km

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km >= other_km
