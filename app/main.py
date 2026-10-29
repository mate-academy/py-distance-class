
from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: Distance | float | int) -> float | int:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            return NotImplemented

        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            return NotImplemented

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km == self._get_km(other)

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return self.km >= self._get_km(other)
