from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def check_type(other: Distance | int) -> int:
        return other.km if type(other) is Distance else other

    def __add__(self, other: Distance | int) -> Distance:
        return Distance(
            km=self.km + self.check_type(other=other)
        )

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km += self.check_type(other=other)
        return self

    def __mul__(self, other: Distance | int) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | int) -> bool:
        return self.km < self.check_type(other=other)

    def __gt__(self, other: Distance | int) -> bool:
        return self.km > self.check_type(other=other)

    def __eq__(self, other: Distance | int) -> bool:
        return self.km == self.check_type(other=other)

    def __le__(self, other: Distance | int) -> bool:
        return self.km <= self.check_type(other=other)

    def __ge__(self, other: Distance | int) -> bool:
        return self.km >= self.check_type(other=other)
