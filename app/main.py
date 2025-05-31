from __future__ import division


class Distance:
    def __init__(self, km: [int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: [int, float]) -> "Distance":
        if isinstance(other, Distance):
            new_value = self.km + other.km
            return Distance(new_value)
        else:
            new_value = self.km + other
            return Distance(new_value)

    def __iadd__(self, other: [int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: [int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            new_value = self.km * other
            return Distance(new_value)

    def __truediv__(self, other: [int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            new_value = self.km / other
            return Distance(round(new_value, 2))

    def __lt__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
