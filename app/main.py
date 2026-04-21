from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        return Distance(self.km + other_distance)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        self.km += other_distance
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: object) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: object) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: object) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: object) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: object) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
