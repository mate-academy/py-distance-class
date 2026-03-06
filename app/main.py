from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_distance_value(
        self,
        other: Distance | int | float
    ) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Distance | int | float) -> Distance:
        value = self.km + self._get_distance_value(other)
        return Distance(value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self._get_distance_value(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._get_distance_value(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._get_distance_value(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self._get_distance_value(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self._get_distance_value(other)
