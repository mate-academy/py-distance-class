from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + other
            )

    def __mul__(self, num: float) -> Distance:
        return Distance(
            km=self.km * num
        )

    def __iadd__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __truediv__(self, num: float) -> Distance:
        return Distance(
            km=round(self.km / num, 2)
        )

    def __lt__(self, other: float) -> bool:
        return self.km < other

    def __gt__(self, other: float) -> bool:
        return self.km > other

    def __eq__(self, other: float) -> bool:
        return self.km == other

    def __le__(self, other: float) -> bool:
        return self.km <= other

    def __ge__(self, other: float) -> bool:
        return self.km >= other
