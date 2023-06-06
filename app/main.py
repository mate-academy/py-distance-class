from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(
            self.km + self.return_number(other)
        )

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += self.return_number(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        self.km *= other
        return Distance(self.km)

    def __truediv__(self, other: int | float) -> Distance:
        self.km /= other
        return Distance(
            round(self.km, 2)
        )

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.return_number(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > self.return_number(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self.return_number(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= self.return_number(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= self.return_number(other)

    @staticmethod
    def return_number(number: int) -> int | float:
        if not isinstance(number, Distance):
            return number
        return number.km
