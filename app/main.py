from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            new_km = self.km + other.km
            return Distance(new_km)
        elif isinstance(other, (int, float)):
            new_km = self.km + other
            return Distance(new_km)

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            multiplied = self.km * other
            return Distance(multiplied)

    def __truediv__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            division = self.km / other
            return Distance(round(division, 2))

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
