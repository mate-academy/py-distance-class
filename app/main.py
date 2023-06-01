from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: isinstance | int | float) -> isinstance:
        if type(other) in (int, float):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: isinstance | int | float) -> isinstance:
        if type(other) in (int, float):
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other: int) -> isinstance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> isinstance:
        return (Distance(km=round(self.km / other, 2)))

    def __lt__(self, other: isinstance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: isinstance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: isinstance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: isinstance | int | float) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: isinstance | int | float) -> bool:
        return not self.__lt__(other)
