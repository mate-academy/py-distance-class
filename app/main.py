from typing import Any


class Distance:
    """A distance in kilometers."""
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Any) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Any:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
            else:
                return False
        else:
            if self.km < other:
                return True
            else:
                return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
            else:
                return False
        else:
            if self.km > other:
                return True
            else:
                return False

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
            else:
                return False
        else:
            if self.km == other:
                return True
            else:
                return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
            else:
                return False
        else:
            if self.km <= other:
                return True
            else:
                return False

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
            else:
                return False
        else:
            if self.km >= other:
                return True
            else:
                return False
