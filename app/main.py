from typing import Any


class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int | float):
            return Distance(self.km + other)
        else:
            raise (
                TypeError("Unsupported")
            )

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int | float):
            self.km += other
            return self
        else:
            raise (
                TypeError("Unsupported")
            )

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, int | float):
            self.km *= other
        else:
            raise (
                TypeError("Unsupported")
            )
        return self

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, int | float):
            self.km = round(self.km / other, 2)
        else:
            raise (
                TypeError("Unsupported")
            )
        return self

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int | float):
            return self.km == other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int | float):
            return self.km > other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int | float):
            return self.km >= other

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int | float):
            return self.km < other

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int | float):
            return self.km <= other
