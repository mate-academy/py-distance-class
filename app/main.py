from __future__ import division
from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        value = None
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (float, int)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: Distance) -> Distance:
        value = None
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (float, int)):
            value = other
        else:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, number: int) -> Distance:
        if not isinstance(number, (int, float)):
            return NotImplemented
        mul_distance = self.km * number
        return Distance(mul_distance)

    def __truediv__(self, number: int) -> Distance:
        if not isinstance(number, (int, float)):
            return NotImplemented
        if number == 0:
            raise ZeroDivisionError
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: Distance) -> bool:
        helper = self._to_km(other)
        if helper is NotImplemented:
            return NotImplemented
        return self.km < helper

    def __gt__(self, other: Distance) -> bool:
        helper = self._to_km(other)
        if helper is NotImplemented:
            return NotImplemented
        return self.km > helper

    def __eq__(self, other: Distance) -> bool:
        helper = self._to_km(other)
        if helper is NotImplemented:
            return NotImplemented
        return self.km == helper

    def __le__(self, other: Distance) -> bool:
        helper = self._to_km(other)
        if helper is NotImplemented:
            return NotImplemented
        return self.km <= helper

    def __ge__(self, other: Distance) -> bool:
        helper = self._to_km(other)
        if helper is NotImplemented:
            return NotImplemented
        return self.km >= helper

    def _to_km(self, other: Distance) -> float | NotImplemented:
        if isinstance(other, Distance):
            rhs = other.km
        elif isinstance(other, (float, int)):
            rhs = other
        else:
            return NotImplemented
        return float(rhs)
