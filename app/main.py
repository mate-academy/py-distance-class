from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        km = other if isinstance(other, int | float) else other.km
        return Distance(self.km + km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        km = other if isinstance(other, int | float) else other.km
        self.km += km
        return self

    def __mul__(self, other: int | float) -> Distance | None:
        if isinstance(other, int | float):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: Distance | int | float) -> Distance | None:
        if isinstance(other, int | float):
            return Distance(round(self.km / other, 2))
        return None

    def __eq__(self, other: Distance | int | float) -> bool:
        number = other if isinstance(other, int | float) else other.km
        return self.km == number

    def __gt__(self, other: Distance | int | float) -> bool:
        number = other if isinstance(other, int | float) else other.km
        return self.km > number

    def __lt__(self, other: Distance | int | float) -> bool:
        number = other if isinstance(other, int | float) else other.km
        return self.km < number

    def __ge__(self, other: Distance | int | float) -> bool:
        number = other if isinstance(other, int | float) else other.km
        return self.km >= number

    def __le__(self, other: Distance | int | float) -> bool:
        number = other if isinstance(other, int | float) else other.km
        return self.km <= number
