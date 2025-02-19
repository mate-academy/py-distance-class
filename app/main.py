from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    @staticmethod
    def validate(other: int | float | Distance) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(f"Unsupported type for operation: {type(other)}")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{type(self).__name__}(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km + self.validate(other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += self.validate(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("__mul__ method should not"
                            " accept Distance instance")
        other_value = self.validate(other)
        return Distance(self.km * other_value)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("__truediv__ method should not"
                            " accept Distance instance")

        other_value = self.validate(other)
        if other_value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(round(self.km / other_value, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.validate(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > self.validate(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self.validate(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= self.validate(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= self.validate(other)
