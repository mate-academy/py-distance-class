from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: Distance) -> Distance:
        return Distance(
            km=self.km + other.km
        )

    def __mul__(self, mul: int) -> Distance:
        return Distance(
            km=self.km * mul
        )

    def __truediv__(self, div: int) -> Distance:
        return Distance(
            km=int(self.km / div)
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
