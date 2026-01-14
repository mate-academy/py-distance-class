from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        return Distance(km=self.km + self.check_argument(other))

    def __iadd__(self, other) -> Distance:
        self.km += self.check_argument(other)
        return self

    def __mul__(self, other) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        return self.km < self.check_argument(other)

    def __gt__(self, other) -> bool:
        return self.km > self.check_argument(other)

    def __eq__(self, other) -> bool:
        return self.km == self.check_argument(other)

    def __le__(self, other) -> bool:
        return self.km <= self.check_argument(other)

    def __ge__(self, other) -> bool:
        return self.km >= self.check_argument(other)

    def __len__(self) -> int | float:
        return self.km

    @staticmethod
    def check_argument(other) -> int | float:
        if type(other) is Distance:
            return other.km
        elif type(other) is int or type(other) is float:
            return other
