from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        km = other.km if isinstance(other, Distance) else other
        return Distance(
            km=self.km + km
        )

    def __iadd__(self, other: Distance) -> Distance:
        km = other.km if isinstance(other, Distance) else other
        self.km += km
        return self

    def __mul__(self, mul: float) -> Distance:
        return Distance(
            km=self.km * mul
        )

    def __truediv__(self, div: float) -> Distance:
        return Distance(
            km=round(self.km / div, 2)
        )

    def __lt__(self, other: Distance) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km < km

    def __gt__(self, other: Distance) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km > km

    def __eq__(self, other: Distance) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km == km

    def __le__(self, other: Distance) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km <= km

    def __ge__(self, other: Distance) -> bool:
        km = other.km if isinstance(other, Distance) else other
        return self.km >= km
