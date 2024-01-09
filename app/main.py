from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        return Distance(self.km + self.get_km(other))

    def __iadd__(self, other: Distance | float) -> Distance:
        self.km += self.get_km(other)
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float) -> bool:
        return self.km < self.get_km(other)

    def __gt__(self, other: Distance | float) -> bool:
        return self.km > self.get_km(other)

    def __eq__(self, other: Distance | float) -> bool:
        return self.km == self.get_km(other)

    def __le__(self, other: Distance | float) -> bool:
        return self.km <= self.get_km(other)

    def __ge__(self, other: Distance | float) -> bool:
        return self.km >= self.get_km(other)

    @staticmethod
    def get_km(obj: Distance | float) -> float:
        return obj.km if isinstance(obj, Distance) else obj
