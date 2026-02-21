from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Not is int of float type")

        self.km = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km:.4g} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km:.4g})"

    def __add__(
            self,
            other: int | float | Distance
    ) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        return NotImplemented

    def __iadd__(
            self,
            other: int | float | Distance
    ) -> Distance:
        if isinstance(other, Distance):
            self.km += float(other.km)
            return self

        if isinstance(other, (int, float)):
            self.km += float(other)
            return self

        raise TypeError("Not is int of float type")

    def __mul__(
            self,
            scalar: int | float
    ) -> Distance:
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)

        raise TypeError("Not is int of float type")

    def __truediv__(
            self,
            scalar: int | float
    ) -> Distance:
        if isinstance(scalar, (int, float)) and scalar == 0:
            raise ZeroDivisionError("Division by zero")

        if isinstance(scalar, (int, float)):
            return Distance(round(self.km / scalar, 2))

        raise TypeError("Not is int of float type")

    def __lt__(
            self,
            other: int | float | Distance
    ) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

        return NotImplemented

    def __gt__(
            self,
            other: int | float | Distance
    ) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

        return NotImplemented

    def __eq__(
            self,
            other: int | float | Distance
    ) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

        return NotImplemented

    def __le__(
            self,
            other: int | float | Distance
    ) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

        return NotImplemented

    def __ge__(
            self,
            other: int | float | Distance
    ) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other

        return NotImplemented
