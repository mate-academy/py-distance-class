from __future__ import annotations


class Distance:
    def __init__(self: Distance, km: float) -> None:
        self.km = km

    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"

    def __add__(
        self: Distance,
        other: float | int | Distance
    ) -> Distance:
        value = other
        if isinstance(other, Distance):
            value = other.km
        return Distance(self.km + value)

    def __iadd__(
        self: Distance,
        other: float | int | Distance
    ) -> Distance:
        value = other
        if isinstance(other, Distance):
            value = other.km
        self.km += value
        return self

    def __mul__(self: Distance, other: float | int) -> Distance:
        result = self.km * other
        return Distance(result)

    def __truediv__(self: Distance, other: float | int) -> Distance:
        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(
        self: Distance,
        other: float | int | Distance
    ) -> bool:
        value = other
        if isinstance(other, Distance):
            value = other.km
        return self.km < value

    def __gt__(
        self: Distance,
        other: float | int | Distance
    ) -> bool:
        value = other
        if isinstance(other, Distance):
            value = other.km
        return self.km > value

    def __eq__(
        self: Distance,
        other: float | int | Distance
    ) -> bool:
        value = other
        if isinstance(other, Distance):
            value = other.km
        return self.km == value

    def __le__(
        self: Distance,
        other: float | int | Distance
    ) -> bool:
        value = other
        if isinstance(other, Distance):
            value = other.km
        return self.km <= value

    def __ge__(
        self: Distance,
        other: float | int | Distance
    ) -> bool:
        value = other
        if isinstance(other, Distance):
            value = other.km
        return self.km >= value
