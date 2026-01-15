from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _check_and_get_value(other: Distance | float | int) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (float, int)):
            return other
        else:
            raise ValueError("Unsupported type for operation")

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km + self._check_and_get_value(other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += self._check_and_get_value(other)
        return self

    def __mul__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            raise TypeError(
                "'__mul__' method should not accept Distance instance")
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | float | int) -> Distance:
        if not isinstance(other, (float, int)):
            raise TypeError("Unsupported type for division")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < self._check_and_get_value(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return not self.__lt__(other) and not self.__eq__(other)

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == self._check_and_get_value(other)

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= self._check_and_get_value(other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return not self.__lt__(other)
