from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            distance = Distance(self.km + other)
            return distance
        distance = Distance(self.km + other.km)
        return distance

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            self.km = self.km + other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, number: int) -> Any:
        distance = Distance(self.km * number)
        return distance

    def __truediv__(self, number: float | int) -> Any:
        distance = Distance(round(self.km / number, 2))
        return distance

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __ne__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km != other
        return self.km != other.km

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km

    def __le__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km
