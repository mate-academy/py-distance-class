from __future__ import annotations, division


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Type is not correct")

    def __iadd__(self, other: Distance | int | float
                 ) -> Distance | int | float:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Type is not correct")
        return self

    def __mul__(self, other: Distance | int | float) -> Distance | int | float:
        if isinstance(other, Distance):
            raise TypeError("Cannot multiply Distance by Distance")
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Type is not correct")

    def __truediv__(self, other: Distance | int | float) -> Distance | float:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide Distance by Distance")
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Type is not correct")

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Type is not correct")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Type is not correct")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Type is not correct")

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Type is not correct")

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Type is not correct")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
