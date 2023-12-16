from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:

        return (Distance(self.km + other.km)
                if type(other) == Distance
                else Distance(self.km + other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km = ((self.km + other.km)
                   if type(other) == Distance
                   else (self.km + other))
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if type(other) == Distance:
            return True if self.km < other.km else False
        else:
            return True if self.km < other else False

    def __gt__(self, other: Distance | int | float) -> bool:
        if type(other) == Distance:
            return True if self.km > other.km else False
        else:
            return True if self.km > other else False

    def __eq__(self, other: Distance | int | float) -> bool:
        if type(other) == Distance:
            return True if self.km == other.km else False
        else:
            return True if self.km == other else False

    def __le__(self, other: Distance | int | float) -> bool:
        if type(other) == Distance:
            return True if self.km <= other.km else False
        else:
            return True if self.km <= other else False

    def __ge__(self, other: Distance | int | float) -> bool:
        if type(other) == Distance:
            return True if self.km >= other.km else False
        else:
            return True if self.km >= other else False
