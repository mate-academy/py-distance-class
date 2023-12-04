from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __eq__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __ne__(self, other: Union["Distance", float]) -> bool:
        result = self.__eq__(other)
        return not result if result is not NotImplemented else NotImplemented

    def __gt__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __ge__(self, other: Union["Distance", float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
