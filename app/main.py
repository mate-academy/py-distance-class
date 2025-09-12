from __future__ import annotations


class Distance:
    def __init__(self, km: float = 0.0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + float(other))
        raise TypeError("Distance can be added only to Distance, int or float")

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += float(other)
            return self
        raise TypeError("Distance can be added only to Distance, int or float")

    def __mul__(self, factor: int | float) -> Distance:
        if isinstance(factor, (int, float)):
            return Distance(self.km * float(factor))
        raise TypeError("Distance can be multiplied only by int or float")
        return NotImplemented

    def __truediv__(self, divisor: int | float) -> Distance:
        if not isinstance(divisor, (int, float)):
            raise TypeError("Distance can be divided only by int or float")
        if divisor == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Distance(round(self.km / float(divisor), 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < float(other)
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > float(other)
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return False

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= float(other)
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= float(other)
        return NotImplemented
