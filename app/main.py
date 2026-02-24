from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        result = self.km / other
        return Distance(round(result, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km == value

    def __ne__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km != value

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km < value

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km > value

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km >= value

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km <= value
