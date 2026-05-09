from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return Distance(self.km + value)

    def __iadd__(self, other) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        self.km += value
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km < value

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km > value

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km == value

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km <= value

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km >= value
