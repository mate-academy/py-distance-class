from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            other_km_data = self.km + other.km
        else:
            other_km_data = self.km + other
        return Distance(
            other_km_data
        )

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            print("Error: object other can not be of type Distance")
        self.km = self.km * other
        return self

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            print("Error: object other can not be of type Distance")
        result = round((self.km / other), 2)
        return Distance(
            result
        )

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
