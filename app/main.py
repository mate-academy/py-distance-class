from typing import Callable


class Distance:
    def __init__(self, km: int) -> Callable:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            res = Distance(self)
            res.km = self.km + other.km
            return res
        if isinstance(other, (int, float)):
            res = Distance(self)
            res.km = self.km + other
            return res

    def __iadd__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: int) -> Callable:
        if isinstance(other, (int, float)):
            res = Distance(self)
            res.km = self.km * other
            return res
        else:
            return self.km * other

    def __truediv__(self, other: int) -> Callable:
        if isinstance(other, (int, float)):
            res = Distance(self)
            res.km = round(self.km / other, 2)
            return res
        else:
            return round(self.km / other, 2)

    def __lt__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: int) -> Callable:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other

    def __len__(self: int) -> Callable:
        return self.km
