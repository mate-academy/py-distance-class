from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # Addition
    def __add__(self, other: int | float | object) -> Distance:
        return (
            Distance(self.km + other.km)
            if isinstance(other, Distance)
            else Distance(self.km + other)
        )

    # In-place Addition
    def __iadd__(self, other: int | float | object) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    # Multiplication
    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    # True Division
    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    # Equal
    def __eq__(self, other: object) -> bool:
        return (
            self.km == other.km
            if isinstance(other, Distance)
            else self.km == other
        )

    # Less Than
    def __lt__(self, other: object | int | float) -> bool:
        return (
            self.km < other.km
            if isinstance(other, Distance)
            else self.km < other
        )

    # Less or Equal
    def __le__(self, other: object | int | float) -> bool:
        return (
            self.km <= other.km
            if isinstance(other, Distance)
            else self.km <= other
        )

    # Greater Than
    def __gt__(self, other: object | int | float) -> bool:
        return (
            self.km > other.km
            if isinstance(other, Distance)
            else self.km > other
        )

    # Greater or Equal
    def __ge__(self, other: object | int | float) -> bool:
        return (
            self.km >= other.km
            if isinstance(other, Distance)
            else self.km >= other
        )
