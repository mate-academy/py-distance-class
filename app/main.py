from __future__ import annotations


class Distance:

    def __init__(self, km: "Distance" | int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        return Distance(self.km + other)

    def __radd__(self, other: "Distance" | int | float) -> "Distance":
        return Distance(self.km + other)

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        self.km *= other
        return self

    def __truediv__(self, other: int | float) -> "Distance":
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: "Distance" | int | float) -> bool:
        if self.km < other:
            return True
        return False

    def __gt__(self, other: "Distance" | int | float) -> bool:
        if self.km > other:
            return True
        return False

    def __eq__(self, other: "Distance" | int | float) -> bool:
        if self.km == other:
            return True
        return False

    def __le__(self, other: "Distance" | int | float) -> bool:
        if self.km <= other:
            return True
        return False

    def __ge__(self, other: "Distance" | int | float) -> bool:
        if self.km >= other:
            return True
        return False
