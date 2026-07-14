from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __float__(self) -> float:
        return float(self.km)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: Distance | int | float) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
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

    def _get_other_value(self, other: Distance | int | float) -> float | int:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_value(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_value(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_value(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_value(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        other_km = self._get_other_value(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km
