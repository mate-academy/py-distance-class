from __future__ import annotations


class Distance:
    def __init__(self: Distance, km: float):
        self.km = km

    def __str__(self: Distance):
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance):
        return f"Distance(km={self.km})"

    def __add__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self: Distance, other: Distance):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self: Distance, other: Distance):
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))

    def __lt__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self: Distance, other: Distance):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other