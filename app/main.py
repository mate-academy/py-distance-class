from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: int | float) -> "Distance" | None:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance | None:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2)) if other != 0 else None
        return None

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km < (
                other.km if isinstance(other, Distance) else other
            )

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km > (
                other.km if isinstance(other, Distance) else other
            )

    def __eq__(self, other: int | float | Distance) -> bool | None:
        if isinstance(other, (Distance, int, float)):
            return self.km == (
                other.km if isinstance(other, Distance) else other
            )

    def __le__(self, other: int | float | Distance) -> bool | None:
        return self < other or self == other

    def __ge__(self, other: int | float | Distance) -> bool | None:
        return self > other or self == other
