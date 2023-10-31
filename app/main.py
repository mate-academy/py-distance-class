from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def get_km(other: Distance | int | float) -> int | float:
        return other.km if isinstance(other, Distance) else other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km + self.get_km(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.get_km(other)

        return self

    def __mul__(self, num: int) -> Distance:
        return Distance(km=self.km * num)

    def __truediv__(self, num: int) -> Distance:
        return Distance(km=round(self.km / num, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.get_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.get_km(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.get_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return not self.km > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self.km < other
