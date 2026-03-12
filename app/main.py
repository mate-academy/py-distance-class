from typing import Any, Union


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
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, number: Union[int, float]) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: Union[int, float]) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        return False

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
