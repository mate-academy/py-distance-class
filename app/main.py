from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            distance = Distance(self.km + other.km)
            return distance
        else:
            self.km = self.km + other
            return self

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, (int, float)):
            self.km = self.km + other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, number: int) -> Distance:
        distance = Distance(self.km * number)
        return distance

    def __truediv__(self, number: float | int) -> Distance:
        distance = Distance(round(self.km / number, 2))
        return distance

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __ne__(self, other: Distance) -> bool:
        return not self.km.__eq__(other.km)

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return not self.km.__eq__(other) and not self.km.__lt__(other)
        return not self.km.__eq__(other.km) and not self.km.__lt__(other.km)

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return not self.km.__lt__(other)
        return not self.km.__lt__(other.km)

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km.__eq__(other) or self.km.__lt__(other)
        return self.km.__eq__(other.km) or self.km.__lt__(other.km)
