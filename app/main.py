from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            value_to_add = other.km
        else:
            value_to_add = other
        return Distance(self.km + value_to_add)

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            value_to_add = other.km
        else:
            value_to_add = other
        self.km += value_to_add
        return self

    def __mul__(self, other: int | float) -> Distance:
        distance2 = self.km * other
        return Distance(distance2)

    def __truediv__(self, other: int | float) -> Distance:
        distance3 = round(self.km / other, 2)
        return Distance(distance3)

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km < other_value

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km > other_value

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km == other_value

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km <= other_value

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        else:
            other_value = other
        return self.km >= other_value
