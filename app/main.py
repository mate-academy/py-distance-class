from __future__ import annotations

from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _value(other: Union[Distance, int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(self.km + self._value(other))

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km += self._value(other)
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < self._value(other)

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > self._value(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == self._value(other)
        return NotImplemented

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= self._value(other)

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= self._value(other)
