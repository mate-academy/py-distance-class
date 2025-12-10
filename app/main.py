from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        return Distance(
            self.km + (other.km if isinstance(other, Distance) else other)
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        self.km = self.km + (
            other.km if isinstance(other, Distance) else other
        )
        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        if not isinstance(multiplier, (int, float)):
            raise TypeError

        return Distance(
            multiplier * self.km
        )

    def __truediv__(self, divider: int | float) -> Distance:
        if not isinstance(divider, (int, float)):
            raise TypeError

        return Distance(
            round(self.km / divider, 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError

        return self.km >= (other.km if isinstance(other, Distance) else other)
