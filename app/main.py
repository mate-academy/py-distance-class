from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (Distance, int, float)):
            self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if other != 0:
            return Distance(round(self.km / other, 2))
        else:
            raise ValueError("Unable to division by zero")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __lt__(self, other: int) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km < (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __le__(self, other: int) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km <= (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __gt__(self, other: int) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km > (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __ge__(self, other: int) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km >= (
                other.km if isinstance(other, Distance) else other
            )
        return False
