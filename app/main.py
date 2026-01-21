from __future__ import annotations

from typing import Union


Number = Union[int, float]
OtherAdd = Union["Distance", Number]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _value(self, other: OtherAdd) -> Union[Number, type(NotImplemented)]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: OtherAdd) -> Distance:
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return Distance(self.km + value)

    def __iadd__(self, other: OtherAdd) -> Distance:
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        self.km += value
        return self

    def __mul__(self, other: Number) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: OtherAdd) -> bool:
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km < value

    def __gt__(self, other: OtherAdd) -> bool:
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km > value

    def __ge__(self, other: OtherAdd) -> bool:
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km >= value

    def __le__(self, other: OtherAdd) -> bool:
        value = self._value(other)
        if value is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km <= value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False
