from typing import Any


class Distance:
    def __init__(self, km: (int or float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int or float)) -> Any:
        if type(other) is float or type(other) is int:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: (int or float)) -> Any:
        if type(other) is float or type(other) is int:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: (int or float)) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: (int or float)) -> Any:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: (int or float)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km == other
        return self.km == other.km

    def __gt__(self, other: (int or float)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km > other
        return self.km > other.km

    def __ge__(self, other: (int or float)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km >= other
        return self.km >= other.km

    def __lt__(self, other: (int or float)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km < other
        return self.km < other.km

    def __le__(self, other: (int or float)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km <= other
        return self.km <= other.km
