from __future__ import annotations


class Distance:
    def __init__(self, distance: int | float) -> None:
        self.km = distance

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
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, Distance):
            return self.km == value.km
        return self.km == value

    def __ne__(self, value: object, /) -> bool:
        if isinstance(value, Distance):
            return self.km != value.km
        return self.km != value

    def __gt__(self, value: object, /) -> bool:
        if isinstance(value, Distance):
            return self.km > value.km
        return self.km > value

    def __ge__(self, value: object, /) -> bool:
        if isinstance(value, Distance):
            return self.km >= value.km
        return self.km >= value

    def __lt__(self, value: object, /) -> bool:
        if isinstance(value, Distance):
            return self.km < value.km
        return self.km < value

    def __le__(self, value: object, /) -> bool:
        if isinstance(value, Distance):
            return self.km <= value.km
        return self.km <= value
