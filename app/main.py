from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            num = other.km
        else:
            num = other
        self.km = self.km.__add__(num)
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            num = other.km
        else:
            num = other
        if self.km < num:
            return True
        return False

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            num = other.km
        else:
            num = other
        if self.km > num:
            return True
        return False

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            num = other.km
        else:
            num = other
        if self.km == num:
            return True
        return False

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            num = other.km
        else:
            num = other
        if self.km <= num:
            return True
        return False

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            num = other.km
        else:
            num = other
        if self.km >= num:
            return True
        return False
