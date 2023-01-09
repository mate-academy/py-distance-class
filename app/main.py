from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)

        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self

        self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __lt__(self, other: Distance) -> bool:
        return self.km < other

    def __gt__(self, other: Distance) -> bool:
        return self.km > other

    def __eq__(self, other: Distance) -> bool:
        return self.km == other

    def __le__(self, other: Distance) -> bool:
        return self.km <= other

    def __ge__(self, other: Distance) -> bool:
        return self.km >= other

    def __truediv__(self, other: int) -> Distance:
        return Distance(km=round(self.km / other, 2))


distance1 = Distance(15.5)

print(distance1 / 7)

# distance1 += 15
distance2 = Distance(14.5)

distance1 += distance2

print(distance1)
