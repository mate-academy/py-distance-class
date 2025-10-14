from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def _get_km(self, other: Distance | int | float) -> float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_km(other)
        return Distance(self.km + other_km)

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            return NotImplemented

        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            return NotImplemented

        result_km = round(self.km / other, 2)
        return Distance(result_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_km(other)
        self.km += other_km
        return self

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = self._get_km(other)
        return self.km >= other_km
