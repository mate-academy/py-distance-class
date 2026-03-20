from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            suma = self.km + other.km
            distance_new = Distance(suma)
            return distance_new
        if isinstance(other, (int, float)):
            suma = self.km + other
            distance_new = Distance(suma)
            return distance_new
        return NotImplemented

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            result_mul = self.km * other
            distance_new = Distance(result_mul)
            return distance_new
        return NotImplemented

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            result_truediv = round(self.km / other, 2)
            distance_new = Distance(result_truediv)
            return distance_new
        return NotImplemented

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
