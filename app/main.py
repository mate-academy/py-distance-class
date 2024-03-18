from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km,
            )
        else:
            return Distance(
                km=self.km + other,
            )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance | None:
        if isinstance(other, int | float):
            return Distance(
                km=self.km * other,
            )
        else:
            return None

    def __truediv__(self, other: int | float) -> Distance | None:
        if isinstance(other, int | float):
            return Distance(
                km=round(self.km / other, 2),
            )
        else:
            return None

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km >= other
        return self.km >= other.km
