from __future__ import annotations
import math


class Distance:
    def __init__(self, km: int | float) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("km must be an integer or float")
        if km < 0:
            raise ValueError("Distance cannot be negative")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | int | Distance) -> Distance:
        return Distance(
            self.km + (other.km if isinstance(other, Distance) else other)
        )

    def __iadd__(self, other: float | int | Distance) -> Distance:
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float | int | Distance) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: float | int | Distance) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: float | int | Distance) -> bool:
        return math.isclose(
            self.km,
            (other.km if isinstance(other, Distance) else other),
            rel_tol=1e-9
        )

    def __le__(self, other: float | int | Distance) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: float | int | Distance) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
