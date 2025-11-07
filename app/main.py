from __future__ import annotations


class Distance:

    def __init__(self, km: (int | float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        return NotImplemented

    def __iadd__(self, other: (int | float | "Distance")) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, multiplayer: (int | float)) -> "Distance":
        if isinstance(multiplayer, (int, float)):
            return Distance(
                km=self.km * multiplayer
            )
        return NotImplemented

    def __truediv__(self, divisor: (int | float)) -> "Distance":
        if isinstance(divisor, (int, float)):
            return Distance(
                km=round(self.km / divisor, 2)
            )
        return NotImplemented

    def __eq__(self, other: (int | float | "Distance")) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
        else:
            if self.km == other:
                return True
        return False

    def __lt__(self, other: (int | float | "Distance")) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
        else:
            if self.km < other:
                return True
        return False

    def __gt__(self, other: (int | float | "Distance")) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
        else:
            if self.km > other:
                return True
        return False

    def __le__(self, other: (int | float | "Distance")) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
        else:
            if self.km <= other:
                return True
        return False

    def __ge__(self, other: (int | float | "Distance")) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
        else:
            if self.km >= other:
                return True
        return False
