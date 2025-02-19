from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def return_number(other: int | float | Distance) -> int | float:
        if isinstance(other, (float, int)):
            return other
        return other.km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km + Distance.return_number(other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += Distance.return_number(other)
        return self

    def __mul__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == Distance.return_number(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > Distance.return_number(other)

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < Distance.return_number(other)

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= Distance.return_number(other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return self.km >= Distance.return_number(other)
