from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number")
        self.km: Number = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _get_km(
        value: Union[Distance, Number]
    ) -> Union[float, type(NotImplemented)]:
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return NotImplemented

    def __add__(
        self, other: Union[Distance, Number]
    ) -> Union[Distance, type(NotImplemented)]:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __radd__(
        self, other: Union[Distance, Number]
    ) -> Union[Distance, type(NotImplemented)]:
        return self + other

    def __iadd__(
        self, other: Union[Distance, Number]
    ) -> Union[Distance, type(NotImplemented)]:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(
        self, other: Number
    ) -> Union[Distance, type(NotImplemented)]:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        if isinstance(other, Distance):
            raise TypeError(
                "Multiplication by Distance is not supported"
            )
        return NotImplemented

    def __rmul__(
        self, other: Number
    ) -> Union[Distance, type(NotImplemented)]:
        return self * other

    def __truediv__(
        self, other: Number
    ) -> Union[Distance, type(NotImplemented)]:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / other, 2))
        if isinstance(other, Distance):
            raise TypeError(
                "Division by Distance is not supported"
            )
        return NotImplemented

    def __rtruediv__(
        self, other: Number
    ) -> type(NotImplemented):
        return NotImplemented

    def __eq__(
        self, other: Union[Distance, Number]
    ) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km == km

    def __lt__(
        self, other: Union[Distance, Number]
    ) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km < km

    def __le__(
        self, other: Union[Distance, Number]
    ) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km <= km

    def __gt__(
        self, other: Union[Distance, Number]
    ) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km > km

    def __ge__(
        self, other: Union[Distance, Number]
    ) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km >= km
