from __future__ import annotations


class Distance:
    @staticmethod
    def _to_km(other: int | float | Distance) -> float:
        return other.km if isinstance(other, Distance) else float(other)

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(km=self.km + Distance._to_km(other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += Distance._to_km(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < Distance._to_km(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > Distance._to_km(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == Distance._to_km(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= Distance._to_km(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= Distance._to_km(other)
