from __future__ import annotations
from numbers import Real


class Distance:
    def __init__(self, km: Real) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _to_km(value: Distance | Real) -> Real | NotImplemented:
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, Real):
            return value
        return NotImplemented

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        other_km = self._to_km(other)
        if other_km is NotImplemented or isinstance(other, Distance):
            return NotImplemented
        return Distance(self.km * other_km)

    def __truediv__(self, other: int | float) -> Distance:
        other_km = self._to_km(other)
        if other_km is NotImplemented or isinstance(other, Distance):
            return NotImplemented
        return Distance(round(self.km / other_km, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return False
        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = self._to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
