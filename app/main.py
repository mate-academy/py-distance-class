from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        new_distance = Distance(self.km)
        if isinstance(other, (int, float)):
            new_distance.km += other
        elif isinstance(other, Distance):
            new_distance.km += other.km
        return new_distance

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divider: int | float) -> Distance:
        divided_distance = Distance(self.km)
        if divider != 0:
            divided_distance.km = round(divided_distance.km / divider, 2)
        return divided_distance

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        return not self > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self < other
