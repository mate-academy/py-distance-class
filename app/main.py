from __future__ import annotations

from typing import Union

OtherAdd = Union["Distance", int, float]
Number = Union[int, float]
NotImpl = type(NotImplemented)


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _to_km(self, other: OtherAdd) -> Union[Number, NotImpl]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: OtherAdd) -> Union[Distance, NotImpl]:
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        return Distance(self.km + km_other)

    def __iadd__(self, other: OtherAdd) -> Union[Distance, NotImpl]:
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        self.km += km_other
        return self

    def __mul__(self, other: Number) -> Union[Distance, NotImpl]:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Union[Distance, NotImpl]:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: OtherAdd) -> Union[bool, NotImpl]:
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        return self.km < km_other

    def __gt__(self, other: OtherAdd) -> Union[bool, NotImpl]:
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        return self.km > km_other

    def __eq__(self, other: object) -> Union[bool, NotImpl]:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        return self.km == km_other

    def __le__(self, other: OtherAdd) -> Union[bool, NotImpl]:
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        return self.km <= km_other

    def __ge__(self, other: OtherAdd) -> Union[bool, NotImpl]:
        km_other = self._to_km(other)
        if km_other is NotImplemented:
            return NotImplemented
        return self.km >= km_other
