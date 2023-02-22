from typing import Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> Any:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> Any:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        elif type(other) is float or type(other) is int:
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        elif type(other) is float or type(other) is int:
            self.km += other
        return self

    def __mul__(self, other: int) -> Any:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int) -> Any:
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km < other.km
        elif type(other) is float or type(other) is int:
            return self.km < other

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km > other.km
        elif type(other) is float or type(other) is int:
            return self.km > other

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km == other.km
        elif type(other) is float or type(other) is int:
            return self.km == other

    def __le__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif type(other) is float or type(other) is int:
            return self.km <= other

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif type(other) is float or type(other) is int:
            return self.km >= other
