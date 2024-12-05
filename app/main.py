from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union["Distance", int]) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Union["Distance", int]) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
