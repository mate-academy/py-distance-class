from __future__ import annotations


class Distance:

    def __init__(self, km: float):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        return Distance(
            self.km + other.real
            if isinstance(other, (int, float))
            else self.km + other.km
        )

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other.real
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: Distance) -> bool:
        return self.km < other.real if isinstance(other, (int, float)) \
            else self.km < other.km

    def __gt__(self, other: Distance) -> bool:
        return self.km > other.real if isinstance(other, (int, float)) \
            else self.km > other.km

    def __eq__(self, other: Distance) -> bool:
        return self.km == other.real if isinstance(other, (int, float)) \
            else self.km == other.km

    def __le__(self, other: Distance) -> bool:
        return not self > other

    def __ge__(self, other: Distance) -> bool:
        return not self < other

    def __len__(self) -> int | float:
        return self.km
