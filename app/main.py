from typing import Any


class Distance:
    def __init__(self, km: (float, int)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(
                self.km + other.km
            )
        if isinstance(other, (float, int)):
            return Distance(
                self.km + other
            )

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (float, int)):
            self.km += other
        return self

    def __mul__(self, other: Any) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Any:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (float, int)):
            return self.km < other

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (float, int)):
            return self.km > other

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (float, int)):
            return self.km == other

    def __le__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (float, int)):
            return self.km <= other

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (float, int)):
            return self.km >= other
