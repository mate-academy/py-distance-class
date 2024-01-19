from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(
            self.km + self.extract_km(other)
        )

    def __iadd__(
            self,
            other: int | float | Distance
    ) -> Distance:
        self.km += self.extract_km(other)

        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            round(self.km / other, 2)
        )

    def __eq__(
            self,
            other: int | float | Distance
    ) -> bool:
        return self.km == self.extract_km(other)

    def __ne__(self, other: int | float | Distance) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > self.extract_km(other)

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.extract_km(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return not self.__lt__(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return not self.__gt__(other)

    @staticmethod
    def extract_km(other: int | float) -> int | float:
        if isinstance(other, Distance):
            other = other.km
        return other
