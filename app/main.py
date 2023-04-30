from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if type(other) == int or type(other) == float:
            new_distance = self.km + other
            return Distance(new_distance)
        new_distance = self.km + other.km
        return Distance(new_distance)

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if type(other) == int or type(other) == float:
            self.km = self.km + other
            return self
        self.km = self.km + other.km
        return self

    def __mul__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if type(other) == int or type(other) == float:
            new_distance = self.km * other
            return Distance(new_distance)

    def __truediv__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if type(other) == int or type(other) == float:
            return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km == other
        return self.km == other.km

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km > other
        return self.km > other.km

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km >= other
        return self.km >= other.km

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km < other
        return self.km < other.km

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km <= other
        return self.km <= other.km
