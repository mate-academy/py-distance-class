from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_other_km(self, other: object) -> int | float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(km=self.km + other_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round((self.km / other), 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
