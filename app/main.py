from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: ("Distance", float)) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (float, int)):
            return Distance(self.km + other)

    def __iadd__(self, other: ("Distance", float)) -> "Distance":
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        elif isinstance(other, (float, int)):
            self.km = self.km + other
            return self

    def __mul__(self, number: float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: float) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __eq__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (float, int)):
            return self.km == other

    def __lt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (float, int)):
            return self.km < other

    def __gt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (float, int)):
            return self.km > other

    def __le__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (float, int)):
            return self.km <= other

    def __ge__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (float, int)):
            return self.km >= other
