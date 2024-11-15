from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: [int, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: [int, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, num: int) -> "Distance":
        if isinstance(num, Distance):
            raise TypeError
        else:
            return Distance(self.km * num)

    def __truediv__(self, num: int) -> "Distance":
        if isinstance(num, Distance):
            raise TypeError
        else:
            return Distance(round(self.km / num, 2))

    def __lt__(self, other: Union[int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Union[int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Union[int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: Union[int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Union[int, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
