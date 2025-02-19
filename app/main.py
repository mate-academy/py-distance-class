from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: any) -> Distance:
        if isinstance(other, Distance):
            result = other.km
        else:
            result = other
        return Distance(self.km + result)

    def __iadd__(self, other: any) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: any) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> float:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: any) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: any) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: any) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: any) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: any) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
