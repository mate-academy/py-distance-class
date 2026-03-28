from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {format(self.km, 'g')} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={format(self.km, 'g')})"

    # ---- arithmetic ----
    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return Distance(self.km + other_km)

    def __radd__(self, other: int | float) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = other.km if isinstance(other, Distance) else float(other)
        self.km += other_km
        return self

    def __mul__(self, factor: int | float) -> Distance:
        return Distance(self.km * float(factor))

    def __rmul__(self, factor: int | float) -> Distance:
        return self.__mul__(factor)

    def __truediv__(self, divisor: int | float) -> Distance:
        return Distance(round(self.km / float(divisor), 2))

    # ---- comparisons ----
    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else float(other)
        return self.km >= other_km
