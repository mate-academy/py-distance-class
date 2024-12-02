from __future__ import annotations


class Distance:
    Variables = "Distance", int, float

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Variables) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (float, int)):
            return Distance(self.km + other)

    def __iadd__(self, other: Variables) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (float, int)):
            self.km += other
        return self

    def __mul__(self, other: Variables) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Variables) -> Distance:
        if isinstance(other, (float, int)):
            if other == 0:
                raise ZeroDivisionError(f"{other} == 0")
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Variables) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (float, int)):
            return self.km < other

    def __gt__(self, other: Variables) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (float, int)):
            return self.km > other

    def __eq__(self, other: Variables) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (float, int)):
            return self.km == other

    def __le__(self, other: Variables) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (float, int)):
            return self.km <= other

    def __ge__(self, other: Variables) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (float, int)):
            return self.km >= other
