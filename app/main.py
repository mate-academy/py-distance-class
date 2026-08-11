from typing import Self


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Self:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        return Distance(self.km + value)

    def __iadd__(self, other: Distance) -> Self:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        self.km += value
        return self

    def __mul__(self, other: float) -> Self:
        value = 1
        if isinstance(other, (int, float)):
            value = other
            self.km *= value
            return self

    def __lt__(self, other: Distance) -> Self:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        return self.km < value

    def __gt__(self, other: Distance) -> bool:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        return self.km > value

    def __eq__(self, other: Distance) -> bool:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        return self.km == value

    def __le__(self, other: Distance) -> bool:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        return self.km <= value

    def __ge__(self, other: Distance) -> bool:
        value = 0
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        return self.km >= value

    def __truediv__(self, other: float) -> Self:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
