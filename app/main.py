from __future__ import annotations


class Distance:

    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        km = other if isinstance(other, (int, float)) else other.km
        return Distance(km=self.km + km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other

        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        km = other if isinstance(other, (int, float)) else other.km
        return Distance(km=self.km * km)

    def __truediv__(self, other: int | float | Distance) -> Distance:
        km = other if isinstance(other, (int, float)) else other.km
        result = round((self.km / km), 2)
        return Distance(km=result)

    def __lt__(self, other: int | float | Distance) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km < km

    def __gt__(self, other: int | float | Distance) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km > km

    def __eq__(self, other: int | float | Distance) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km == km

    def __le__(self, other: Distance | int) -> bool:
        return not self > other

    def __ge__(self, other: Distance | int) -> bool:
        return not self < other
