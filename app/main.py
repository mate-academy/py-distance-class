from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
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
            value_add = other.km
        else:
            value_add = other
        self.km += value_add
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> object:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km < other_value

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km > other_value

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km == other_value

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km <= other_value

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km >= other_value
