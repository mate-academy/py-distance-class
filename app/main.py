from typing import Self


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Self | int | float) -> Self:
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Self | int | float) -> Self:
        if isinstance(other, (int, float)):
            self.km += other
            return self

        self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Self:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Self:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float) -> bool:
        return True if self.km < other else False

    def __gt__(self, other: int | float) -> bool:
        return True if self.km > other else False

    def __eq__(self, other: int | float) -> bool:
        return True if self.km == other else False

    def __le__(self, other: int | float) -> bool:
        return True if self.km <= other else False

    def __ge__(self, other: int | float) -> bool:
        return True if self.km >= other else False
