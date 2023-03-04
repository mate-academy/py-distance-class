from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        final = None

        if isinstance(other, int) or isinstance(other, float):
            final = Distance(self.km + other)
        else:
            final = Distance(self.km + other.km)

        return final

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        else:
            self.km += other.km

        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        final = None

        if isinstance(other, Distance):
            final = self.km > other.km
        else:
            final = self.km > other

        return final

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= other
