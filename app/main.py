from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Number) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> "Distance":
        return Distance(round(self.km / other, 2))
