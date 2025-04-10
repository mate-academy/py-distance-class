import math


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Disnatce(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            unrounded = self.km / other
            rounded = math.floor(unrounded)
            return Distance(rounded)
        return NotImplemented

    def __lt__(self,other):
        if isinstance(other, int):
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, int):
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, int):
            return self.km == other

    def __le__(self, other):
        if isinstance(other, int):
            return self.km <= other

    def __ge__(self, other):
        if isinstance(other, int):
            return self.km >= other



