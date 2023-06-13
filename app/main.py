from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        return Distance(other + self.km)

    def __iadd__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, other: float) -> Distance | None:
        if isinstance(other, Distance):
            other.km = self.km * other.km
            return None

        return Distance(other * self.km)

    def __truediv__(self, other: float) -> Distance | None:
        if isinstance(other, Distance):
            other.km = round(self.km / other.km, 2)
            return None

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float) -> bool:
        return self.km < other

    def __gt__(self, other: Distance | float) -> bool:
        return self.km > other

    def __eq__(self, other: Distance | float) -> bool:
        return self.km == other

    def __le__(self, other: Distance | float) -> bool:
        return self.km <= other

    def __ge__(self, other: Distance | float) -> bool:
        return self.km >= other
