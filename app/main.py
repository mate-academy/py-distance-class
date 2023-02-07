from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: int | float | Distance) -> Distance:
        if type(other) is Distance:
            return Distance(
                self.km + other.km
            )
        self.km += other
        return self

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if type(other) == Distance:
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: int | float | Distance) -> Distance:
        if type(other) == Distance:
            Distance(
                self.km / other.km
            )
        self.km = round((self.km / other), 2)
        return self

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other
