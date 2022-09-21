from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def check_type(other) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        return Distance(self.km + self.check_type(other))

    def __iadd__(self, other) -> Distance:
        self.km += self.check_type(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other) -> bool:
        return self.km < self.check_type(other)

    def __gt__(self, other) -> bool:
        return self.km > self.check_type(other)

    def __eq__(self, other) -> bool:
        return self.km == self.check_type(other)

    def __le__(self, other) -> bool:
        return self.km <= self.check_type(other)

    def __ge__(self, other) -> bool:
        return self.km >= self.check_type(other)

    def __len__(self) -> int:
        return self.km
