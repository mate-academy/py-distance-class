from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: Distance | int | float) -> "Distance":
        if isinstance(other, Distance):
            return self.__class__(self.km + other.km)
        return self.__class__(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        self.km = self.km + other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return self.__class__(self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        return self.__class__(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
