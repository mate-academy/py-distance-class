from typing import Optional as Optinal


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | Optinal["Distance"]) -> "Distance":
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: int | Optinal["Distance"]) -> "Distance":
        if not isinstance(other, Distance):
            other = Distance(km=other)
        self.km += other.km
        return self

    def __truediv__(self, other: int | Optinal["Distance"]) -> "Distance":
        return Distance(km=round(self.km / other, 2))

    def __mul__(self, other: int | Optinal["Distance"]) -> "Distance":
        return Distance(km=self.km * other)

    def __lt__(self, other: int | Optinal["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km < other.km

    def __gt__(self, other: int | Optinal["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km > other.km

    def __eq__(self, other: int | Optinal["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km == other.km

    def __le__(self, other: int | Optinal["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km <= other.km

    def __ge__(self, other: int | Optinal["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km >= other.km
