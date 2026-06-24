from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # ================== math

    def __add__(self, other: Distance | int | float) -> Distance:

        if isinstance(other, Distance) is True:
            total_distance = self.km + other.km

        elif isinstance(other, (int, float)) is True:
            total_distance = self.km + other

        return Distance(total_distance)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance) is True:
            self.km += other.km
        elif isinstance(other, (int, float)) is True:
            self.km += other

        return self

    def __mul__(self, other: int | float) -> Distance:

        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:

        return Distance(round(self.km / other, 2))

    # ======================== comparing
    # __lt__, __gt__, __eq__, __le__, __ge__

    # less
    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) is True:
            compared_res = self.km < other.km

        elif isinstance(other, (int, float)) is True:
            compared_res = self.km < other

        return compared_res

    # less or eq
    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) is True:
            compared_res = self.km <= other.km

        elif isinstance(other, (int, float)) is True:
            compared_res = self.km <= other

        return compared_res

    # more
    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) is True:
            compared_res = self.km > other.km

        elif isinstance(other, (int, float)) is True:
            compared_res = self.km > other

        return compared_res

    # more or eq
    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) is True:
            compared_res = self.km >= other.km

        elif isinstance(other, (int, float)) is True:
            compared_res = self.km >= other

        return compared_res

    # eq
    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) is True:
            compared_res = self.km == other.km

        elif isinstance(other, (int, float)) is True:
            compared_res = self.km == other

        return compared_res
