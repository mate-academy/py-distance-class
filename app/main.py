from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            if isinstance(other, (float, int)):
                other = Distance(other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)

        self.km += other.km
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)

        return self.km == other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)

        return self.km > other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)

        return self.km >= other.km

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)

        return self.km < other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)

        return self.km <= other.km
