from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise ValueError(f"We can`t add {other}")

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError(f"We can`t add {other}")
        return self

    def __mul__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise ValueError(f"We can`t mul {other}")

    def __truediv__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km / other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km / other)
        else:
            raise ValueError(f"We can`t mul {other}")

    def __lt__(self, something: Distance) -> bool:
        return self.km < something.km

    def __gt__(self, other: Distance) -> bool:
        return self.km > other.km

    def __eq__(self, other: Distance) -> bool:
        return self.km == other.km

    def __le__(self, other: Distance) -> bool:
        return self.km <= other.km

    def __ge__(self, other: Distance) -> bool:
        return self.km >= other.km
