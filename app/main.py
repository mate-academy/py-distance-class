from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:

        # if isinstance(other, Distance):
        #     self.km += other.km
        #
        # else:
        #     self.km += other
        value = self.km
        if isinstance(other, Distance):
            value += other.km

        else:
            value += other

        return Distance(value)

    def __iadd__(self, other: Distance) -> Distance:

        if isinstance(other, Distance):
            self.km += other.km

        else:
            self.km += other

        return self

    def __mul__(self, other: Distance) -> Distance:
        # self.km *= other
        # return Distance(self.km)
        value = self.km
        value *= other
        return Distance(value)

    def __truediv__(self, other: Distance) -> Distance:
        # self.km /= other
        # return Distance(round(self.km, 2))
        value = self.km
        value /= other
        return Distance(round(value, 2))

    def __eq__(self, other: float) -> bool:
        return self.km == other

    def __lt__(self, other: float) -> bool:
        return self.km < other

    def __gt__(self, other: float) -> bool:
        return self.km > other

    def __le__(self, other: float) -> bool:
        return self.km <= other

    def __ge__(self, other: float) -> bool:
        return self.km >= other
