from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, multiplier: int) -> Any:
        return Distance(
            km=self.km * multiplier
        )

    def __truediv__(self, divisor: int) -> Any:
        self.km = round(self.km / divisor, 2)
        return self

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
