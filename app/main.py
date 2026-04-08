from typing import Any


class Distans:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> Any:
        if isinstance(other, Distans):
            return Distans(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distans(self.km + other)

    def __iadd__(self, other: (int, float)) -> Any:
        if isinstance(other, Distans):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: (int, float)) -> Any:
        if isinstance(other, (int, float)):
            return Distans(self.km * other)

    def __truediv__(self, other: (int, float)) -> Any:
        if isinstance(other, (int, float)) and other != 0:
            return Distans(round(self.km / other, 2))

    def __lt__(self, other: (int, float)) -> bool | None | Any:
        if isinstance(other, Distans):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: (int, float)) -> bool | None | Any:
        if isinstance(other, Distans):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: (int, float)) -> bool | None | Any:
        if isinstance(other, Distans):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: (int, float)) -> bool | None | Any:
        if isinstance(other, Distans):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: (int, float)) -> bool | None | Any:
        if isinstance(other, Distans):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
