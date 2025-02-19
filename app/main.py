from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self  # Return self only once

    def __mul__(self, multiplier: int | float) -> "Distance":
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: int | float) -> "Distance":
        result = self.km / divisor
        return Distance(round(result, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return (
            self.km < other.km
            if isinstance(other, Distance)
            else self.km < other
        )

    def __gt__(self, other: Distance | int | float) -> bool:
        return (
            self.km > other.km
            if isinstance(other, Distance)
            else self.km > other
        )

    def __eq__(self, other: Distance | int | float) -> bool:
        return (
            self.km == other.km
            if isinstance(other, Distance)
            else self.km == other
        )

    def __le__(self, other: Distance | int | float) -> bool:
        return (
            self.km <= other.km
            if isinstance(other, Distance)
            else self.km <= other
        )

    def __ge__(self, other: Distance | int | float) -> bool:
        return (
            self.km >= other.km
            if isinstance(other, Distance)
            else self.km >= other
        )
