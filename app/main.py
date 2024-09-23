from __future__ import annotations


class Distance:
    def __init__(self, distance: Distance) -> None:
        self.km = distance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other.real
        return Distance(distance=self.km)

    def __iadd__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            # return Distance(distance=self.km + other.real)
            self.km += other.real
        # return Distance(distance=self.km)
        return self

    def __mul__(self, other: Distance or int) -> Distance or None:
        if isinstance(other, Distance):
            return None
        else:
            return Distance(distance=self.km * other.real)

    def __truediv__(self, other: Distance or int) -> Distance or None:
        if isinstance(other, Distance):
            return None
        else:
            return Distance(distance=round(self.km / other.real, 2))

    def __eq__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other.real

    def __lt__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other.real

    def __gt__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other.real

    def __le__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other.real

    def __ge__(self, other: Distance or int) -> Distance:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other.real


# distance1 = Distance(30)
# distance2 = Distance(3)
# distance3 = distance1 / distance2
# print(distance1)
# print(repr(distance3))
# distance1 += distance2
# print(distance1)
