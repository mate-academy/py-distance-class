from __future__ import annotations

Number = int | float


class Distance:

    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | Number) -> Distance:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | Number) -> Distance:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: Number) -> Distance:
        if not isinstance(other, Number):
            return NotImplemented

        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Distance:
        if not isinstance(other, Number):
            return NotImplemented

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | Number) -> bool:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: Distance | Number) -> bool:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __le__(self, other: Distance | Number) -> bool:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: Distance | Number) -> bool:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        return self.km >= value

    def __eq__(self, other: Distance | Number) -> bool:
        if not isinstance(other, (Distance, Number)):
            return NotImplemented

        value = other.km if isinstance(other, Distance) else other
        return self.km == value
