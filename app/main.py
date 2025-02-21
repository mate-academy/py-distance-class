from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance | bool:
        if isinstance(other, (Distance, int, float)):
            return Distance(
                self.km + (other.km if isinstance(other, Distance) else other)
            )
        return False

    def __iadd__(self, other: Distance | int | float) -> Distance | bool:
        if isinstance(other, (Distance, int, float)):
            self.km += (
                other.km if isinstance(other, Distance) else other
            )
            return self
        return False

    def __mul__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance | bool:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km < (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km > (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km <= (
                other.km if isinstance(other, Distance) else other
            )
        return False

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km >= (
                other.km if isinstance(other, Distance) else other
            )
        return False
