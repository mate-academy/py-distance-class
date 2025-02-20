from __future__ import annotations


Numeric = int | float


class Distance:
    def __init__(self, km: Numeric) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_str = int(self.km) if self.km.is_integer() else self.km
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        km_str = int(self.km) if self.km.is_integer() else self.km
        return f"Distance(km={km_str})"

    def __add__(self, other: Distance | Numeric) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: Distance | Numeric) -> Distance:
        if isinstance(other, (int, float, Distance)):
            self.km += other.km if isinstance(other, Distance) else other
            return self
        return NotImplemented

    def __mul__(self, other: Numeric) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Numeric) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | Numeric) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Distance | Numeric) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Distance | Numeric) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Distance | Numeric) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Distance | Numeric) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
