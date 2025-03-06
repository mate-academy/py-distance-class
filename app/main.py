from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        # Store km as a float, even if it is an integer value
        self.km = km

    def __str__(self) -> str:
        return (f"Distance: {self.km:.1f}".rstrip("0").rstrip(".")
                + " kilometers.")

    def __repr__(self) -> str:
        return f"Distance(km={int(self.km)})" if isinstance(self.km, int)\
            else f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        # Handle addition of Distance objects or a number (float or int)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | float) -> Distance:
        # Handle in-place addition (+=)
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other: float) -> Distance:
        # Handle multiplication by a float or integer
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        # Handle division by a float or integer, result should be a Distance
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | float) -> bool:
        # Equality comparison (==)
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __lt__(self, other: Distance | float) -> bool:
        # Less than comparison (<)
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | float) -> bool:
        # Greater than comparison (>)
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __le__(self, other: Distance | float) -> bool:
        # Less than or equal to comparison (<=)
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | float) -> bool:
        # Greater than or equal to comparison (>=)
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
