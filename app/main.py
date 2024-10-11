from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return self

    def __iadd__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, factor: Union[int, float]) -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return self

    def __truediv__(self, divisor: Union[int, float]) -> "Distance":
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        return self

    def __lt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return False

    def __gt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return False

    def __eq__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return False

    def __ge__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return False
