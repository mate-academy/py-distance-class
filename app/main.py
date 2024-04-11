from typing import Any


class Distance:
    def __init__(self, km: Any) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other: Any) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        elif isinstance(other, int | float):
            return True if self.km < other else False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        elif isinstance(other, int | float):
            return True if self.km > other else False

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        elif isinstance(other, int | float):
            return True if self.km == other else False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        elif isinstance(other, int | float):
            return True if self.km <= other else False

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        elif isinstance(other, int | float):
            return True if self.km >= other else False
