from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: OtherType) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: OtherType) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        new_km = round(self.km / other, 2)
        return Distance(new_km)

    def __lt__(self, other: OtherType) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: OtherType) -> bool:
        value = other.km if isinstance(other, Distance) else other

        return self.km > value

    def __eq__(self, other: OtherType) -> bool:
        value = other.km if isinstance(other, Distance) else other

        return self.km == value

    def __le__(self, other: OtherType) -> bool:
        value = other.km if isinstance(other, Distance) else other

        return self.km <= value

    def __ge__(self, other: OtherType) -> bool:
        value = other.km if isinstance(other, Distance) else other

        return self.km >= value


OtherType = Distance | int | float
