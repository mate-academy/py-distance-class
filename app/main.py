from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int]) -> "Distance":
        if type(other) is Distance:
            self.km += other.km
        else:
            self.km += other
        return self

    def __iadd__(self, other: Union["Distance", int]) -> "Distance":
        if type(other) is Distance:
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        self.km *= other
        return self

    def __truediv__(self, other: int) -> "Distance":
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __eq__(self, other: int) -> bool:
        return self.km == other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other
