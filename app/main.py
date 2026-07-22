from typing import Callable


class Distance:

    def __init__(self, km: float | int) -> None:
        self.km = km

    @staticmethod
    def normalize_other(func: Callable) -> Callable:
        def conwer_in_int(self: Distance, other: Distance | int) -> Callable:
            other_km = other.km if isinstance(other, Distance) else other
            return func(self, other_km)
        return conwer_in_int

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @normalize_other
    def __add__(self, other: Distance | int) -> Distance:
        return Distance(
            km=self.km + other
        )

    @normalize_other
    def __iadd__(self, other: Distance | int) -> Distance:
        self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int) -> Distance:
        return Distance(
            km=round(self.km / other, 2)
        )

    @normalize_other
    def __lt__(self, other: Distance | int) -> bool:
        return self.km < other

    @normalize_other
    def __gt__(self, other: Distance | int) -> bool:
        return self.km > other

    @normalize_other
    def __eq__(self, other: Distance | int) -> bool:
        return self.km == other

    @normalize_other
    def __le__(self, other: Distance | int) -> bool:
        return self.km <= other

    @normalize_other
    def __ge__(self, other: Distance | int) -> bool:
        return self.km >= other
