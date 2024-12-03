from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise ValueError("Cannot divide by zero")
        return Distance(round(self.km / other, 2))

    @staticmethod
    def _get_km(other: Distance | int | float) -> float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return not self > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self < other
