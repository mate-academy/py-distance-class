from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        other = Distance.detect_type_and_get_value(other)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other = Distance.detect_type_and_get_value(other)
        self.km += other
        return self

    def __mul__(self, number: int) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int) -> Distance:
        calculated = round(self.km / number, 2)
        return Distance(calculated)

    def __lt__(self, other: Distance | int | float) -> bool:
        other = Distance.detect_type_and_get_value(other)
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        other = Distance.detect_type_and_get_value(other)
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        other = Distance.detect_type_and_get_value(other)
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        other = Distance.detect_type_and_get_value(other)
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        other = Distance.detect_type_and_get_value(other)
        return self.km >= other

    def __len__(self) -> int:
        return self.km

    @staticmethod
    def detect_type_and_get_value(
            other: Distance | int | float
    ) -> Distance | int | float:

        if isinstance(other, Distance):
            return other.km
        return other
