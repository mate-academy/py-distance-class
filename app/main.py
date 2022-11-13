from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int) or isinstance(other, float):
            self.km += other
            return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        if isinstance(other, int) or isinstance(other, float):
            return True if self.km < other else False

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        if isinstance(other, int) or isinstance(other, float):
            return True if self.km > other else False

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        if isinstance(other, int) or isinstance(other, float):
            return True if self.km == other else False

    def __le__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        if isinstance(other, int) or isinstance(other, float):
            return True if self.km <= other else False

    def __ge__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        if isinstance(other, int) or isinstance(other, float):
            return True if self.km >= other else False

    def __len__(self) -> int:
        return len(range(int(self.km)))
