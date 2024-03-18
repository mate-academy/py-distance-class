from __future__ import annotations


class Distance:
    __slots__ = "km"

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km + getattr(other, "km", other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += getattr(other, "km", other)
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float | int) -> bool:
        return self.km < getattr(other, "km", other)

    def __gt__(self, other: float | int) -> bool:
        return self.km > getattr(other, "km", other)

    def __eq__(self, other: float | int) -> bool:
        return self.km == getattr(other, "km", other)

    def __le__(self, other: float | int) -> bool:
        return self.km <= getattr(other, "km", other)

    def __ge__(self, other: float | int) -> bool:
        return self.km >= getattr(other, "km", other)
