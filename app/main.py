from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return "Distance: {} kilometers.".format(self.km)

    def __repr__(self) -> str:
        return "Distance(km={})".format(self.km)

    def __add__(self, other: Distance | int | float) -> Distance:
        value = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        value = other if isinstance(other, (int, float)) else other.km
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise Exception("Division by zero")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        value = other if isinstance(other, (int, float)) else other.km
        return self.km < value

    def __gt__(self, other: Distance | int | float) -> bool:
        value = other if isinstance(other, (int, float)) else other.km
        return self.km > value

    def __eq__(self, other: Distance | int | float) -> bool:
        value = other if isinstance(other, (int, float)) else other.km
        return self.km == value

    def __le__(self, other: Distance | int | float) -> bool:
        value = other if isinstance(other, (int, float)) else other.km
        return self.km <= value

    def __ge__(self, other: Distance | int | float) -> bool:
        value = other if isinstance(other, (int, float)) else other.km
        return self.km >= value
