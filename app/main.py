from __future__ import annotations


class Distance:
    def __init__(self, km: float = 0.0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return NotImplemented

    def __iadd__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        if other != 0:
            result = self.km / other
            result_rounded = round(result, 2)
            return Distance(result_rounded)
        else:
            raise ZeroDivisionError("Division by zero is not allowed.")

    def __eq__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return round(self.km, 2) == round(other.km, 2)
        elif isinstance(other, (int, float)):
            return round(self.km, 2) == round(other, 2)
        else:
            return NotImplemented

    def __lt__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __gt__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __le__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented
