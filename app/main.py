from typing import Self


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> object:
        other = other.km if isinstance(other, Distance) else other

        return Distance(self.km + other)

    __radd__ = __add__

    def __iadd__(self, other: int) -> Self:

        other = other.km if isinstance(other, Distance) else other
        self.km += other

        return self

    def __mul__(self, other: int | float) -> Self:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    __rmul__ = __mul__

    def __truediv__(self, other: int | float) -> Self:
        if isinstance(other, (float, int)):
            return Distance(round((self.km / other), 2))

    def __eq__(self, other: int | float) -> bool:
        other = other.km if isinstance(other, Distance) else other
        return self.km == other

    def __lt__(self, other: int | float) -> bool:
        other = other.km if isinstance(other, Distance) else other
        return self.km < other

    def __le__(self, other: int | float) -> bool:
        other = other.km if isinstance(other, Distance) else other
        return self.km <= other

    def __gt__(self, other: int | float) -> bool:
        other = other.km if isinstance(other, Distance) else other
        return self.km > other

    def __ge__(self, other: int | float) -> bool:
        other = other.km if isinstance(other, Distance) else other
        return self.km >= other
