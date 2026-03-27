from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _to_km(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Distance | int | float) -> Distance:
        km_to_add = self._to_km(other)
        return Distance(self.km + km_to_add)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        km_to_add = self._to_km(other)
        self.km += km_to_add
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            return Distance(0)
        result_km = round(self.km / other, 2)
        return Distance(result_km)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._to_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._to_km(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self._to_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self._to_km(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self._to_km(other)
