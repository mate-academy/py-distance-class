from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
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
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> Distance:
        div_result = round((self.km / other), 2)
        return Distance(km=div_result)

    def __lt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance) and self.km < other.km:
            return True
        if self.km < other:
            return True
        return False

    def __gt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance) and self.km > other.km:
            return True
        if self.km > other:
            return True
        return False

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance) and self.km == other.km:
            return True
        if self.km == other:
            return True
        return False

    def __le__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance) and self.km <= other.km:
            return True
        if self.km <= other:
            return True
        return False

    def __ge__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance) and self.km >= other.km:
            return True
        if self.km >= other:
            return True
        return False
