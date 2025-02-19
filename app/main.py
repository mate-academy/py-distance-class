from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _to_km(self, other: Distance | int | float) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        raise TypeError("Unsupported type for operation")

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self._to_km(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self._to_km(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Unsupported type for multiplication")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Unsupported type for division")

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
