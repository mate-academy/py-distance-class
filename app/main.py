from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + other.km if isinstance(other, Distance)
                        else self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, multiplier: int) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, devider: int) -> Distance:
        self.km = round(self.km / devider, 2)
        return self

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        return not self < other and not self > other

    def __le__(self, other: Distance | int | float) -> bool:
        return not self > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self < other
