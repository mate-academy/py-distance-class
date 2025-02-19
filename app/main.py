from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = self.validate_number(km)

    @staticmethod
    def validate_number(value: int | float) -> int | float | None:
        if isinstance(value, (int, float)) and value > 0:
            return value
        raise TypeError("Try a positive number!")

    @staticmethod
    def validate_distance_or_number(
            other: int | float | Distance
    ) -> int | float | Distance | None:
        if isinstance(other, (int, float)):
            return other
        if isinstance(other, Distance):
            return other.km
        raise TypeError("Try a Distance object or a number!")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.validate_distance_or_number(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.validate_distance_or_number(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(
            km=self.km * self.validate_number(other)
        )

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            km=round(self.km / self.validate_number(other), 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.validate_distance_or_number(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.validate_distance_or_number(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.validate_distance_or_number(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.validate_distance_or_number(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.validate_distance_or_number(other)
