from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __rmul__(self, other: int) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, number: int | float) -> "Distance":
        if not isinstance(number, (int, float)):
            return NotImplemented
        amount = round(self.km / number, 2)
        return Distance(amount)

    def __lt__(self, other: "Distance" | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: "Distance" | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: "Distance" | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: "Distance" | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: "Distance" | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
