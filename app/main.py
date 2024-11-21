from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def determine_type(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.determine_type(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.determine_type(other)
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.determine_type(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.determine_type(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.determine_type(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.determine_type(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.determine_type(other)
