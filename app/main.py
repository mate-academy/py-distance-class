from typing import Any


class Distance:

    @staticmethod
    def isinstance_(other: int | float) -> int | float:
        return other.km if isinstance(other, Distance) else other

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> Any:
        return Distance(self.km + Distance.isinstance_(other))

    def __iadd__(self, other: int | float) -> Any:
        self.km += Distance.isinstance_(other)
        return self

    def __mul__(self, other: int | float) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Any:
        if other != 0:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float) -> bool:
        return self.km < Distance.isinstance_(other)

    def __gt__(self, other: int | float) -> bool:
        return self.km > Distance.isinstance_(other)

    def __eq__(self, other: int | float) -> bool:
        return self.km == Distance.isinstance_(other)

    def __le__(self, other: int | float) -> bool:
        return self.km <= Distance.isinstance_(other)

    def __ge__(self, other: int | float) -> bool:
        return self.km >= Distance.isinstance_(other)
