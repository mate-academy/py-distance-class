from __future__ import annotations

from typing import Union


Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: Number = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: Number) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Number) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _get_value(
            self,
            other: Union[Distance, Number]) -> Union[Number, object]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __le__(self, other: Union[Distance, Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented
