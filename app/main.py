from typing import Union


Number = Union[int, float]


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented  # type: ignore

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented  # type: ignore
        return self

    def __mul__(self, other: Number) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError

    def __truediv__(self, other: Number) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError

    def __eq__(self, other: Union["Distance", Number]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented  # type: ignore

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented  # type: ignore

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented  # type: ignore

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented  # type: ignore

    def __le__(self, other: Union["Distance", Number]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented  # type: ignore
