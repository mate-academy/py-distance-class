from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    @staticmethod
    def check_value(value: [Distance, int]) -> int:
        return (
            value.real if "real" in dir(value)
            else value.km
        )

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: [Distance, int]) -> Distance:
        return Distance(
            km=self.km + self.check_value(other)
        )

    def __iadd__(self, other: [Distance, int]) -> Distance:
        self.km += self.check_value(other)
        return self

    def __mul__(self, other: [Distance, int]) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide one Distance instance by another")

        elif isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )
        else:
            raise TypeError(
                f"Unsupported type for division: {type(other).__name__}"
            )

    def __truediv__(self, other: [Distance, int]) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide one Distance instance by another")
        elif isinstance(other, (int, float)):
            return Distance(
                round((self.km / other), 2)
            )
        else:
            raise TypeError(
                f"Unsupported type for division: {type(other).__name__}"
            )

    def __lt__(self, other: [Distance, int]) -> bool:
        return (
            self.km < self.check_value(other)
        )

    def __gt__(self, other: [Distance, int]) -> bool:
        return (
            self.km > self.check_value(other)
        )

    def __eq__(self, other: [Distance, int]) -> bool:
        return (
            self.km == self.check_value(other)
        )

    def __le__(self, other: [Distance, int]) -> bool:
        return (
            self.km <= self.check_value(other)
        )

    def __ge__(self, other: [Distance, int]) -> bool:
        return (
            self.km >= self.check_value(other)
        )
