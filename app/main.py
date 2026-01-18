from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

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

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = round(self.km / other, 2)
            return Distance(result)
        return NotImplemented

    def _to_km(self, other: Distance | int | float) -> float | None:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return float(other)
        return None

    def __lt__(self, other: Distance | int | float) -> bool:
        km = self._to_km(other)
        if km is None:
            return NotImplemented
        return self.km < km

    def __gt__(self, other: Distance | int | float) -> bool:
        km = self._to_km(other)
        if km is None:
            return NotImplemented
        return self.km > km

    def __eq__(self, other: Distance | int | float) -> bool:
        km = self._to_km(other)
        if km is None:
            return NotImplemented
        return self.km == km

    def __le__(self, other: Distance | int | float) -> bool:
        km = self._to_km(other)
        if km is None:
            return NotImplemented
        return self.km <= km

    def __ge__(self, other: Distance | int | float) -> bool:
        km = self._to_km(other)
        if km is None:
            return NotImplemented
        return self.km >= km
