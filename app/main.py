from typing import Any


class Distance:

    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def check_isinstance(other: Distance | float | int) -> Any:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km + Distance.check_isinstance(other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += Distance.check_isinstance(other)
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < Distance.check_isinstance(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > Distance.check_isinstance(other)

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == Distance.check_isinstance(other)

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= Distance.check_isinstance(other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return self.km >= Distance.check_isinstance(other)
