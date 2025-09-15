from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        # __str__
        # distance = Distance(20)
        # print(distance)  # "Distance: 20 kilometers."
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        # __repr__
        # distance = Distance(20)
        # repr(distance)  # "Distance(km=20)"
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        # __add__
        # distance1 = Distance(20)
        # distance2 = Distance(30)
        # distance3 = distance1 + distance2
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        # distance1 = Distance(20)
        # distance2 = Distance(30)
        # distance1 += distance2  # distance1.km is 50
        #
        # distance = Distance(20)
        # distance += 30  # distance.km == 50
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, other: int) -> Distance:
        # __mul__
        # distance1 = Distance(20)
        # distance2 = distance1 * 5
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int) -> Distance:
        # __truediv__
        # distance1 = Distance(20)
        # distance2 = distance1 / 7
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km

        return self.km < other

    def __gt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km

        return self.km > other

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        return self.km == other

    def __le__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km or self.km == other.km

        return self.km < other or self.km == other

    def __ge__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km or self.km == other.km

        return self.km > other or self.km == other
