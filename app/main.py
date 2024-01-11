from __future__ import annotations
from functools import total_ordering
@total_ordering
class Distance:
    def __init__(self, km: int) -> None:
        self.km = km
    @staticmethod
    def is_instance_check(other: Distance) -> bool:
        return isinstance(other, Distance)

    def __str__(self):
        return f"Distance: {self.km} kilometers."
    def __repr__(self):
        return f"Distance(km={self.km})"
    def __add__(self, other: Distance) -> int :
        if Distance.is_instance_check(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)
    def __iadd__(self, other: Distance):
        if Distance.is_instance_check(other):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: Distance):
        return  Distance(self.km *other)

    def __truediv__(self, other) -> float:
        return  Distance(round((self.km / other), 2))
    def __lt__(self, other: Distance):
        if Distance.is_instance_check(other):
            return self.km < other.km
        return  self.km < other
    def __gt__(self, other):
        if Distance.is_instance_check(other):
            return self.km > other.km
        return self.km > other
    def __eq__(self, other):
        if Distance.is_instance_check(other):
            return self.km == other.km
        return self.km == other



