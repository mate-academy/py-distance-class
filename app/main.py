from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if type(other) == int or type(other) == float:
            new_distance = self.km + other
            return Distance(new_distance)
        else:
            new_distance = self.km + other.km
            return Distance(new_distance)

    def __iadd__(self, other: Any) -> Any:
        if type(other) == int or type(other) == float:
            self.km = self.km + other
            return self
        else:
            self.km = self.km + other.km
            return self

    def __mul__(self, other: (int, float)) -> Any:
        if type(other) == int or type(other) == float:
            new_distance = self.km * other
            return Distance(new_distance)

    def __truediv__(self, other: (int, float)) -> Any:
        if type(other) == int or type(other) == float:
            new_distance = round(self.km / other, 2)
            return Distance(new_distance)

    def __eq__(self, other: Any) -> bool:
        if type(other) == int or type(other) == float:
            return self.km == other
        return self.km == other.km

    def __gt__(self, other: Any) -> bool:
        if type(other) == int or type(other) == float:
            return self.km > other
        else:
            return self.km > other.km

    def __ge__(self, other: Any) -> bool:
        if type(other) == int or type(other) == float:
            return self.km >= other
        else:
            return self.km >= other.km

    def __lt__(self, other: Any) -> bool:
        if type(other) == int or type(other) == float:
            return self.km < other
        else:
            return self.km < other.km

    def __le__(self, other: Any) -> bool:
        if type(other) == int or type(other) == float:
            return self.km <= other
        else:
            return self.km <= other.km
