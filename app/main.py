from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: object) -> int | float | None:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return None

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_km(other)
        if other_km is None:
            return NotImplemented
        return Distance(self.km + other_km)

    def __radd__(self, other: int | float) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_km(other)
        if other_km is None:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: int | float) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        if other_km is None:
            return False
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        if other_km is None:
            return False
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        other_km = self._get_km(other)
        if other_km is None:
            return False
        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        if other_km is None:
            return False
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        if other_km is None:
            return False
        return self.km >= other_km
