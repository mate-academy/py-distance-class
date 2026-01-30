from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, divisor: int | float) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, km: Distance | float | int) -> bool:
        if isinstance(km, Distance):
            return self.km < km.km
        return self.km < km

    def __gt__(self, km: Distance | float | int) -> bool:
        if isinstance(km, Distance):
            return self.km > km.km
        return self.km > km

    def __eq__(self, km: Distance | float | int) -> bool:
        if isinstance(km, Distance):
            return self.km == km.km
        return self.km == km

    def __le__(self, km: Distance | float | int) -> bool:
        if isinstance(km, Distance):
            return self.km <= km.km
        return self.km <= km

    def __ge__(self, km: Distance | float | int) -> bool:
        if isinstance(km, Distance):
            return self.km >= km.km
        return self.km >= km
