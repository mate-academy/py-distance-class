from typing import Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: Any, allow_distance: bool = True) -> float:
        if allow_distance and isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return float(other)
        return NotImplemented

    def __add__(self, other: Any) -> Distance:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __iadd__(self, other: Any) -> Distance:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(self, other: int | float) -> Distance:
        km = self._get_km(other, allow_distance=False)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km * km)

    def __truediv__(self, other: int | float) -> Distance:
        km = self._get_km(other, allow_distance=False)
        if km is NotImplemented:
            return NotImplemented
        if km == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(round(self.km / km, 2))

    def __lt__(self, other: Any) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km < km

    def __gt__(self, other: Any) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km > km

    def __eq__(self, other: Any) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km == km

    def __le__(self, other: Any) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km <= km

    def __ge__(self, other: Any) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km >= km
