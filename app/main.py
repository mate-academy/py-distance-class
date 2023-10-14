from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if type(other) == Distance:
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | float) -> Distance:
        if type(other) == Distance:
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))
