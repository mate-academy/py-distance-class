from __future__ import annotations


class Distance:
    def _get_km(self, other: Distance | int | float) -> float:
        if isinstance(other, Distance):
            return other.km
        return float(other)

    def __init__(self, km: int | float) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        if self.km == int(self.km):
            return f"Distance: {int(self.km)} kilometers."
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        if self.km == int(self.km):
            return f"Distance(km={int(self.km)})"
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_km(other)
        new_km = self.km + other_km
        return Distance(new_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = self._get_km(other)
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        result = self.km / other
        rounded_result = round(result, 2)
        return Distance(rounded_result)

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
