from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    @staticmethod
    def __typecheck__(other: any) -> None:
        return isinstance(other, Distance)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: any) -> float:
        if Distance.__typecheck__(other):
            return Distance(self.km + other.km)
        distance = Distance(other)
        return Distance(self.km + distance.km)

    def __iadd__(self, other: any) -> float:
        if Distance.__typecheck__(other):
            self.km += other.km
            return self
        distance = Distance(other)
        self.km += distance.km
        return self

    def __mul__(self, other: int) -> float:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> float:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        if Distance.__typecheck__(other):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: any) -> bool:
        if Distance.__typecheck__(other):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: any) -> bool:
        if Distance.__typecheck__(other):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: any) -> bool:
        if Distance.__typecheck__(other):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: any) -> bool:
        if Distance.__typecheck__(other):
            return self.km >= other.km
        return self.km >= other
