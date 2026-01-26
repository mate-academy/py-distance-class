from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _get_value(self, other: Distance | float | int) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == self._get_value(other)

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < self._get_value(other)

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= self._get_value(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > self._get_value(other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return self.km >= self._get_value(other)
