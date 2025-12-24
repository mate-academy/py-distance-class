from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if self.is_number(other):
            return Distance(km=self.km + other)

        return Distance(
            km=self.km + other.km
        )

    def __eq__(self, other: Distance | int | float) -> bool:
        if self.is_number(other):
            return self.km == other

        return self.km == other.km

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if self.is_number(other):
            self.km += other
        else:
            self.km += other.km

        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise ValueError("Division by zero")

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if self.is_number(other):
            return self.km > other

        return self.km > other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if self.is_number(other):
            return self.km <= other

        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if self.is_number(other):
            return self.km >= other

        return self.km >= other.km

    @staticmethod
    def is_number(other: int | float) -> bool:
        return isinstance(other, int) or isinstance(other, float)
