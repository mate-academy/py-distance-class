from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km = self.__add__(other)
        return self

    def __mul__(self, other: int | float) -> Distance | None:
        if isinstance(other, (int, float)):
            return Distance(round(self.km * other, 3))
        return None

    def __truediv__(self, other: int | float) -> Distance | None:
        if isinstance(other, (int, float)):
            if other == 0:
                return None
            return Distance(round(self.km / other, 2))

        return None

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __le__(self, other: Distance | int | float) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other
