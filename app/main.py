from __future__ import annotations


class Distance:
    # Write your code here
    pass

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)

        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, value: int) -> Distance:
        return Distance(km=self.km * value)

    def __truediv__(self, value: int | float) -> Distance:
        real_distance = round(self.km / value, 2)

        return Distance(km=real_distance)

    def __lt__(self, other: Distance | float | int) -> bool:
        if other is Distance:
            return self.km < other.km

        return self.km < other

    def __gt__(self, other: Distance | float | int) -> bool:
        if other is Distance:
            return self.km > other.km

        return self.km > other

    def __eq__(self, other: Distance | float | int) -> bool:
        if other is Distance:
            return self.km == other.km

        return self.km == other

    def __le__(self, other: Distance | float | int) -> bool:
        if other is Distance:
            return self.km <= other.km

        return self.km <= other

    def __ge__(self, other: Distance | float | int) -> bool:
        if other is Distance:
            return self.km >= other.km

        return self.km >= other
