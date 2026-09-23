from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            return Distance(self.km + other_km)

        return NotImplemented

    def __iadd__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            self.km += other_km
            return self

        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

        return NotImplemented

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

        return NotImplemented

    def __lt__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            return True if self.km < other_km else False

        return NotImplemented

    def __gt__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            return True if self.km > other_km else False

        return NotImplemented

    def __eq__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            return True if self.km == other_km else False

        return NotImplemented

    def __le__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            return True if self.km <= other_km else False

        return NotImplemented

    def __ge__(self, other: Any) -> Any:
        other_km = Distance.return_km_value(other)

        if other_km is not None:
            return True if self.km >= other_km else False

        return NotImplemented

    @staticmethod
    def return_km_value(other: Any) -> Any:
        if isinstance(other, Distance):
            return other.km

        elif isinstance(other, (int, float)):
            return other

        return None
