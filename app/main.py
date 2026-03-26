from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def _value(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km + self._value(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self._value(other)
        return self

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __mul__(self, multiplier: int | float) -> Distance:
        return Distance(km=self.km * multiplier)

    def __truediv__(self, divisor: float | int) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._value(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._value(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self._value(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self._value(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        return self.km == other
