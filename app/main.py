from __future__ import annotations

from numbers import Real
from typing import Union


class Distance:
    def __init__(self, km: Real) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km:g} kilometers."

    def __repr__(self) -> str:
        km_value = int(self.km) if self.km.is_integer() else self.km
        return f"Distance(km={km_value})"

    @staticmethod
    def _as_km(other: object) -> Union[float, NotImplemented]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, Real):
            return float(other)
        return NotImplemented

    def __add__(self, other: object) -> "Distance":
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __radd__(self, other: object) -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other: object) -> "Distance":
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(self, other: object) -> "Distance":
        if not isinstance(other, Real):
            return NotImplemented
        return Distance(self.km * float(other))

    def __rmul__(self, other: object) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: object) -> "Distance":
        if not isinstance(other, Real):
            return NotImplemented
        value = float(other)
        if value == 0:
            raise ZeroDivisionError("division by zero")
        return Distance(round(self.km / value, 2))

    def __lt__(self, other: object) -> bool:
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
        return bool(self.km < km)

    def __gt__(self, other: object) -> bool:
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
        return bool(self.km > km)

    def __eq__(self, other: object) -> bool:
        km = self._as_km(other)
        if km is NotImplemented:
            return False
        return bool(self.km == km)

    def __le__(self, other: object) -> bool:
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
        return bool(self.km <= km)

    def __ge__(self, other: object) -> bool:
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
        return bool(self.km >= km)
