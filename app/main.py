from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int | float) -> None:
        if km < 0:
            raise ValueError("Distance cannot be negative.")
        self.km = float(km)

    def _format_km(self) -> int | float:
        return int(self.km) if self.km.is_integer() else self.km

    def __str__(self) -> str:
        return f"Distance: {self._format_km()} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self._format_km()})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: int | float) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: int | float) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("Cannot divide distance by zero.")
        return Distance(self.km / other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented
